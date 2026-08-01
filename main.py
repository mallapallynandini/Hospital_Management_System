from fastapi import FastAPI, Query, Body

app = FastAPI(title="Hospital Management System",description="Hospital Management API using FastAPI",version="1.0")


# Sample Patient Data
patients = [{"id": 1,"patient_name": "Ramu","age": 34,"gender": "Male","blood_group": "O+","disease": "Fever","doctor": "Dr. Sharma","room_type": "General","admission_status": "Admitted"},
    {"id": 2,"patient_name": "Priya ","age":28,"gender": "Female","blood_group": "A+","disease": "Diabetes","doctor": "Dr. Mehta","room_type": "Private","admission_status": "Under Observation"},
    {"id": 3,"patient_name": "laddu","age": 45,"gender": "Male","blood_group": "B+","disease": "BP","doctor": "Dr. Rao","room_type": "Semi-Private","admission_status": "Admitted"},
    {"id": 4, "patient_name": "varsha", "age": 60, "gender": "Female", "blood_group": "AB+", "disease": "Arthritis", "doctor": "Dr. Sharma","room_type": "ICU","admission_status": "Admitted"},
    {"id": 5,"patient_name": "sonu","age": 38,"gender": "Male","blood_group": "O-","disease": "Typhoid","doctor": "Dr. Khan","room_type": "General","admission_status": "Discharged"}]


# Home Route
@app.get("/")
def home():
    return {"message": "Hospital Management API is running!"}


# Get All Patients
@app.get("/patients")
def get_all_patients():
    if len(patients) == 0:
        return {"message": "No patients found"}

    return patients


# Get Patient By ID
@app.get("/patients/{patient_id}")
def get_patient(patient_id: int):
    for patient in patients:
        if patient["id"] == patient_id:
            return patient

    return {"message": f"Patient with ID {patient_id} not found"}



# Register New Patient
@app.post("/patients")
def add_patient(patient: dict = Body(...)):

    for p in patients:
        if p["id"] == patient["id"]:
            return {"message": "Patient ID already exists"}

    patients.append(patient)

    return {"message": "Patient registered successfully","patient": patient}
    


# Update Patient
@app.put("/patients/{patient_id}")
def update_patient(
    patient_id: int,
    updated_data: dict = Body(...)):

    for patient in patients:
        if patient["id"] == patient_id:
            patient.update(updated_data)

            return {"message": "Patient updated successfully","patient": patient}
            

    return {"message": f"Patient with ID {patient_id} not found"}


# Delete Patient
@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int):

    for patient in patients:
        if patient["id"] == patient_id:
            patients.remove(patient)

            return {"message": "Patient deleted successfully","patient": patient}
            

    return {"message": f"Patient with ID {patient_id} not found"}