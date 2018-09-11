from flask import Flask,render_template, request,redirect, url_for

from models.user import User



app = Flask(__name__)

users = {}

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/auth/login', methods=['POST'])
def login_template():

    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/auth/register', methods=['POST'])
def register_template():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

        id = len(users) +1
        for user in users:
            current_person = users[user]
            if name == current_person.name:
                return render_template('exists.html')

        new_person = User(name,password,id)
        return redirect(url_for('login'))



     

 


if __name__ == '__main__':
    app.run(debug=True)