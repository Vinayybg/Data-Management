import pandas as pd

def process_employees(df):
    # Task 1: Filter IT department employees
    it_employees = df[df['Department'] == 'IT'].copy()

    # Task 2: Average salary of ALL employees
    avg_salary = round(df['Salary'].mean(), 2)

    # Task 3: Find the oldest employee's name and department
    oldest_row = df.loc[df['Age'].idxmax()]
    oldest_name = oldest_row['Employee_Name']
    oldest_dept = oldest_row['Department']

    # Add as new columns
    it_employees['Average_Salary_All_Employees'] = avg_salary
    it_employees['Oldest_Employee_Name'] = oldest_name
    it_employees['Oldest_Employee_Department'] = oldest_dept

    return it_employees

def get_output_schema():
    return pd.DataFrame({
        'Employee_ID'                  : prep_string(),
        'Employee_Name'                : prep_string(),
        'Department'                   : prep_string(),
        'Age'                          : prep_int(),
        'Salary'                       : prep_decimal(),
        'Hire_Date'                    : prep_string(),
        'City'                         : prep_string(),
        'Average_Salary_All_Employees' : prep_decimal(),
        'Oldest_Employee_Name'         : prep_string(),
        'Oldest_Employee_Department'   : prep_string()
    })