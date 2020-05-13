import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()

df = pd.DataFrame(iris.data, columns = iris.feature_names)
plt.scatter(df['petal length (cm)'], df['petal width (cm)'], c=iris.target)

plt.show()