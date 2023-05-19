import psycopg2

conn=psycopg2.connect(database="motoring",host="localhost",user="postgres",password="London1031",port="5432")

cur=conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS supplier(supplierID serial PRIMARY KEY, supplier_name varchar(100),address varchar(100), mobile_phone varchar(100), email varchar(100), contact_name varchar(100));''')

#cur.execute('''INSERT INTO courses(name,fees,duration) VALUES ('python', 6500,45),('javascript',6000,30);''')



conn.commit()

cur.close()

conn.close()
