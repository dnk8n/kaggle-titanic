import pandas as pd
import numpy as np

if __name__ == "__main__":
    df = pd.read_csv("train.csv")
    print(df.head())
    print()

def one_hot_encode(dataframe, column_name, prefix = None):
    """
    Returns dataframe with one-hot encoding of variable in column_name
    """
    if not prefix:
        prefix = column_name
    return pd.get_dummies(dataframe,columns=[column_name],prefix=prefix)

def one_hot_encode_categorical_variables(dataframe,category_count_definer,exception_list = ['Survived']):
    """
    One-hot encodes variables which take on fewer than category_count_definer many values
    """
    oh_columns = []
    for col in dataframe.columns:
        if dataframe[col].unique().shape[0] <= category_count_definer:
            oh_columns.append(col)
    df = pd.DataFrame(dataframe)
    for col in oh_columns:
        if col not in exception_list:
            df = one_hot_encode(dataframe=df,column_name=col)
    return df

