# define a class computer as example


class Computer:									# self automaticlly passed ny python. There is a secret
    def config(self):							# reson for this, We'll understand it letter ..!
        print("i5 - 8 GB Ram - 1 TB HDD")


comp1 = Computer()			# now ~comp1 is a object of computer !

# acess the values
# there are two ways for it ! :)

Computer.config(comp1)  # i5 - 8 GB Ram - 1 TB HDD

comp1.config()			# i5 - 8 GB Ram - 1 TB HDD
# naturally we use this.
