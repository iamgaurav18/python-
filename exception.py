a=int(input('Enter a number:'))
b=int(input('Enter a number:'))
try:
    print(a/b)
except ZeroDivisionError as r:
    print(r)
finally:
    print('khatam......!!')