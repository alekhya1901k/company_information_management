# Test Cases

## Company Information Management CLI Application

---

## Test Case 1: Add Valid Company

### Objective

Verify that a new company can be added successfully.

### Input

```text
Company Name     : Forsys
Address          : Hyderabad
Industry Type    : IT
Domain           : Salesforce
Projects         : Hitachi Vantara, FDB
Project Budget   : 600000
Project Timeline : 6
```

### Expected Result

```text
Company added successfully
```

### Actual Result

```text
Company added successfully
```

### Status

```text
PASS
```

---

## Test Case 2: Add Company with Empty Company Name

### Objective

Verify mandatory field validation.

### Input

```text
Company Name : Empty
```

### Expected Result

```text
company_name cannot be empty
```

### Actual Result

```text
company_name cannot be empty
```

### Status

```text
PASS
```

---

## Test Case 3: Add Duplicate Company

### Objective

Verify duplicate company validation.

### Input

```text
Company Name : Forsys
```

### Expected Result

```text
Company name already exists
```

### Actual Result

```text
Company name already exists
```

### Status

```text
PASS
```

---

## Test Case 4: Search Existing Company

### Objective

Verify search functionality for an existing company.

### Input

```text
Forsys
```

### Expected Result

```text
Matching company displayed
```

### Actual Result

```text
Matching company displayed
```

### Status

```text
PASS
```

---

## Test Case 5: Search Non-Existing Company

### Objective

Verify search functionality when company does not exist.

### Input

```text
ABC Technologies
```

### Expected Result

```text
No company found
```

### Actual Result

```text
No company found
```

### Status

```text
PASS
```

---

## Test Case 6: List Companies by Domain

### Objective

Verify companies can be listed by domain.

### Input

```text
Salesforce
```

### Expected Result

```text
Matching companies displayed
```

### Actual Result

```text
Matching companies displayed
```

### Status

```text
PASS
```

---

## Test Case 7: List Companies by Industry

### Objective

Verify companies can be listed by industry.

### Input

```text
IT
```

### Expected Result

```text
Matching companies displayed
```

### Actual Result

```text
Matching companies displayed
```

### Status

```text
PASS
```

---

## Test Case 8: List Companies by Project

### Objective

Verify companies can be listed by project.

### Input

```text
Hitachi Vantara
```

### Expected Result

```text
Matching companies displayed
```

### Actual Result

```text
Matching companies displayed
```

### Status

```text
PASS
```

---

## Test Case 9: Display Company Details

### Objective

Verify complete company details are displayed.

### Input

```text
Forsys
```

### Expected Result

```text
===== Company Details =====
Company Name     : Forsys
Address          : Hyderabad
Industry Type    : IT
Domain           : Salesforce
Projects         : ['Hitachi Vantara', 'FDB']
Project Budget   : 600000.0
Project Timeline : 6
```

### Actual Result

```text
===== Company Details =====
Company Name     : Forsys
Address          : Hyderabad
Industry Type    : IT
Domain           : Salesforce
Projects         : ['Hitachi Vantara', 'FDB']
Project Budget   : 600000.0
Project Timeline : 6
```

### Status

```text
PASS
```

---

## Test Case 10: Edit Existing Company

### Objective

Verify an existing company can be updated.

### Input

```text
Company Name     : Forsys
Updated Address  : Bangalore
```

### Expected Result

```text
Company updated successfully
```

### Actual Result

```text
Company updated successfully
```

### Status

```text
PASS
```

---

## Test Case 11: Edit Non-Existing Company

### Objective

Verify edit stops when company does not exist.

### Input

```text
Company Name : ABC Technologies
```

### Expected Result

```text
Company not found
```

### Actual Result

```text
Company not found
```

### Status

```text
PASS
```

---

## Test Case 12: Invalid Menu Choice

### Objective

Verify invalid menu option is handled.

### Input

```text
9
```

### Expected Result

```text
Invalid choice. Please enter a number between 1 and 8.
```

### Actual Result

```text
Invalid choice. Please enter a number between 1 and 8.
```

### Status

```text
PASS
```

---

## Test Case 13: Continue Application

### Objective

Verify user can continue after completing an operation.

### Input

```text
Do you want to continue? (y/n): y
```

### Expected Result

```text
Menu displayed again
```

### Actual Result

```text
Menu displayed again
```

### Status

```text
PASS
```

---

## Test Case 14: Exit Application

### Objective

Verify user can exit the application.

### Input

```text
Do you want to continue? (y/n): n
```

### Expected Result

```text
Exiting the application.
```

### Actual Result

```text
Exiting the application.
```

### Status

```text
PASS
```

---

## Test Case 15: Persistence Verification

### Objective

Verify data is saved permanently in companies.json.

### Steps

```text
1. Add a company
2. Exit the application
3. Run the application again
4. Search for the same company
```

### Expected Result

```text
Previously saved company should still exist
```

### Actual Result

```text
Previously saved company still exists
```

### Status

```text
PASS
```

---

# Test Summary

| Test Case | Description                 | Status |
| --------- | --------------------------- | ------ |
| TC01      | Add Valid Company           | PASS   |
| TC02      | Empty Company Name          | PASS   |
| TC03      | Duplicate Company           | PASS   |
| TC04      | Search Existing Company     | PASS   |
| TC05      | Search Non-Existing Company | PASS   |
| TC06      | List By Domain              | PASS   |
| TC07      | List By Industry            | PASS   |
| TC08      | List By Project             | PASS   |
| TC09      | Display Company Details     | PASS   |
| TC10      | Edit Existing Company       | PASS   |
| TC11      | Edit Non-Existing Company   | PASS   |
| TC12      | Invalid Menu Choice         | PASS   |
| TC13      | Continue Application        | PASS   |
| TC14      | Exit Application            | PASS   |
| TC15      | Persistence Verification    | PASS   |

---

# Overall Result

```text
Total Test Cases Executed : 15
Passed                    : 15
Failed                    : 0

Application Status        : PASS
```
