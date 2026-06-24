import company_service


def start_app():
    want_to_continue = True
    while want_to_continue:
        print("\n===== Company Management System =====")
        print("\nWelcome to the Company Management System")
        print("1. Add a new company")
        print("2. Edit a company")
        print("3. Search for a company")
        print("4. List companies by domain")
        print("5. List companies by industry")  
        print("6. List companies by project")
        print("7. Get company details")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            company_data = {}
            company_data["company_name"] = input("Enter company name: ")
            exists = company_service.company_exists(company_data["company_name"])
            if exists:
                print(f"Company with name '{company_data['company_name']}' already exists.")
                continue
            company_data["address"] = input("Enter address: ")
            company_data["industry_type"] = input("Enter industry type: ")
            company_data["domain"] = input("Enter domain: ")
            company_data["projects"] = input("Enter projects (comma-separated): ").split(",")
            company_data["project_budget"] = float(input("Enter project budget(in $): "))
            company_data["project_timeline"] = input("Enter project timeline(in months): ")

            success, message = company_service.add_company(company_data)
            print(message)
        
        elif choice == "2":
            company_name = input("Enter the name of the company to edit: ")
            exists = company_service.company_exists(company_name)

            if not exists:
                print("Company not found")
            else:
                updated_data = {}
                updated_data["company_name"] = input("Enter new company name: ")
                updated_data["address"] = input("Enter new address: ")
                updated_data["industry_type"] = input("Enter new industry type: ")
                updated_data["domain"] = input("Enter new domain: ")
                updated_data["projects"] = input("Enter new projects (comma-separated): ").split(",")
                updated_data["project_budget"] = float(input("Enter new project budget(in $): "))
                updated_data["project_timeline"] = input("Enter new project timeline: ")

                success, message = company_service.edit_company(company_name, updated_data)
                print(message)  

        elif choice == "3":
            search_name = input("Enter the company name to search: ")
            company = company_service.search_company(search_name)

            if company:
                print(f"Company found: {company}")
        
            else:
                print(f"{search_name} Company not found.") 

        elif choice == "4":
            domain = input("Enter the domain to list companies: ")
            companies = company_service.list_by_domain(domain)

            if companies:
                print(f"Companies in domain '{domain}':")
                for company in companies:
                    print(f"\n Company: {company.get('company_name')}")
            else:
                print(f"No companies found in domain '{domain}'.")
        elif choice == "5":
            industry = input("Enter the industry to list companies: ")
            companies = company_service.list_by_industry(industry)

            if companies:
                print(f"Companies in industry '{industry}':")
                for company in companies:
                    print(f"\n Company: {company.get('company_name')}")
            else:
                print(f"No companies found in industry '{industry}'.")
        elif choice == "6":
            project_name = input("Enter the project name to list companies: ")
            companies = company_service.list_by_project(project_name)

            if companies:
                print(f"Companies working on project '{project_name}':")
                for company in companies:
                    print(f"\n Company: {company.get('company_name')}")
            else:
                print(f"No companies found working on project '{project_name}'.")
        
        elif choice == "7":
            company_name = input("Enter the company name to get details: ")

            company = company_service.get_company_details(company_name)

            if company:
                print("\n===== Company Details =====")
                print(f"Company Name     : {company['company_name']}")
                print(f"Address          : {company['address']}")
                print(f"Industry Type    : {company['industry_type']}")
                print(f"Domain           : {company['domain']}")
                print(f"Projects         : {company['projects']}")
                print(f"Project Budget   : {company['project_budget']}")
                print(f"Project Timeline : {company['project_timeline']}")

            else:
                print(f"No details found for company '{company_name}'.")
        
        elif choice == "8":
            print("Exiting the application.")
            want_to_continue = False                       
        
        else:

            print("Invalid choice. Please enter a number between 1 and 8.")

        if choice != "8":

            continue_choice = input("\nDo you want to continue? (y/n): ")

            if continue_choice.lower() != "y":
                print("Exiting the application.")
                want_to_continue = False