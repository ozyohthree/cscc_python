

def stairs(n):
    for step in range(0,n+1):
        for x in range(0,step):
            print("#",end="")
        print("")

def recursivestep(n):
    if (n<1):
        return
    else:
        for step in range(0,n):
            print("#",end="")
            recursivestep(n-step)

#
def steps(n):
    for row in range(n):
        #print('row=',row)
        stair = ''
        for column in range(n):
            #print('column=',column)
            #print(column,'<=',row,'?',column <= row)
            if column <= row:
                stair += '#'
            else:
                stair += ' '
        print(stair)

steps(4)
