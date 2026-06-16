# using ststicmethod to check if number is even

class number:
    @staticmethod
    def check (num):
        if num % 2==0:
            print("number is even")
        else:
            print("number is odd")
number.check(5)