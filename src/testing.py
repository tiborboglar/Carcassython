import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


img = Image.open('./resources/images/filler.png')
new_image = img.resize((130, 130), Image.ANTIALIAS)
new_image.save('./resources/images/filler2.png')
print(img)
plt.imshow(img)
plt.show()
#
# cur_board = np.ones(shape=(3,3))
# print(cur_board)
#
# # appending above
# new_row = np.full(shape=(1, cur_board.shape[1]), fill_value=None)
# print(new_row)
#
# # new table
# new_board = np.append(new_row, cur_board, axis=0)
# print('\nNew Board!\n')
# print(new_board)
#
# new_col = np.full(shape=(new_board.shape[0], 1), fill_value=None)
# print(new_col)
# print(new_col.shape)
# new_board = np.append(new_col, new_board, axis=1)
# print('\nNew Board 2!\n')
# print(new_board)