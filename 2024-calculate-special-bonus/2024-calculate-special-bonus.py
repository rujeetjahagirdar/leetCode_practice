import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    mask = (employees['employee_id']%2!=0) & (~employees['name'].str.startswith('M'))
    # print(employees[mask])
    employees['bonus']=0
    employees.loc[mask, 'bonus'] = employees['salary']
    print(employees)

    return employees[['employee_id', 'bonus']].sort_values(by="employee_id")