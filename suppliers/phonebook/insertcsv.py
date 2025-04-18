import psycopg2, csv

from config import load_config

def insert_from_csv(filename):

    sql = """INSERT INTO phonebook(phonebook_name, phone_number) VALUES(%s, %s) RETURNING phonebook_id;"""
    phonebook_id = None
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                
                f = open(filename, "r")
                reader = csv.reader(f)
                
                for i in reader:
                    phonebook_name = i[0]
                    phone_number = i[1]
                    cur.execute(sql, (phonebook_name, phone_number))

                
                rows = cur.fetchone()
                if rows:
                    phonebook_id = rows[0]

                
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return phonebook_id
    
if __name__ == '__main__':
    filename = input()
    insert_from_csv(filename)