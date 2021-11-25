import pandas as pd

def get_dummy_df(df, cat_cols, dummy_na=False):
    """
    It returns dataframe with the cat_cols as dummy columns.

    Input
        df - pandas dataframe with categorical variables you want to dummy.
        dummy_na - boolean, indicates if na values are allowed at creating the dummy columns.
        cat_cols - list, each element is a string with the name of the column to convert to a dummy variable.

    Output
        df_dummy - pandas dataframe with dummy variables to represent its categorical features.
    """
    # Copy the input to prevent from modifying global variables
    temp_df = df.copy()
    cat = temp_df.select_dtypes(include=['object'])
    no_cat = temp_df.drop(cat.columns, axis=1)
    dummy_cat = pd.get_dummies(cat[cat_cols], dummy_na=dummy_na)
    df_dummy = pd.merge(no_cat, dummy_cat, left_index=True, right_index=True)
    return df_dummy

def bool_to_int(in_str):
    """
    It returns 1 if in_str is equal to t, 0 if in_str is equal to f else it returns empty.
    
    Input
        in_str - string, 

    Output
        1,0, , - int

    """

    if in_str == 't':
        return 1
    elif in_str == 'f':
        return 0
    else:
        return

def lis_len(input_list):
    """
    It returns the length if input_list

    Input
        input_list - list with n number of elements, it may be empty 
    Output
        number_of_elem - int, indicates the number of elements in input_list 
    """

    number_of_elem = len(input_list)
    return number_of_elem

def listings_preprocessing(file_path, col_of_interest):
    """
    It preproces the listings.csv file. It converts the columns with prices to float.
    and it filter the columns of the dataframe by col_of_interest.

    Input
        file_path - str with a valid path of the listing.csv file
        col_of_interest - list where each element is a string with the name of the column to keep.
    Output
        df - Pandas dataframe with the information from listings.csv
    """
    df = pd.read_csv(file_path)
    df = df[col_of_interest]

    # Columns to format as float
    col_to_float = ['price', 'weekly_price', 'monthly_price', 'security_deposit']
    for col in col_to_float:
        df[col] = df[col].replace('[\$,]', '', regex=True).astype(float)

    return df

def calendar_preprocessing(file_path, col_of_interest=[]):
    """
    It preprocess the calendar.csv file. It converts the columns with prices.
    It adds some extra columns useful for the Airbnb demand analysis.

    Input
        file_path str - path of the calendar.csv file
        col_of_interest list - list of the column to return in df. if empty it includes all columns
    Output
        df pandas dataframe - 
    """
    df = pd.read_csv(file_path)
    if col_of_interest:
        df = df[col_of_interest]
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
    df['date'] = pd.to_datetime(df['date'])
    df.sort_values(by='date', inplace=True)
    df['available'] = df['available'].apply(bool_to_int)
    df['day_of_week'] = df['date'].dt.day_name()
    df.sort_values(by='date', inplace=True)
    return df