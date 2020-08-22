class A:
    def feature1(self):
        print("feature 1 of A")

    def feature2(self):
        print("feature 2 of A")


class B(A):
    def feature3(self):
        print("feature 3 of B")

    def feature4(self):
        print("feature 4 of B")


class C(B):
    def feature5(self):
        print("feature 5 of C")

    def feature6(self):
        print("feature 6 of C")


f1 = A()
f1.feature1()
f1.feature2()

f2 = B()
f2.feature1()
f2.feature2()
f2.feature3()
f2.feature4()

f3 = C()
f3.feature1()
f3.feature2()
f3.feature3()
f3.feature4()
f3.feature5()
f3.feature6()

# A is superClass. B inherits from A. So B can access all the features of A.
# Now, C inherits from B, so C can access all the features of B and A.
# So, it's called inheritance.
