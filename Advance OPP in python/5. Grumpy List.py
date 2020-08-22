class GrumpyList(list):
    def __repr__(self):
        print("Go and Sleep !")
        return super().__repr__()

    def __getitem__(self, item):
        print(f"Why are you want to find index {item} ??")
        try:
            return f"value on index {item} = {super().__getitem__(item)}"
        except IndexError:
            return f"Are you don't know? index {item} not available"
        except TypeError:
            return f"Are you kidding ? What you are find? {item} :|"

    def __len__(self):
        print("It's none of your business !")

    def __del__(self):
        print(f"Now you want to delete it ? :| \n Okay! deleting {self}")


data = GrumpyList([1, 2, 3, 4, 5])
print(data)
data.reverse()
print(data)
print(data[2])
print(data[9])
print(data['apple'])
print(len(list(data)))
del data
