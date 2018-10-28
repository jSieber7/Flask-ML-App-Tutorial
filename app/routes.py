from app import app
from flask import render_template, url_for, request

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'tenten'}
    return render_template('index.html', user = user)

@app.route('/lister', methods=['POST', 'GET'])
def dropdown():
    ML_Models = ['Decision Tree','Random Forest','Support Vector Machine']

    if request.method == 'POST':
        return request.form['The_Model_Name']
        
    return render_template('dropdown.html', ML_Models = ML_Models)
