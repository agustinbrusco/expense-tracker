# 💰 Expense Tracker

A simple and flexible Streamlit app for tracking expenses and income with automatic Google Sheets integration.

## Features

- 📝 Easy-to-use form for quick expense/income entry
- 💳 Track payment methods (Credit Card, Debit Card, Cash, Bank Transfer)
- 🏷️ Categorize transactions (Food, Transportation, Shopping, etc.)
- 📊 Automatic data storage in Google Sheets
- 📱 Clean, responsive interface
- 🔄 Real-time sync with Google Sheets
- 📈 View recent transactions

## Setup Instructions

### 1. Prerequisites

- Python 3.8 or higher
- A Google account
- Google Cloud Project with Sheets API enabled

### 2. Google Cloud Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Google Sheets API:
   - Go to "APIs & Services" > "Library"
   - Search for "Google Sheets API"
   - Click "Enable"
4. Create a Service Account:
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "Service Account"
   - Fill in the service account details
   - Click "Done"
5. Create a key for the Service Account:
   - Click on the service account you just created
   - Go to "Keys" tab
   - Click "Add Key" > "Create new key"
   - Choose "JSON" format
   - Download the JSON file

### 3. Installation

1. Clone this repository:
```bash
git clone https://github.com/agustinbrusco/expense-tracker.git
cd expense-tracker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up credentials:
   - Rename the downloaded JSON key file to `credentials.json`
   - Place it in the root directory of the project
   
   **OR** use environment variables:
   - Copy `.env.example` to `.env`
   - Add your credentials as `GOOGLE_CREDENTIALS` environment variable

4. (Optional) Configure settings:
   - Set `SHEET_NAME` in `.env` to customize your spreadsheet name (default: "Expense Tracker")
   - Set `USER_EMAIL` in `.env` to automatically share the sheet with your email

### 4. Run the Application

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## Usage

1. **Select Transaction Type**: Choose between Expense or Income
2. **Enter Amount**: Input the transaction amount
3. **Choose Category**: Select an appropriate category (categories change based on transaction type)
4. **Add Description**: Optionally add notes or details about the transaction
5. **Select Payment Method**: Choose how you made the payment
6. **Submit**: Click "Add Entry" to save to Google Sheets

Your data is automatically saved to your Google Sheet, which you can access anytime for analysis or backup.

## Project Structure

```
expense-tracker/
├── app.py                      # Main Streamlit application
├── google_sheets.py            # Google Sheets integration
├── requirements.txt            # Python dependencies
├── credentials.json.example    # Example credentials file
├── .env.example               # Example environment variables
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## Security Notes

- Never commit `credentials.json` to version control
- The `.gitignore` file is configured to exclude credentials
- Keep your service account key secure
- Consider using environment variables for production deployments

## Customization

### Categories

You can customize expense and income categories by editing the `categories` lists in `app.py`:

```python
# For expenses
categories = [
    "Food & Dining",
    "Transportation",
    # Add your custom categories here
]
```

### Payment Methods

Modify the payment methods list in `app.py`:

```python
payment_method = st.selectbox(
    "Payment Method",
    ["Credit Card", "Debit Card", "Cash", "Bank Transfer", "Your Custom Method"],
)
```

## Troubleshooting

**Error: "No Google credentials found"**
- Make sure `credentials.json` exists in the project root
- Or set the `GOOGLE_CREDENTIALS` environment variable

**Error: "SpreadsheetNotFound"**
- The app will automatically create a new spreadsheet
- Make sure your service account has necessary permissions

**Error: Permission denied**
- Share your Google Sheet with the service account email
- The email is in your `credentials.json` as `client_email`

## License

This project is open source and available under the MIT License.

## Contributing

Contributions, issues, and feature requests are welcome!
