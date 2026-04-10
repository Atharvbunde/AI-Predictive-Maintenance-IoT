from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 🔹 Model 1: Random Forest
    rf_model = RandomForestClassifier()
    rf_model.fit(X_train, y_train)
    rf_pred = rf_model.predict(X_test)

    rf_acc = accuracy_score(y_test, rf_pred)
    print("Random Forest Accuracy:", rf_acc)

    # 🔹 Model 2: Logistic Regression
    lr_model = LogisticRegression()
    lr_model.fit(X_train, y_train)
    lr_pred = lr_model.predict(X_test)

    lr_acc = accuracy_score(y_test, lr_pred)
    print("Logistic Regression Accuracy:", lr_acc)

    # Save best model
    if rf_acc > lr_acc:
        joblib.dump(rf_model, "models/model.pkl")
        print("Saved: Random Forest Model")
        return y_test, rf_pred
    else:
        joblib.dump(lr_model, "models/model.pkl")
        print("Saved: Logistic Regression Model")
        return y_test, lr_pred