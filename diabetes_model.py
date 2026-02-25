import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("diabetes_prediction.csv")

data.head()
data.info()


data.isnull().sum()


x=data.drop("diabetes",axis=1)
y=data[["diabetes"]]

sns.countplot(x='diabetes', data=data)
plt.title("Distribution of Diabetes")

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler

# Apply one-hot encoding to categorical columns
x_train_encoded = pd.get_dummies(x_train, columns=['gender', 'smoking_history'], drop_first=True)
x_test_encoded = pd.get_dummies(x_test, columns=['gender', 'smoking_history'], drop_first=True)

# scale numerical features
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train_encoded)
x_test_scaled = scaler.transform(x_test_encoded)

model = DecisionTreeClassifier()
model.fit(x_train_scaled, y_train)

y_pred = model.predict(x_test_scaled)


from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y_test,y_pred)
print("Accuracy:", accuracy)

import joblib
model_columns = x_train_encoded.columns
joblib.dump((model, model_columns), "model.pkl")