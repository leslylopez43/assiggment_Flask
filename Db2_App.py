

from flask import Flask, render_template, redirect, request, url_for 
import psycopg2
app=Flask(__name__)
def db_conn():
    conn=psycopg2.connect(database="flask_db1",host="localhost",user="postgres",password="London1031",port="5432")
    return conn


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search i think")
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
      
@app.route('/create',methods=['POST'])
def create():
    conn=db_conn()
    cur=conn.cursor()
    name=request.form['name']
    fees=request.form['fees']
    duration=request.form['duration']
    cur.execute('''INSERT INTO courses (name, fees,duration) VALUES (%S,%S,%S)'''),(name,fees,duration)
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))
     
   
if __name__ == '__main__':
    app.run(debug=True)

