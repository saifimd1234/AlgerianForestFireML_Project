import pickle
from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


application = Flask(__name__)
app = application

# import ridge regression and standard scaler pickle
ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        Temperature=float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        new_data_scaled=standard_scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result=ridge_model.predict(new_data_scaled)

        return render_template('home.html',result=result[0])
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    # when we are running with the above host=0.0.0.0 we can access the application from any device in the same network, this is getting mapped to local IP address with port 5000 or you can provide the port number as well such as port = 5001 etc. By default the port number is 5000. Even if you give it or not

