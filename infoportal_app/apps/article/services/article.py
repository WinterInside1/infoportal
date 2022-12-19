from apps.article import crud
from apps.article.models import Article
from apps.article.schemas.user import (
    CreateArticleSchema,
    UpdateArticleSchema,
)
from core.exceptions import NotFoundException
import psycopg2
from config import config


class UserService:
    @staticmethod
    async def create_user(user_create: CreateArticleSchema) -> Article:
        return await crud.user.create(user_create)

    @staticmethod
    async def get_user(user_id: int) -> Article:
        try:
            connection = psycopg2.connect(config.DB_USER,
                                          config.DB_PASS,
                                          config.DB_HOST,
                                          config.DB_PORT,
                                          config.DB_NAME)
            cursor = connection.cursor()
            postgreSQL_select_Query = "select * from User where id = %s"
            cursor.execute(postgreSQL_select_Query, (user_id,))
            user = cursor.fetchall()
            #user = await crud.user.get(user_id)
            if not user:
                raise NotFoundException(message="Item not found")
            return user
        except (Exception, psycopg2.Error) as error:
            print("Error in update operation", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    @staticmethod
    async def get_user_list(page: int, *, page_size: int) -> Article:
        return await crud.user.get_multi(page=page, page_size=page_size)

    @staticmethod
    async def update_user(user_id: int, user_update: UpdateArticleSchema) -> Article:
        try:
            connection = psycopg2.connect(config.DB_USER,
                                          config.DB_PASS,
                                          config.DB_HOST,
                                          config.DB_PORT,
                                          config.DB_NAME)
            cursor = connection.cursor()
            postgreSQL_select_Query = """select * from User where id = %s"""
            cursor.execute(postgreSQL_select_Query, (user_id,))
            old_user = cursor.fetchone()
            if not old_user:
                raise NotFoundException(message="Item not found")

            postgreSQL_update_Query = "update User set username = %s , email = %s where id = %s "
            cursor.execute(postgreSQL_update_Query, ( user_update.username, user_update.email, user_id))

        except (Exception, psycopg2.Error) as error:
            print("Error in update operation", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

        user = await crud.user.get(user_id)
        if not user:
            raise NotFoundException(message="Item not found")
        return await crud.user.update(db_obj=user, obj_in=user_update)

    @staticmethod
    async def delete_user(user_id: int) -> None:
        user = crud.user.get(user_id)
        if not user:
            raise NotFoundException(message="Item not found")
        await crud.user.remove(user_id)
