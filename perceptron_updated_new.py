import time
def calc_wt(x,t):
    yin = 0
    act_op = 0
    weights = []
    for u in range(len(x[0])+1):
        weights.append(0)
    cnt = 0
    length1 = len(t)
    learning_rate = float(input("Specify learning rate: "))
    cnot = 1
    while(cnot == 1):
        for i in range(length1):
            #print(weights)
            yin = weights[len(x[0])]
            for j in range(len(x[0])):
                yin += weights[j]*x[i][j]

            #print(yin)
            if yin > 0:
                act_op = 1
            elif yin == 0:
                act_op = 0
            else:
                act_op = -1

            #print(act_op)
            if (act_op == t[i]):
                cnt +=1
                if cnt == length1:
                    break
            else:
                cnt = 0
                for a in range(len(x[0])+1):
                    if a != len(x[0]):
                        weights[a] += (learning_rate*t[i]*x[i][a])
                    else:
                        weights[a] += (learning_rate*t[i])
            #time.sleep(5)
        if cnt == len(x):
            cnot = 0

    return(weights)

x = [[1,1],[1,-1],[-1,1],[-1,-1]]
#x = list(input("enter the data set: "))
y = [-1,1,-1,-1]
#y = list(input("enter the target output: "))
print(calc_wt(x,y))
