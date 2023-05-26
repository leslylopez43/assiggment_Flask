import psycopg2

conn=psycopg2.connect(database="motoring",host="localhost",user="postgres",password="London1031",port="5432")

cur=conn.cursor()


cur.execute('''CREATE TABLE IF NOT EXISTS maintenance(maintenanceID serial PRIMARY KEY, vehicle_id varchar(100), registration_number varchar(100), date_performed varchar(100), task_to_be_performed_Services varchar(100), performed_by varchar(100), validate_by varchar(100), material varchar(100), labor varchar(100), total varchar(100));''')
sql_string="INSERT INTO maintenance(vehicle_id, registration_number, date_performed, task_to_be_performed_Services, performed_by, validate_by, validate, material, labor, total) VALUES ('123445','10kkjsd', '5', '5', '3', '133094', '20034', '12345', 'hibrid');"

cur.execute(sql_string)


conn.commit()

cur.close()

conn.close()
