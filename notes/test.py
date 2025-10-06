# def foo():
#     lst = [1, 2, 3]
#     for v in lst:
#         yield v
# 
# 
# g = foo()
# print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# 
# print(foo())
# print(foo())
# print(foo())
# print(foo())
# 
# print(__builtins__.open)
# 
# class Foo(object):
#     def __init__(self):
#         self._list = [1, 2, 3, 4, 5]
# 
#     def __iter__(self):
#         counter = [0]
# 
#         def get():
#             if counter[0] >= len(self._list):
#                 return None
#             res = self._list[counter[0]]
#             counter[0] += 1
#             return res
# 
#         return iter(get, None)
# 
# a = Foo()
# for e1 in a:
#     for e2 in a:
#         print (e1, e2)


# def foo(a, items=[], added=True):
#     if added:
#         items.append(a)
#     print items
# 
# foo(1)
# foo(2)
# foo(3, added=False)

# a = 10
# b = 10
# 
# print a == b
# print a is b

def test_metaclass(name, bases, dic):
    print 'The class name is', name
    print 'The class bases is', bases
    print 'The dict has', len(dic), 'elems, the keys are', dic.keys()
    return 'yellow'


class TestName(object, None, int, 1):
    __metaclass__ = test_metaclass
    foo = 1
    def baz(self, arr):
        pass

print 'TestName = ', repr(TestName)
# a = TestName()
# print repr(a)
print NotImplemented, type(NotImplemented)
print None, type(None)
print Ellipsis, type(Ellipsis)


class A(object):
    def __new__(cls, aa, bb):
        print 'A.__new__(%s, %s, %s)' % (cls.__class__.__name__, aa, bb)
        return super(A, cls).__new__(cls, aa, bb)
    
    def __init__(self, aa, bb):
        print 'A.__init__(%s, %s, %s)' % (self, aa, bb)

    def foo(self):
        print 'A.foo'

a = A(11, 22)
a.foo()

CLASS_DICT = {}

class Base(object):
    def __new__(cls):
        global CLASS_DICT
        CLASS_DICT[cls.__name__] = cls
        return super(Base, cls).__new__(cls)

class AA(Base):
    def __init__(self):
        pass

class BB(Base):
    def __init__(self):
        pass

aa = AA()
bb = BB()
print CLASS_DICT

print None, type(None)
print NotImplemented, type(NotImplemented)
print Ellipsis, type(Ellipsis)