import numpy as np

connections = np.array(['C','C','F','C'])
rotation = 5

# if rotation = 2
# ['C', 'C', 'C', 'F']

# if rotation = 3
# ['F', 'C', 'C', 'C']

new_connections = np.roll(connections, shift=rotation-1)
print(new_connections)
