def star(func):
    def inner(*args,**kwargs):
        print('*'*30)
        func(*args,**kwargs)
        print('*'*30)
    return inner                        
def percent(func):
    def inner(*args,**kwargs):
        print('%'*30)
        func(*args,**kwargs)
        print('%'*30)
    return inner

@star                           #this block similar to printer=star(percent(printer))
@percent
def printer(msg):
    print(msg)

printer('Hello')                    