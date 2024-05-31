import psycopg2

connection = psycopg2.connect(host="localhost", database="hw_db",user="jack", password="fit32114")

current = connection.cursor()

current.execute('''
                CREATE TABLE userDailyTasks (
                user_id int,
                task varchar(50) NOT NULL,
                due_date varchar(10),
                completed int
                );
                ''')

current.execute('''
                INSERT INTO userDailyTasks (user_id, task, due_date, completed)
                VALUES (%s, %s, %s, %s)
                ''', (1, 'Math Homework', '6/10/24', 0))

connection.commit()

current.close()
connection.close()