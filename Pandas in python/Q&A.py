# <----- Question 1 --->

The Pandas Series can be defined as a one-dimensional array that is capable of storing various data types.
We can easily convert the list, tuple, and dictionary into series using "series' method. The row labels of
series are called the index. A Series cannot contain multiple columns.
>> Example --->
import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)

>> output -->
0   a
1   b
2   c
3   d
dtype: object

# <----- Question 2 --->
 rename() method in pandas can be used to change the index of rows and columns of a seires or Dataframe.add()
 
# <----- Question 3 --->
 correct --> df.tail(4)

# <----- Question 4 --->
 command for insert a new column in the last position(3rd pos) -->
 DataFrameName.insert(loc, column, value, allow_duplicates=False)
    so, here --> sal.insert(3, Salary)

# <----- Question 5 --->
 Drop rows with label 0df = df.drop0printdf

# <----- Question 6 --->

# importiong the modules 
import pandas as pd 
import numpy as np 
  
# creating the Numpy array 
array = np.array([['S101','Amy','70'], ['S102','Bandhi','69'],['S104','Cathy','75'],['S105','Gundaho','82']]) 
  
# creating a list of index names 
index_values = [0, 1, 2, 3] 
   
# creating a list of column names 
column_values = ['number', 'Name', 'age'] 
  
# creating the dataframe 
df = pd.DataFrame(data = array,  
                  index = index_values,  
                  columns = column_values) 
  
# displaying the dataframe 
print(df) 

output --->
   number     Name age
0   S101      Amy  70
1   S102   Bandhi  69
2   S104    Cathy  75
3   S105  Gundaho  82


# <----- Question 7 --->

# importiong the modules 
import pandas as pd 
import numpy as np 
  
# creating the Numpy array 
array = np.array([[1,2],[3,4],[5,6],[7,8]]) 
  
# creating a list of index names 
index_values = [0, 1, 2, 3] 
   
# creating a list of column names 
column_values = ['a', 'b'] 
  
# creating the dataframe 
df = pd.DataFrame(data = array,  
                  index = index_values,  
                  columns = column_values) 
  
# displaying the dataframe 
print(df) 
   a  b
0  1  2
1  3  4
2  5  6
3  7  8

# <----- Question 8 --->

print(df1)
   	a	b
first	10	20
second	6	32

print(df2)
      a	b1
first	10	NaN      
second	6	NaN
   # b1 shows Nan, becuase there's no column name b1 ..!


# <----- Question 9 --->

def randomIndex(data):  # create random set of arr
    from random import randint
    arr = []
    for i in range(len(data)):
        arr.append(randint(1,len(data)-1))
    return arr

# import pandas as pd 
import pandas as pd 
  
# import numpy as np 
import numpy as np 
  
# simple array 
data = np.array(['p', 'a', 'n', 'd', 'a', 's']) 

randArr = randomIndex(data)
ser = pd.Series(data) 
ser = ser.reindex(index = randArr)

print(ser) 

output -->
   # ouput will change each time the program will run because we create a func randomIndex!
1    a
4    a
4    a
2    n
2    n
1    a
dtype: object

# <----- Question 10 --->

import pandas as pd
import numpy as np
weather  = {'day': ['1/1/2017', '2/1/2017', '3/1/2017', '4/1/2017', '5/1/2017', '6/1/2017'],
        'temp': [32, 23, 22, 34, 19, 28],
        'windspeed': [7, 3, 5, 1, 2, 9],
        'event': ['Sunny', 'Rain', 'snow', 'Sunny', 'Cloudy', 'Rain']}

labels = [1, 2, 3, 4, 5, 6]

df = pd.DataFrame(weather , index=labels)

total_rows=len(df.axes[0])
total_cols=len(df.axes[1])
print("Number of Rows: "+str(total_rows))
print("Number of Columns: "+str(total_cols))

output -->
Number of Rows: 6
Number of Columns: 4

# <----- Question 11 --->

# output -->
x1
    var1
10     9
1     11
2     13
x2
   var1
9     1
8     3
x3
   var1
2    13
3    15
4    17
5    19

# <----- Question 12 --->

# importiong the modules 
import pandas as pd 
import numpy as np 
  
# creating the Numpy array 
array = np.array([['Raj','19','51'],['Colt','23','63'],['Andrie','27','75']]) 
  
# creating a list of index names 
index_values = [0, 1, 2] 
   
# creating a list of column names 
column_values = ['name', 'age', 'weight'] 
  
# creating the dataframe 
df = pd.DataFrame(data = array,  
                  index = index_values,  
                  columns = column_values) 
result = df.transpose()

# displaying the dataframe 
print(df) 
# displaying the transpose 
print(result)

output --->
     name age weight
0     Raj  19     51
1    Colt  23     63
2  Andrie  27     75

          0     1       2
name    Raj  Colt  Andrie
age      19    23      27
weight   51    63      75

# <----- Question 13 --->

# list only column 'Item' and 'Revenue'
SALES[['Item', 'Revenue']]

# list rows from 3 to 7
SALES[3:8]

# list the value of cell in 5th row, 'Item' column
SALES[5:6]['Item']


# <----- Question 14 --->

import pandas as pd 
import numpy as np 
data = np.array(['a1', 'b1', 'c1', 'd1', 'e1', 'f1'])
s = pd.Series(data)
print("I.")
print(s[:3])
print("II.")
print(s[:-3])

# output --->

I.
0    a1
1    b1
2    c1
dtype: object
II.
0    a1
1    b1
2    c1
dtype: object