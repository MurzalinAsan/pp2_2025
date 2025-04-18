import psycopg2
from config import load_config

def get_user_level(name):
    config = load_config()
    sql = "SELECT level FROM scores WHERE scores_name = %s ORDER BY scores_id DESC LIMIT 1;"
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    sql,
                    (name,)
                )
                row = cur.fetchone()
                if row:
                    return row[0]
    except Exception as error:
        print(error)
    return None