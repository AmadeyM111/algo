import pandas as pd
from functools import reduce
import operator

numbers = [5, 8, 3, 7, 12, 21]

print("agrr operations")
# associative aggregates
print(reduce(operator.add, numbers))
print(reduce(operator.mul, numbers))
print(reduce(min, numbers))
print(reduce(max, numbers))


df = pd.DataFrame({'group': ['A', 'A', 'B', 'B'], 'value': [10, 20, 15, 30]})

print(df.groupby('group').agg({
    'value': ['sum', 'count', 'min', 'max'] # all associative
}))
