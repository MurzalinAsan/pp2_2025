import psycopg2, re

from config import load_config

def correct(phone):
    return bool(re.fullmatch(r'\d{0,15}', phone))

def insert_list(users):
    config = load_config()
    invalid = []

    sql = """INSERT INTO phonebook(phonebook_name, phone_number) VALUES (%s, %s);"""

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for name, phone in users:

                    if correct(phone):
                        cur.execute(sql, (name, phone))
                    else:
                        invalid.append((name, phone))

            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return invalid


if __name__ == '__main__':
    users = []

    n = int(input("no of users: "))

    for i in range(n):
        name = input("name: ")
        phone = input("num: ")
        users.append((name, phone))

    invalid = insert_list(users)
    print(invalid)

    