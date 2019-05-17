#!/usr/bin/env python3
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv('../scripts/mtcars.csv', header=0)
y = df.loc[:, df.columns == 'mpg']
x = df.loc[:, ['cyl', 'disp', 'hp', 'drat']]

lr = LinearRegression()
lr.fit(x, y)


def predict(dict_values, columns=x.columns, model=lr):
    x = np.array([float(dict_values[col]) for col in columns])
    x = x.reshape(1,-1)
    y_pred = float(model.predict(x)[0])
    return y_pred

