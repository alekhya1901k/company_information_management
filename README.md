# Company Information Management CLI Application

## Project Overview

The Company Information Management CLI Application is a Python-based command-line application that manages company information using a JSON flat-file database.

The application allows users to store, update, search, and retrieve company records through a user-friendly command-line interface.

The project follows a layered architecture and Bottom-Up Development Approach to ensure modularity, maintainability, and separation of responsibilities.

---

# Business Requirement

Develop a lightweight company information management system without using a relational database.

The application must:

* Store company information
* Allow creation and modification of company records
* Support searching and retrieval
* Persist data using a flat-file storage mechanism
* Provide a command-line interface for user interaction

---

# Technology Stack

* Python 3.x
* JSON File Storage
* Command Line Interface (CLI)

---

# Features

## Add Company

Create a new company record.

## Edit Company

Update an existing company record.

## Search Company

Search companies by company name.

## List Companies by Domain

Retrieve companies belonging to a specific domain.

## List Companies by Industry

Retrieve companies belonging to a specific industry.

## List Companies by Project

Retrieve companies associated with a specific project.

## Display Company Details

Display complete information of a company.

## Data Persistence

All company records are permanently stored in a JSON file.

---

# Company Information Structure

Each company record contains:

| Field            | Description                  |
| ---------------- | ---------------------------- |
| company_name     | Name of the company          |
| address          | Company address              |
| industry_type    | Industry classification      |
| domain           | Business domain              |
| projects         | List of projects             |
| project_budget   | Budget allocated to projects |
| project_timeline | Project duration             |

---

# Project Structure

```text
company_information_management/
│
├── main.py
├── cli.py
├── company_service.py
├── validator.py
├── file_handler.py
├── companies.json
├── README.md
└── test_cases.md
```

---

# Architecture

```text
User
 |
 v
cli.py
 |
 v
company_service.py
 |
 v
validator.py
 |
 v
file_handler.py
 |
 v
companies.json
```

---

# Module Responsibilities

## main.py

Application entry point.

Responsibilities:

* Start the application
* Invoke CLI layer

---

## cli.py

Presentation Layer.

Responsibilities:

* Display menu
* Accept user input
* Display application output
* Navigate application flow

---

## company_service.py

Business Logic Layer.

Responsibilities:

* Add company
* Edit company
* Search company
* Display company details
* List companies by domain
* List companies by industry
* List companies by project
* Check company existence

---

## validator.py

Validation Layer.

Responsibilities:

* Validate mandatory fields
* Validate project budget
* Check duplicate company names

---

## file_handler.py

Data Access Layer.

Responsibilities:

* Read company records from JSON
* Write company records to JSON
* Handle file operations

---

## companies.json

Storage Layer.

Responsibilities:

* Store company records
* Maintain persistence between executions

---

# Validation Rules

| Validation        | Rule                      |
| ----------------- | ------------------------- |
| Company Name      | Mandatory                 |
| Address           | Mandatory                 |
| Industry Type     | Mandatory                 |
| Domain            | Mandatory                 |
| Projects          | Mandatory                 |
| Project Budget    | Must be Numeric           |
| Project Budget    | Must be Greater Than Zero |
| Project Timeline  | Mandatory                 |
| Duplicate Company | Not Allowed               |

---

# How to Run

## Step 1

Open Command Prompt.

## Step 2

Navigate to project directory.

```cmd
cd D:\company_information_management
```

## Step 3

Run the application.

```cmd
python main.py
```

---

# Sample Menu

```text
===== Company Management System =====

1. Add a new company
2. Edit a company
3. Search for a company
4. List companies by domain
5. List companies by industry
6. List companies by project
7. Get company details
8. Exit
```

---

# Sample Company Record

```json
{
    "company_name": "Forsys",
    "address": "Hyderabad",
    "industry_type": "IT",
    "domain": "Salesforce",
    "projects": [
        "Hitachi Vantara",
        "FDB"
    ],
    "project_budget": 600000.0,
    "project_timeline": "6"
}
```

---

# Testing

The application was tested for:

* Add Company
* Duplicate Company Validation
* Mandatory Field Validation
* Search Existing Company
* Search Non-Existing Company
* List Companies by Domain
* List Companies by Industry
* List Companies by Project
* Display Company Details
* Edit Existing Company
* Edit Non-Existing Company
* Invalid Menu Choice
* Continue Application Flow
* Exit Application Flow
* JSON Persistence Verification

Refer to **test_cases.md** for detailed test scenarios and results.

---

# Error Handling

The application handles:

* Missing JSON file
* Empty JSON file
* Invalid JSON structure
* Missing mandatory fields
* Duplicate company names
* Invalid project budget
* Company not found
* Invalid menu options

---

# Limitations

Current version does not support:

* Delete Company
* Import Data
* Export Data
* CSV File Support
* Logging
* Unit Testing
* Database Integration

---

# Future Enhancements

* Delete Company Functionality
* Import Companies from CSV/JSON
* Export Company Data
* Logging Framework
* Unit Test Coverage
* Database Integration (MySQL/PostgreSQL)
* GUI Interface
* Web-Based Version

---

# Design Approach

The application was developed using a Bottom-Up Development Approach:

### Day 1

Design and Architecture Planning

### Day 2

Data Access Layer (`file_handler.py`)

### Day 3

Validation Layer (`validator.py`)

### Day 4

Business Logic Layer (`company_service.py`)

### Day 5

CLI Layer (`cli.py`) and Application Integration

---

# Conclusion

The Company Information Management CLI Application provides a lightweight and modular solution for managing company information using a JSON flat-file database. The layered architecture ensures separation of concerns, easier maintenance, and future scalability while meeting all current business requirements.
