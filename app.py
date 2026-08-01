import streamlit as st
import requests

BASE_URL = "https://hospital-management-system-u.onrender.com"
st.set_page_config(page_title="Hospital Management System")

st.title("🏥 Hospital Management System")

menu = st.sidebar.selectbox("Navigation",["Home","View All Patients","Search Patient","Update Patient","Delete Patient"])


# HOME PAGE
if menu == "Home":

    st.header("Welcome")

    st.write("This Hospital Management System helps manage patient records.")

    st.success("Welcome Receptionist!")

# VIEW ALL PATIENTS
elif menu == "View All Patients":

    st.header("All Patients")

    if st.button("Load Patients"):

        response = requests.get(f"{BASE_URL}/patients")

        if response.status_code == 200:

            data = response.json()

            if isinstance(data, list) and len(data) > 0:

                st.write(f"Total Patients: {len(data)}")

                for patient in data:
                    st.json(patient)
                    st.write("----------------------------")

            else:
                st.warning("No patients found")

# SEARCH PATIENT
elif menu == "Search Patient":

    st.header("Search Patient By ID")

    patient_id = st.number_input("Enter Patient ID",min_value=1,step=1)

    if st.button("Search"):

        response = requests.get(
            f"{BASE_URL}/patients/{patient_id}")

        data = response.json()

        if "id" in data:
            st.success("Patient Found")
            st.json(data)
        else:
            st.error(data["message"])

# UPDATE PATIENT
elif menu == "Update Patient":

    st.header("Update Patient")

    patient_id = st.number_input("Patient ID",min_value=1,step=1)


    updated_data = {"patient_name": st.text_input("Patient Name"),"age": st.number_input("Age", min_value=1, step=1),"gender": st.selectbox("Gender",["Male", "Female", "Other"]),"blood_group": st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]),"disease": st.text_input("Disease"),"doctor": st.text_input("Doctor"),"room_type": st.selectbox("Room Type",["General", "Semi-Private", "Private", "ICU"]),"admission_status": st.selectbox("Admission Status",["Admitted", "Discharged", "Under Observation"])}
        

    if st.button("Update Patient"):

        response = requests.put(f"{BASE_URL}/patients/{patient_id}",json=updated_data)
        

        st.success(response.json()["message"])

# DELETE PATIENT
elif menu == "Delete Patient":

    st.header("Delete Patient")

    patient_id = st.number_input("Patient ID",min_value=1,step=1)
    

    confirm = st.checkbox("I confirm patient deletion")
    

    if st.button("Delete") and confirm:

        response = requests.delete(f"{BASE_URL}/patients/{patient_id}")
        

        data = response.json()

        st.success(data["message"])