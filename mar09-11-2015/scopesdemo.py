__author__ = 'ravi'

n = 'python'  #global scope

def demo():
    global n         #to refer a variable in the global namespace
    n = 100
    print n

demo()
print n
