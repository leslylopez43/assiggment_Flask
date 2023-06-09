

from flask import Flask, render_template, redirect, request, url_for 
import psycopg2
app=Flask(__name__)
def db_conn():
    conn=psycopg2.connect(database="motoring",host="localhost",user="postgres",password="London1031",port="5432")
    return conn


@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/supplier")
# def supplier():
#     conn=db_conn()
#     cur=conn.cursor()
#     sql_select_query="SELECT * FROM supplier;" 
#     cur.execute(sql_select_query)
#     supplier_details=cur.fetchall()
#     return render_template("supplier.html",list_of_suppliers=supplier_details)

@app.route("/supplier", methods=["GET", "POST"])
def supplier():
    conn = db_conn()
    cur = conn.cursor()

    if request.method == "POST":
        search_term = request.form.get("search")
        if search_term:
            sql_select_query = f"SELECT * FROM supplier WHERE supplier_name = '{search_term}' OR mobile_phone = '{search_term}' OR email = '{search_term}'"
            cur.execute(sql_select_query)
            supplier_details = cur.fetchall()
        else:
            sql_select_query = "SELECT * FROM supplier;"
            cur.execute(sql_select_query)
            supplier_details = cur.fetchall()
    else:
        sql_select_query = "SELECT * FROM supplier;"
        cur.execute(sql_select_query)
        supplier_details = cur.fetchall()

    cur.close()
    conn.close()

    return render_template("supplier.html", list_of_suppliers=supplier_details)



@app.route("/vehicles", methods=["GET", "POST"])
def vehicles():
    conn=db_conn()
    cur=conn.cursor()
    sql_select_query="SELECT * FROM vehicles;"
    cur.execute(sql_select_query)
    vehicles_details=cur.fetchall()
    return render_template("vehicles.html",list_of_vehicles=vehicles_details)

@app.route("/sales")
def sales():
    conn = db_conn()
    cur = conn.cursor()
    sql_select_query = "SELECT * FROM sales;"
    cur.execute(sql_select_query)
    sales_details = cur.fetchall()
    cur.close()
    conn.close()
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

@app.route('/search', methods=['POST'])
def search():
    # Handle the search functionality here
    search_term = request.form.get('search')
    # Perform search logic

    return render_template("search.html", results=search_term)
      
@app.route("/get_new_supplier_details")
def get_new_supplier_details():
    return render_template("insert_supplier.html")

@app.route('/insert_new_supplier',methods=['POST'])
def insert_sales():
    conn = psycopg2.connect(database="motoring", host="localhost", user="postgres", password="London1031", port="5432")
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS vehicles(
        VehiclesID serial PRIMARY KEY,
        registration_number varchar(100),
        brand varchar(100),
        model varchar(100),
        color varchar(100),
        Price money,
        car_year varchar(100),
        On_stock_from varchar(100),
        available varchar(100)
        number_of_new_cars_sold(100)
    );''')

    sql_string = "INSERT INTO vehicles(registration_number, brand, model, color, price, car_year, on_stock_from, available, number_of_new_cars_sold) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
    values = ('MC23URD', 'Mercedes', 'Benz', 'White', '2020', '2023', '23/02/2023', 'yes', '2')

    cur.execute(sql_string, values)
    conn.commit()

    cur.close()
    conn.close()
    if number_of_new_cars_sold is not None and number_of_new_cars_sold.isdigit():
        number_of_new_cars_sold = int(number_of_new_cars_sold)
    else:
        number_of_new_cars_sold = 0
    
    
    
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

     insert_sql="INSERT INTO vehicles (registration_number, brand, model, color, Price, car_year, On_stock_from, available) VALUES ('" + registration_number  + "','" + brand  + "','" + model + "','" + color+ "','" + Price_money+ "','" + car_year + "','" + On_stock_from + "','" + available + "')"
     print(insert_sql)
     cur.execute(insert_sql)
     conn.commit()
     cur.close()
     conn.close()
     return redirect(url_for('index'))


@app.route("/get_new_sales_details")
def get_new_sales_details():
    return render_template("insert_sales.html")


@app.route('/insert_new_sales', methods=['POST'])
def create_new_sales():
    conn = db_conn()
    cur = conn.cursor()

    sale_employee_number = request.form['sale_employee_number']
    new_car_brand = request.form['new_car_brand']
    used_car_brand = request.form['used_car_brand']
    number_of_used_cars_sold = request.form['number_of_used_cars_sold']
    profit_from_new_cars = request.form['profit_from_new_cars']
    profit_from_used_cars = request.form['profit_from_used_cars']
    Profit = request.form['Profit']
    vehicle_category = request.form['vehicle_category']
    number_of_new_cars_sold = int(request.form['number_of_new_cars_sold'])
    insert_sql = "INSERT INTO sales (sale_employee_number, new_car_brand, used_car_brand, number_of_used_cars_sold, profit_from_new_cars, profit_from_used_cars, profit, vehicle_category, number_of_new_cars_sold) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    cur.execute(
        insert_sql, (sale_employee_number, new_car_brand, used_car_brand, number_of_used_cars_sold, profit_from_new_cars, profit_from_used_cars, Profit, vehicle_category, number_of_new_cars_sold)
    )
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
    sql_select_query="SELECT * FROM supplier where supplier_list='"  + supplier_id + "';"
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
    Companyname = request.form['Companyname']
    Address = request.form['Address']
    MobilePhone = request.form['MobilePhone']
    EmailAddress = request.form['EmailAddress']
    contactName = request.form['contactName']
    vat = request.form['vat']

    sql_select_query = "SELECT * FROM supplier WHERE supplier_id = %s"
    cur.execute(sql_select_query, (supplier_id,))
    single_supplier = cur.fetchone()  # Fetch a single row instead of fetching all rows

    update_sql = "UPDATE supplier SET supplier_name = %s, address = %s, mobile_phone = %s, email = %s, contact_name = %s, vat = %s WHERE supplier_id = %s"
    values = (Companyname, Address, MobilePhone, EmailAddress, contactName, vat, supplier_id)

    try:
        cur.execute(update_sql, values)
        conn.commit()

        # Fetch the updated supplier details
        cur.execute(sql_select_query, (supplier_id,))
        single_supplier = cur.fetchone()

        return render_template("update_supplier.html", list_of_supplier=[single_supplier])
    except Exception as e:
        return render_template("update_supplier.html", supplier_id=supplier_id, list_of_supplier=[single_supplier])
    finally:
        cur.close()
        conn.close()

@app.route('/delete_supplier/<int:supplier_id>', methods=['GET', 'POST'])
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

@app.route('/print_supplier/<int:supplier_id>', methods=['GET'])
def print_supplier(supplier_id):
    conn = db_conn()
    cur = conn.cursor()
    
    select_sql = "SELECT * FROM supplier WHERE supplier_id = %s"
    
    try:
        cur.execute(select_sql, (supplier_id,))
        supplier_data = cur.fetchone()
        return render_template("print_supplier.html", supplier_data=supplier_data)
    except Exception as e:
        return 'Error occurred while retrieving supplier data: ' + str(e)
    finally:
        cur.close()
        conn.close()





@app.route('/submit_form', methods=['POST'])
def submit_form():
    option = request.form.get('cars')
    if option == 'supplier':
        # Handle supplier option
        return render_template('supplier.html')
    elif option == 'vehicles':
        # Handle vehicles option
        return render_template('vehicles.html')
    elif option == 'sales':
        # Handle sales option
        return render_template('sales.html')
    elif option == 'maintenance':
        # Handle maintenance option
        return render_template('maintenance.html')
    else:
        # Handle invalid option
        return 'Invalid option'



         
if __name__ == '__main__':
    app.run(debug=True)

