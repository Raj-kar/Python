class GrumpyDict(dict):
    def __repr__(self):
        print("None of your business")
        return super().__repr__()