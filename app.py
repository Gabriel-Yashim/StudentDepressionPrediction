# -*- coding: utf-8 -*-
"""
Created on Mon May 16 12:36:23 2022

@author: YASHIM GABRIEL
"""

import numpy as np 
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('RandomForest.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
     ag = int(request.form['age'])
     lvl = int(request.form['level'])
     usd = int(request.form['used'])
     lck = int(request.form['lack'])
     slp = int(request.form['sleep'])
     trd = int(request.form['tired'])
     apt = int(request.form['appetite'])
     bd = int(request.form['bad'])
     conc = int(request.form['concentrate'])
     rest = int(request.form['restless'])
     dth = int(request.form['death'])
     att = int(request.form['attack'])
     diag = int(request.form['diagnosed'])
     #scr = int(request.form['score'])
     score = lck + slp + trd + apt + bd + conc + rest + dth
    
     final_features = np.array([[ag,lvl,usd,lck,slp,trd,apt,bd,conc,rest,dth,att,diag,score]])
     prediction = model.predict(final_features)
    
     output = prediction[0]
     
     return render_template('results.html', Score_num=score, prediction_text=output)
     

if __name__ == "__main__":
    app.run(debug=True)