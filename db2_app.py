
from flask import Flask, render_template, redirect, request, url_for 
import psycopg2
app=Flask(__name__)
def db_conn2():
    conn=psycopg2.connect(database="motoring",
    host="dpg-cijtiih8g3nc2ge601gg-a", 
    user="motoring_user",
    password="an0qLg5cQMuA6gyATcsElx0L1srvkvGb",
    port="5432")
    return conn

def db_conn():
    conn=psycopg2.connect(database="motoring",
    host="localhost", 
    user="postgres",
    password="London1031",
    port="5432")
    return conn 


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/supplier", methods=["GET", "POST"])
def supplier():
    conn = db_conn()
    cur = conn.cursor()

    if request.method == "POST":
        search_term = request.form.get("search")
        if search_term:
            sql_select_query = "SELECT * FROM supplier WHERE supplier_name = %s OR mobile_phone = %s OR email = %s"
            cur.execute(sql_select_query, (search_term, search_term, search_term))
            supplier_details = cur.fetchall()
        else:
            sql_select_query = "SELECT * FROM supplier"
            cur.execute(sql_select_query)
            supplier_details = cur.fetchall()
    else:
        sql_select_query = "SELECT * FROM supplier"
        cur.execute(sql_select_query)
        supplier_details = cur.fetchall()

    cur.close()
    conn.close()

    return render_template("supplier.html", list_of_suppliers=supplier_details)



@app.route("/vehicles", methods=["GET", "POST"])
def vehicles():
    conn = db_conn()
    cur = conn.cursor()
    if request.method == "POST":
        search_term = request.form.get("search")
        if search_term:
            sql_select_query = f"SELECT * FROM vehicles WHERE Registration_Number = '{search_term}' OR Brand = '{search_term}' OR Model = '{search_term}'"
            cur.execute(sql_select_query)
            vehicles_details = cur.fetchall()
        else:
            sql_select_query="SELECT * FROM vehicles;"
        cur.execute(sql_select_query)
        vehicles_details=cur.fetchall()
    else:
        sql_select_query = "SELECT * FROM vehicles;"
        cur.execute(sql_select_query)
        vehicles_details = cur.fetchall()

    cur.close()
    conn.close()

    return render_template("vehicles.html",list_of_vehicles=vehicles_details)

@app.route("/sales", methods=["GET", "POST"])
def sales():
    conn = db_conn()
    cur = conn.cursor()
    if    request.method == "POST":
        search_term = request.form.get("search")
        if  search_term: 
            sql_select_query = f"SELECT * FROM sales WHERE New_Car_Brand = '{search_term}' OR Sale_Employee_Number = '{search_term}'"
            cur.execute(sql_select_query)
            sales_details = cur.fetchall()
        else:
            sql_select_query="SELECT * FROM sales;"
        cur.execute(sql_select_query)
        sales_details=cur.fetchall()
    else:
        sql_select_query = "SELECT * FROM sales;"
        cur.execute(sql_select_query)
        sales_details = cur.fetchall()

    cur.close()
    conn.close()

    return render_template("sales.html", list_of_sales=sales_details)


@app.route("/maintenance", methods=["GET", "POST"])
def maintenance():
    conn = db_conn()
    cur=conn.cursor()
    if    request.method == "POST":
        search_term = request.form.get("search")
        if  search_term: 
            sql_select_query = f"SELECT * FROM maintenance WHERE Vehicle_ID = '{search_term}' OR Performed_By = '{search_term}' OR Performed_By = '{search_term}'"
            cur.execute(sql_select_query)
            maintenance_details = cur.fetchall()
        else:
            sql_select_query="SELECT * FROM maintenance;"
            cur.execute(sql_select_query)
            maintenance_details=cur.fetchall()
    else:
        sql_select_query = "SELECT * FROM maintenance;"
        cur.execute(sql_select_query)
        maintenance_details = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("maintenance.html",list_of_maintenance=maintenance_details)

@app.route('/search', methods=['POST'])
def search():
    search_term = request.form.get('search')

    return render_template("search.html", results=search_term)
      
@app.route("/get_new_supplier_details")
def get_new_supplier_details():
    return render_template("insert_supplier.html")

@app.route('/insert_new_supplier', methods=['POST'])
def insert_new_supplier():
    conn = db_conn()
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS supplier (
        supplierid SERIAL PRIMARY KEY,
        supplier_name VARCHAR(100),
        address VARCHAR(100),
        mobile_phone VARCHAR(100),
        email VARCHAR(100),
        contact_name VARCHAR(100)
    );''')

    sql_string = "INSERT INTO supplier (supplier_name, address, mobile_phone, email, contact_name) VALUES (%s, %s, %s, %s, %s);"
    values = ('MCM', '103 unit 5 brodway Road D30 8UJ', '020333654389', 'zoo@ool.com', 'Blue')

    cur.execute(sql_string, values)  # Pass the values parameter to execute
    conn.commit()

    cur.close()
    conn.close()

    return redirect(url_for('index'))


@app.route("/get_new_vehicles_details")
def get_new_vehicles_details():
    return render_template("insert_vehicles.html")

@app.route('/insert_new_vehicles', methods=['POST'])
def create_new_vehicles():
    registration_number = request.form['registration_number']
    brand = request.form['brand']
    model = request.form['model']
    color = request.form['color']
    price_money = request.form['Price_money']
    car_year = request.form['car_year']
    on_stock_from = request.form['On_stock_from']
    availability = request.form['availability']
    
    conn = db_conn()
    cur = conn.cursor()
    
    insert_sql = "INSERT INTO vehicles (registration_number, brand, model, color, Price, car_year, On_stock_from, availability) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (registration_number, brand, model, color, price_money, car_year, on_stock_from, availability)
    
    cur.execute(insert_sql, values)
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

    sale_employee_number = request.form.get('sale_employee_number')
    new_car_brand = request.form.get('new_car_brand')
    used_car_brand = request.form.get('used_car_brand')
    number_of_used_cars_sold = request.form.get('number_of_used_cars_sold')
    profit_from_new_cars = request.form.get('profit_from_new_cars')
    profit_from_used_cars = request.form.get('profit_from_used_cars')
    profit = request.form.get('profit')
    vehicle_category = request.form.get('vehicle_category')
    number_of_new_cars_sold = request.form.get('number_of_new_cars_sold')

    insert_sql = "INSERT INTO sales (sale_employee_number, new_car_brand, used_car_brand, number_of_used_cars_sold, profit_from_new_cars, profit_from_used_cars, profit, vehicle_category, number_of_new_cars_sold) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (
        sale_employee_number,
        new_car_brand,
        used_car_brand,
        number_of_used_cars_sold,
        profit_from_new_cars,
        profit_from_used_cars,
        profit,
        vehicle_category,
        number_of_new_cars_sold,
    )

    cur.execute(insert_sql, values)
    conn.commit()

    cur.close()
    conn.close()

    return redirect(url_for('index'))

@app.route("/get_new_maintenance_details")
def get_new_maintenance_details():
    return render_template("insert_maintenance.html")


@app.route('/insert_new_maintenance', methods=['POST'])
def create_new_maintenance():
    conn = db_conn()
    cur = conn.cursor()

    vehicle_id = request.form.get('vehicle_id')
    registration_number = request.form.get('registration_number')
    date_performed = request.form.get('date_performed')
    task_to_be_performed_Services = request.form.get('task_to_be_performed_Services')
    performed_by = request.form.get('performed_by')
    validate_by = request.form.get('validate_by')
    material = request.form.get('material')
    labor = request.form.get('labor')
    total = request.form.get('total')

    insert_sql = "INSERT INTO maintenance (vehicle_id, registration_number, date_performed, task_to_be_performed_Services, performed_by, validate_by, material, labor, total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (vehicle_id, registration_number, date_performed, task_to_be_performed_Services, performed_by, validate_by, material, labor, total)

    cur.execute(insert_sql, values)
    conn.commit()

    cur.close()
    conn.close()
    return redirect(url_for('index'))



@app.route("/get_single_supplier", methods=['POST'])
def single_supplier():
    conn = db_conn()
    cur = conn.cursor()
    supplier_id = request.form['supplier']
    sql_select_query = "SELECT * FROM supplier WHERE supplierid = %s;"  # Update the column name
    
    try:
        cur.execute(sql_select_query, (supplier_id,))
        single_supplier = cur.fetchall()
    except Exception as e:
        return 'Error occurred while retrieving supplier data: ' + str(e)
    finally:
        cur.close()
        conn.close()

    return render_template("single_supplier.html", list_of_supplier=single_supplier)


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

    sql_select_query = "SELECT * FROM supplier WHERE supplier_id = %s;"
    cur.execute(sql_select_query, (supplier_id,))
    single_supplier = cur.fetchone()

    update_sql = "UPDATE supplier SET supplier_name = %s, address = %s, mobile_phone = %s, email = %s, contact_name = %s, vat = %s WHERE supplier_id = %s;"
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

    delete_sql = "DELETE FROM supplier WHERE supplier_id = %s;"

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

    select_sql = "SELECT * FROM supplier WHERE supplier_id = %s;"

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
