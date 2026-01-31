# Quick Start Guide

## First Time Setup

1. **Get Google Credentials**
   - Follow the Google Cloud Setup steps in README.md
   - Download your `credentials.json` file
   - Place it in the project root directory

2. **Install & Run**
   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   ```

3. **First Use**
   - The app will automatically create a Google Sheet named "Expense Tracker"
   - You can find it in your Google Drive
   - The sheet will have a "Transactions" worksheet with your data

## Daily Usage

1. Open the app: `streamlit run app.py`
2. Fill in the form:
   - Choose Expense or Income
   - Enter the amount
   - Select category
   - Add description (optional)
   - Choose payment method
3. Click "Add Entry"
4. Your data is saved to Google Sheets automatically!

## Tips

- **Categories change** based on whether you select Expense or Income
- **View your data** in Google Sheets for analysis, charts, or export
- **Recent entries** are shown at the bottom of the app
- **Data is synced** in real-time to your Google Sheet

## Customization

### Change Sheet Name
Create a `.env` file:
```
SHEET_NAME=My Personal Budget
```

### Auto-share Sheet
Add your email to `.env`:
```
USER_EMAIL=your-email@gmail.com
```

### Add Custom Categories
Edit the `categories` list in `app.py`

## Troubleshooting

### "No Google credentials found"
- Make sure `credentials.json` is in the project root
- Check the file name (it's case-sensitive)
- Verify the JSON format is valid

### "Permission denied"
- Share your Google Sheet with the service account email
- The email is in `credentials.json` under `client_email`

### Cannot find the sheet
- Check your Google Drive for "Expense Tracker" spreadsheet
- The app creates it automatically on first run
- You can change the name with SHEET_NAME environment variable
