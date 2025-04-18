import psycopg2

from config import load_config

def remove(name):

    sql = """DELETE FROM phonebook WHERE phonebook_name = %s"""
    rows_deleted = 0
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
           
                cur.execute(sql, (name,))
                rows_deleted = cur.rowcount
 
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return rows_deleted
    
if __name__ == '__main__':
    name = input()
    
    print("contacts removed: ", remove(name))