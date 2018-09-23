from abc import ABC, abstractmethod

class A(ABC):

    @abstractmethod
    def m1(self):
        print('In class A, Method m1.')

class B(A):

    @staticmethod
    def m1(self):
        print('In class B, Method m1.')

b = B()
B.m1(b)
