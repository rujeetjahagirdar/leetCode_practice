import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    conditions = ((triangle['x']+triangle['y']>triangle['z']) & (triangle['z']+triangle['x']>triangle['y']) & (triangle['z']+triangle['y']>triangle['x']))
    
    triangle["triangle"] = conditions.map({True:"Yes", False: "No"})

    return(triangle)