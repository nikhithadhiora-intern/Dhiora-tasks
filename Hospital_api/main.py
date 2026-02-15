from fastapi import FastAPI
from database import engine, Base
from routers import (
    patients,
    doctors,
    appointments,
    staff,
    beds,
    inventory,
    billing,
    laboratory,
    staffleave,
    telemedicine,
    erx
)

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Hospital Management System")

# include routers
app.include_router(patients.router)
app.include_router(doctors.router)
app.include_router(appointments.router)
app.include_router(staff.router)
app.include_router(beds.router)
app.include_router(inventory.router)
app.include_router(billing.router)
app.include_router(laboratory.router)
app.include_router(staffleave.router)
app.include_router(telemedicine.router)
app.include_router(erx.router)
