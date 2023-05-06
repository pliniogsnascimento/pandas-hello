import pandas as pd

# Series are an one dimensional array
def create_series():
    # return pd.Series([1, 7, 2], index=['x', 'y', 'z'])
    return pd.Series({"day1": 420, "day2": 380, "day3": 390})

# Dataframe is a 2 dimensional data structure like a 2 dimensional array
def create_dataframe():
    data = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
    }

    return pd.DataFrame(data)

def data_cleaning():
    df = pd.read_csv('data.csv')
    new_df = df.dropna()
    new_df.plot()
    

    print(new_df.to_string())