import streamlit as st
from datetime import datetime
from google_sheets import GoogleSheetsHandler
import os

# Page configuration
st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",
    layout="centered"
)

# Initialize Google Sheets handler
@st.cache_resource
def get_sheets_handler():
    """Initialize and cache the Google Sheets handler"""
    return GoogleSheetsHandler()

def main():
    st.title("💰 Expense Tracker")
    st.markdown("Track your expenses and income easily!")
    
    # Initialize sheets handler
    try:
        sheets = get_sheets_handler()
    except Exception as e:
        st.error(f"Error connecting to Google Sheets: {str(e)}")
        st.info("Please make sure you have set up your Google Sheets credentials correctly.")
        st.stop()
    
    # Form for expense/income entry
    with st.form("expense_form"):
        st.subheader("Add New Entry")
        
        # Transaction type
        transaction_type = st.radio(
            "Type",
            ["Expense", "Income"],
            horizontal=True
        )
        
        # Amount
        amount = st.number_input(
            "Amount",
            min_value=0.01,
            step=0.01,
            format="%.2f",
            help="Enter the amount in your currency"
        )
        
        # Category
        if transaction_type == "Expense":
            categories = [
                "Food & Dining",
                "Transportation",
                "Shopping",
                "Entertainment",
                "Bills & Utilities",
                "Healthcare",
                "Education",
                "Travel",
                "Other"
            ]
        else:
            categories = [
                "Salary",
                "Freelance",
                "Investment",
                "Gift",
                "Other"
            ]
        
        category = st.selectbox(
            "Category",
            categories,
            help="Select the category for this transaction"
        )
        
        # Description
        description = st.text_area(
            "Description",
            placeholder="Enter a description (optional)",
            help="Add any notes or details about this transaction"
        )
        
        # Payment method
        payment_method = st.selectbox(
            "Payment Method",
            ["Credit Card", "Debit Card", "Cash", "Bank Transfer", "Other"],
            help="How did you make this payment?"
        )
        
        # Submit button
        submitted = st.form_submit_button("Add Entry", use_container_width=True)
        
        if submitted:
            if amount > 0:
                # Prepare data
                entry = {
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "type": transaction_type,
                    "amount": amount,
                    "category": category,
                    "description": description,
                    "payment_method": payment_method
                }
                
                try:
                    # Add to Google Sheets
                    sheets.add_entry(entry)
                    st.success(f"✅ {transaction_type} of ${amount:.2f} added successfully!")
                    st.balloons()
                except Exception as e:
                    st.error(f"Error adding entry: {str(e)}")
            else:
                st.error("Please enter a valid amount greater than 0")
    
    # Display recent entries
    st.markdown("---")
    st.subheader("Recent Entries")
    
    try:
        recent_entries = sheets.get_recent_entries(limit=10)
        if recent_entries is not None:
            st.dataframe(
                recent_entries,
                use_container_width=True,
                hide_index=True
            )
        else:
            st.info("No entries yet. Add your first transaction above!")
    except Exception as e:
        st.warning(f"Could not load recent entries: {str(e)}")
    
    # Footer
    st.markdown("---")
    st.markdown("*Data is automatically saved to your Google Sheet*")

if __name__ == "__main__":
    main()
