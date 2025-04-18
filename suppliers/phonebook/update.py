import psycopg2
from config import load_config


def update(phonebook_id, phonebook_name, phone_number):
    

    updated_row_count = 0

    sql = """ UPDATE phonebook
                    SET phonebook_name = %s, phone_number = %s
                    
                    WHERE phonebook_id = %s"""

    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:

                # execute the UPDATE statement
                cur.execute(sql, (phonebook_name, phone_number, phonebook_id))
                updated_row_count = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return updated_row_count

if __name__ == '__main__':
    id = input()
    newname = input()
    newphone = input()
    update(id, newname, newphone)