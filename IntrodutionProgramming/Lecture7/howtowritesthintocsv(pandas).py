import pandas as pd # take pandas library into your code, firstly you need to install pandas library into your system through the shell, the command is "pip install pandas" for Windows OS, and the command is "pip3 install pandas" for MAC OS.
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

df = pd.DataFrame(x, columns = ['col1', 'col2', 'col3']) # create name for each line in the x, like col1: [1, 2, 3]
df.to_csv("digits.csv")
