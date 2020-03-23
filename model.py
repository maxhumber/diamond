import pickle
import pandas as pd
from sklearn.impute import SimpleImputer as SI
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import LabelBinarizer as LB
from sklearn.preprocessing import StandardScaler as SS
from sklearn_pandas import DataFrameMapper

df = pd.read_csv('data/diamonds.csv')

target = 'price'
y = df[target]
X = df.drop(target, axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y)

mapper = DataFrameMapper([
    (['cut'], [SI(strategy='most_frequent'), LB()]),
    (['color'], [SI(strategy='most_frequent'), LB()]),
    (['clarity'], [SI(strategy='most_frequent'), LB()]),
    (['carat'], [SI(strategy='mean'), SS()]),
], df_out=True)

model = LinearRegression()
pipe = make_pipeline(mapper, model)
pipe.fit(X_train, y_train)

with open('model/pipe.pkl', 'wb') as f:
    pickle.dump(pipe, f)
