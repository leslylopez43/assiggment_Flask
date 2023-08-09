# Import the necessary modules from Flask
from flask import Flask, flash, render_template, redirect, request, url_for
import psycopg2  # Import the psycopg2 module for PostgreSQL database interactions
import os  # Import the os module for environment variable access

# Now you can use these variables to establish a database connection
app = Flask(__name__) # Create a Flask app instance
app.secret_key="secret_key"   # Set the secret key for the app to enable session usage

# Retrieving sensitive data from environment variables
db_user = os.environ.get('MY_USERNAME')
db_password = os.environ.get('MY_PASSWORD')
db_host = os.environ.get('MY_HOST')
db_port = os.environ.get('MY_PORT')


def db_conn():
    conn = psycopg2.connect(
        database="motoring",
        host=db_host,
        user=db_user,
        password=db_password,
        port=db_port
    )
    return conn


@app.route("/")     # Define a route for the root URL ("/")
def index():
    return render_template("index.html")        # Render the "index.html" template and return the rendered content


# Define a route for the "/supplier" URL path, supporting GET and POST methods
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


# Define a route for the "/vehicles" URL path, supporting GET and POST methods

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

# Define a route for the "/sales" URL path, supporting GET and POST methods
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

# Define a route for the "/maintenance" URL path, supporting GET and POST methods
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

# Define a route for the "/search" URL path, supporting POST methods
@app.route('/search', methods=['POST'])
def search():
    search_term = request.form.get('search')

    return render_template("search.html", results=search_term)

# Define a route for the "/get new supplier" URL path.
@app.route("/get_new_supplier_details")
def get_new_supplier_details():
    return render_template("insert_supplier.html")

# Define a route for the "/insert new supplier" URL path.
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
    flash('New supplier   added')
    return redirect(url_for('supplier'))

# Define a route for the "/get new vehicles" URL path.
@app.route("/get_new_vehicles_details")
def get_new_vehicles_details():
    return render_template("insert_vehicles.html")

# Define a route for the "/insert new vehicles" URL path.
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

# Define a route for the "/get new sales" URL path.
@app.route("/get_new_sales_details")
def get_new_sales_details():
    return render_template("insert_sales.html")

# Define a route for the "/insert new sales" URL path.
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

# Define a route for the "/nuw maintenance details" URL path.
@app.route("/get_new_maintenance_details")
def get_new_maintenance_details():
    return render_template("insert_maintenance.html")

# Define a route for the "/insert new maintenance" URL path.
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


# Define a route for the "/get  supplier" URL path.
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

# Define a route for the "/update supplier" URL path.


# Placeholder function to simulate fetching supplier data from the database
def fetch_supplier_data(supplier_id):
    # Replace this with your actual code to fetch data from the database
    # For demonstration purposes, I'm returning a dictionary with placeholder data
    return {
        "company_name": "ABC Corporation",
        "address": "123 Main St",
        "mobile_phone": "555-1234",
        "email_address": "contact@abc.com",
        "contact_name": "John Doe",
        "vat": "123456789"
    }

@app.route("/update_supplier", methods=["GET", "POST"])
def update_supplier():
    try:
        if request.method == "POST":
            supplier_id = request.form.get("supplier")
            Companyname = request.form.get("Companyname")
            Address = request.form.get("Address")
            MobilePhone = request.form.get("MobilePhone")
            EmailAddress = request.form.get("EmailAddress")
            contactName = request.form.get("contactName")
            vat = request.form.get("vat")

            # Update the data in the database or perform other actions
            # You would typically use these values to update the corresponding supplier record in the database

            return "Supplier data updated successfully"

        else:
            supplier_id = request.args.get("supplier_id")  # Assuming you have a supplier_id in the URL
            supplier_data = fetch_supplier_data(supplier_id)
            
            # Return the template for editing the supplier data
            return render_template("update_supplier.html", supplier_data=supplier_data)

    except Exception as e:
        return f"An error occurred: {str(e)}"

   

# Define a route for the "/delete supplier" URL path.
@app.route('/delete_supplier/<int:supplier_id>', methods=['GET', 'POST'])
def delete_supplier(supplier_id):
    conn = db_conn()  # Assuming you have a function called db_conn() to establish a database connection
    cur = conn.cursor()

    delete_sql = "DELETE FROM supplier WHERE supplierid = %s;"

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

    select_sql = "SELECT * FROM supplier WHERE supplierid = %s;"

    try:
        cur.execute(select_sql, (supplier_id,))
        supplier_data = cur.fetchone()
        return render_template("print.html", supplier_data=supplier_data, supplier_id=supplier_id)
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
    app.run(debug=False)
