 #Optional, initializes the app if needed

import sqlite3
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import hashlib
from main import main
#===================================================================================================================================
# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create users table
c.execute('''
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username text NOT NULL UNIQUE,
    password text NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

c.execute("""
CREATE TABLE IF NOT EXISTS Assets (
    asset_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INT,
    asset_name text NOT NULL,
    asset_value DECIMAL(15, 2) NOT NULL,
    asset_type text,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
)
""")
c.execute("""
CREATE TABLE IF NOT EXISTS Liabilities (
    liability_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INT,
    liability_name VARCHAR(100) NOT NULL,
    liability_value DECIMAL(15, 2) NOT NULL,
    liability_type VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
)
""")
c.execute("""
CREATE TABLE IF NOT EXISTS Budgets (
    budget_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INT,
    budget_month DATE NOT NULL,
    total_income DECIMAL(15, 2) NOT NULL,
    total_expenses DECIMAL(15, 2) NOT NULL DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
)
""")
c.execute("""
CREATE TABLE IF NOT EXISTS Expenses (
    expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
    budget_id INT,
    user_id INT,
    expense_name VARCHAR(100) NOT NULL,
    expense_value DECIMAL(15, 2) NOT NULL,
    expense_date DATE NOT NULL,
    expense_category VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (budget_id) REFERENCES Budgets(budget_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
)
""")
conn.commit()
conn.close()
#=======================================================================
# Hashing function for passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to create a user in the database
def create_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('INSERT INTO Users (username, password) VALUES (?, ?)', (username, hash_password(password)))
    conn.commit()
    conn.close()

# Function to check if a user exists and the password is correct
def login_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM Users WHERE username = ? AND password = ?', (username, hash_password(password)))
    user = c.fetchone()
    conn.close()
    return user

# Function to delete a user from the database
def delete_user(username):
    conn = sqlite3.connect('Users.db')
    c = conn.cursor()
    c.execute('DELETE FROM Users WHERE username = ?', (username,))
    conn.commit()
    conn.close()

#===================================================================================================================================
def show_dashboard(user_id):
    st.header("Dashboard")
    
    # Connect to SQLite database
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Fetch data from database
    c.execute("SELECT asset_id, asset_name, asset_value, asset_type FROM Assets WHERE user_id = ?", (user_id))
    assets = c.fetchall()
    c.execute("SELECT liability_id, liability_name, liability_value, liability_type FROM Liabilities WHERE user_id = ?", (user_id))
    liabilities = c.fetchall()

    # Convert to DataFrames
    assets_df = pd.DataFrame(assets, columns=['asset_id', 'asset_name', 'asset_value', 'asset_type'])
    liabilities_df = pd.DataFrame(liabilities, columns=['liability_id', 'liability_name', 'liability_value', 'liability_type'])
    assets_df['asset_value'] = pd.to_numeric(assets_df['asset_value'])
    liabilities_df['liability_value'] = pd.to_numeric(liabilities_df['liability_value'])


    # Calculate total assets and liabilities
    total_assets = assets_df['asset_value'].sum()
    total_liabilities = liabilities_df['liability_value'].sum()

    # Create donut pie chart
    labels = ['Assets', 'Liabilities']
    values = [total_assets, total_liabilities]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5)])
    fig.update_traces(textinfo='percent+label')

    st.plotly_chart(fig, use_container_width=True)


     # Add new asset
    with st.expander("Add New Asset"):
        with st.form(key="asset_form"):
            asset_name = st.text_input("Asset Name")
            asset_value = st.number_input("Asset Value", min_value=0.00, step=0.01)
            asset_type = st.selectbox("Asset Type", ["Cash", "Investment", "Real Estate", "Retirement", "Precious Metals", "Collectibles", "Other"])
            submitted = st.form_submit_button("Add Asset")
            if submitted:
                c.execute('INSERT INTO Assets (user_id, asset_name, asset_value, asset_type) VALUES (?, ?, ?, ?)', (user_id[0], asset_name, asset_value, asset_type))
                c.execute("Select * from Assets")
                print(c.fetchall())
                conn.commit()
                st.success(f"Asset '{asset_name}' added successfully!")
    

    # Add new liability
    with st.expander("Add New Liability"):
        with st.form(key="liability_form"):
            liability_name = st.text_input("Liability Name")
            liability_value = st.number_input("Liability Value", min_value=0.00, step=0.01)
            liability_type = st.selectbox("Liability Type", ["Loan", "Credit Card", "Other"])
            submitted = st.form_submit_button("Add Liability")
            if submitted:
                c.execute("INSERT INTO Liabilities (user_id, liability_name, liability_value, liability_type) VALUES (?, ?, ?, ?)", 
                          (user_id[0], liability_name, liability_value, liability_type))
                conn.commit()
                st.success(f"Liability '{liability_name}' added successfully!")


    # Display and manage assets
    with st.expander("View and Manage Assets"):
        for _, row in assets_df.iterrows():
            st.write(f"**{row['asset_name']}** ({row['asset_type']}) - ${row['asset_value']:,.2f}")
            if st.button("Edit", key=f"edit_asset_{row['asset_id']}"):
                with st.form(key=f"edit_asset_form_{row['asset_id']}"):
                    new_name = st.text_input("Asset Name", value=row['asset_name'])
                    new_value = st.number_input("Asset Value", min_value=0.00, step=0.01, value=float(row['asset_value']))
                    new_type = st.selectbox("Asset Type", ["Cash", "Investment", "Real Estate", "Retirement", "Precious Metals", "Collectibles", "Other"], index=["Cash", "Investment", "Real Estate", "Retirement", "Precious Metals", "Collectibles", "Other"].index(row['asset_type']))
                    update_submitted = st.form_submit_button("Update Asset")


                    st.write("Form Key: ", f"edit_asset_form_{row['asset_id']}")
                    st.write("Form Submitted: ", update_submitted)
                    print(update_submitted)


                    if update_submitted:
                        
                        c.execute("UPDATE Assets SET asset_name = ?, asset_value = ?, asset_type = ? WHERE asset_id = ?", (new_name, new_value, new_type, row['asset_id']))
                        conn.commit()
                        st.success(f"Asset '{new_name}' updated successfully!")
                        # st.experimental_rerun()

            if st.button("Delete", key=f"delete_asset_{row['asset_id']}"):
                c.execute("DELETE FROM Assets WHERE asset_id = ?", (row['asset_id'],))
                conn.commit()
                st.success(f"Asset '{row['asset_name']}' deleted successfully!")
                # st.experimental_rerun()

    # Display and manage liabilities
    with st.expander("View and Manage Liabilities"):
        for _, row in liabilities_df.iterrows():
            st.write(f"**{row['liability_name']}** ({row['liability_type']}) - ${row['liability_value']:,.2f}")
            if st.button("Edit", key=f"edit_liability_{row['liability_id']}"):
                with st.form(key=f"edit_liability_form_{row['liability_id']}"):
                    new_name = st.text_input("Liability Name", value=row['liability_name'])
                    new_value = st.number_input("Liability Value", min_value=0.00, step=0.01, value=float(row['liability_value']))
                    new_type = st.selectbox("Liability Type", ["Loan", "Credit Card", "Other"], index=["Loan", "Credit Card", "Other"].index(row['liability_type']))
                    update_submitted = st.form_submit_button("Update Liability")
                    if update_submitted:
                        c.execute("UPDATE Liabilities SET liability_name = ?, liability_value = ?, liability_type = ? WHERE liability_id = ?", 
                                  (new_name, new_value, new_type, row['liability_id']))
                        conn.commit()
                        st.success(f"Liability '{new_name}' updated successfully!")

            if st.button("Delete", key=f"delete_liability_{row['liability_id']}"):
                c.execute("DELETE FROM Liabilities WHERE liability_id = ?", (row['liability_id'],))
                conn.commit()
                st.success(f"Liability '{row['liability_name']}' deleted successfully!")
             




    # # Top 5 Assets by value
    # st.subheader("Top 5 Assets")
    # top_assets = assets_df.nlargest(5, 'asset_value')
    # st.table(top_assets[['asset_name', 'asset_type', 'asset_value']])

    # # Top 5 Liabilities by value
    # st.subheader("Top 5 Liabilities")
    # top_liabilities = liabilities_df.nlargest(5, 'liability_value')
    # st.table(top_liabilities[['liability_name', 'liability_type', 'liability_value']])

    # # Expandable section for Assets
    # with st.expander("View All Assets"):
    #     sorted_assets = assets_df.sort_values(by='asset_value', ascending=False)
    #     st.table(sorted_assets[['asset_name', 'asset_type', 'asset_value']])

    # # Expandable section for Liabilities
    # with st.expander("View All Liabilities"):
    #     sorted_liabilities = liabilities_df.sort_values(by='liability_value', ascending=False)
    #     st.table(sorted_liabilities[['liability_name', 'liability_type', 'liability_value']])


    # Close the database connection
    conn.close()


def show_net_worth():
    st.header("Net Worth")
    # Add components for net worth calculation and display

def manage_budget():
    st.header("Manage Budget")
    # Add components to create and manage budget

def track_expenses():
    st.header("Track Expenses")
    # Add components to input and view expenses

def manage_profile():
    st.header("Manage Profile")
    # Add components to update user profile information


# Function to log out
def logout():
    st.session_state['logged_in'] = False
    st.session_state['username'] = None

def deleteAcct():
    st.warning("Are you sure you want to delete your account? This action cannot be undone.")
    if st.button("Yes, delete my account"):
        delete_user(st.session_state['username'])
        st.session_state['logged_in'] = False
        st.session_state['username'] = None
        st.success("Your account has been deleted.")
        st.stop()  # Stop further execution after account deletion

# Main app content after logging in
def main_page():
    page = st.sidebar.selectbox("Select a page", ["Dashboard", "Net Worth", "Budget", "Expenses", "Profile", "Logout", "Delete Account"])
    st.title(f"Hello, {st.session_state['username']}!")

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT user_id FROM Users WHERE username = ?", (st.session_state['username'],))
    user_id = c.fetchall()
    conn.close()

    if page == "Logout":
        logout()
    elif page == "Delete Account":
        deleteAcct()
    elif page == "Dashboard":
        show_dashboard(user_id[0])
    elif page == "Net Worth":
        show_net_worth()
    elif page == "Budget":
        manage_budget()
    elif page == "Expenses":
        track_expenses()
    elif page == "Profile":
        manage_profile()

#===================================================================================================================================
# Streamlit App
# Initialize session state for login status
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'username' not in st.session_state:
    st.session_state['username'] = None

# Login or Signup selection
if not st.session_state['logged_in']:
    st.title("Login/Signup")
    auth_choice = st.sidebar.selectbox("Choose an option", ["Login", "Signup"])

    if auth_choice == "Signup":
        st.subheader("Create a new account")
        
        new_username = st.text_input("Username")
        new_password = st.text_input("Password", type='password')
        confirm_password = st.text_input("Confirm Password", type='password')
        
        if st.button("Signup"):
            # print(new_password, confirm_password, new_username)
            if new_password == confirm_password:
                try:
                    create_user(new_username, new_password)
                    st.success("Account created successfully! You can now log in.")
                except sqlite3.IntegrityError:
                    st.error("Username already exists. Please choose another one.")
            else:
                st.error("Passwords do not match!")

    if auth_choice == "Login":
        st.subheader("Log in to your account")
        
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')
        
        if st.button("Login"):
            user = login_user(username, password)
            if user:
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.success("Logged in successfully!")
            else:
                st.error("Invalid username or password.")
else:
    main_page()
#===================================================================================================================================