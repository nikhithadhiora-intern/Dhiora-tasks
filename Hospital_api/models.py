from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from database import Base

class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    contact = Column(String)

class Doctor(Base):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    specialty = Column(String)
    available = Column(Boolean, default=True)


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    appointment_date = Column(Date)
    appointment_time = Column(String)
    status = Column(String)


class Staff(Base):
    __tablename__ = "staff"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    role = Column(String)
    shift = Column(String)
    contact = Column(String)

class Bed(Base):
    __tablename__ = "beds"
    id = Column(Integer, primary_key=True, index=True)
    bed_number = Column(String,nullable =False)
    ward = Column(String)
    occupied = Column(Boolean, default=False)

class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String)
    quantity = Column(Integer)

class Billing(Base):
    __tablename__ = "billing"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    status = Column(String, nullable=False)   # paid / unpaid / pending
    payment_method = Column(String, nullable=True)


class LabTest(Base):
    __tablename__ = "lab_tests"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer)
    test_name = Column(String)
    result = Column(String, nullable=True)

