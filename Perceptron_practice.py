def calc_wt(x,y):
    yin = 0
    act_op = 0
    w1 = 0
    w2 = 0
    b = 0
    cnt = 0
    length1 = len(y)
    learning_rate = 1
    cnot = 1
    while(cnot == 1):
        for i in range(length1):
            yin = b + (w1*(x[i][0])) + (w2*(x[i][1]))
            if yin > 0:
                act_op = 1
            elif yin == 0:
                act_op = 0
            else:
                act_op = -1
            if (act_op == y[i]):
                cnt +=1
                if cnt == length1:
                    break
            else:
                cnt = 0
                b += (y[i])
                w1 += (y[i]*x[i][0])
                w2 += (y[i]*x[i][1])
                
        if cnt == len(x):
            cnot = 0

    return(w1,w2,b)

x = [[1,1],[1,0],[0,1],[0,0]]
y = [1,1,1,-1]
print(calc_wt(x,y))

