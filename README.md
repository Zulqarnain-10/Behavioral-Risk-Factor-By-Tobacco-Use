# Behavioral Risk Factor by Tobacco Use

## Project Overview
This project aims to analyze the behavioral risk factors associated with tobacco use using various machine learning algorithms. The dataset includes multiple features and the target variable is 'High Confidence Limit'.

## Techniques Implemented
- **Data Preprocessing**: Cleaning, encoding, and normalizing data to ensure quality and consistency.
- **Exploratory Data Analysis (EDA)**: Utilizing Matplotlib and Seaborn for visualizations to uncover patterns and relationships.
- **Dimensionality Reduction**: Employing PCA to enhance model performance and visualization.
- **Modeling and Evaluation**: Implemented and compared multiple algorithms including:
  - **Regression Models**: Linear Regression.
  - **Classification Models**: Logistic Regression, Naive Bayes, K-Nearest Neighbors, Decision Trees, Random Forest, and SVM.
  - **Neural Networks**: Perceptron and Multi-Layer Perceptron (MLP).
  - **Clustering**: K-Means and K-Medoids.
  - **Regularization**: Lasso and Ridge Regression.
  - **Cross-Validation**: Ensuring robust model evaluation through k-fold cross-validation.

## Results
- **Random Forest** and **SVM** models achieved the highest accuracy, demonstrating their robustness and generalization capabilities.
- Detailed performance metrics such as accuracy, precision, recall, and F1-score were calculated for each model, allowing us to identify the most effective algorithms.

## Future Scope
- Further tuning of hyperparameters to optimize model performance.
- Exploring advanced algorithms like XGBoost and LightGBM.
- Implementing strategies to handle class imbalance and deploying models into production environments.

## Files
- [Dataset File](Behavioral_Risk_Factor_Data__Tobacco_Use__2011_to_present_.csv): The dataset used for the analysis.
- [Python Script](behavioral_risk_factor_by_tobacco_use.py): The Python script containing the data preprocessing and machine learning code.
- [Jupyter Notebook](Behavioral_Risk_Factor_By_Tobacco_Use.ipynb): The notebook file showcasing the entire analysis, code, and outputs.

## How to Run
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Zulqarnain-10/Behavioral-Risk-Factor-By-Tobacco-Use.git
   ```
2. **Navigate to the repository directory**:
   ```bash
   cd Behavioral-Risk-Factor-By-Tobacco-Use
   ```
3. **Install the required libraries**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Python script**:
   ```bash
   python behavioral_risk_factor_by_tobacco_use.py
   ```
5. **Open the Jupyter notebook**:
   ```bash
   jupyter notebook Behavioral_Risk_Factor_By_Tobacco_Use.ipynb
   ```

## License
This project is licensed under the MIT License - see the LICENSE file for details.
