# import data
import pandas as pd

url = 'https://raw.githubusercontent.com/tidyverse/ggplot2/master/data-raw/diamonds.csv'
df = pd.read_csv(url)

# slim and add missingno
import numpy as np

np.random.seed(42)
df = df[['carat', 'cut', 'color', 'clarity', 'price']]
df = df.mask(np.random.random(df.shape) < 0.05)
df = df.dropna(subset=['price'])
df.head()

df.to_csv('data/diamonds.csv', index=False)
