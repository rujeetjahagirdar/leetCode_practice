import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    
    direct_reports_count = employee.groupby('managerId')['id'].count()

    direct_report_counts_filtered = direct_reports_count[direct_reports_count>=5]

    result = employee[employee['id'].isin(direct_report_counts_filtered.index)]

    print(result['name'])

    return pd.DataFrame({'name': result['name']})