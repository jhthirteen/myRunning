import psycopg2

connection = psycopg2.connect(host="localhost", database="hw_db",user="jack", password="fit32114")

current = connection.cursor()

current.execute('DROP TABLE IF EXISTS users;')
current.execute('''
                CREATE TABLE users (
                id serial PRIMARY KEY,
                username varchar(20) NOT NULL,
                password varchar(20) NOT NULL,
                date_added date DEFAULT CURRENT_TIMESTAMP
                );
                ''')

current.execute('''
                INSERT INTO users (username, password) 
                VALUES (%s, %s)          
                ''', ('jackHunter', 'testPassword'))

connection.commit()

current.close()
connection.close()