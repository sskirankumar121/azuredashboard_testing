from flask import Flask, render_template, request, redirect, url_for
#121
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Placeholder for authentication logic
    if username == 'admin' and password == 'password':
        return "Login successful!"
    else:
        return "Invalid credentials, please try again."

if __name__ == '__main__':
    app.run(debug=True)
