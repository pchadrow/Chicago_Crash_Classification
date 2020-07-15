import pandas as pd


def column_cutter(df, threshold):
    """
    Takes in a dataframe and removes columns that have missing data over a specified threshold.
    
    Inputs:
    df: The dataframe to be evaluated for columns with missing data
    threshold: The amount of missing data required to remove the column specified in a float
    
    Output: Returns a new dataframe with columns removed that surpassed the threshold.
    
    Ex: new_df = column_cutter(df, .8)
        will assign a modified version of the original df to new_df with all columns removed that had more than 80% of their values missing.
    
    """
    
    df = df.copy()
    total = df.shape[0]
    columns_dropped = []
    for col in df.columns:
        if df[col].isna().sum() >= float(total*threshold):
            df = df.drop(col, axis = 1)
            columns_dropped.append(col)
    n = '\n'
    print(f'A total of {len(columns_dropped)} columns were removed due to {threshold*100}% or more of the values missing.{n}The columns were{n} {columns_dropped}')
    return df