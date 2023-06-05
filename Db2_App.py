

from flask import Flask, render_template, redirect, request, url_for 
import psycopg2
app=Flask(__name__)
def db_conn():
    conn=psycopg2.connect(database="motoring",host="localhost",user="postgres",password="London1031",port="5432")
    return conn


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/supplier")
def supplier():
    conn=db_conn()
    cur=conn.cursor()
    sql_select_query="SELECT * FROM supplier;"
    cur.execute(sql_select_query)
    supplier_details=cur.fetchall()
    return render_template("supplier.html",list_of_suppliers=supplier_details)

@app.route("/vehicles")
def vehicles():
    conn=db_conn()
    cur=conn.cursor()
    sql_select_query="SELECT * FROM vehicles;"
    cur.execute(sql_select_query)
    vehicles_details=cur.fetchall()
    return render_template("vehicles.html",list_of_vehicles=vehicles_details)

@app.route("/sales")
def sales():
    conn=db_conn()
    cur=conn.cursor()
    sql_select_query="SELECT * FROM sales;"
    cur.execute(sql_select_query)
    sales_details=cur.fetchall()
    return render_template("sales.html", list_of_sales=sales_details)

@app.route("/maintenance")
def maintenance():
    conn=db_conn()
    cur=conn.cursor()
    sql_select_query="SELECT * FROM maintenance;"
    cur.execute(sql_select_query)
    maintenance_details=cur.fetchall()
    print (maintenance)
    return render_template("maintenance.html",list_of_maintenance=maintenance_details)

@app.route("/search")
def oldindex():
    conn=db_conn()
    cur=conn.cursor()
   # cur.execute('''SELECT * FROM courses''')
    length_of_duration=30
    cur.execute('''select * from courses where duration='''+str(length_of_duration))
    data=cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", data=data) 
      
@app.route("/get_new_supplier_details")
def get_new_supplier_details():
    return render_template("insert_supplier.html")

@app.route('/insert_new_supplier',methods=['POST'])
def create():
    conn=db_conn()
    cur=conn.cursor()
    Companyname=request.form['Company Name']
    Address=request.form['Address']
    MobilePhone=request.form['Mobile Phone']
    EmailAddress=request.form['Email Address']
    contactName=request.form['contact Name']
    vat=request.form['VAT']
    print(vat)


    insert_sql="INSERT INTO supplier (supplier_name, address, mobile_phone, email, contact_name, vat) VALUES ('" + Companyname  + "','" + Address  + "','" + MobilePhone + "','" + EmailAddress+ "','" + contactName+ "','" + vat + "')"
    cur.execute(insert_sql)
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))



@app.route("/get_new_vehicles_details")
def get_new_vehicles_details():
    return render_template("insert_vehicles.html")

@app.route('/insert_new_vehicles',methods=['POST'])
def create_new_vehicles():
     conn=db_conn()
     cur=conn.cursor()
     registration_number=request.form['registration_number']
     brand=request.form['brand']
     model=request.form['model']
     color=request.form['color']
     Price_money=request.form['Price_money']
     car_year=request.form['car_year']
     On_stock_from=request.form['On_stock_from'] 
     available=request.form['available'] 
     print(available)

    
     insert_sql="INSERT INTO vehicles (registration_number, brand, model, color, Price, car_year, On_stock_from, available) VALUES ('" + registration_number  + "','" + brand  + "','" + model + "','" + color+ "'," + Price_money+ ",'" + car_year + "','" + On_stock_from + "','" + available + "')"
     print(insert_sql)
     cur.execute(insert_sql)
     conn.commit()
     cur.close()
     conn.close()
     return redirect(url_for('index'))




@app.route("/get_new_maintenance_details")
def get_new_maintenance_details():
    return render_template("insert_maintenance.html")

@app.route('/insert_new_maintenance',methods=['POST'])
def create_new_maintenance():
     conn=db_conn()
     cur=conn.cursor()
     vehicle_id=request.form['vehicle_id']
     registration_number=request.form['registration_number']
     date_performed=request.form['date_performed']
     task_to_be_performed_Services=request.form['task_to_be_performed_Services']
     performed_by=request.form['performed_by']
     validate_by=request.form['validate_by']
     material=request.form['material'] 
     labor=request.form['labor'] 
     total=request.form['total']
     print(total)

    
     insert_sql="INSERT INTO maintenance (vehicle_id, registration_number, date_performed, task_to_be_performed_Services, performed_by, validate_by, material, labor, total) VALUES ('" + vehicle_id  + "','" + registration_number  + "','" + date_performed + "','" + task_to_be_performed_Services+ "','" + performed_by+ "','" + validate_by + "','" + material + "','" + labor + "','" + total + "')"
     print(insert_sql)
     cur.execute(insert_sql)
     conn.commit()
     cur.close()
     conn.close()
     return redirect(url_for('index'))

@app.route("/get_single_supplier" ,methods=['POST'])
def single_supplier():
    conn=db_conn()
    cur=conn.cursor()
    supplier_id=request.form['supplier']
    #print ("supplier " + str(supplier_id))
    sql_select_query="SELECT * FROM supplier where supplier_name='"  + supplier_id + "';"
    cur.execute(sql_select_query)
    single_supplier=cur.fetchall()
    cur.close()
    conn.close()
    #print(" found " + str(single_supplier))
    return render_template("single_supplier.html",list_of_supplier=single_supplier)







@app.route("/update_supplier", methods=['POST'])
def update_supplier():
    conn = db_conn()
    cur = conn.cursor()
    
    supplier_id = request.form['supplier']
    sql_select_query = "SELECT * FROM supplier WHERE single_supplier = %s"
    cur.execute(sql_select_query, (supplier_id,))
    single_supplier = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return render_template("update_supplier.html", list_of_supplier=single_supplier)
# perform_supplier_update route
 
@app.route("/perform_supplier_update", methods=['POST'])
def perform_supplier_update():
    conn = db_conn()
    cur = conn.cursor()
# Existing code for database connection and update operation
    supplier_id = request.form['supplier_id']
    Companyname = request.form['Companyname']
    Address = request.form['Address']
    MobilePhone = request.form['MobilePhone']
    EmailAddress = request.form['EmailAddress']
    contactName = request.form['contactName']
    vat = request.form['vat']
    
    update_sql = "UPDATE supplier SET supplier_name = %s, address = %s, mobile_phone = %s, email = %s, contact_name = %s, vat = %s WHERE supplier_id = %s"
    values = (Companyname, Address, MobilePhone, EmailAddress, contactName, vat, supplier_id)
    
    try:
        cur.execute(update_sql, values)
        conn.commit()
        return redirect(url_for('index'))
    except Exception as e:
        return 'Error occurred while updating supplier: ' + str(e)
    finally:
        cur.close()
        conn.close()



@app.route('/delete_supplier/<int:supplier_id>', methods=['POST'])
def delete_supplier(supplier_id):
    conn = db_conn()
    cur = conn.cursor()
    
    delete_sql = "DELETE FROM supplier WHERE supplier_id = %s"
    
    try:
        cur.execute(delete_sql, (supplier_id,))
        conn.commit()
        return redirect(url_for('index'))
    except Exception as e:
        return 'Error occurred while deleting supplier: ' + str(e)
    finally:
        cur.close()
        conn.close()



    
     
if __name__ == '__main__':
    app.run(debug=True)
