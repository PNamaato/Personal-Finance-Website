# Main Streamlit app file

import streamlit as st
import pandas as pd
from data import load_data, save_data
from utils import calculate_net_worth, create_pie_chart
from auth import login, logout

st.set_page_config(page_title="Budgeting App", layout="wide")


def main():
        st.title("Budgeting Tool")
        page = st.sidebar.selectbox("Select a page", ["Dashboard", "Net Worth", "Budget", "Expenses", "Profile", "Logout"])
        
        if page == "Logout":
            # logout()
            pass
            #st.experimental_rerun()  # Refresh the page
        elif page == "Dashboard":
            show_dashboard()
        elif page == "Net Worth":
            show_net_worth()
        elif page == "Budget":
            manage_budget()
        elif page == "Expenses":
            track_expenses()
        elif page == "Profile":
            manage_profile()

def show_dashboard():
    st.header("Dashboard")
    st.write(f"Welcome to your dashboard, !")

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

if __name__ == "__main__":
    main()
