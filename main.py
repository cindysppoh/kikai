from fastapi import FastAPI
from blog import models
from blog.database import engine
from blog.routers import blog, user, authentication
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
origins = ["http://127.0.0.1:3000", "http://10.0.0.44:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=3600,
)

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


if __name__ == "__main_":
    #  uvicorn.run(app, host="127.0.0.1",port=9000)
    uvicorn.run(app, host="10.0.0.44", port=3000)
