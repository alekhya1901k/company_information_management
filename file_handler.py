import json
import os


DATA_FILE = "companies.json"

def read_companies():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            companies = json.load(file)
            return companies

    except json.JSONDecodeError:
        return []


def write_companies(companies):
    with open(DATA_FILE, "w") as file:
        json.dump(companies, file, indent=4)


companies = read_companies()

new_company = {
    "company_name": "XYZ Solutions",
    "address": "Plano, Texas",
    "industry_type": "Finance",
    "domain": "Banking",
    "projects": ["Loan Processing System"],
    "project_budget": 75000,
    "project_timeline": "8 Months"
}

companies.append(new_company)

write_companies(companies)

print("Company saved successfully.")