import pandas as pd
import matplotlib.pyplot as plt
data = {"month": ["Jan", "Feb", "Mar"], "sales": [100, 120, 90]}
df = pd.DataFrame(data)
df.plot(x="month", y="sales", kind="bar")
plt.show()