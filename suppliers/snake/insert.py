import psycopg2
from config import load_config


def insert_score(scores_name, scores_number, level):


    sql = """INSERT INTO scores(scores_name, scores_number, level)
             VALUES(%s, %s, %s) RETURNING scores_id;"""

    scores_id = None
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                
                cur.execute(sql, (scores_name, scores_number, level))

                
                rows = cur.fetchone()
                if rows:
                    scores_id = rows[0]

                
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return scores_id

