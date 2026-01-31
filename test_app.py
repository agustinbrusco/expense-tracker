#!/usr/bin/env python
"""
Simple test script to verify the app structure and functionality.
This doesn't require Google credentials.
"""

import sys
import os

def test_imports():
    """Test that all required modules can be imported"""
    print("Testing imports...")
    try:
        import streamlit as st
        print("  ✓ Streamlit imported")
        
        import gspread
        print("  ✓ gspread imported")
        
        from google.oauth2.service_account import Credentials
        print("  ✓ Google auth imported")
        
        import pandas as pd
        print("  ✓ pandas imported")
        
        # Test our modules
        import app
        print("  ✓ app module imported")
        
        import google_sheets
        print("  ✓ google_sheets module imported")
        
        return True
    except ImportError as e:
        print(f"  ✗ Import error: {e}")
        return False

def test_app_structure():
    """Test that app.py has the expected structure"""
    print("\nTesting app structure...")
    try:
        import app
        
        # Check main function exists
        assert hasattr(app, 'main'), "main() function missing"
        print("  ✓ main() function exists")
        
        # Check get_sheets_handler function exists
        assert hasattr(app, 'get_sheets_handler'), "get_sheets_handler() function missing"
        print("  ✓ get_sheets_handler() function exists")
        
        return True
    except AssertionError as e:
        print(f"  ✗ Structure error: {e}")
        return False

def test_google_sheets_class():
    """Test that GoogleSheetsHandler class has expected methods"""
    print("\nTesting GoogleSheetsHandler class...")
    try:
        from google_sheets import GoogleSheetsHandler
        
        # Check required methods exist
        required_methods = [
            '_get_credentials',
            '_get_or_create_sheet',
            '_ensure_headers',
            'add_entry',
            'get_recent_entries',
            'get_all_entries'
        ]
        
        for method in required_methods:
            assert hasattr(GoogleSheetsHandler, method), f"{method} method missing"
            print(f"  ✓ {method}() method exists")
        
        return True
    except AssertionError as e:
        print(f"  ✗ Class structure error: {e}")
        return False

def test_configuration_files():
    """Test that configuration files exist"""
    print("\nTesting configuration files...")
    
    files = {
        'requirements.txt': 'Dependencies file',
        'credentials.json.example': 'Example credentials',
        '.env.example': 'Example environment variables',
        'README.md': 'Documentation',
        'QUICKSTART.md': 'Quick start guide'
    }
    
    all_exist = True
    for filename, description in files.items():
        if os.path.exists(filename):
            print(f"  ✓ {filename} exists ({description})")
        else:
            print(f"  ✗ {filename} missing ({description})")
            all_exist = False
    
    return all_exist

def main():
    print("=" * 60)
    print("Expense Tracker - Test Suite")
    print("=" * 60)
    
    tests = [
        test_imports,
        test_app_structure,
        test_google_sheets_class,
        test_configuration_files
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n" + "=" * 60)
    print("Test Results")
    print("=" * 60)
    
    total = len(results)
    passed = sum(results)
    
    print(f"Passed: {passed}/{total}")
    
    if all(results):
        print("\n✓ All tests passed!")
        return 0
    else:
        print("\n✗ Some tests failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())
