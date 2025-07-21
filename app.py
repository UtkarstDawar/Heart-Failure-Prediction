from flask import Flask, request, render_template, flash
import joblib

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

# Load trained model
model = joblib.load('hf_rf_model.pkl')

# Homepage route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    fields = [
        'age','anaemia','creatinine_phosphokinase','diabetes',
        'ejection_fraction','high_blood_pressure','platelets',
        'serum_creatinine','serum_sodium','sex','smoking','time'
    ]
    
    try:
        data = [float(request.form.get(f)) for f in fields]
    except Exception as e:
        flash(f"Invalid input: {e}")
        return render_template('index.html')
    
    pred = model.predict([data])[0]
    proba = model.predict_proba([data])[0][1]

    result = "HIGH risk of heart failure." if pred == 1 else "LOW risk of heart failure."
    return render_template('index.html', prediction=result, probability=round(proba, 2))

if __name__ == '__main__':
    app.run(debug=True)
