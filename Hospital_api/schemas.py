from pydantic import BaseModel
from typing import Optional
from datetime import date


class PatientBase(BaseModel):
    name: str
    age: int
    gender: str
    contact: str


class PatientCreate(PatientBase):
    pass


class PatientResponse(PatientBase):
    id: int

    class Config:
        from_attributes = True





class DoctorBase(BaseModel):
    name: str
    specialty: str
    available: bool

class Doctor(DoctorBase):
    id: int
    class Config:
        orm_mode = True

class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: date
    appointment_time: Optional[str] =None
    status: str


class AppointmentCreate(AppointmentBase):
    pass


class AppointmentResponse(AppointmentBase):
    id: int

    class Config:
        from_attributes = True

class StaffBase(BaseModel):
    name: str
    role: str
    shift: str
    contact: Optional[str] =None
class StaffCreate(StaffBase):
    pass   

class Staff(StaffBase):
    id: int
    class Config:
        from_attributes = True
from pydantic import BaseModel
from datetime import date

# ---------- STAFF ----------
class StaffCreate(BaseModel):
    name: str
    role: str
    shift: str
    contact: str

class StaffResponse(StaffCreate):
    id: int

    class Config:
        from_attributes = True


# ---------- LEAVES ----------
class StaffLeaveCreate(BaseModel):
    staff_id: int
    leave_date: date
    reason: str | None = None

class StaffLeaveResponse(StaffLeaveCreate):
    id: int
    status: str

    class Config:
        from_attributes = True



class BedBase(BaseModel):
    bed_number: str
    ward: str
    occupied: bool = False
class BedCreate(BedBase):
    pass    

class Bed(BedBase):
    id: int
    class Config:
        orm_mode = True


class InventoryBase(BaseModel):
    item_name: str
    quantity: int

class Inventory(InventoryBase):
    id: int
    class Config:
        orm_mode = True


class BillingBase(BaseModel):
    patient_id: int
    amount: float
    status: str
    payment_method: str | None = None

class BillingCreate(BillingBase):
    pass

class Billing(BillingBase):
    id: int

    class Config:
        from_attributes = True



class LabTestBase(BaseModel):
    patient_id: int
    test_name: str
    result: Optional[str] = None

class LabTest(LabTestBase):
    id: int
    class Config:
        orm_mode = True

from pydantic import BaseModel
from datetime import date
from typing import Optional

class TelemedicineBase(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: date
    meeting_link: str
    status: Optional[str] = "scheduled"
    notes: Optional[str] = None

class TelemedicineCreate(TelemedicineBase):
    pass

class TelemedicineResponse(TelemedicineBase):
    id: int

    class Config:
        from_attributes = True
        
class ERXBase(BaseModel):
    patient_id: int
    doctor_id: int
    telemedicine_id: Optional[int] = None
    prescription_date: date
    medicines: str
    dosage: str
    instructions: Optional[str] = None

class ERXCreate(ERXBase):
    pass

class ERXResponse(ERXBase):
    id: int

    class Config:
        from_attributes = True

