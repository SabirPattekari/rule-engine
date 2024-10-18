# Rule Engine with AST

## Objective
This is a simple 3-tier rule engine application that evaluates user eligibility based on attributes such as age, department, income, and spend. The system uses an Abstract Syntax Tree (AST) to represent conditional rules and allows for dynamic creation, combination, and modification of these rules.

## Features
- *AST Representation*: Converts conditional rules into an Abstract Syntax Tree (AST).
- *Dynamic Rule Creation*: Allows creation of custom rules dynamically.
- *Rule Combination*: Combines multiple rules into a single AST to optimize evaluation.
- *Rule Evaluation*: Evaluates user data against the rule using JSON input.

## Installation

1. *Clone the repository*:
    bash
    git clone <repository-url>
    

2. *Install dependencies*:
    Make sure you have Python and pip installed. Then, run:
    bash
    pip install -r requirements.txt
    

3. *Run the Flask server*:
    bash
    python app.py
    

The server should be running at http://127.0.0.1:5000.

## API Endpoints

### 1. Create Rule
- *Endpoint*: /create_rule
- *Method*: POST
- *Description*: Creates an AST from a rule string.
- *Request Body*:
    json
    {
      "rule_string": "age > 30 AND department == 'Sales'"
    }
    
- *Response*:
    json
    {
      "message": "Rule created successfully",
      "ast": "<AST Representation>"
    }
    

### 2. Combine Rules
- *Endpoint*: /combine_rules
- *Method*: POST
- *Description*: Combines multiple rules into one AST.
- *Request Body*:
    json
    {
      "rules": [
        "age > 30 AND department == 'Sales'",
        "salary > 50000 OR experience > 5"
      ]
    }
    
- *Response*:
    json
    {
      "message": "Rules combined successfully",
      "ast": "<Combined AST Representation>"
    }
    

### 3. Evaluate Rule
- *Endpoint*: /evaluate_rule
- *Method*: POST
- *Description*: Evaluates user data against the combined rule AST.
- *Request Body*:
    json
    {
      "rule_ast": "<AST JSON Representation>",
      "data": {
        "age": 35,
        "department": "Sales",
        "salary": 60000,
        "experience": 3
      }
    }
    
- *Response*:
    json
    {
      "result": true
    }
    

## Sample Rules
- Rule 1: ((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)
- Rule 2: ((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)

## Testing
You can test the application by running the server and using the following cURL commands or Postman to test the APIs.

### Example cURL Commands

1. *Create Rule*:
    bash
    curl -X POST http://127.0.0.1:5000/create_rule -H "Content-Type: application/json" -d '{"rule_string": "age > 30 AND department == \"Sales\""}'
    

2. *Combine Rules*:
    bash
    curl -X POST http://127.0.0.1:5000/combine_rules -H "Content-Type: application/json" -d '{"rules": ["age > 30 AND department == \"Sales\"", "salary > 50000 OR experience > 5"]}'
    

3. *Evaluate Rule*:
    bash
    curl -X POST http://127.0.0.1:5000/evaluate_rule -H "Content-Type: application/json" -d '{"rule_ast": <AST JSON>, "data": {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}}'
    

## Bonus Features
- *Error Handling*: The system checks for invalid rule strings and provides appropriate error messages.
- *Catalog Validations*: Ensures attributes used in the rules are valid.
- *Rule Modifications*: Provides the ability to modify existing rules by updating operators, operands, or adding/removing sub-expressions.

## Future Enhancements
- Add user-defined functions for more advanced conditions.
- Extend the system to support more complex rule combinations and external functions.

## Non-functional Considerations
- *Security Layer*: Consider adding authentication and authorization for managing sensitive rules.
- *Performance Optimizations*: The application could be optimized for performance by caching frequently used rules or adding indexing for faster lookups.

## Running Tests
Unit tests can be found in the tests directory. To run them, use:
```bash
python -m unittest discover tests


### *Key Sections to Review:*
- *Installation*: Clear instructions on how to set up the project.
- *API Endpoints*: Descriptions of how to interact with the rule engine.
- *Sample Rules and Testing*: Sample rules provided with cURL commands for testing the API.
- *Bonus and Non-functional Items*: If you've implemented any bonus features like error handling or performance improvements, highlight them here.