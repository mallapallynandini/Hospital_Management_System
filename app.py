import streamlit as st
import requests

BASE_URL = "https://hospital-management-system-u.onrender.com"

st.title("🏥 Hospital Management System")

menu = st.sidebar.selectbox(
    "Select Option",
    [
        "Home",
        "View All Patients",
        "Search Patient",
        "Register New Patient",
        "Update Patient",
        "Delete Patient"
    ]
)

# ---------------- HOME ----------------
if menu == "Home":
    st.header("Welcome")
    st.write("Hospital Management System using Streamlit and FastAPI.")
    st.write("Use the sidebar to manage patient records.")

# ---------------- VIEW ----------------
elif menu == "View All Patients":
    st.header("All Patients")

    if st.button("Load Patients"):
        response = requests.get(f"{BASE_URL}/patients")

        if response.status_code == 200:
            data = response.json()
            st.write("Total Patients:", len(data))
            st.dataframe(data)
        else:
            st.error("Failed to load patients.")

# ---------------- SEARCH ----------------
elif menu == "Search Patient":
    st.header("Search Patient")

    pid = st.number_input("Patient ID", min_value=1, step=1)

    if st.button("Search"):
        response = requests.get(f"{BASE_URL}/patients/{pid}")

        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("Patient not found.")

# ---------------- REGISTER ----------------
elif menu == "Register New Patient":
    st.header("Register Patient")

    pid = st.number_input("ID", min_value=1)
    name = st.text_input("Patient Name")
    age = st.number_input("Age", min_value=1)

    gender = st.selectbox("Gender", ["Male", "Female", "Other"])

    blood = st.selectbox(
        "Blood Group",
        ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
    )

    disease = st.text_input("Disease")
    doctor = st.text_input("Doctor")

    room = st.selectbox(
        "Room Type",
        ["General", "Semi-Private", "Private", "ICU"]
    )

    status = st.selectbox(
        "Admission Status",
        ["Admitted", "Discharged", "Under Observation"]
    )

    if st.button("Register"):
        patient = {
            "id": pid,
            "patient_name": name,
            "age": age,
            "gender": gender,
            "blood_group": blood,
            "disease": disease,
            "doctor": doctor,
            "room_type": room,
            "admission_status": status
        }

        response = requests.post(f"{BASE_URL}/patients", json=patient)

        if response.status_code == 200:
            st.success("Patient Registered Successfully")
            st.json(response.json())
        else:
            st.error("Registration Failed")

# ---------------- UPDATE ----------------
elif menu == "Update Patient":
    st.header("Update Patient")

    pid = st.number_input("Patient ID", min_value=1)

    name = st.text_input("Patient Name")
    age = st.number_input("Age", min_value=1)

    gender = st.selectbox("Gender", ["Male", "Female", "Other"])

    blood = st.selectbox(
        "Blood Group",
        ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
    )

    disease = st.text_input("Disease")
    doctor = st.text_input("Doctor")

    room = st.selectbox(
        "Room Type",
        ["General", "Semi-Private", "Private", "ICU"]
    )

    status = st.selectbox(
        "Admission Status",
        ["Admitted", "Discharged", "Under Observation"]
    )

    if st.button("Update"):
        patient = {
            "patient_name": name,
            "age": age,
            "gender": gender,
            "blood_group": blood,
            "disease": disease,
            "doctor": doctor,
            "room_type": room,
            "admission_status": status
        }

        response = requests.put(
            f"{BASE_URL}/patients/{pid}",
            json=patient
        )

        if response.status_code == 200:
            st.success("Patient Updated Successfully")
            st.json(response.json())
        else:
            st.error("Patient Not Found")

# ---------------- DELETE ----------------
elif menu == "Delete Patient":
    st.header("Delete Patient")

    pid = st.number_input("Patient ID", min_value=1)

    confirm = st.checkbox("I confirm deletion")

    if st.button("Delete") and confirm:
        response = requests.delete(f"{BASE_URL}/patients/{pid}")

        if response.status_code == 200:
            st.success("Patient Deleted Successfully")
            st.json(response.json())
        else:
            st.error("Patient Not Found")
