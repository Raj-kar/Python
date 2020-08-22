# Write a Python class to reverse a string word by word.
# Input string : 'hello .py'
# Expected Output : '.py hello'

class ReverseSentence:
    def __init__(self, string):
        self.sting = string

    @property
    def get_str(self):
        return self.sting

    def reverse_str(self):
        split_str = self.sting.split(" ")
        return ' '.join(reversed(split_str))


s1 = ReverseSentence("Hello .py")
print(s1.reverse_str())
s2 = ReverseSentence("Sky is Blue")
print(s2.reverse_str())
s3 = ReverseSentence("Python is awesome")
print(s3.reverse_str())
