import psycopg2
from config import load_config

def name_exists(name):
    config = load_config()
    sql = "SELECT 1 FROM phonebook WHERE phonebook_name = %s LIMIT 1;"
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name,))
                return cur.fetchone() is not None
    except Exception as e:
        print(e)
        return False
