from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Details(BaseModel):
    name: str
    age: int
    aadhar: str
    legacyID: int
    cardType: str
    status: str



detailsobj = [
    Details(
        name="Rajesh",
        age=25,
        aadhar="1234-5678-9012",
        legacyID=1,
        cardType="Debit",
        status="Active"
    ),
    Details(
        name="Ramya",
        age=30,
        aadhar="2345-6789-0123",
        legacyID=2,
        cardType="Credit",
        status="Inactive"
    ),
    Details(
        name="Rahul",
        age=28,
        aadhar="3456-7890-1234",
        legacyID=3,
        cardType="Debit",
        status="Active"
    ),
]



@app.get("/")
def home():
    return {"message": "Welcome  Card Management System"}


@app.get("/details")
def get_all_details():
    return detailsobj


@app.post("/details")
def add_details(detail: Details):
    detailsobj.append(detail)
    return {"message": "Record added successfully", "data": detail}


@app.put("/details/{id}")
def update(id: int, updated_detail: Details):
    for index, d in enumerate(detailsobj):
        if d.legacyID == id:
            updated_detail.legacyID = id  
            detailsobj[index] = updated_detail
            return {"message": "Record updated successfully", "data": updated_detail}
    raise HTTPException(status_code=404, detail="Record not found")


@app.delete("/details/{id}")
def delete(id: int):
    for d in detailsobj:
        if d.legacyID == id:
            detailsobj.remove(d)
            return {"message": "Record deleted successfully"}
    raise HTTPException(status_code=404, detail="Record not found")

        