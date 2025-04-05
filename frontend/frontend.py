import streamlit as st
import requests

backend_url = "http://backend-app-backend.default.svc.cluster.local:5000"

st.title("User Management")

menu = st.sidebar.selectbox("Menu", ["Add User", "View Users"])

if menu == "Add User":
    st.header("Add a New User")
    name = st.text_input("Name")
    email = st.text_input("Email")
    if st.button("Add"):
        if name and email:
            response = requests.post(f"{backend_url}/users", json={"name": name, "email": email})
            if response.status_code == 200:
                st.success("User added successfully!")
            else:
                st.error(f"Failed to add user: {response.text}")
        else:
            st.warning("Please enter both name and email.")

elif menu == "View Users":
    st.header("All Users")
    response = requests.get(f"{backend_url}/users")
    if response.status_code == 200:
        users = response.json()
        for user in users:
            st.write(f"**{user['id']} - {user['name']}** ({user['email']})")
    else:
        st.error("Failed to fetch users.")

