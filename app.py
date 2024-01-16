from flask import Flask,render_template,request
import pickle
import bz2
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

R_pickle = bz2.BZ2File('Regression_trial2.pkl', 'rb')
model = pickle.load(R_pickle)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_fire():
    Temperature = float(request.form.get('Temperature'))
    Ws = float(request.form.get('Ws'))
    FFMC = float(request.form.get('FFMC'))
    DMC = float(request.form.get('DMC'))
    ISI = float(request.form.get('ISI'))
    

    #prediction
    result = model.predict(np.array([[Temperature, Ws, FFMC, DMC, ISI]]))
    if result[0] >= 1:
        result = "FOREST IS IN DANGER, CHANCES OF OCCURING FIRE IS",str(result),"%"
        
    else:
        result = 'FOREST IS IN SAFE CONDITION,NOT IN DANGER'

    return render_template('index.html',result=result)#for displaying output
    return str(result)
 
    print(result)

    if __name__ == '__main__':
        app.run(debug=True)
        


