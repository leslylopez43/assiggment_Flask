from flask import Flask, render_template, redirect, request, url_for 
import psycopg2
app=Flask(__name__)



@app.route("/")
def index():
    return "Lesly"
