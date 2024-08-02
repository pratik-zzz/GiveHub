from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import os

# Initialize the Flask application
app = Flask(__name__)

# Get the database URL from environment variables or use a default value
DATABASE_URL = os.environ.get('DATABASE_URL', 'dbname=GiveHub user=postgres password=password host=localhost port=5432')

# Function to establish a connection to the PostgreSQL database
def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

# Define the route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Define the route for the About Us page
@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

# Define the route for the Contact Us page
@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

# Define the route for the Donation page, supporting both GET and POST methods
@app.route('/donation', methods=['GET', 'POST'])
def donation():
    if request.method == 'POST':
        # Get form data
        medicine = request.form['medicine']
        expiry_date = request.form['meetingDate']
        quantity = request.form['number']
        image = request.files['image']
        donor_name = request.form['name']
        contact_number = request.form['contactNumber']
        address = request.form['address']

        # Connect to the database and insert the form data into the donations table
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO donations (medicine, expiry_date, quantity, image, donor_name, contact_number, address) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (medicine, expiry_date, quantity, image.read(), donor_name, contact_number, address)
        )
        conn.commit()  # Commit the transaction
        cur.close()  # Close the cursor
        conn.close()  # Close the connection

        # Redirect to the home page after successful form submission
        return redirect(url_for('index'))

    # Render the donation form if the request method is GET
    return render_template('donation.html')

# Define the route for the Request page, supporting both GET and POST methods
@app.route('/request', methods=['GET', 'POST'])
def request_medicine():
    if request.method == 'POST':
        # Get form data
        medicine = request.form['medicine']
        quantity = request.form['number']
        requester_name = request.form['name']
        contact_number = request.form['contactNumber']
        address = request.form['address']

        # Connect to the database and insert the form data into the requests table
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO requests (medicine, quantity, requester_name, contact_number, address) VALUES (%s, %s, %s, %s, %s)",
            (medicine, quantity, requester_name, contact_number, address)
        )
        conn.commit()  # Commit the transaction
        cur.close()  # Close the cursor
        conn.close()  # Close the connection

        # Redirect to the home page after successful form submission
        return redirect(url_for('index'))

    # Render the request form if the request method is GET
    return render_template('request.html')

# Run the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)
