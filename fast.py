from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def start():
    return {"message": "the api we built yersterday i want you 3 to build a fresh one."}