# PRACTICAL NO. 04
# AIM: To implement a Feed Forward Backpropagation Neural Network and evaluate it.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Scaling helps the neural network learn more reliably.
nn = make_pipeline(
    StandardScaler(),
    MLPClassifier(
        hidden_layer_sizes=(10,),
        max_iter=1000,
        learning_rate_init=0.01,
        random_state=42
    )
)

nn.fit(X_train, y_train)
y_pred = nn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
