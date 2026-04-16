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
- **Python**: Primary language (96.5%)
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning algorithms
- **Matplotlib & Seaborn**: Data visualization
- **Jupyter Notebook**: Interactive analysis and documentation
- **Cython**: Performance optimization (2.6%)
- **C/C++**: Low-level optimizations

## Prerequisites
- Python 3.8 or higher
- Jupyter Notebook or JupyterLab
- pip or conda package manager

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/nika131/Analysis-and-Price-Prediction-of-Fully-Electric-Cars-Using-Machine-Learning.git
   cd Analysis-and-Price-Prediction-of-Fully-Electric-Cars-Using-Machine-Learning
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

2. Open the analysis notebooks in order:
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

## Future Improvements
- Incorporate real-time market data
- Add time-series analysis for price trends
- Implement advanced deep learning models
- Create a web-based prediction interface
- Add geolocation-based pricing factors

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

## Contributing
Contributions are welcome! Please feel free to submit a pull request with improvements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Support
For issues, questions, or suggestions, please open an issue on GitHub.