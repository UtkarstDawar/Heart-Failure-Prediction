# Heart Failure Risk Prediction

A machine learning-powered web application that predicts heart failure risk based on clinical parameters using a Random Forest model.

## Overview

This Flask web application uses a trained Random Forest model to predict the risk of heart failure based on patient clinical data. The model analyzes 12 key medical parameters to provide a risk assessment with probability scores.

## Features

- **Web Interface**: Clean, responsive web form for data input
- **Machine Learning**: Random Forest model trained on clinical data
- **Risk Assessment**: Provides both risk classification (HIGH/LOW) and probability scores
- **Input Validation**: Comprehensive error handling for invalid inputs
- **Real-time Predictions**: Instant results upon form submission

## Clinical Parameters

The model analyzes the following 12 parameters:

1. **Age** - Patient age in years
2. **Anaemia** - Decrease of red blood cells or hemoglobin (0: No, 1: Yes)
3. **Creatinine Phosphokinase** - Level of CPK enzyme in blood (mcg/L)
4. **Diabetes** - Whether patient has diabetes (0: No, 1: Yes)
5. **Ejection Fraction** - Percentage of blood leaving heart at each contraction (%)
6. **High Blood Pressure** - Whether patient has hypertension (0: No, 1: Yes)
7. **Platelets** - Platelet count in blood (kiloplatelets/mL)
8. **Serum Creatinine** - Level of serum creatinine in blood (mg/dL)
9. **Serum Sodium** - Level of serum sodium in blood (mEq/L)
10. **Sex** - Gender (0: Female, 1: Male)
11. **Smoking** - Whether patient smokes (0: No, 1: Yes)
12. **Time** - Follow-up period (days)

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/heart-failure-prediction.git
   cd heart-failure-prediction
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the application**
   ```bash
   python app.py
   ```

2. **Access the web interface**
   - Open your browser and go to `http://localhost:5000`

3. **Input patient data**
   - Fill in all required clinical parameters
   - Click "Predict Risk" to get results

4. **View results**
   - The application will display risk classification (HIGH/LOW)
   - Probability score indicating confidence level

## File Structure

```
heart-failure-prediction/
├── app.py                                    # Main Flask application
├── hf_rf_model.pkl                          # Trained Random Forest model
├── heartfailure.ipynb                       # Jupyter notebook for model training
├── heart_failure_clinical_records_dataset (1).csv  # Training dataset
├── templates/
│   └── index.html                           # Web interface template
├── requirements.txt                         # Python dependencies
├── README.md                               # Project documentation
└── .gitignore                              # Git ignore file
```

## Model Information

- **Algorithm**: Random Forest Classifier
- **Training Data**: Heart failure clinical records dataset
- **Features**: 12 clinical parameters
- **Output**: Binary classification (0: No heart failure, 1: Heart failure risk)
- **Model File**: `hf_rf_model.pkl` (trained using scikit-learn)

## API Endpoints

- `GET /` - Main page with input form
- `POST /predict` - Submit patient data for prediction

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Machine Learning**: scikit-learn, joblib
- **Frontend**: HTML5, CSS3, JavaScript
- **Data Processing**: pandas, numpy
- **Model**: Random Forest Classifier

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

**Important**: This application is for educational and research purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical decisions.

## Dataset Source

The model is trained on the Heart Failure Clinical Records Dataset, which contains medical records of 299 patients with heart failure collected during their follow-up period.

## Contact

Your Name - your.email@example.com

Project Link: [https://github.com/yourusername/heart-failure-prediction](https://github.com/yourusername/heart-failure-prediction)
