import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    temp = pd.merge(employee, bonus, left_on="empId", right_on="empId", how="left")
    print(temp)
    result = temp[(temp['bonus']<1000) | (temp['bonus'].isna())]
    return result[['name', 'bonus']]

