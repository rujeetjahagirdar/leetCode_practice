import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    temp = pd.merge(employee, employee, left_on='managerId', right_on='id', suffixes=("_emp", "_mgr"))
    # print(temp)
    
    result = temp[temp['salary_emp']>temp['salary_mgr']]['name_emp']

    return(pd.DataFrame({'Employee':result}))