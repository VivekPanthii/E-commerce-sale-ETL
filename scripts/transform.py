import pandas as pd

def transform(df):
    """
    Clean and prepare the DataFrame
    """
    if df is None or df.empty:
        print("No Data is available to transform")
        return df
    

    df=df.drop(['index'],axis=1)
    # Drop unnecessary column if it exists
    df = df.drop(['Unnamed: 22'], axis=1, errors='ignore')

    # Drop duplicate rows
    df = df.drop_duplicates()

    # Fill NaN in 'Courier Status' with 'Cancelled'
    df['Courier Status'] = df['Courier Status'].fillna('Cancelled')

    # Fill NaN in 'promotion-ids' with 'No Promo'
    df['promotion-ids'] = df['promotion-ids'].fillna('No Promo')

    # Convert 'Date' to datetime type
    df['Date'] = pd.to_datetime(df['Date'], format='%m-%d-%y', errors='coerce')

    df.columns=df.columns.str.strip()
    df.columns=df.columns.str.replace(' ','_')
    df.columns=df.columns.str.replace('-','_')
    df.columns=df.columns.str.lower()

    return df
