from flask import Flask,render_template,request
import os
import numpy as np
import pickle
model = pickle.load(open(r"C:\Users\renuk\june\model.pkl",'rb'))
app= Flask(__name__)
#FLASK_APP=app
@app.route('/')
def home():
     return render_template('titanic.html')
@app.route('/predict',methods=['POST'])
def predict():
    pclass= int(request.form.get('pclass')) ## pclass give in text convert in to int
    age = float(request.form.get('age'))
    sibsp = int(request.form.get('sibsp'))
    parch = int(request.form.get('parch'))
    fare = float(request.form.get('fare'))
    result = model.predict(np.array([pclass,age,sibsp,parch,fare]).reshape(1,5))
    print(result)
    if result[0]==1:
        result = 'survived'
    else:
        result = 'not survived'
    return render_template('titanic.html',result=result)

if __name__=='__main__':
    app.run('0.0.0.0',port=7845)

