import psycopg2

conn=psycopg2.connect(database="motoring",host="localhost",user="postgres",password="London1031",port="5432")

cur=conn.cursor()

#cur.execute('''CREATE TABLE IF NOT EXISTS supplier(supplierID serial PRIMARY KEY, supplier_name varchar(100), address varchar(100), mobile_phone varchar(100), email varchar(100), contact_name(100);''')
#sql_string="INSERT INTO supplier(supplier_name, address, mobile_phone, email, contact_name) VALUES ('supplier','Imperial', '123456', 'Manuel', '02030495853');"
sql_string="INSERT INTO supplier(supplier_name, address, mobile_phone, email, contact_name) VALUES ('MCM','103 unit 5 brodway Road D30 8UJ', '020333654389', 'zoo@ool.com', 'BLue');"

cur.execute(sql_string)
#cur.execute('''INSERT INTO supplier(supplier_name, address, mobile_phone, email, contact_name) VALUES ('supplier','Imperial', '123456', 'Manuel', '02030495853';''') # imperial@imperial.com, 40 Bounder roar unit 5 N15 9HI, London),('supplier',6000,30);''')


conn.commit()

cur.close()

conn.close()

