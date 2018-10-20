
import os,re, glob
from pathlib import Path
from collections import defaultdict
from flask import Flask, render_template, session, request
from datetime import datetime
import requests
import json

app = Flask(__name__)
##

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     return render_template('home.html')

@app.route('/', methods=['GET'])
def signin_form():
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
    	return render_template('signin-ok.html', username = username)
    return render_template('signin.html', message = 'invalid username or password', username = username)


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
        return render_template('signin-ok.html', username = username)
    return render_template('signin.html', message = item['message'])

@app.route('/predictions', methods=['GET'])
def get_pred_list():

    response = requests.get('http://127.0.0.1:5000/predictions', headers={'AUTH-TOKEN':token} )
    print(token)
    item = response.json()
    print(item)
    if response.ok:
    	return render_template('signin-ok.html', username='username',data= item)
    return render_template('signin-ok.html', username='username',data=item['message'])

@app.route('/predictions', methods=['POST'])
def post_pred():
    if 'p_id' in request.form:
        p_id = request.form['p_id']
        response = requests.get('http://127.0.0.1:5000/predictions/'+str(p_id), headers={'AUTH-TOKEN':token} )
        match = response.json()
        print(match)

        if response.ok:
            return render_template('signin-ok.html',H_1=match['H_buildUpPlaySpeed'],H_2=match['H_buildUpPlayDribbling'],\
                H_3=match['H_buildUpPlayPassing'],H_4=match['H_chanceCreationPassing'],H_5=match['H_chanceCreationShooting'],\
                H_6=match['H_defencePressure'],H_7=match['H_defenceAggression'],H_8=match['H_defenceAggression'],\
                H_9=match['H_defenceTeamWidth'],A_1=match['A_buildUpPlayDribbling'],A_2=match['A_buildUpPlaySpeed'],\
                A_3=match['A_buildUpPlayPassing'],A_4=match['A_chanceCreationPassing'],A_5=match['A_chanceCreationCrossing'],\
                A_6=match['A_chanceCreationShooting'],A_7=match['A_defencePressure'],A_8=match['A_defenceAggression'],\
                A_9=match['A_defenceTeamWidth'])
        return render_template('signin-ok.html', username='username',data3=match['message'])

    if 'team1' in request.form:
        team1 = request.form['team1']
        team2 = request.form['team2']
        team1speed = request.form['team1speed']
        team2speed = request.form['team2speed']
        team1crossing = request.form['team1crossing']
        team2crossing = request.form['team2crossing']
        global pid
        data = {'prediction_id':pid,
        'team1':team1,
        'team2':team2,
        'team1speed':int(team1speed),
        'team2speed':int(team2speed),
        'team1crossing':int(team1crossing),
        'team2crossing':int(team2crossing)
        }
        #
        #'Content-Type': 'application/json'

        print(data)

        response = requests.post('http://127.0.0.1:5000/predictions',headers={'AUTH-TOKEN':token},json=data)
        item = response.json()
        print(item)
        if response.ok:
            return render_template('signin-ok.html', username='username',data2=item)
        return render_template('signin-ok.html', username='username',data2=item['message'])

    if 'delete_id' in request.form:
        delete_id = request.form['delete_id']
        response = requests.delete('http://127.0.0.1:5000/predictions/'+str(delete_id), headers={'AUTH-TOKEN':token} )
        item = response.json()
        print(item)
        if response.ok:
            return render_template('signin-ok.html', username='username',data4= item)
        return render_template('signin-ok.html', username='username',data4=item['message'])


# @app.route('/predictions/<p_id>', methods=['GET'])
# def get_pred(p_id):
#     #preid = request.form['preid']
#     print(p_id)

#     response = requests.get('http://127.0.0.1:5000/predictions/'+str(p_id), headers={'AUTH-TOKEN':token} )
#     print(token)
#     item = response.json()
#     print(item)
#     if response.ok:
#     	return render_template('signin-ok.html', username='username',data3= item)
#     return render_template('signin-ok.html', username='username',data3=item['message'])




if __name__ == '__main__':
    token = ''
    pid = 0
    app.run(debug=True, port=2424)   #Ive change from 5000 to 2424
