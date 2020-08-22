class GrumpyDict(dict):
    def __repr__(self):
        print("None of your business")
        return super().__repr__()

    def __missing__(self, key):
        print(f"{key} is no present !")

    def __setitem__(self, key, value):
        print("How many time want to change ?")
        print(f"UGH! setting {key} to {value}")
        super().__setitem__(key, value)


data = GrumpyDict({"first": "Raj", "last": "kar", "age": 30})
print(data)
var = data['city']
data['age'] = 65
print(data)
