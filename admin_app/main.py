import uvicorn
from config import config


def main():
    uvicorn.run(
        app="app:app",
        host=config.APP_HOST,
        port=config.APP_PORT,
        reload=True,
        workers=1,
    )


if __name__ == "__main__":
    main()
