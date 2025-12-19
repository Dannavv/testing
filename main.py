from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI is running"}


@app.get("/test")
def root():
    return {"message": "test is running"}


@app.get("/hello")
def root():
    return {"message": "hello is running"}

#hey team
# new
#eee

