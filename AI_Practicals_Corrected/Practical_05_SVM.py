# PRACTICAL NO. 05
# AIM: To implement SVM for binary classification and evaluate its performance.
# Keep diabetes.csv in the same folder as this Python file.

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

file_path = os.path.join(os.path.dirname(__file__), "diabetes.csv")
if not os.path.exists(file_path):
    raise FileNotFoundError(
        "diabetes.csv not found. Download the dataset and place it beside this Python file."
    )

data = pd.read_csv(file_path)
print(data.head())

if "Outcome" not in data.columns:
    raise ValueError("The CSV file must contain an 'Outcome' column.")

X = data.drop("Outcome", axis=1)
y = data["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

svm = SVC(kernel="rbf", C=1.0, gamma="scale")
svm.fit(X_train, y_train)

y_pred = svm.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy =", accuracy)
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred, zero_division=0))
