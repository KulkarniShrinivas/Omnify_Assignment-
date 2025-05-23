
```markdow
# QA Intern Assignment 2025 - OrangeHRM Test Automation and Analysis

## Project Overview

This repository contains the manual and automated testing work completed as part of the QA Intern Assignment 2025. The objective is to analyze the OrangeHRM web application, test its login and employee management functionality, automate key workflows using Selenium and the Page Object Model (POM), and document any defects found during testing.

## Website Under Test

- URL: [https://opensource-demo.orangehrmlive.com/web/index.php/auth/login](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)


![Screenshot from 2025-04-14 00-55-02](https://github.com/user-attachments/assets/cef65169-19ec-4715-b939-4f5a37920f06)


## Manual Test Deliverables

The `Qa Intern Test Cases` document includes:

- Eight detailed test cases for the login functionality
- Six test cases for employee management (Add, View, Update, Delete)
- A list of three confirmed bugs/usability issues
- expected and actual results with pass/fail status

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

