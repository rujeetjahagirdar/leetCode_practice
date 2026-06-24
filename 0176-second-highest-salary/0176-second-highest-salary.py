import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # unique_salaries = employee['salary'].drop_duplicates()
    # sorted_salaries = unique_salaries.sort_values(ascending=False)
    # # print(sorted_salaries)
    # if(len(sorted_salaries)<2):
    #     result = pd.DataFrame({'SecondHighestSalary':[None]})
    # else:
    #     result = pd.DataFrame({'SecondHighestSalary':[sorted_salaries.iloc[1]]})
    
    # return(result)

    unique_salaries = employee.drop_duplicates(subset=['salary'])
    unique_salaries = unique_salaries.nlargest(2, columns=['salary'])

    print(unique_salaries)

    if(len(unique_salaries)<2):
        return pd.DataFrame({"SecondHighestSalary": [None]})
    else:
        return pd.DataFrame({"SecondHighestSalary": [unique_salaries.iloc[-1]['salary']]})