import psycopg2

conn=psycopg2.connect(database="motoring",host="localhost",user="postgres",password="London1031",port="5432")

cur=conn.cursor()


cur.execute('''CREATE TABLE IF NOT EXISTS vehicles(VehiclesID serial PRIMARY KEY, registration_number varchar(100), brand varchar(100), model varchar(100), color varchar(100), Price money, car_year varchar(100), On_stock_from varchar(100), available varchar(100));''')
sql_string="INSERT INTO vehicles(Registration_number, Brand, Model, Color, price, Car_year, On_stock_From, Available) VALUES ('MC23URD','Mercedez', 'Benz', 'White', '2020', '2023', '23/02/2023', 'yes');"

cur.execute(sql_string)
#cur.execute('''INSERT INTO vehicles(registration_number, brand, model, color, price, car_year, on_stock_from, available) VALUES ('bre12wef','Mercedes', 'Benz', 'white', '10233','2023', '20/02/2033', 'yes');''') 


conn.commit()

cur.close()

conn.close()

