import psycopg2

conn=psycopg2.connect(database="motoring",host="localhost",user="postgres",password="London1031",port="5432")

cur=conn.cursor()


cur.execute('''CREATE TABLE IF NOT EXISTS maintenance(maintenanceID serial PRIMARY KEY, vehicle_id varchar(100), registration_number varchar(100), date_performed varchar(100), task_to_be_performed_Services varchar(100), performed_by varchar(100), validate_by varchar(100), material varchar(100), labor varchar(100), total varchar(100));''')
sql_string="INSERT INTO maintenance(registration_number, date_performed, task_to_be_performed_Services, performed_by, validate_by, material, labor, total) VALUES ('10kkjsd','12-11-2004', 'to be performd', 'someone', 'mane', 'material', 'chnging', '£1000');"
cur.execute(sql_string)

conn.commit()

cur.close()

conn.close()
