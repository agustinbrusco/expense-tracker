import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import os
import json

class GoogleSheetsHandler:
    """Handler for Google Sheets operations"""
    
    def __init__(self):
        """Initialize the Google Sheets connection"""
        self.scopes = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
        self.credentials = self._get_credentials()
        self.client = gspread.authorize(self.credentials)
        self.sheet = self._get_or_create_sheet()
        self._ensure_headers()
    
    def _get_credentials(self):
        """Get Google credentials from file or environment variable"""
        # Try to load from file first
        if os.path.exists('credentials.json'):
            return Credentials.from_service_account_file(
                'credentials.json',
                scopes=self.scopes
            )
        
        # Try to load from environment variable
        if 'GOOGLE_CREDENTIALS' in os.environ:
            credentials_dict = json.loads(os.environ['GOOGLE_CREDENTIALS'])
            return Credentials.from_service_account_info(
                credentials_dict,
                scopes=self.scopes
            )
        
        raise ValueError(
            "No Google credentials found. Please provide credentials.json "
            "or set GOOGLE_CREDENTIALS environment variable"
        )
    
    def _get_or_create_sheet(self):
        """Get or create the expense tracker spreadsheet"""
        sheet_name = os.environ.get('SHEET_NAME', 'Expense Tracker')
        
        try:
            # Try to open existing sheet
            spreadsheet = self.client.open(sheet_name)
        except gspread.SpreadsheetNotFound:
            # Create new sheet if it doesn't exist
            spreadsheet = self.client.create(sheet_name)
            # Share with your email if provided
            if 'USER_EMAIL' in os.environ:
                spreadsheet.share(
                    os.environ['USER_EMAIL'],
                    perm_type='user',
                    role='writer'
                )
        
        # Get or create the main worksheet
        try:
            worksheet = spreadsheet.worksheet('Transactions')
        except gspread.WorksheetNotFound:
            worksheet = spreadsheet.add_worksheet(
                title='Transactions',
                rows=1000,
                cols=10
            )
        
        return worksheet
    
    def _ensure_headers(self):
        """Ensure the spreadsheet has proper headers"""
        headers = ['Date', 'Type', 'Amount', 'Category', 'Description', 'Payment Method']
        
        # Check if headers exist
        first_row = self.sheet.row_values(1)
        
        if not first_row or first_row != headers:
            # Set headers
            self.sheet.update('A1:F1', [headers])
            # Format headers (bold)
            self.sheet.format('A1:F1', {
                'textFormat': {'bold': True},
                'backgroundColor': {'red': 0.9, 'green': 0.9, 'blue': 0.9}
            })
    
    def add_entry(self, entry):
        """Add a new entry to the spreadsheet
        
        Args:
            entry (dict): Dictionary containing transaction data
                - date: Transaction date/time
                - type: 'Expense' or 'Income'
                - amount: Transaction amount
                - category: Transaction category
                - description: Transaction description
                - payment_method: Payment method used
        """
        row = [
            entry['date'],
            entry['type'],
            entry['amount'],
            entry['category'],
            entry['description'],
            entry['payment_method']
        ]
        
        self.sheet.append_row(row)
    
    def get_recent_entries(self, limit=10):
        """Get recent entries from the spreadsheet
        
        Args:
            limit (int): Number of recent entries to retrieve
            
        Returns:
            pd.DataFrame: DataFrame containing recent entries
        """
        # Get all values
        all_values = self.sheet.get_all_values()
        
        if len(all_values) <= 1:
            # Only headers or empty
            return None
        
        # Convert to DataFrame
        headers = all_values[0]
        data = all_values[1:]
        
        df = pd.DataFrame(data, columns=headers)
        
        # Return last N entries
        return df.tail(limit)[::-1]  # Reverse to show newest first
    
    def get_all_entries(self):
        """Get all entries from the spreadsheet
        
        Returns:
            pd.DataFrame: DataFrame containing all entries
        """
        all_values = self.sheet.get_all_values()
        
        if len(all_values) <= 1:
            return None
        
        headers = all_values[0]
        data = all_values[1:]
        
        return pd.DataFrame(data, columns=headers)
