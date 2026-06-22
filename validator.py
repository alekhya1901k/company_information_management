MANDATORY_FIELDS = [
    "company_name",
    "address",
    "industry_type",
    "domain",
    "projects",
    "project_budget",
    "project_timeline"
]


def validate_mandatory_fields(company):
    for field in MANDATORY_FIELDS:
        if field not in company:
            return False, f"{field} is required"

        if isinstance(company[field], str) and company[field].strip() == "":
            return False, f"{field} cannot be empty"

        if isinstance(company[field], list) and len(company[field]) == 0:
            return False, f"{field} cannot be empty"

    return True, "All mandatory fields are present"


def validate_project_budget(budget):
    if not isinstance(budget, (int, float)):
        return False, "Project budget must be numeric"

    if budget <= 0:
        return False, "Project budget must be greater than zero"

    return True, "Project budget is valid"


def is_duplicate_company(company_name, companies):
    for company in companies:
        if company["company_name"].lower() == company_name.lower():
            return True

    return False


def validate_company(company, companies):
    is_valid, message = validate_mandatory_fields(company)

    if not is_valid:
        return False, message

    is_budget_valid, budget_message = validate_project_budget(company["project_budget"])

    if not is_budget_valid:
        return False, budget_message

    if is_duplicate_company(company["company_name"], companies):
        return False, "Company name already exists"

    return True, "Company data is valid"
    