import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Find the maximum salary for each department.
    # Group the employee dataframe by 'departmentId' and find the maximum salary in each group.
    # This creates a mapping of departmentId to its maximum salary.

    # Step 2: Merge the employee data with the max salary information.
    # Join the original employee dataframe with the max salary mapping on 'departmentId'.
    # This adds a 'max_salary' column to each employee row, corresponding to their department's highest salary.

    # Step 3: Filter employees who have the highest salary.
    # Select rows where the employee's 'salary' is equal to the 'max_salary' for their department.

    # Step 4: Join with the department table to get department names.
    # Merge the filtered employee dataframe with the department dataframe on the department ID.
    # This adds the department name to the results.

    # Step 5: Format the final output.
    # Select and rename the columns to 'Department', 'Employee', and 'Salary'.
    # Return the formatted dataframe.
    t=employee.groupby(['departmentId'])['salary'].max()
    # print(t)

    t2 = employee.merge(t, how="inner", left_on=['departmentId', 'salary'], right_on=['departmentId','salary'])
    # print(t2)

    t3 = t2.merge(department, how='left', left_on=['departmentId'], right_on=["id"], suffixes=("_temp","_dept"))
    t3 = t3[['name_dept','name_temp', 'salary']]

    ans = t3.rename(columns={"name_dept": "Department", "name_temp": "Employee", "salary": "Salary"})
    print(ans)

    return ans