from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib  # For sending emails (optional)
#ADDING Sample text to check myself
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

# Simulated user database
users = {
    'user@example.com': 'password123'
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Placeholder  for the authentication logic
    if username == 'admin' and password == 'password':
        return "Login successful!"
    else:
        return "Invalid credentials, please try again."

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        if email in users:
            # Here you would typically send an email with a reset link
            flash(f'Reset link sent to {email}', 'success')
            return redirect(url_for('forgot_password'))
        else:
            flash('Email not found', 'error')

    return render_template('forgot_password.html')

if __name__ == '__main__':
    app.run(debug=True)
