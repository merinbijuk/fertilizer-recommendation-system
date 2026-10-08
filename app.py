
```python
from flask import Flask, render_template, request, send_from_directory
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Load the trained Decision Tree model
model_path = os.path.join(
    os.path.dirname(__file__),
    'fertilizer_decision_tree.pkl'
)

model = joblib.load(model_path)


@app.route('/')
def home():
    return render_template('index.html')


# Serve the PWA manifest
@app.route('/manifest.json')
def manifest():
    return send_from_directory('static', 'manifest.json')


@app.route('/predict', methods=['POST'])
def predict():

    data = {
        'Soil_Type': request.form['Soil_Type'],
        'Soil_pH': float(request.form['Soil_pH']),
        'Soil_Moisture': float(request.form['Soil_Moisture']),
        'Organic_Carbon': float(request.form['Organic_Carbon']),
        'Electrical_Conductivity': float(request.form['Electrical_Conductivity']),
        'Nitrogen_Level': float(request.form['Nitrogen_Level']),
        'Phosphorus_Level': float(request.form['Phosphorus_Level']),
        'Potassium_Level': float(request.form['Potassium_Level']),
        'Temperature': float(request.form['Temperature']),
        'Humidity': float(request.form['Humidity']),
        'Rainfall': float(request.form['Rainfall']),
        'Crop_Type': request.form['Crop_Type'],
        'Crop_Growth_Stage': request.form['Crop_Growth_Stage'],
        'Season': request.form['Season']
    }

    input_data = pd.DataFrame([data])

    prediction = model.predict(input_data)[0]

    return render_template(
        'index.html',
        prediction=prediction
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
