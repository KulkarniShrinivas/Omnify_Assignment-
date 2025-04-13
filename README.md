
```markdow
# QA Intern Assignment 2025 - OrangeHRM Test Automation and Analysis

## Project Overview

This repository contains the manual and automated testing work completed as part of the QA Intern Assignment 2025. The objective is to analyze the OrangeHRM web application, test its login and employee management functionality, automate key workflows using Selenium and the Page Object Model (POM), and document any defects found during testing.

## Website Under Test

- URL: [https://opensource-demo.orangehrmlive.com/web/index.php/auth/login](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)

![image](https://github.com/user-attachments/assets/73dc9eba-e6ce-4770-bd5a-62c28b40370a)


## Manual Test Deliverables

The `Qa Intern Test Cases` document includes:

- Eight detailed test cases for the login functionality
- Six test cases for employee management (Add, View, Update, Delete)
- A list of three confirmed bugs/usability issues
- Humanized expected and actual results with pass/fail status

## Automation Summary

The automation scripts were written using:

- **Language:** Python
- **Framework:** Selenium WebDriver
- **Design Pattern:** Page Object Model (POM)

### Automated Workflow Implemented

- Login to the OrangeHRM portal using provided credentials
- Navigate to the PIM module
- Add three unique employees
- Scroll through the Employee List to verify their presence
- Log out

### Notes

- Unique employee IDs are generated using the system time to avoid duplication errors
- Verification fails due to known defects in the OrangeHRM demo site:
  - No visual confirmation after saving an employee
  - Added employees do not appear in the list consistently
  - Search functionality fails intermittently

These issues are logged in the test document as confirmed bugs.

## Folder Structure

```
OrangeHRM_Automation/
├── pages/                  # POM-based Page Classes
│   ├── LoginPage.py
│   ├── DashboardPage.py
│   ├── PIMPage.py
│   └── LogoutPage.py
├── tests/                  # Automation test script
│   └── EmployeeTest.py
├── utils/                  # Driver setup
│   └── driver_setup.py
├── Qa Intern Test Cases.docx  # Manual test cases and bug report
└── README.md
```

## How to Run

1. Install requirements:
   ```
   pip install selenium
   ```

2. Run the script:
   ```
   python3 -m tests.EmployeeTest
   ```

3. Chrome browser with chromedriver must be properly set up on your system.

## Bugs Identified

See the `Qa Intern Test Cases` document for details.

```

