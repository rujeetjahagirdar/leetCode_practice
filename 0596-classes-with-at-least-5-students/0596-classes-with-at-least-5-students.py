import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    result = courses[courses.groupby("class")['student'].transform("count")>=5]['class'].drop_duplicates()
    
    return pd.DataFrame({"class": result})