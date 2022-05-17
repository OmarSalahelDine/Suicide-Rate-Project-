from flask import Flask, request, jsonify , render_template
from joblib import load
from helper import transform_features
import pandas as pd
from xgboost import XGBClassifier

app = Flask(__name__)

scaler = load('scaler.h5')
model = XGBClassifier()
model.load_model('model5.h5')

@app.route('/', methods = ['GET'])
def index():
    
    return render_template('suicide_html.html')

@app.route('/predict', methods = ['POST'])
def predict():

    #d = request.json
    
    d = request.form.to_dict()


    keys = ['country', 'year', 'sex', 'age','population', 'HDI', 'gdp_per_capita']


    d = {key: d[key] for key in keys}


    x = pd.DataFrame.from_records([d])
    x = transform_features(x)
    x = scaler.transform(x)
    prediction = int(model.predict(x)[0])
    
    d['prediction'] = f'{prediction + 1} out of 4'

    return render_template('suicide_html.html', **d)

    #danger_levels = [ 'yellow' , 'dark yellow' , 'orange' , 'red']
    
    #return jsonify({'danger_levels': danger_levels[prediction]})


if __name__ == '__main__':
    
    app.run(debug = True)


