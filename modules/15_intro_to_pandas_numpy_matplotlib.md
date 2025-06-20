# Module 15: Introduction to pandas, numpy, matplotlib

## Overview
These libraries are essential for data analysis and visualization in Python.

---

## pandas: Data Analysis
```python
import pandas as pd
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(df)
```

---

## numpy: Numerical Computing
```python
import numpy as np
arr = np.array([1, 2, 3])
print(arr * 2)
```

---

## matplotlib: Plotting
```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
```

---

## Mini Exercises
1. Create a pandas DataFrame with two columns and three rows.
2. Use numpy to create an array of numbers from 0 to 9.
3. Plot a simple line graph with matplotlib.

### Answers
```python
# 1
import pandas as pd
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

# 2
import numpy as np
arr = np.arange(10)

# 3
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [1, 4, 9])
plt.show()
```

---

## Real-World Use Case
Suppose you want to analyze and plot sales data:
```python
import pandas as pd
import matplotlib.pyplot as plt
data = {"month": ["Jan", "Feb", "Mar"], "sales": [100, 120, 90]}
df = pd.DataFrame(data)
df.plot(x="month", y="sales", kind="bar")
plt.show()
``` 