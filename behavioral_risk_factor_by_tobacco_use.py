# -*- coding: utf-8 -*-
"""Behavioral Risk Factor By Tobacco Use.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FgVre0Z58u0W4at98J5j9oXRy_ioMDja

***APPLIED MACHINE LEARNING LAB PROJECT***  📊

**Behavioral Risk Factor By Tobacco Use** 🚬

Importing Libraries & reading data
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Behavioral_Risk_Factor_Data__Tobacco_Use__2011_to_present_.csv")

df.head()

df.tail()

df.describe()

df.shape

df.dtypes

df.info()

pd.DataFrame(df)

df.nunique()

df.duplicated()

df.duplicated().sum()

df.isnull().sum()

float_columns = df.select_dtypes(include=['float64']).columns
int_columns = df.select_dtypes(include=['int64']).columns
df[float_columns] = df[float_columns].fillna(df[float_columns].mean())
df[int_columns] = df[int_columns].fillna(df[int_columns].mean())

columns_to_drop = ['YEAR', 'LocationAbbr', 'DataSource', 'Response', 'Data_Value_Unit', 'Data_Value_Footnote_Symbol', 'Data_Value_Footnote',
                   'GeoLocation', 'TopicTypeId', 'TopicId', 'MeasureId', 'StratificationID1', 'StratificationID2', 'StratificationID3', 'StratificationID4',
                   'SubMeasureID', 'DisplayOrder']
df = df.drop(columns=columns_to_drop)

print(df.info())

df.isnull().sum()

df.isna().sum()

df['Gender'].value_counts()

mask = np.random.choice([True, False], size=len(df))
df.loc[mask, 'Gender'] = 'Male'
df.loc[~mask, 'Gender'] = 'Female'
df['Gender'].value_counts()

import matplotlib.pyplot as plt
topic_high_confidence_sum = df.groupby('TopicDesc')['High_Confidence_Limit'].sum()

plt.figure(figsize=(6, 6))
topic_high_confidence_sum.plot(kind='pie', autopct='%1.1f%%', startangle=140,
                               colors=['lightseagreen', 'lightsalmon', 'lightblue', 'lightcoral', 'lightgoldenrodyellow'])
plt.title('Sum of High Confidence Limit by Topic')
plt.ylabel('')
plt.show()

"""Data Splitting"""

X = df.drop(['High_Confidence_Limit', 'LocationDesc', 'TopicType', 'Data_Value_Type',], axis=1)
y = df['High_Confidence_Limit']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""Linear Regression"""

from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
label_encoders = {}
categorical_columns = X.select_dtypes(include=['object']).columns

for col in categorical_columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
y_pred = lin_reg.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

coefficients = pd.DataFrame(lin_reg.coef_, X.columns, columns=['Coefficient'])
print(coefficients)

"""Logistic Regression"""

from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Define features and target variable
X = df.drop(['High_Confidence_Limit', 'LocationDesc', 'TopicType', 'Data_Value_Type'], axis=1)
y = df['High_Confidence_Limit'].apply(lambda x: 1 if x > df['High_Confidence_Limit'].mean() else 0)  # Binarize the target variable

# Convert categorical variables to numeric using LabelEncoder
label_encoders = {}
categorical_columns = X.select_dtypes(include=['object']).columns

for col in categorical_columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the logistic regression model
log_reg = LogisticRegression(max_iter=1000)

# Train the model
log_reg.fit(X_train, y_train)

# Make predictions
y_pred = log_reg.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# Output results
print(f"Accuracy: {accuracy}")
print("Confusion Matrix:")
print(conf_matrix)
print("Classification Report:")
print(class_report)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Define features and target variable
X = df.drop(['High_Confidence_Limit', 'LocationDesc', 'TopicType', 'Data_Value_Type'], axis=1)
y = df['High_Confidence_Limit']

# Convert categorical variables to numeric using LabelEncoder
label_encoders = {}
categorical_columns = X.select_dtypes(include=['object']).columns

for col in categorical_columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

# Ensure there are no NaN values in X and y
X = X.fillna(X.mean())
y = y.fillna(y.mean())

# Normalize the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Check for NaN values in X and y
print("Checking for NaN values in X and y:")
print(pd.DataFrame(X).isna().sum())
print(y.isna().sum())

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the gradient descent function
def gradient_descent(X, y, learning_rate=0.001, epochs=1000):
    m, n = X.shape
    X = np.c_[np.ones(m), X]  # Add a column of ones for the intercept term
    theta = np.zeros(n + 1)   # Initialize weights

    for epoch in range(epochs):
        predictions = X.dot(theta)
        errors = predictions - y
        gradient = X.T.dot(errors) / m
        theta -= learning_rate * gradient

        # Check for NaN or infinite values in theta
        if not np.all(np.isfinite(theta)):
            print(f"Non-finite theta values at epoch {epoch}: {theta}")
            break

    return theta

# Perform gradient descent
theta = gradient_descent(X_train, y_train, learning_rate=0.001, epochs=1000)

# Make predictions
X_test_b = np.c_[np.ones(X_test.shape[0]), X_test]
y_pred = X_test_b.dot(theta)

# Check for NaN values in predictions
print("Checking for NaN values in predictions:")
print(np.isnan(y_pred).sum())

# Compute MAE and MSE
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

# Output results
print(f"Coefficients: {theta}")
print(f"Mean Absolute Error: {mae}")
print(f"Mean Squared Error: {mse}")

"""Gradient Descent, MAE & MSE"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Define features and target variable
X = df.drop(['High_Confidence_Limit', 'LocationDesc', 'TopicType', 'Data_Value_Type'], axis=1)
y = df['High_Confidence_Limit']

# Convert categorical variables to numeric using LabelEncoder
label_encoders = {}
categorical_columns = X.select_dtypes(include=['object']).columns

for col in categorical_columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

# Ensure there are no NaN values in X and y
X = X.fillna(X.mean())
y = y.fillna(y.mean())

# Normalize the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the gradient descent function
def gradient_descent(X, y, learning_rate=0.001, epochs=1000):
    m, n = X.shape
    X = np.c_[np.ones(m), X]  # Add a column of ones for the intercept term
    theta = np.zeros(n + 1)   # Initialize weights
    cost_history = []         # To store the cost at each iteration

    for epoch in range(epochs):
        predictions = X.dot(theta)
        errors = predictions - y
        gradient = X.T.dot(errors) / m
        theta -= learning_rate * gradient
        cost = (1 / (2 * m)) * np.sum(errors ** 2)
        cost_history.append(cost)

    return theta, cost_history

# Perform gradient descent
theta, cost_history = gradient_descent(X_train, y_train, learning_rate=0.001, epochs=1000)

# Plot the cost history
plt.plot(range(len(cost_history)), cost_history)
plt.xlabel("Iterations")
plt.ylabel("Cost")
plt.title("Cost History over Iterations")
plt.show()

# Make predictions
X_test_b = np.c_[np.ones(X_test.shape[0]), X_test]  # Add a column of ones for the intercept term
y_pred = X_test_b.dot(theta)

# Compute MAE and MSE
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

# Output results
print(f"Gradient Descent: {theta}")
print(f"Mean Absolute Error: {mae}")
print(f"Mean Squared Error: {mse}")

"""Naive Bayes"""

import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

columns_to_drop = ['High_Confidence_Limit', 'LocationDesc', 'TopicType', 'Data_Value_Type']
X = df.drop(columns_to_drop, axis=1)

Y = pd.qcut(df['High_Confidence_Limit'], q=4, labels=False)

categorical_cols = X.select_dtypes(include=['object']).columns
X_encoded = pd.get_dummies(X, columns=categorical_cols)

X_train, X_test, Y_train, Y_test = train_test_split(X_encoded, Y, test_size=0.2, random_state=42)

nb_classifier = GaussianNB()
nb_classifier.fit(X_train, Y_train)
Y_pred = nb_classifier.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)
print("Naive Bayes Accuracy:", accuracy)

"""Decision Tree"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

df_sample = df.sample(frac=0.1, random_state=42)

X = df_sample.drop(['High_Confidence_Limit', 'LocationDesc', 'TopicType', 'Data_Value_Type'], axis=1)
y = df_sample['High_Confidence_Limit'].apply(lambda x: 1 if x > df_sample['High_Confidence_Limit'].mean() else 0)

label_encoders = {}
categorical_columns = X.select_dtypes(include=['object']).columns

for col in categorical_columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

column_names = X.columns

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

dt_classifier = DecisionTreeClassifier(random_state=42)
dt_classifier.fit(X_train, y_train)

y_pred = dt_classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Decision Tree Accuracy:", accuracy)

plt.figure(figsize=(20, 10))
plot_tree(dt_classifier, feature_names=column_names, class_names=['0', '1'], filled=True)
plt.show()

"""Random Forest"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

# Sample the data
df_sample = df.sample(frac=0.1, random_state=42)

# Preparing the data
X = df_sample.drop(['High_Confidence_Limit', 'LocationDesc', 'TopicType', 'Data_Value_Type'], axis=1)
y = df_sample['High_Confidence_Limit'].apply(lambda x: 1 if x > df_sample['High_Confidence_Limit'].mean() else 0)

# Convert categorical variables to numeric using LabelEncoder
label_encoders = {}
categorical_columns = X.select_dtypes(include=['object']).columns

for col in categorical_columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

# Store the column names
column_names = X.columns

# Normalize the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest classifier with reduced number of trees
rf_classifier = RandomForestClassifier(n_estimators=50, random_state=42)  # Reduced to 50 trees
rf_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_classifier.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Random Forest Accuracy:", accuracy)

# Visualize one of the trees from the forest
plt.figure(figsize=(20, 10))
plot_tree(rf_classifier.estimators_[0], feature_names=column_names, class_names=['0', '1'], filled=True)
plt.show()

"""KNN Classifier"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

X = df.drop(['High_Confidence_Limit', 'LocationDesc', 'TopicType', 'Data_Value_Type'], axis=1)
y = df['High_Confidence_Limit'].apply(lambda x: 1 if x > df['High_Confidence_Limit'].mean() else 0)

label_encoders = {}
categorical_columns = X.select_dtypes(include=['object']).columns

for col in categorical_columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

X = X.fillna(X.mean())
y = y.fillna(y.mean())

scaler = StandardScaler()
X = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

knn_classifier = KNeighborsClassifier(n_neighbors=5)

knn_classifier.fit(X_train, y_train)
y_pred = knn_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f"K-Nearest Neighbors Accuracy: {accuracy}")
print("Confusion Matrix:")
print(conf_matrix)
print("Classification Report:")
print(class_report)

"""Comparison"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
classifiers = {
    "Naive Bayes": GaussianNB(),
    "Logistic Regression": LogisticRegression(),
    "K-Nearest Neighbors": KNeighborsClassifier(),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier()
}

results = {}
for name, clf in classifiers.items():
    clf.fit(X_train, Y_train)
    Y_pred = clf.predict(X_test)
    accuracy = accuracy_score(Y_test, Y_pred)
    results[name] = accuracy
# Step 5: Compare the results
print("Accuracy Scores:")
for name, accuracy in results.items():
    print(f"{name}: {accuracy}")
best_algorithm = max(results, key=results.get)
print(f"\nBest performing algorithm: {best_algorithm} with accuracy {results[best_algorithm]}")

"""

```
# This is formatted as code
```

Feature Regularization (Ridge & Lasso)"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import Ridge, Lasso
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Define features and target variable
X = df.drop(['High_Confidence_Limit', 'LocationDesc', 'TopicType', 'Data_Value_Type'], axis=1)
y = df['High_Confidence_Limit'].apply(lambda x: 1 if x > df['High_Confidence_Limit'].mean() else 0)  # Binarize the target variable

# Convert categorical variables to numeric using LabelEncoder
label_encoders = {}
categorical_columns = X.select_dtypes(include=['object']).columns

for col in categorical_columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

X = X.fillna(X.mean())
y = y.fillna(y.mean())

feature_names = X.columns
scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Function to evaluate models
def evaluate_model(y_true, y_pred, model_name):
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    print(f"{model_name} - Mean Absolute Error: {mae}")
    print(f"{model_name} - Mean Squared Error: {mse}")
    print(f"{model_name} - R^2 Score: {r2}")

# Lasso Regularization with multiple alpha values
lasso_alphas = [0.01, 0.1, 1.0]

for alpha in lasso_alphas:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    y_pred_lasso = lasso.predict(X_test)
    print(f"\nEvaluating Lasso Regression with alpha={alpha}")
    evaluate_model(y_test, y_pred_lasso, f"Lasso Regression (alpha={alpha})")
    print(f"Lasso Intercept (alpha={alpha}): {lasso.intercept_}")
    lasso_coefficients = pd.DataFrame(lasso.coef_, index=feature_names, columns=[f'Lasso Coefficient (alpha={alpha})'])
    print(f"\nLasso Coefficients (alpha={alpha}):")
    print(lasso_coefficients)

# Ridge Regularization with multiple alpha values
ridge_alphas = [0.01, 0.1, 1.0]

for alpha in ridge_alphas:
    ridge = Ridge(alpha=alpha)
    ridge.fit(X_train, y_train)
    y_pred_ridge = ridge.predict(X_test)
    print(f"\nEvaluating Ridge Regression with alpha={alpha}")
    evaluate_model(y_test, y_pred_ridge, f"Ridge Regression (alpha={alpha})")
    print(f"Ridge Intercept (alpha={alpha}): {ridge.intercept_}")
    ridge_coefficients = pd.DataFrame(ridge.coef_, index=feature_names, columns=[f'Ridge Coefficient (alpha={alpha})'])
    print(f"\nRidge Coefficients (alpha={alpha}):")
    print(ridge_coefficients)

"""Perceptron (from Scratch)"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler


X = df.drop(['High_Confidence_Limit', 'LocationDesc', 'TopicType', 'Data_Value_Type'], axis=1)
y = df['High_Confidence_Limit'].apply(lambda x: 1 if x > df['High_Confidence_Limit'].mean() else 0)

# Convert categorical variables to numeric using LabelEncoder
label_encoders = {}
categorical_columns = X.select_dtypes(include=['object']).columns

for col in categorical_columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

# Normalize the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Convert DataFrame to numpy array
X = X if isinstance(X, np.ndarray) else X.values
y = y.values

# Ensure there are no NaNs or infinities
assert not np.isnan(X).any(), "NaN values found in X"
assert not np.isinf(X).any(), "Infinite values found in X"
assert not np.isnan(y).any(), "NaN values found in y"
assert not np.isinf(y).any(), "Infinite values found in y"

# Initialize weights and bias
weights = np.random.rand(X.shape[1])
bias = np.random.rand(1)

# Hyperparameters
alpha = 0.00001  # Further reduce learning rate
iterations = 500  # Reduce iterations to observe initial behavior

# Training the perceptron
for i in range(iterations):
    y_pred = np.dot(X, weights) + bias
    error = y - y_pred

    # Compute gradients
    grad_weights = np.dot(X.T, error)
    grad_bias = np.sum(error)

    # Gradient clipping
    grad_weights = np.clip(grad_weights, -1, 1)
    grad_bias = np.clip(grad_bias, -1, 1)

    weights += alpha * grad_weights
    bias += alpha * grad_bias

    # Check for numerical issues
    if np.isnan(weights).any() or np.isnan(bias).any():
        print("Numerical issue detected, stopping training.")
        break

# Predict
y_pred = np.dot(X, weights) + bias

# Evaluation
regression_score = np.mean(np.abs(y_pred - y))
mse = np.mean((y_pred - y) ** 2)

print(f"Perceptron Regression (from scratch) - Regression Score: {regression_score}")
print(f"Perceptron Regression (from scratch) - Mean Squared Error: {mse}")
print(f"Perceptron Regression (from scratch) - Weights: {weights}")
print(f"Perceptron Regression (from scratch) - Bias: {bias}")

"""Perceptron (with Library)"""

import pandas as pd
from sklearn.linear_model import Perceptron
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

X = df.drop(['High_Confidence_Limit', 'LocationDesc', 'TopicType', 'Data_Value_Type'], axis=1)
y = df['High_Confidence_Limit'].apply(lambda x: 1 if x > df['High_Confidence_Limit'].mean() else 0)

label_encoders = {}
categorical_columns = X.select_dtypes(include=['object']).columns

for col in categorical_columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

scaler = StandardScaler()
X = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = Perceptron(fit_intercept=True, max_iter=1000, tol=1e-3)

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

# Evaluation
reg_score = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
error = np.sum(np.abs(y_test - y_pred))

print(f"Perceptron Regression (with library) - Regression Score: {reg_score}")
print(f"Perceptron Regression (with library) - Mean Squared Error: {mse}")
print(f"Perceptron Regression (with library) - Total Error: {error}")
print(f"Perceptron Regression (with library) - Weights: {clf.coef_}")
print(f"Perceptron Regression (with library) - Intercept: {clf.intercept_}")

"""  MLP Regressor"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, r2_score

X = df.drop(['High_Confidence_Limit', 'LocationDesc', 'TopicType', 'Data_Value_Type'], axis=1)
y = df['High_Confidence_Limit']

label_encoders = {}
categorical_columns = X.select_dtypes(include=['object']).columns

for col in categorical_columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

scaler = StandardScaler()
X = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

mlp_regressor = MLPRegressor(hidden_layer_sizes=(10,), activation='relu', random_state=1, max_iter=1000)

mlp_regressor.fit(X_train, y_train)

predictions = mlp_regressor.predict(X_test)

mse = mean_squared_error(y_test, predictions)
score = mlp_regressor.score(X_test, y_test)

print(f"Regression Score: {score:.2f}")
print(f"Mean Squared Error: {mse:.2f}")

"""MLP Classifier"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score


X = df.drop(['High_Confidence_Limit', 'LocationDesc', 'TopicType', 'Data_Value_Type'], axis=1)
y = df['High_Confidence_Limit'].apply(lambda x: 1 if x > df['High_Confidence_Limit'].mean() else 0)

label_encoders = {}
categorical_columns = X.select_dtypes(include=['object']).columns

for col in categorical_columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

scaler = StandardScaler()
X = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

mlp_classifier = MLPClassifier(hidden_layer_sizes=(8, 4), activation='tanh', solver='adam', random_state=1, max_iter=1000)

mlp_classifier.fit(X_train, y_train)
predictions = mlp_classifier.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions, average='macro')
recall = recall_score(y_test, predictions, average='macro')

print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
cross_val_scores = cross_val_score(mlp_classifier, X, y, cv=5, scoring='accuracy')
print(f"Cross-validation Accuracy: {cross_val_scores.mean():.2f} ± {cross_val_scores.std():.2f}")

"""K-Fold Cross-Validation"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, KFold
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

X = df.drop(['High_Confidence_Limit', 'LocationDesc', 'TopicType', 'Data_Value_Type'], axis=1)
y = df['High_Confidence_Limit'].apply(lambda x: 1 if x > df['High_Confidence_Limit'].mean() else 0)

label_encoders = {}
categorical_columns = X.select_dtypes(include=['object']).columns

for col in categorical_columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

scaler = StandardScaler()
X = scaler.fit_transform(X)
X = np.array(X)
y = np.array(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

k = 10
kf = KFold(n_splits=k, shuffle=True, random_state=42)

train_accuracy = []
train_precision = []
train_recall = []
train_f1 = []
val_accuracy = []
val_precision = []
val_recall = []
val_f1 = []
for train_index, val_index in kf.split(X_train):
    X_fold_train, X_fold_val = X_train[train_index], X_train[val_index]
    y_fold_train, y_fold_val = y_train[train_index], y_train[val_index]

    mlp_classifier = MLPClassifier(hidden_layer_sizes=(8, 4), activation='tanh', solver='adam', random_state=1, max_iter=1000)

    mlp_classifier.fit(X_fold_train, y_fold_train)

    # Evaluate on training data
    train_pred = mlp_classifier.predict(X_fold_train)
    train_accuracy.append(accuracy_score(y_fold_train, train_pred))
    train_precision.append(precision_score(y_fold_train, train_pred, average='macro'))
    train_recall.append(recall_score(y_fold_train, train_pred, average='macro'))
    train_f1.append(f1_score(y_fold_train, train_pred, average='macro'))

    # Evaluate on validation data
    val_pred = mlp_classifier.predict(X_fold_val)
    val_accuracy.append(accuracy_score(y_fold_val, val_pred))
    val_precision.append(precision_score(y_fold_val, val_pred, average='macro'))
    val_recall.append(recall_score(y_fold_val, val_pred, average='macro'))
    val_f1.append(f1_score(y_fold_val, val_pred, average='macro'))

# Evaluate the model on the test set
test_pred = mlp_classifier.predict(X_test)
test_accuracy = accuracy_score(y_test, test_pred)
test_precision = precision_score(y_test, test_pred, average='macro')
test_recall = recall_score(y_test, test_pred, average='macro')
test_f1 = f1_score(y_test, test_pred, average='macro')

# Calculate the average of all folds
print("Training Set Metrics:")
print(f"Accuracy: {np.mean(train_accuracy):.2f} ± {np.std(train_accuracy):.2f}")
print(f"Precision: {np.mean(train_precision):.2f} ± {np.std(train_precision):.2f}")
print(f"Recall: {np.mean(train_recall):.2f} ± {np.std(train_recall):.2f}")
print(f"F1-score: {np.mean(train_f1):.2f} ± {np.std(train_f1):.2f}")

print("\nValidation Set Metrics:")
print(f"Accuracy: {np.mean(val_accuracy):.2f} ± {np.std(val_accuracy):.2f}")
print(f"Precision: {np.mean(val_precision):.2f} ± {np.std(val_precision):.2f}")
print(f"Recall: {np.mean(val_recall):.2f} ± {np.std(val_recall):.2f}")
print(f"F1-score: {np.mean(val_f1):.2f} ± {np.std(val_f1):.2f}")

print("\nTest Set Metrics:")
print(f"Accuracy: {test_accuracy:.2f}")
print(f"Precision: {test_precision:.2f}")
print(f"Recall: {test_recall:.2f}")
print(f"F1-score: {test_f1:.2f}")

"""K-Means Clustering"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

X = df.drop(['High_Confidence_Limit', 'LocationDesc', 'TopicType', 'Data_Value_Type'], axis=1)

label_encoders = {}
categorical_columns = X.select_dtypes(include=['object']).columns

for col in categorical_columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le
scaler = StandardScaler()
X = scaler.fit_transform(X)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

wcss = []
max_clusters = 10
for i in range(1, max_clusters + 1):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X_pca)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(10, 6))
plt.plot(range(1, max_clusters + 1), wcss, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.grid(True)
plt.show()
k = 2
kmeans = KMeans(n_clusters=k, random_state=42)
y_kmeans = kmeans.fit_predict(X_pca)
plt.figure(figsize=(10, 6))
colors = ['r', 'g', 'b', 'y', 'c', 'm']
for i in range(k):
    plt.scatter(X_pca[y_kmeans == i, 0], X_pca[y_kmeans == i, 1], s=100, c=colors[i], label=f'Cluster {i}')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='black', marker='x', label='Centroids')
plt.title('K-Means Clustering')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend()
plt.grid(True)
plt.show()

"""K-Medoids Clustering"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA

columns_to_drop = ['LocationDesc', 'TopicType', 'Data_Value_Type']
columns_to_drop = [col for col in columns_to_drop if col in df.columns]
df = df.drop(columns_to_drop, axis=1)
X = df.drop(['High_Confidence_Limit'], axis=1)
Y = df['High_Confidence_Limit']

label_encoders = {}
categorical_columns = X.select_dtypes(include=['object']).columns
for col in categorical_columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col].astype(str))
    label_encoders[col] = le
X = X.values

scaler = StandardScaler()
X = scaler.fit_transform(X)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
np.random.seed(42)
subsample_indices = np.random.choice(X_pca.shape[0], size=1000, replace=False)
X_pca_subsample = X_pca[subsample_indices]

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

def assign_clusters(X, medoids):
    distances = np.array([[euclidean_distance(x, medoid) for medoid in medoids] for x in X])
    clusters = {i: [] for i in range(len(medoids))}
    for i, dist in enumerate(distances):
        cluster = np.argmin(dist)
        clusters[cluster].append(X[i])
    return clusters

def update_medoids(clusters):
    medoids = []
    for cluster_points in clusters.values():
        if len(cluster_points) > 0:
            cluster_points = np.array(cluster_points)
            cluster_distances = np.zeros((cluster_points.shape[0], cluster_points.shape[0]))
            for i, point1 in enumerate(cluster_points):
                for j, point2 in enumerate(cluster_points):
                    cluster_distances[i, j] = euclidean_distance(point1, point2)
            medoid_index = np.argmin(np.sum(cluster_distances, axis=1))
            medoids.append(cluster_points[medoid_index])
    return np.array(medoids)


def plot_clusters_medoids(X, clusters, medoids):
    colors = ['r', 'g', 'b', 'y', 'c', 'm']
    for cluster_id, cluster_points in clusters.items():
        cluster_color = colors[cluster_id % len(colors)]
        cluster_points = np.array(cluster_points)
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], c=cluster_color, label=f'Cluster {cluster_id}')
    plt.scatter(medoids[:, 0], medoids[:, 1], marker='x', s=200, c='black', label='Medoids')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('Custom K-Medoids Clustering')
    plt.legend()
    plt.show()

def kmedoids(X, k, max_iters=100):
    medoids = X[np.random.choice(X.shape[0], k, replace=False)]
    for _ in range(max_iters):
        clusters = assign_clusters(X, medoids)
        new_medoids = update_medoids(clusters)
        if np.array_equal(medoids, new_medoids):
            break
        medoids = new_medoids
    return clusters, medoids

def calculate_wcss(X, medoids):
    wcss = 0
    for point in X:
        distances = [euclidean_distance(point, medoid) for medoid in medoids]
        wcss += min(distances) ** 2
    return wcss

# Determine the optimal number of clusters using the elbow method
wcss_values = []
max_clusters = 10
for k in range(1, max_clusters + 1):
    _, medoids = kmedoids(X_pca_subsample, k, max_iters=50)
    wcss = calculate_wcss(X_pca_subsample, medoids)
    wcss_values.append(wcss)

plt.figure(figsize=(10, 6))
plt.plot(range(1, max_clusters + 1), wcss_values, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.grid(True)
plt.show()

# Fit the K-Medoids model
k = 2
clusters_medoids, medoids = kmedoids(X_pca_subsample, k, max_iters=50)
plot_clusters_medoids(X_pca_subsample, clusters_medoids, medoids)

print("Final clusters (K-Medoids):")
for i, cluster_points in clusters_medoids.items():
    print(f"Cluster {i}:")
    for point in cluster_points:
        print(point)
print("\nFinal medoids (K-Medoids):")
for medoid in medoids:
    print(medoid)

"""Dimentionality Reducton - PCA"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X = df.drop(['High_Confidence_Limit', 'LocationDesc', 'TopicType', 'Data_Value_Type'], axis=1)
y = df['High_Confidence_Limit'].apply(lambda x: 1 if x > df['High_Confidence_Limit'].mean() else 0)

# Convert categorical variables to numeric using LabelEncoder
label_encoders = {}
categorical_columns = X.select_dtypes(include=['object']).columns

for col in categorical_columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

# Normalize the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# PCA
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# Logistic Regression Model for PCA
model_pca = LogisticRegression()
model_pca.fit(X_train_pca, y_train)
y_pred_pca = model_pca.predict(X_test_pca)
accuracy_pca = accuracy_score(y_test, y_pred_pca)

print("Accuracy with PCA:", accuracy_pca)

"""Dimentionality Reduction - LDA"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


X = df.drop(['High_Confidence_Limit', 'LocationDesc', 'TopicType', 'Data_Value_Type'], axis=1)
y = df['High_Confidence_Limit'].apply(lambda x: 1 if x > df['High_Confidence_Limit'].mean() else 0)

# Convert categorical variables to numeric using LabelEncoder
label_encoders = {}
categorical_columns = X.select_dtypes(include=['object']).columns

for col in categorical_columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

# Normalize the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# LDA
lda = LinearDiscriminantAnalysis(n_components=1)
X_train_lda = lda.fit_transform(X_train, y_train)
X_test_lda = lda.transform(X_test)

# Logistic Regression Model for LDA
model_lda = LogisticRegression()
model_lda.fit(X_train_lda, y_train)
y_pred_lda = model_lda.predict(X_test_lda)
accuracy_lda = accuracy_score(y_test, y_pred_lda)

print("Accuracy with LDA:", accuracy_lda)

"""SVM - Classification"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

X = df.drop(['High_Confidence_Limit', 'LocationDesc', 'TopicType', 'Data_Value_Type'], axis=1)
y = df['High_Confidence_Limit'].apply(lambda x: 1 if x > df['High_Confidence_Limit'].mean() else 0)

label_encoders = {}
categorical_columns = X.select_dtypes(include=['object']).columns

for col in categorical_columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

scaler = StandardScaler()
X = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

svm_classifier = SVC()
svm_classifier.fit(X_train, y_train)
y_pred = svm_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
print("SVM Classification Results:")
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)

"""SVM - Regression"""

from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score

# For regression, we will not binarize the target variable
y = df['High_Confidence_Limit']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train SVM regressor
svm_regressor = SVR()
svm_regressor.fit(X_train, y_train)

# Predict and evaluate the regressor
y_pred = svm_regressor.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nSVM Regression Results:")
print("Mean Squared Error:", mse)
print("R^2 Score:", r2)
