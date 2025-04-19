import psycopg2

from config import load_config

def contact(limit, offset):
    contacts = []
    config = load_config()

    sql = """SELECT phonebook_id, phonebook_name FROM phonebook ORDER BY phonebook_name LIMIT %s OFFSET %s;"""

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (limit, offset))
                contacts = cur.fetchall()
            conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return contacts

if __name__ == '__main__':
    limit = int(input())
    offset = int(input())
    print(contact(limit, offset))