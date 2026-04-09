import streamlit as st
import requests

BASE_URL = http://127.0.0.1:8000 

st.title("🎓 Chemistry Hub")

menu = st.sidebar.selectbox("Menu", ["Add Student", "View Students"])

# ------------------ ADD STUDENT ------------------
if menu == "Add Student":
    st.subheader("Add New Student")

    name = st.text_input("Name")
    std = st.number_input("Class", min_value=11, max_value=12)
    contact = st.text_input("Contact")
    doj = st.text_input("Date of Joining (YYYY-MM-DD)")

    if st.button("Submit"):
        data = {
            "name": name,
            "std": std,
            "contact": contact,
            "doj": doj,
            "status": "active"
        }

        res = requests.post(f"{BASE_URL}/add_stu", json=data)

        if res.status_code == 201:
            st.success("Student Added Successfully")
        else:
            st.error("Error adding student")


# ------------------ VIEW STUDENTS ------------------
elif menu == "View Students":
    st.subheader("All Students")

    res = requests.get(f"{BASE_URL}/details")

    if res.status_code == 200:
        data = res.json()
        st.write(data)
    else:
        st.error("Failed to fetch data")