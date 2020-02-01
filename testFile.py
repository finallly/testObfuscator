#  test file for obfuscation needs
import random

X = 42
STRING = 'this is for needs'
array = [1, 2, 3, 4]


class testInheritance:
    pass


class testClass(testInheritance):  # this is a
    """this is documentation"""
    classobj = 'this is a of class a'  # this is also a
    smth = classobj
    classdick = 111

    def __init__(self):
        self.inst = testClass.classobj  # and this is a
        x = 3
        y = testClass.classobj

    @staticmethod
    def func1():  # same as others
        zo = 72

        def dickydicky():
            zizi = zo
            dicky = testClass.classobj
            return dicky

        return dickydicky()


def testThis():
    test1 = 'test'
    test2 = 123
    test3 = test1


x = testClass
y = testClass()
print(y.inst)
print(x.func1())
print(x.classobj)
print(x.classdick)
print(x.func1)
print(random.randint(0, 100))

b = [1, 2, 3]
for i in range(len(b)):
    b.append(i + 4)

print(b)

testClass = 43
print(testClass)
