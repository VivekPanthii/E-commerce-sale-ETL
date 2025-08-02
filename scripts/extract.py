import pandas as pd
import os

def extract_new_file(data_dir='data'):
    """Reads the newest CSV file in the data_dir"""

    files =[f for f in os.listdir(data_dir) if f.endswith('.csv')]
    if not files:
        print("No CSV files found in data directory")
        return None, None
    
    latest_file=max(files,key=lambda f: os.path.getctime(os.path.join(data_dir,f)))
    file_path=os.path.join(data_dir,latest_file)

    print(f"Extracting data from the file:{latest_file}")
    df=pd.read_csv(file_path, low_memory=False)

    return df,latest_file