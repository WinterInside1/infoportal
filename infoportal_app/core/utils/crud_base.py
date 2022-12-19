from typing import Generic, List, Optional, Type, TypeVar

import ormar
from pydantic import BaseModel


ModelType = TypeVar("ModelType", bound=ormar.Model)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def _prefetch_related(self, query, prefetch_related: List[str] = None):
        if prefetch_related:
            for related in prefetch_related:
                query = query.prefetch_related(related)
        return query

    async def get(
            self,
            id: int,
            *,
            prefetch_related: List[str] = None
    ) -> Optional[ModelType]:
        query = self.model.objects
        query = self._prefetch_related(query, prefetch_related)
        return await query.get_or_none(id=id)

    async def get_multi(
            self,
            page: int,
            *,
            page_size: int = 20,
            prefetch_related: List[str] = None
    ) -> List[ModelType]:
        query = self.model.objects
        query = self._prefetch_related(query, prefetch_related)
        return await query.paginate(page, page_size).all()

    async def create(self, obj_in: CreateSchemaType, *, save_related=True) -> ModelType:
        db_obj = self.model(**obj_in.dict())
        await db_obj.save()
        if save_related:
            await db_obj.save_related(follow=True, save_all=True)
        return db_obj

    async def update(
        self,
        *,
        db_obj: ModelType,
        obj_in: UpdateSchemaType
    ) -> ModelType:
        obj_dict = obj_in if isinstance(obj_in, dict) else obj_in.dict()
        obj = await db_obj.update(**obj_dict)
        await obj.save_related(follow=True, save_all=True)
        return obj

    async def remove(self, id: int) -> ModelType:
        return await self.model.objects.delete(id=id)

    async def get_filtered(self, *, prefetch_related: List[str] = None, **kwargs) -> List[ModelType]:
        query = self.model.objects.filter(**kwargs)
        query = self._prefetch_related(query, prefetch_related)
        return await query.all()
