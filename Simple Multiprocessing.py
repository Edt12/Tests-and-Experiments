import multiprocessing


def Steve():
    print("Steve")

def John():
    print("John")

def Phil():
    print("Phil")

if __name__=="__main__":
    m1=multiprocessing.Process(target=Steve)#defines a thread/core
    m1.start()
    m2=multiprocessing.Process(target=John)
    m2.start()
    m3=multiprocessing.Process(target=Phil)
    m3.start()
