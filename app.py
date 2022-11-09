from flask import Flask

app = Flask(__name__)

#Home Page 
@app.route('/')
def home_page():
    return 'Flask Assignment 1' 
#Dashboard Page
@app.route('/dashboard')
def dashboard_page():
    return 'This is the Dashboard Page'
#Login Page
@app.route('/login')
def login_page():
    return 'This is the Login Page'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
#this is a change