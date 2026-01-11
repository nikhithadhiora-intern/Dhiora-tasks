from fastapi import FastAPI

app = FastAPI()
data = []

@app.get("/")
def get_data():
    return data

@app.post("/")
def add_data(item: dict):
    data.append(item)
    return data

@app.put("/{i}")
def update_data(i: int, item: dict):
    data[i] = item
    return data

@app.delete("/{i}")
def delete_data(i: int):
    data.pop(i)
    return data
