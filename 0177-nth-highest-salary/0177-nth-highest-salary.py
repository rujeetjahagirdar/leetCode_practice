import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salary = employee['salary'].drop_duplicates()
    # print(type(unique_salary))
    result = unique_salary.nlargest(N).reset_index(drop=True)
    # print(result)
    if(len(result)<N or N<=0):
        return pd.DataFrame({f'getNthHighestSalary({N})':[None]})
    else:
        return pd.DataFrame({f'getNthHighestSalary({N})':[result.iloc[-1]]})