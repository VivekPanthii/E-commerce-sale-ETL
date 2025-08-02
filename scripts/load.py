from sqlalchemy import *
from sqlalchemy.exc import ProgrammingError


def create_database_if_not_exists(db_uri):

    from urllib.parse import urlparse

    url = urlparse(db_uri)
    db_name = url.path.lstrip("/")

    default_db_uri = db_uri.replace(f"/{db_name}", "/postgres")
    engine = create_engine(default_db_uri)

    with engine.connect() as conn:
        conn.execution_options(isolation_level="AUTOCOMMIT")

        result = conn.execute(
            text(f"SELECT 1 FROM pg_database WHERE datname='{db_name}'")
        ).scalar()

        if not result:
            print(f"Database '{db_name}' does not exist. Creating........")

            try:
                conn.execute(text(f"CREATE DATABASE {db_name}"))
                print(f"Database '{db_name}' created.")

            except ProgrammingError as e:
                print(f"Error creating database: {e}")
        else:
            print(f"Database '{db_name}',already exists")


############# *******Create table if not exists*********


def create_table_if_not_exists(db_uri, table_name="AmazonSalesReport"):
    engine = create_engine(db_uri)
    metadata = MetaData()
    table = Table(
        table_name,
        metadata,
        Column("id", Integer, primary_key=True,autoincrement=True),
        Column("order_id", String(50), nullable=False),
        Column("date", DateTime, nullable=False),
        Column("status", String(30)),
        Column("fulfilment", String(50)),
        Column("sales_channel", String(50)),
        Column("ship_service_level", String(50)),
        Column("style", String(50)),
        Column("sku", String(50)),
        Column("category", String(50)),
        Column("size", String(10)),
        Column("asin", String(20)),
        Column("courier_status", String(50)),
        Column("qty", Integer),
        Column("currency", String(10)),
        Column("amount", Float),
        Column("ship_city", String(50)),
        Column("ship_state", String(50)),
        Column("ship_postal_code", String(20)),
        Column("ship_country", String(10)),
        Column("promotion_ids", Text),
        Column("b2b", Boolean),
        Column("fulfilled_by", String(50), nullable=True),
    )

    metadata.create_all(engine)
    print(f"Table '{table_name}' checked/created if needed.")


def load(df, table_name="AmazonSalesReport", db_uri=None):
    """Loads the dataFrame into postgresql"""
    if df is None or df.empty:
        print("No data to load.")
        return
    if not db_uri:
        raise ValueError("DATABASE URI is required")

    create_database_if_not_exists(db_uri)

    create_table_if_not_exists(db_uri, table_name)
    if 'id' in df.columns:
        df = df.drop(columns=['id'])

    engine = create_engine(db_uri)
    print(f"Loading {df.shape[0]} records into {table_name}.....")
    df.to_sql(table_name, engine, if_exists="append", index=False)
    print("Load Complete.....")
