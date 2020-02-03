def make_pretty(func):
    print('i am pretty')
    def inner():
        print('I got decorated')
        func()
    return inner

@make_pretty                      #similar to ordinary=make_pretty(ordinary) and store the returned value to ordinary
def ordinary():
    print('I am ordinary!')   

ordinary()