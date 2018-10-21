
import os,re, glob
from pathlib import Path
from collections import defaultdict
from flask import Flask, render_template, session, request
from datetime import datetime
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def signin_form():
    session['token'] = None
    return render_template('signin.html')

@app.route('/', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
	#curl -X GET "http://127.0.0.1:5000/token?username=admin&password=admin" -H "accept: application/json"
    #headers = {'Accept':'application/json'}
    r = requests.get('http://127.0.0.1:5000/token?username=' + str(username) + '&password=' + str(password))
    item = r.json()
    print(item)
    if r.ok:
        global token
        token = item['token']
        session['token'] = token
        return render_template('dashboard.html', username = username)
    return render_template('signin.html', message = 'invalid username or password', username = username)

@app.route('/prediction', methods=['GET'])
def prediction():
    return render_template('dashboard.html')

@app.route('/all', methods=['GET'])
def all():
    response = requests.get('http://127.0.0.1:5000/predictions', headers={'AUTH-TOKEN':token} )
    item = response.json()
    print(item)
    if response.ok:
        return render_template('all.html',records=item)
    return render_template('all.html',message='request refused')


@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register_post():
    username = request.form['username']
    password = request.form['password']
    #curl -X GET "http://127.0.0.1:5000/token?username=admin&password=admin" -H "accept: application/json"
    #headers = {'Accept':'application/json'}
    r = requests.post('http://127.0.0.1:5000/token?username=' + str(username) + '&password=' + str(password))
    item = r.json()
    if r.ok:
        return render_template('signin.html', username = 'registe successfully')
    return render_template('signin.html', message = item['message'])



@app.route('/predictions', methods=['GET'])
def make_history():
    print('saved')
    return render_template('dashboard.html',message='prediction saved successfully.')

@app.route('/new_prediction', methods=['GET'])
def delete_history():
    print('unsaved')
    global curr_pred
    print(curr_pred)
    response = requests.delete('http://127.0.0.1:5000/predictions/'+str(curr_pred), headers={'AUTH-TOKEN':token} )
    item = response.json()
    print(item)

    curr_pred = ''
    if response.ok:
        return render_template('dashboard.html', message=f'prediction {curr_pred} unsaved.')
    return render_template('dashboard.html',message=f'prediction {curr_pred} unsaved.')


@app.route('/predictions', methods=['POST'])
def post_pred():

    if 'pid' in request.form:
        try:
            H_buildUpPlaySpeed = int(request.form['H_buildUpPlaySpeed'])
            H_buildUpPlayDribbling = int(request.form['H_buildUpPlayDribbling'])
            H_buildUpPlayPassing = int(request.form['H_buildUpPlayPassing'])
            H_chanceCreationPassing = int(request.form['H_chanceCreationPassing'])
            H_chanceCreationCrossing = int(request.form['H_chanceCreationCrossing'])
            H_chanceCreationShooting = int(request.form['H_chanceCreationShooting'])
            H_defencePressure = int(request.form['H_defencePressure'])
            H_defenceAggression = int(request.form['H_defenceAggression'])

            A_buildUpPlaySpeed = int(request.form['A_buildUpPlaySpeed'])
            A_buildUpPlayDribbling = int(request.form['A_buildUpPlayDribbling'])
            A_buildUpPlayPassing = int(request.form['A_buildUpPlayPassing'])
            A_chanceCreationPassing = int(request.form['A_chanceCreationPassing'])
            A_chanceCreationCrossing = int(request.form['A_chanceCreationCrossing'])
            A_chanceCreationShooting = int(request.form['A_chanceCreationShooting'])
            A_defencePressure = int(request.form['A_defencePressure'])
            A_defenceAggression = int(request.form['A_defenceAggression'])
        except:
            return render_template('dashboard.html',message='Please give an int in attributes filds.')

        match = {'p_name':request.form['pid'],
                'H_name':request.form['H_name'],
                'H_buildUpPlaySpeed':H_buildUpPlaySpeed,
                'H_buildUpPlayDribbling':H_buildUpPlayDribbling,
                'H_buildUpPlayPassing':H_buildUpPlayPassing,
                'H_chanceCreationPassing':H_chanceCreationPassing,
                'H_chanceCreationCrossing':H_chanceCreationCrossing,
                'H_chanceCreationShooting':H_chanceCreationShooting,
                'H_defencePressure':H_defencePressure,
                'H_defenceAggression':H_defenceAggression,
                'A_name':request.form['A_name'],
                'A_buildUpPlayDribbling':A_buildUpPlayDribbling,
                'A_buildUpPlaySpeed':A_buildUpPlaySpeed,
                'A_buildUpPlayPassing':A_buildUpPlayPassing,
                'A_chanceCreationPassing':A_chanceCreationPassing,
                'A_chanceCreationCrossing':A_chanceCreationCrossing,
                'A_chanceCreationShooting':A_chanceCreationShooting,
                'A_defencePressure':A_defencePressure,
                'A_defenceAggression':A_defenceAggression
                }
        print(match)
        response = requests.post('http://127.0.0.1:5000/predictions',headers={'AUTH-TOKEN':token},json=match)
        r = response.json()
        print(r)
        if response.ok:
            response = requests.get('http://127.0.0.1:5000/predictions/'+r['location'][7:], headers={'AUTH-TOKEN':token})
            match = response.json()
            if response.ok:
                global curr_pred
                curr_pred = match['_id']
                return render_template('result.html',H_1=match['H_buildUpPlaySpeed'],H_2=match['H_buildUpPlayDribbling'],\
                    H_3=match['H_buildUpPlayPassing'],H_4=match['H_chanceCreationPassing'],H_5=match['H_chanceCreationShooting'],\
                    H_6=match['H_defencePressure'],H_7=match['H_defenceAggression'],H_8=match['H_defenceAggression'],\
                    A_1=match['A_buildUpPlayDribbling'],A_2=match['A_buildUpPlaySpeed'],\
                    A_3=match['A_buildUpPlayPassing'],A_4=match['A_chanceCreationPassing'],A_5=match['A_chanceCreationCrossing'],\
                    A_6=match['A_chanceCreationShooting'],A_7=match['A_defencePressure'],A_8=match['A_defenceAggression'],\
                    H_result=match['result'])
            return render_template('dashboard.html',message=match['message'])
    return render_template('dashboard.html',message=r['message'])


@app.route('/history/<p_id>', methods=['GET'])
def show_history(p_id):
    print(p_id)
    response = requests.delete('http://127.0.0.1:5000/predictions/'+str(p_id), headers={'AUTH-TOKEN':token} )
    match = response.json()
    print(match)   
    return all()


@app.route('/predictions/<p_id>', methods=['GET'])
def get_pred(p_id):
    #preid = request.form['preid']
    print(p_id)
    response = requests.get('http://127.0.0.1:5000/predictions/'+str(p_id), headers={'AUTH-TOKEN':token} )
    match = response.json()
    print(match)
    if response.ok:
    	return render_template('record.html',H_1=match['H_buildUpPlaySpeed'],H_2=match['H_buildUpPlayDribbling'],\
                    H_3=match['H_buildUpPlayPassing'],H_4=match['H_chanceCreationPassing'],H_5=match['H_chanceCreationShooting'],\
                    H_6=match['H_defencePressure'],H_7=match['H_defenceAggression'],H_8=match['H_defenceAggression'],\
                    A_1=match['A_buildUpPlayDribbling'],A_2=match['A_buildUpPlaySpeed'],\
                    A_3=match['A_buildUpPlayPassing'],A_4=match['A_chanceCreationPassing'],A_5=match['A_chanceCreationCrossing'],\
                    A_6=match['A_chanceCreationShooting'],A_7=match['A_defencePressure'],A_8=match['A_defenceAggression'],\
                    H_result=match['result'],pre_id=p_id)
    return all()




if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    token = ''
    pid = 0
    curr_pred = ''
    app.run(debug=True, port=2424)   #Ive change from 5000 to 2424
