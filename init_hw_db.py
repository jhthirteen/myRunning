import psycopg2

connection = psycopg2.connect(host="localhost", database="hw_db",user="jack", password="fit32114")

current = connection.cursor()

current.execute('DROP TABLE IF EXISTS users;')
current.execute('CREATE TABLE users (id serial PRIMARY KEY,'
                                    'username varchar (20) NOT NULL,'
                                    'password varchar (10) NOT NULL,'
                                    'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                    )

connection.commit()

current.close()
connection.close()