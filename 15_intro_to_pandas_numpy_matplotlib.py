import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

df.plot(x="A", y="B", kind="bar")
plt.show()