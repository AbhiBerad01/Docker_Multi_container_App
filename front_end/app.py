from flask import Flask, render_template, request
import requests
import mysql.connector

app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/vaccine_status", methods=["POST"])
def vaccine_status():
    reg_no = request.form["reg_no"]

    cnx = mysql.connector.connect(user='root', password='rootpassword',
                              host='vaccination_database',
                              database='vaccination_db')

    # Execute a query
    cursor = cnx.cursor()
    query = ("SELECT * FROM student WHERE reg_no = %s")
    cursor.execute(query, (reg_no,))
    result = cursor.fetchone()
    if result:
        status = True
        reg_no,name,vaccine_status = result  # unpacking the result
    else:
        status = False
        reg_no = None
        name = None
        vaccine_status = None
        print("No record found")

    cursor.close()
    cnx.close()
    return render_template('result.html',status=status,reg_no=reg_no,name=name,vaccine_status=vaccine_status)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
