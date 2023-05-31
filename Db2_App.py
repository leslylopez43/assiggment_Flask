

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
    return render_template("maintenance.html")

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
    print(Address)

    #fees=request.form['fees']
    #duration=request.form['duration']
    #cur.execute('''INSERT INTO courses (name, fees,duration) VALUES (%S,%S,%S)'''),(name,fees,duration)
    #conn.commit()
    #cur.close()
    #conn.close()
    return redirect(url_for('index'))
     
   
if __name__ == '__main__':
    app.run(debug=True)
