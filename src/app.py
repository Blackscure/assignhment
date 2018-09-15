from flask import Flask,render_template, request,redirect, url_for

from models.db import users

from models.user import User

 



app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/createquestion', methods=['GET', 'POST'])
def questions():
    if request.method == 'GET':
        return render_template('createquestion.html')
    elif request.method == 'POST':
        title = request.form['title'],
        question = request.form['question'],
        answer = request.form['answer'],
        #print('------------>>>>>>>>>>', question[0])

        
    # import pdb; pdb.set_trace()
    return render_template('created.html', question=question[0])

    
@app.route('/answers')
def answers():
    return render_template('answers.html')   


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/auth/login', methods=['POST'])
def login_template():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        

        for user in users:
            current_person = users[user]
            if name == current_person.name and password == current_person.password:
                # import pdb; pdb.set_trace()
                return redirect(url_for('questions'))
        
        return redirect(url_for('login'))

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