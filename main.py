import psycopg2
from config import dbconfig
from calc_db import CalcDB

def connect():
    conn = None
    print ('1')
    try:
        print('2')
        params = dbconfig()

        print('Connecting to the PostgreSQL database...')

        conn = psycopg2.connect(**params)
        cur = conn.cursor()


        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)

        db = CalcDB(conn, cur)
        db.initialize_table()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

#    if __name__ == '__main__':
#        connect()

connect()