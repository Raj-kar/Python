{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5-final"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "Python 3.8.5 64-bit",
   "display_name": "Python 3.8.5 64-bit",
   "metadata": {
    "interpreter": {
     "hash": "13386ea5553e948bd6c6e1cde2b2fc1d0a3aa26366b36725fe8e3aa4b8cbbfc4"
    }
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": "     name age weight\n0     Raj  19     51\n1    Colt  23     63\n2  Andrie  27     75\n          0     1       2\nname    Raj  Colt  Andrie\nage      19    23      27\nweight   51    63      75\n"
    }
   ],
   "source": [
    "# importiong the modules \n",
    "import pandas as pd \n",
    "import numpy as np \n",
    "  \n",
    "# creating the Numpy array \n",
    "array = np.array([['Raj','19','51'],['Colt','23','63'],['Andrie','27','75']]) \n",
    "  \n",
    "# creating a list of index names \n",
    "index_values = [0, 1, 2] \n",
    "   \n",
    "# creating a list of column names \n",
    "column_values = ['name', 'age', 'weight'] \n",
    "  \n",
    "# creating the dataframe \n",
    "df = pd.DataFrame(data = array,  \n",
    "                  index = index_values,  \n",
    "                  columns = column_values) \n",
    "result = df.transpose()\n",
    "\n",
    "# displaying the dataframe \n",
    "print(df) \n",
    "# displaying the transpose \n",
    "print(result)"
   ]
  }
 ]
}