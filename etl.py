from scripts.extract import extract_new_file
from scripts.transform import transform
from scripts.load import load
import os
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env into environment

db_uri = os.getenv("DB_URL")
if not db_uri:
    raise ValueError("DATABASE_URI not set in environment")

df,latest_file=extract_new_file()
transf=transform(df)

load(transf,db_uri=db_uri)