import psycopg2

from config import load_config

def delete(number):

    sql = """DELETE FROM phonebook WHERE phone_number = %s"""

    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (number,))
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    number = input()
    delete(number)