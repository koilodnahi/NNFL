import numpy as np

def predict(x1,x2,t,y,w1,w2,yin,threshold):
    for i in range(4):
        if yin[i] >= threshold:
            y[i] = 1
        else:
            y[i] = 0

    print(y)
    print(t)
    if np.array_equal(y,t):
        return("Network has proper weights and threshold")
    else:
        print("Network has been assigned wrong parameters, run the program again to achieve outputs")
        x = int(input("enter 1 to continue: "))
        if x == 1:
            inp(x1,x2,t,y)
        else:
            return 0


def inp(x1,x2,t,y):
    w1 = int(input("enter w1: "))
    w2 = int(input("enter w2: "))
    yin = np.multiply(w1,x1) + np.multiply(w2,x2)
    print(yin)
    threshold = int(input("enter the threshold value: "))
    print(predict(x1,x2,t,y,w1,w2,yin,threshold))

x1 = np.array([1,1,0,0])
x2 = np.array([1,0,1,0])
t = np.array([1,0,0,0])
t1 = np.array([1,1,1,0])
y = np.array([0,0,0,0])
print("for AND gate")
inp(x1,x2,t,y)
print("for OR gate")
inp(x1,x2,t1,y)
