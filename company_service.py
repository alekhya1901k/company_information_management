from file_handler import read_companies
from file_handler import write_companies

from validator import validate_company


def add_company(company):

    # Read existing companies
    companies = read_companies()

    # Validate company data
    is_valid, message = validate_company(
        company,
        companies
    )

    # Stop if validation fails
    if not is_valid:
        return False, message

    # Add company to list
    companies.append(company)

    # Save updated list
    write_companies(companies)

    return True, "Company added successfully"


def company_exists(company_name):

    companies = read_companies()

    for company in companies:

        if company["company_name"].strip().lower() == company_name.strip().lower():
            return True

    return False

def search_company(search_text):

    companies = read_companies()

    matching_companies = []

    for company in companies:

        if search_text.lower() in company["company_name"].lower():
            matching_companies.append(company)

    return matching_companies


def list_by_domain(domain):

    companies = read_companies()

    matching_companies = []

    for company in companies:

        if company["domain"].lower() == domain.lower():
            matching_companies.append(company)

    return matching_companies


def list_by_industry(industry):

    companies = read_companies()

    matching_companies = []

    for company in companies:

        if company["industry_type"].lower() == industry.lower():
            matching_companies.append(company)

    return matching_companies


def list_by_project(project_name):

    companies = read_companies()

    matching_companies = []

    for company in companies:

        if project_name in company["projects"]:
            matching_companies.append(company)

    return matching_companies


def get_company_details(company_name):

    companies = read_companies()

    for company in companies:
        if company["company_name"].strip().lower() == company_name.strip().lower():
            return company
    return None


def edit_company(company_name, updated_company):

    companies = read_companies()

    for index in range(len(companies)):

        if companies[index]["company_name"].strip().lower() == company_name.strip().lower():

            companies[index] = updated_company

            write_companies(companies)

            return True, "Company updated successfully"

    return False, "Company not found"