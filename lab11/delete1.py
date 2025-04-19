import psycopg2

from config import load_config

def delete(name):
    sql = """DELETE FROM phonebook WHERE phonebook_name = %s"""

    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name,))
            conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    name = input()
    delete(name)