import psycopg2

from config import load_config

def filter(name):

    sql = """
                    SELECT * FROM phonebook
                    WHERE phonebook_name ILIKE %s
                    ORDER BY phonebook_name;
                """
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (f"{name}%",))
                
                row = cur.fetchone()
                while row is not None:
                    print(row)
                    row = cur.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
if __name__ == '__main__':
    name = input()
    filter(name)