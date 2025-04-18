import psycopg2
from config import load_config

def create_tables():
    """ Create tables in the PostgreSQL database """

    commands = (
    """
    DROP TABLE IF EXISTS phonebook_parts, part_drawings, parts, phonebook CASCADE;
    """,
    """
    CREATE TABLE phonebook (
        phonebook_id SERIAL PRIMARY KEY,
        phonebook_name VARCHAR(255) NOT NULL,
        phone_number VARCHAR(20) NOT NULL
    )
    """,
    """ 
    CREATE TABLE parts (
        part_id SERIAL PRIMARY KEY,
        part_name VARCHAR(255) NOT NULL
    )
    """,
    """
    CREATE TABLE part_drawings (
        part_id INTEGER PRIMARY KEY,
        file_extension VARCHAR(5) NOT NULL,
        drawing_data BYTEA NOT NULL,
        FOREIGN KEY (part_id)
            REFERENCES parts (part_id)
            ON UPDATE CASCADE ON DELETE CASCADE
    )
    """,
    """
    CREATE TABLE phonebook_parts (
        phonebook_id INTEGER NOT NULL,
        part_id INTEGER NOT NULL,
        PRIMARY KEY (phonebook_id, part_id),
        FOREIGN KEY (phonebook_id)
            REFERENCES phonebook (phonebook_id)
            ON UPDATE CASCADE ON DELETE CASCADE,
        FOREIGN KEY (part_id)
            REFERENCES parts (part_id)
            ON UPDATE CASCADE ON DELETE CASCADE
    )
    """
)


    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
                conn.commit()
                print("Tables dropped and recreated successfully.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()
