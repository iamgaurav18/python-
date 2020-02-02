import time
def client():
    print('we are at client side')
    time.sleep(1)
    middleware()
def middleware():
    print('we are at middleware level')
    time.sleep(1)
    server()
def server():
    print('we are at server side')
    time.sleep(1)
    print('done!')        

client()        