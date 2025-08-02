from scripts.extract import extract_new_file
from scripts.transform import transform
from scripts.load import load

DB_URL="postgresql://postgres:postgres@localhost:5432/amazon_sales_report"


df,latest_file=extract_new_file()
transf=transform(df)

load(transf,db_uri=DB_URL)