# Analysis and Price Prediction of Fully Electric Cars Using Machine Learning

## Overview
This project performs comprehensive analysis of fully electric cars and implements machine learning models to predict electric vehicle prices. It includes data exploration, feature engineering, model training, and evaluation using various ML algorithms.

## Features
- **Exploratory Data Analysis (EDA)**: Detailed analysis of electric vehicle dataset
- **Feature Engineering**: Creation and transformation of relevant features
- **Multiple ML Models**: Comparison of different regression models
- **Price Prediction**: Accurate prediction of EV prices based on vehicle characteristics
- **Model Evaluation**: Comprehensive metrics and visualizations
- **Data Visualization**: Insightful charts and graphs for data understanding
- **Statistical Analysis**: Deep dive into correlations and patterns

## Technologies Used
- **Python**: Primary language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning algorithms
- **Matplotlib & Seaborn**: Data visualization
- **Jupyter Notebook**: Interactive analysis and documentation

## Prerequisites
- Python 3.8 or higher
- Jupyter Notebook or JupyterLab
- pip or conda package manager

Open the analysis notebooks in order:
   - `01_data_exploration.ipynb` - Initial data exploration
   - `02_data_cleaning.ipynb` - Data preprocessing and cleaning
   - `03_feature_engineering.ipynb` - Feature creation and selection
   - `04_model_training.ipynb` - Model development and training
   - `05_model_evaluation.ipynb` - Results analysis and comparison

## Dataset
The project uses a comprehensive dataset of electric vehicles including:
- **Features**: Brand, model, battery capacity, range, motor power, etc.
- **Target**: Price of the vehicle
- **Records**: Multiple EV models from various manufacturers

## Machine Learning Models
The project implements and compares:
- **Linear Regression**: Baseline model
- **Decision Tree Regressor**: Tree-based approach
- **Random Forest**: Ensemble method
- **Gradient Boosting**: Advanced ensemble technique
- **Support Vector Regression (SVR)**: Kernel-based method
- **Neural Networks**: Deep learning approach

## Key Findings
- Battery capacity is a strong predictor of EV price
- Motor power significantly influences pricing
- Brand reputation affects market price
- Driving range correlates with overall cost
- Charging infrastructure affects market value

## Model Performance
Results include:
- **R² Score**: Model accuracy on test data
- **Mean Absolute Error (MAE)**: Average prediction error
- **Root Mean Squared Error (RMSE)**: Error magnitude
- **Cross-validation scores**: Model generalization ability

## Data Preprocessing
- Handling missing values
- Outlier detection and treatment
- Categorical variable encoding
- Feature scaling and normalization
- Train-test split (80-20)

## Visualizations
The project includes:
- Distribution plots of features
- Correlation heatmaps
- Price vs feature scatter plots
- Model performance comparisons
- Residual analysis plots
- Feature importance charts

## Results
The best-performing model achieves:
- High R² score on test data
- Low prediction error
- Good generalization capability
- Reliable price predictions for new EV models

## Project Structure
```
├── data/                    # Dataset files
├── notebooks/              # Jupyter notebooks
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_model_training.ipynb
│   └── 05_model_evaluation.ipynb
├── src/                    # Python scripts
├── models/                 # Trained model files
├── requirements.txt        # Python dependencies
└── README.md
```
