from flask import Flask, render_template,request,session,redirect,url_for
app = Flask(__name__)
app.secret_key = "2j6"
@app.route('/')
def index():
    if 'email' in session:
        email = session['email']
        return 'Logged in as ' + email + '<br>' + \
            "<b><a href = '/logout'>click here to logout</a></b>"

    return "You are not logged in <br><a href = '/login'></b>" + \
            "click here to log in</b></a>"
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['email']= request.form['email']
        session['password']= request.form['password']
        return redirect(url_for('index'))
    return render_template('login.html')
@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug= True)
