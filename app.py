import streamlit as st
import mysql.connector
import pyodbc
import base64
from time import sleep
from db_utils import save_file_details
from v3 import encrypt_file_ui
from Decryption import decrypt_file_ui
from navigation import make_sidebar
from dNFT import UI_NFT_download
from track import ui_track
import json


# Connect to the MySQL database
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
            user="root",
            password="",
            database="project"
    )


# Function to save a new user
def save_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        st.write("Attempting to insert:", username, password)
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        st.write("User successfully inserted into database.")
    except mysql.connector.Error as err:
        st.error(f"Database Error: {err}")
    finally:
        cursor.close()
        conn.close()


# Function to check if a user exists
def check_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        return user
    except mysql.connector.Error as err:
        st.error(f"Database Error: {err}")
    finally:
        cursor.close()
        conn.close()





def get_user_files(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT file_name, ipfs_link, encryption_key FROM files WHERE user_id = %s", (user_id,))
        files = cursor.fetchall()
        return files
    except mysql.connector.Error as err:
        st.error(f"Database Error: {err}")
    finally:
        cursor.close()
        conn.close()

# Function to handle page navigation
def handle_navigation():
    selected_page = st.sidebar.selectbox("Choose a page", ["Home", "Encryption", "Decryption","NFT-Download","Track NFT"])
    
    if selected_page == "Home":
        st.title("Your Encrypted Files")
        
        # Get the logged-in user's ID
        user_id = st.session_state.get('user_id')
        if user_id:
            files = get_user_files(user_id)
            if files:
                for file_name, ipfs_link, encryption_key in files:
                    st.write(f"**File Name:** {file_name}")
                    try:
                        if ipfs_link:
                            ipfs_link_dict = json.loads(ipfs_link)
                            url = ipfs_link_dict.get('ipfs_storage', {}).get('ipfs_url', 'No URL found')
                        else:
                            url = 'No IPFS link provided'
                    except json.JSONDecodeError as e:
                        st.error(f"Error parsing IPFS link: {e}")
                        url = 'Invalid IPFS link format'
                    except Exception as e:
                        st.error(f"Unexpected error: {e}")
                        url = 'Error retrieving IPFS link'

                    st.write(f"**IPFS Link:** [Link]({url})")
                    st.write(f"**Key :** {encryption_key}")
                    st.markdown("---")
            else:
                st.write("No encrypted files found.")
        else:
            st.error("User ID not found. Please log in again.")

    elif selected_page == "Encryption":
        encrypt_file_ui()
    elif selected_page == "Decryption":
        decrypt_file_ui()
    elif selected_page=="NFT-Download":
        UI_NFT_download()
    elif selected_page=='Track NFT':
        ui_track()

    # Logout button
    st.sidebar.markdown("---")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.login_username = ""
        st.session_state.user_id = None
        st.success("You have logged out successfully!")
        sleep(0.5)
        st.experimental_rerun()



# Sidebar and Logout button
make_sidebar()
if 'logged_in' in st.session_state and st.session_state.logged_in:
    handle_navigation()

# Main Application Logic
else:
    # Tabs for registration and login
    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab2:
        st.header("Register")
        with st.form("register_form"):
            st.write("Create a new account.")
            reg_username = st.text_input("Username")
            reg_password = st.text_input("Password", type="password")
            reg_confirm_password = st.text_input("Confirm Password", type="password")

            reg_submit = st.form_submit_button("Register")

            if reg_submit:
                if reg_password == reg_confirm_password:
                    save_user(reg_username, reg_password)
                    st.success("Registration successful!")
                    st.session_state.registration_success = True
                else:
                    st.error("Passwords do not match.")

    with tab1:
        st.header("Login")
        with st.form("login_form"):
            st.write("Already have an account? Log in here.")
            login_username = st.text_input("Username", key="login_username")
            login_password = st.text_input("Password", type="password", key="login_password")

            login_submit = st.form_submit_button("Login")

            if login_submit:
                user = check_user(login_username, login_password)
                if user:
                    st.session_state.logged_in = True
                    st.session_state.user_id = user[0]  # Assuming user[0] contains the user_id
                    st.success("Logged in successfully!")
                    sleep(0.5)
                    st.experimental_rerun()
                else:
                    st.error("Incorrect username or password.")

