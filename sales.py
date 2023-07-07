import psycopg2


conn=psycopg2.connect(database="motoring",host="localhost",user="postgres",password="London1031",port="5432")

cur=conn.cursor()


cur.execute('''CREATE TABLE IF NOT EXISTS sales(salesID serial PRIMARY KEY, sale_employee_number varchar(100), new_car_brand varchar(100), used_car_brand varchar(100), number_0f_new_cars_sold varchar(100), number_of_used_cars_sold varchar(100), profit_from_new_cars varchar(100), profit_from_used_cars varchar(100), profit varchar(100), vehicle_category varchar(100));''')
sql_string="INSERT INTO sales(sale_employee_number, new_car_brand, used_car_brand, number_0f_new_cars_sold, number_0f_used_cars_sold, profit_from_new_cars, profit_from_used_cars, profit, vehicle_category) VALUES ('123445','10', '5', '5', '3', '133094', '20034', '12345', 'hibrid');"

cur.execute(sql_string)


conn.commit()

cur.close()

conn.close()

