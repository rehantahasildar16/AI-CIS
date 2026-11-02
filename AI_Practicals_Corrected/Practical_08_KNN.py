# PRACTICAL NO. 08
# AIM: To implement K-Nearest Neighbors and evaluate classification accuracy.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

data = {
    'Hours': [2, 3, 4, 5, 6, 7],
    'Attendance': [50, 60, 65, 70, 80, 90],
    'Result': ['Fail', 'Fail', 'Pass', 'Pass', 'Pass', 'Pass']
}

df = pd.DataFrame(data)
X = df[['Hours', 'Attendance']]
y = df['Result']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

# Scaling is useful because Hours and Attendance use different ranges.
model = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=3)
)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Actual:", list(y_test))
print("Predicted:", list(y_pred))

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy =", accuracy)

cm = confusion_matrix(y_test, y_pred, labels=['Fail', 'Pass'])
print("Confusion Matrix:")
print(cm)

new_student = pd.DataFrame([[3, 70]], columns=['Hours', 'Attendance'])
prediction = model.predict(new_student)
print("New Student Prediction:", prediction[0])
