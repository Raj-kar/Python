Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
>>> sys.getsizeof(int)
416
>>> sys.getsizeof(int)
416
>>> sys.getsizeof(str)
416
>>> sys.getsizeof(float)
416
>>> 
KeyboardInterrupt
>>> sys.getsizeof(map)
416
>>> sys.getsizeof(list)
416
>>> names = ["Raj","Rahul","Raima"]
>>> sys.getsizeof(names)
80
>>> names_1 = ("Raj","Rahul","Raima")
>>> sys.getsizeof(names_1)
64
>>> names_2 = {"Raj","Rahul","Raima"}
>>> sys.getsizeof(names_2)
216
>>> num = [1,2,3,4,5]
>>> sys.getsizeof(num)
96
>>> sys.getsizeof("RAJ")
52
>>> sys.getsizeof("Raj")
52
>>> sys.getsizeof("Rahul kar")
58
>>> sys.getsizeof("Rahul")
54
