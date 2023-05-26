import psycopg2

conn=psycopg2.connect(database="motoring",host="localhost",user="postgres",password="London1031",port="5432")

cur=conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS supplier(supplierID serial PRIMARY KEY, VAT_number varchar(100),Contact_name varchar(100), Telephone_number varchar(100), Email_address varchar(100), Address varchar(100), Country varchar(100));''')
sql_string="INSERT INTO supplier(supplier_name, address, mobile_phone, email, contact_name) VALUES ('supplier','Imperial', '123456', 'Manuel', '02030495853';"
cur.execute(sql_string)
#cur.execute('''INSERT INTO supplier(supplier_name, address, mobile_phone, email, contact_name) VALUES ('supplier','Imperial', '123456', 'Manuel', '02030495853';''') # imperial@imperial.com, 40 Bounder roar unit 5 N15 9HI, London),('supplier',6000,30);''')



conn.commit()

cur.close()

conn.close()

