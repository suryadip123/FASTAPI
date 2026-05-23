from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root ():
    return {"message" : "Hello Surya"}

@app.get("/{id}")
def root_with_id(id:int):
    return {"message" : f"success with id {id}"}

@app.post("/todo")
def create_data(item : dict):
    return {"message " : item}
    


