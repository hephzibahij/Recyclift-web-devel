from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mail import Mail, Message
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.yourmailserver.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_email_password'

mail = Mail(app)

verification_codes = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
@app.route('/signup', methods=['GET', 'POST'])
def handle_login_signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Handle login/signup logic here (e.g., check credentials, create user, etc.)
        # Assuming login/signup is successful, store session info
        session['email'] = email

        # Send job notification email
        send_job_notification(email)
        
        return redirect(url_for('dashboard'))
    return render_template('login_signup.html')

@app.route('/dashboard')
def dashboard():
    if 'email' in session:
        email = session['email']
        return render_template('dashboard.html', email=email)
    return redirect(url_for('handle_login_signup'))

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        new_password = request.form['new_password']
        verification_code = random.randint(1000, 9999)
        verification_codes[email] = (new_password, verification_code)
        
        # Send verification code email
        send_verification_code(email, verification_code)
        
        return redirect(url_for('verify_password'))
    return render_template('forgot_password.html')

@app.route('/verify_password', methods=['GET', 'POST'])
def verify_password():
    if request.method == 'POST':
        email = request.form['email']
        verification_code = int(request.form['verification_code'])
        if email in verification_codes and verification_codes[email][1] == verification_code:
            new_password = verification_codes[email][0]
            # Update the user's password in the database
            # (this example does not include database handling)
            flash('Password successfully reset!', 'success')
            return redirect(url_for('handle_login_signup'))
        else:
            flash('Invalid verification code', 'danger')
    return render_template('verify_password.html')

def send_job_notification(email):
    msg = Message('Job Opportunities', sender='your_email@example.com', recipients=[email])
    msg.body = 'Here are some job opportunities that might interest you...'
    mail.send(msg)

def send_verification_code(email, verification_code):
    msg = Message('Password Reset Verification Code', sender='your_email@example.com', recipients=[email])
    msg.body = f'Your verification code is {verification_code}.'
    mail.send(msg)

# Example class and function outside Flask routes
class Recycler:
    def __init__(self, name, address, estimated_weight):
        self.name = name
        self.address = address
        self.estimated_weight = estimated_weight

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"House Address: {self.address}")
        print(f"Estimated Weight of Recycled Bottles: {self.estimated_weight} kg")

def register_recycler():
    print("Welcome to the Recycler Registration Portal!")
    name = input("Enter your name: ")
    address = input("Enter your house address: ")
    estimated_weight = float(input("Enter the estimated weight of recycled bottles (in kg): "))

    recycler = Recycler(name, address, estimated_weight)
    print("\nRegistration Complete!")
    recycler.display_info()

if __name__ == "__main__":
    app.run(debug=True)
