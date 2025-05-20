import streamlit as st
from cryptography.fernet import Fernet
import hashlib, json, os, time

# File paths
DATA_FILE = "data.json"
ATTEMPTS_FILE = "attempts.json"

# Helper functions for file I/O
def load_json(file):
    if os.path.exists(file):
        with open(file, "r") as f:
            return json.load(f)
    return {}

def save_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f)

# Session state initialization
if "fernet_key" not in st.session_state:
    st.session_state.fernet_key = Fernet.generate_key()

if "authorized" not in st.session_state:
    st.session_state.authorized = True

fernet = Fernet(st.session_state.fernet_key)
stored_data = load_json(DATA_FILE)
failed_attempts = load_json(ATTEMPTS_FILE)

# Utility to hash passkeys
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# Function to store data
def store_data(user_id, text, passkey):
    encrypted = fernet.encrypt(text.encode()).decode()
    hashed_key = hash_passkey(passkey)
    stored_data[user_id] = {"data": encrypted, "passkey": hashed_key}
    save_json(DATA_FILE, stored_data)
    st.success("Data stored securely.")

# Function to retrieve data
def retrieve_data(user_id, passkey):
    if user_id not in stored_data:
        st.error("User not found.")
        return

    if failed_attempts.get(user_id, 0) >= 3:
        st.session_state.authorized = False
        st.warning("Too many failed attempts. Please login again.")
        time.sleep(1)
        st.rerun()
        return

    if hash_passkey(passkey) == stored_data[user_id]["passkey"]:
        decrypted = fernet.decrypt(stored_data[user_id]["data"].encode()).decode()
        st.success(f"Decrypted data: {decrypted}")
        failed_attempts[user_id] = 0
    else:
        failed_attempts[user_id] = failed_attempts.get(user_id, 0) + 1
        attempts_left = 3 - failed_attempts[user_id]
        st.error(f"Incorrect passkey. Attempts left: {attempts_left}")

    save_json(ATTEMPTS_FILE, failed_attempts)

# Login screen
def login_page():
    st.title("🔐 Admin Login")
    user = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if user == "admin" and password == "admin123":
            st.session_state.authorized = True
            failed_attempts.clear()
            save_json(ATTEMPTS_FILE, failed_attempts)
            st.success("Login successful. Redirecting...")
            time.sleep(1)
            st.rerun()
        else:
            st.error("Invalid credentials.")

# Main app interface
def main():
    if not st.session_state.authorized:
        login_page()
        return

    st.sidebar.title("🔐 Menu")
    option = st.sidebar.radio("Select", ["Home", "Store", "Retrieve", "Login"])

    if option == "Home":
        st.title("Welcome to Secure Vault")
        st.info("Use the sidebar to store or retrieve encrypted data.")

    elif option == "Store":
        st.title("📥 Store Encrypted Data")
        user_id = st.text_input("User ID")
        text = st.text_area("Data to Encrypt")
        passkey = st.text_input("Passkey", type="password")
        if st.button("Save Data"):
            if user_id and text and passkey:
                store_data(user_id, text, passkey)
            else:
                st.warning("Please fill all fields.")

    elif option == "Retrieve":
        st.title("🔓 Retrieve Encrypted Data")
        user_id = st.text_input("User ID")
        passkey = st.text_input("Passkey", type="password")
        if st.button("Decrypt"):
            if user_id and passkey:
                retrieve_data(user_id, passkey)
            else:
                st.warning("Both fields are required.")

    elif option == "Login":
        login_page()

if __name__ == "__main__":
    main()
