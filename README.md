# Local CSV to PostgreSQL ETL Pipeline with Pandas, SQLAlchemy, and dotenv

This project implements a simple ETL (Extract, Transform, Load) pipeline that extracts data from the newest CSV file in a local directory, transforms it using Pandas, and loads it into a PostgreSQL database. The pipeline dynamically creates the database and table if they do not exist, enabling automated data ingestion. Database connection details are securely loaded from a `.env` file.

---

## 🚀 Project Overview

This project serves as a practical example of building a modular ETL pipeline with Python. It automates loading CSV data from local files into PostgreSQL using Pandas for transformation and SQLAlchemy for database interaction. Environment variables are used to securely manage sensitive database credentials.

---

## 🧩 Features

- Detect and extract the newest CSV file from a local directory automatically.
- Perform data cleaning and preparation using Pandas.
- Dynamically create PostgreSQL database and tables if they don’t exist.
- Append data with simple SCD Type 0 (no history tracking).
- Modular ETL functions separated into `extract`, `transform`, and `load` scripts.
- Secure database connection via `.env` environment variables using `python-dotenv`.

---

## 📂 Project Structure

```plaintext
.
├── data/                  # Folder for CSV files
├── scripts/               # Python modules: extract.py, transform.py, load.py
├── .env                   # Environment variables (not committed)
├── .gitignore             # Ignoring .env and other files
├── etl.py                 # Main script to run the ETL pipeline
├── requirements.txt       # Python dependencies
├── README.md              # This documentation


---

## ⚙️ How to Use

1. Place your CSV files inside the `data/` directory.

2. Create a `.env` file in the project root with your PostgreSQL connection string:

```bash
DB_URL=postgresql://username:password@host:port/dbname

3. Ensure .env is added to .gitignore to avoid committing sensitive data.

4. Install dependencies:

```bash
pip install -r requirements.txt

5. Run the ETL pipeline:

```bash
python etl.py



The script will:

- Detect the newest CSV file in data/.

- Extract and transform data using Pandas.

- Create the PostgreSQL database and table if missing.

- Load cleaned data into the database.



---

## 🚧 Limitations & Future Improvements

- Currently supports only append mode (SCD Type 0) without tracking data changes.

- No orchestration or scheduling implemented (can add Airflow or cron jobs).

- Transformation logic is basic; can be extended with validation, testing, and error handling.

- Database creation logic is PostgreSQL-specific; adding support for other databases is a future enhancement.



---

## 📚 Learning & References

This project is a hands-on learning exercise to understand ETL pipelines using Python libraries such as Pandas, SQLAlchemy, and python-dotenv for environment management.



## 🧑‍💻 Author

**Vivek Panthi**  
📧 vpanthi45@gmail.com  
🔗 [GitHub](https://github.com/VivekPanthii) | [LinkedIn](https://www.linkedin.com/in/bibek-sunar-7650542a3/)
