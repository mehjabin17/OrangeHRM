# OrangeHRM Automation Script

This repository contains an automated test script using **Selenium WebDriver** for the [OrangeHRM Demo Site](https://opensource-demo.orangehrmlive.com/). The script logs in to the system, navigates through the PIM module, creates a new employee with dummy data (with the assistance of the `Faker` library), and finishes basic and personal employee details.

---

## Features

* Automated login with admin credentials
* Navigation to the "Add Employee" section via the PIM module
* Adding an employee with:
* Basic details (name, ID, username, password)
* Personal details (license number, DOB, nationality, etc.)
* Utilization of `Faker` to generate dynamic test usernames
* Utilization of explicit and implicit waits for UI stability

---

## Getting Started

### Prerequisites

* Python 3.x
* Google Chrome browser
* ChromeDriver (of your browser version match) in PATH

### Install dependencies

```bash
pip install selenium faker
```

---

## Running the Script

```bash
python main.py
```

The script will open a Chrome window, log in automatically and create the employee, and prompt you for confirmation before closing.

---

## Project Structure

```bash
.
├── main.py # Main script with all functionality
├── README.md # Project documentation
```

---

## Customization

* You can modify the `add_employee_basic_info` and `fill_employee_personal_details` functions to insert different or random data as per your requirement.
* Add assertions or validations to make this a full test suite.

---

## Disclaimer

This script is intended for learning and demonstration purposes **only**. It is interacting with a public demo system. Do **not** use it for malicious purposes.
