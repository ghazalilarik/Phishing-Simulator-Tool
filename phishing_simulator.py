from flask import Flask, request, render_template, redirect, url_for
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sqlite3
import random
import string

app = Flask(__name__)

db_file = 'phishing_simulator.db'

# Database setup for user responses
def setup_database():
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS responses (id INTEGER PRIMARY KEY, email TEXT, clicked BOOLEAN, data_entered TEXT)''')
    conn.commit()
    conn.close()

# Generate a random token for tracking who clicked the link
def generate_tracking_token():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

# Send phishing email using SMTP
def send_phishing_email(recipient_email, tracking_token):
    try:
        smtp_server = "smtp.example.com"  # Replace with actual SMTP server
        smtp_port = 587
        smtp_user = "your_email@example.com"  # Replace with your email
        smtp_password = "your_password"  # Replace with your email password

        sender_email = smtp_user
        subject = "Urgent: Account Update Required"
        body = f"Please update your account by clicking on the link below:\nhttp://127.0.0.1:5000/click/{tracking_token}"

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print(f"Phishing email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send phishing email: {e}")

# Landing page for tracking clicks and gathering data
@app.route('/click/<tracking_token>', methods=['GET', 'POST'])
def phishing_landing_page(tracking_token):
    if request.method == 'POST':
        # Save data entered by the victim
        data_entered = request.form['sensitive_data']
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute("UPDATE responses SET data_entered=? WHERE id=?", (data_entered, tracking_token))
        conn.commit()
        conn.close()
        return "Thank you for submitting your details."
    else:
        # Log the click
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute("UPDATE responses SET clicked=? WHERE id=?", (True, tracking_token))
        conn.commit()
        conn.close()
        return render_template('phishing_form.html')

# Send phishing emails to a group of users
@app.route('/send_emails', methods=['POST'])
def send_emails():
    recipient_emails = request.form['recipient_emails'].split(',')
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    for email in recipient_emails:
        tracking_token = generate_tracking_token()
        c.execute("INSERT INTO responses (email, clicked, data_entered) VALUES (?, ?, ?)", (email, False, None))
        send_phishing_email(email, tracking_token)
    conn.commit()
    conn.close()
    return "Phishing emails have been sent."

# View report on responses
@app.route('/report')
def view_report():
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("SELECT * FROM responses")
    rows = c.fetchall()
    conn.close()
    return render_template('report.html', rows=rows)

# Landing page for managing the phishing simulator
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    setup_database()
    app.run(debug=True)
