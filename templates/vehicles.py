import psycopg2

conn=psycopg2.connect(database="motoring",host="localhost",user="postgres",password="London1031",port="5432")

cur=conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS vehicles(VehiclesID serial PRIMARY KEY, Registration_number varchar(100), Brand varchar(100), Model varchar(100), Color varchar(100), Price money, Car_year varchar(100), On_stock_From varchar(100), Available varchar(100);"))
#sql_string="INSERT INTO vehicles(Registracion_number, Brand, Model, Color, price, Car_year, On_stock_From, Available) VALUES ('MC23URD','Mercedez', 'Benz', 'White', '£2020', '2023', '23/02/2023', 'yes');"

#cur.execute(sql_string)
#cur.execute('''INSERT INTO supplier(supplier_name, address, mobile_phone, email, contact_name) VALUES ('supplier','Imperial', '123456', 'Manuel', '02030495853';''') # imperial@imperial.com, 40 Bounder roar unit 5 N15 9HI, London),('supplier',6000,30);''')


conn.commit()

cur.close()

conn.close()

