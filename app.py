from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import os

app = Flask(__name__)

DATABASE_URL = os.environ.get('DATABASE_URL', 'dbname=GiveHub user=postgres password=password host=localhost port=5432')

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')   

@app.route('/donation', methods=['GET', 'POST'])
def donation():
    if request.method == 'POST':
        medicine = request.form['medicine']
        other = request.form['name']
        expiry_date = request.form['meetingDate']
        quantity = request.form['number']
        image = request.files['image']
        donor_name = request.form['name']
        contact_number = request.form['contactNumber']
        address = request.form['address']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO donations (medicine, expiry_date, quantity, image, donor_name, contact_number, address) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (medicine, expiry_date, quantity, image.read(), donor_name, contact_number, address))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('donation.html')

@app.route('/request', methods=['GET', 'POST'])
def request_medicine():
    if request.method == 'POST':
        medicine = request.form['medicine']
        quantity = request.form['number']
        image = request.files['image']
        requester_name = request.form['name']
        contact_number = request.form['contactNumber']
        address = request.form['address']
        conn = get_db_connection()
        cur = conn.cursor() 
        cur.execute("INSERT INTO requests (medicine, quantity, requester_name, contact_number, address) VALUES (%s, %s, %s, %s, %s)",
                    (medicine, quantity, requester_name, contact_number, address))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('request.html')

if __name__ == '__main__':
    app.run(debug=True)