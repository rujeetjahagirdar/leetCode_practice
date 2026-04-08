import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates()
    sorted_salaries = unique_salaries.sort_values(ascending=False)
    # print(sorted_salaries)
    if(len(sorted_salaries)<2):
        result = pd.DataFrame({'SecondHighestSalary':[None]})
    else:
        result = pd.DataFrame({'SecondHighestSalary':[sorted_salaries.iloc[1]]})
    
    return(result)