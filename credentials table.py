import psycopg2
conn = psycopg2.connect(database = "postgres", user = "postgres", password = "testpwd", host = "127.0.0.1", port = "5432")
print("Opened database successfully")

cur = conn.cursor()
cur.execute('''create table credentials
                (id serial primary key,
                email text ,
                username text,
                password text);''')

print("Table created successfully")



