def delta(inp, sts, check):
    tran = dict()
    for i in sts:
        tran1 = dict()
        for j in inp:
            if (check == 'Y')or (check == 'y'):
                print('enter transitions for ', i, '[', j, ']')
            else:
                print('enter transitions for ', i, '[', chr(j), ']')
            tran1[j] = int(input())
        tran[i] = tran1
    return tran

# get input values of a language
nk = int  (input("enter the total number of inputs: "))
sig = list()
check = input("Enter Y if inputs belong to numbers else enter N: ")
print("enter the input symbols")
if (check == 'Y')or (check == 'y'):
    for i in range(nk):
        sig.append(int(input()))
else:
    for i in range(nk):
        sig.append(int(ord(input())))


# get all the states
ns = int (input("enter the total number of states including trap states: "))
k=list()
print("enter states values in digits:")
for i in range(ns):
  a=input()
  if a.isdecimal():
     k.append(int(a))
  else:
    exit()


# get delta
delt = delta(sig, k, check)

# get start states , accepting states
s = int (input("enter the start state:"))
ter = int(input("enter the number terminal states:\n"))
a =list()
print("enter the accepting states: \n")
for i in range(ter):
    a.append(int(input()))



def dfsm(delt, s, a, str ,check):
    state=s
    for i in str:
        temp = state
        if (check == 'Y') or (check == 'y'):
            state = delt[state][int(i)]
        else:
            state = delt[state][ord(i)]
        print('(',temp,',',i,')=',state)
    if state in a:
        print('String is accepted ')
    else:
        print('String is rejected ')

# get the string
n=int (input('enter the number of testcases:'))
for i in range(n):
   strg=input("enter the string: ")
   dfsm(delt, s, a, strg , check)

