from sqlalchemy import create_engine, text

def upsert(df, table, key):
    eng = create_engine(CONFIG['target']['dsn'])
    with eng.begin() as conn:
        for _, row in df.iterrows():
            cols = ', '.join(row.index)
            vals = ', '.join(f":{c}" for c in row.index)
            conn.execute(text(f"INSERT INTO {table} ({cols}) VALUES ({vals}) "
                              f"ON CONFLICT ({key}) DO UPDATE SET ..."),
                         row.to_dict())
