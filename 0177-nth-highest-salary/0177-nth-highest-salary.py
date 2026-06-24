import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salaries = employee.drop_duplicates(subset='salary')

    temp = unique_salaries.nlargest(N, columns=["salary"])
    print(temp)

    if(len(temp)<N or N<=0):
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})
    else:
        return pd.DataFrame({f"getNthHighestSalary({N})": [temp.iloc[-1]['salary']]})