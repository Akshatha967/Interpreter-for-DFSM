from tkinter import *

root = Tk()
root.geometry("900x900")
#root.minsize("500","500")
#root.maxsize("900","900")
root.title('Interpreter for DFSM')

Label(root, text="Interpreter For DFSM",font=("cosmeticians", 19, "bold"), bg='grey', fg='black').grid(row=0, column=0)

# var
nk = IntVar()
check = StringVar()
ns = IntVar(value=0)

# get input values of a language
Label(root, text="Enter The total number of inputs: ").grid(row=1, column=2)
Entry(root, textvariable=nk).grid(row=1, column=4)

sig = list()

Label(root, text="Enter Y if inputs belong to numbers else enter N").grid(row=2, column=2)
Entry(root, textvariable=check).grid(row=2, column=4)

Label(root, text="enter the input symbols").grid(row=3, column=2)


nst = nk.get()
row = 3
tran = {}
acpt = list()

starts = IntVar()
ter = IntVar()
strg = StringVar()

#def clear():

def dfsm():
    global row, ter, tran, starts, acpt, strg, check
    row = row + 1
    state = int(starts.get())
    delt = tran
    strng = str(strg.get())
    label = {}

    f1 = Frame(root, bg="grey", borderwidth=200)
    f1.grid(row=3, column=3)
    rowd = 3
    cold = 3
    for i in strng:

        temp = state
        if (check.get() == 'Y') or (check.get() == 'y'):

            state = delt[state][int(i)]

        else:
            state = delt[state][ord(i)]

        label[i] = Label(f1,text=f"( {temp} , {i} )={state}")
        label[i].grid(row=rowd, column=2)
        rowd = rowd + 1

    if state in acpt:

        labels = Label(f1,text="String is accepted")
        labels.grid(row=row - 1, column=8)
        rowd = rowd + 1


    else:
        labels = Label(f1,text="String is rejected")
        labels.grid(row=row - 1, column=8)
        rowd = rowd + 1

    def clear():
        f1.destroy()

    Button(f1, text="clear", command=clear).grid(row=row, column=8)

def textc():
    global row

    Label(text="enter the string: ").grid(row=row, column=2)
    Entry(root, textvariable=strg).grid(row=row, column=4)
    Button(text="OK", command=dfsm).grid(row=row, column=6)


def geta(var):
    global ter, tran, starts

    for i in range(ter.get()):
        b = (var[i].get())
        acpt.append(int(b))

    Button(text="OK", command=textc).grid(row=row - 1, column=6)


def getl():
    global row, starts, tran, ter
    a = starts
    Label(text="enter the accepting states").grid(row=row, column=2)
    var = {}
    for i in range(ter.get()):
        var[i] = IntVar(value=0)
    for i in range(ter.get()):
        Entry(root, textvariable=var[i]).grid(row=row, column=4)
        row = row + 1
    Button(text="OK", command=lambda: geta(var)).grid(row=row - 1, column=6)


def getstfin():
    global row, tran, ter, starts

    Label(text="enter the start state").grid(row=row, column=2)
    Entry(root, textvariable=starts).grid(row=row, column=4)
    row = row + 1

    Label(text="enter the number terminal states").grid(row=row, column=2)
    Entry(root, textvariable=ter).grid(row=row, column=4)
    row = row + 1
    Button(text="OK", command=getl).grid(row=row - 1, column=6)


def tranget(sts, inp, st):
    for i in sts:
        tran1 = dict()
        for j in inp:
            m = str(i)
            n = str(j)
            k = m + n
            tran1[j] = int(st[k].get())
        tran[i] = tran1
    Button(text="OK", command=getstfin).grid(row=row - 1, column=6)


def delta(var):  # to get transitions
    global check, row, sig
    k = list()
    sts = k
    inp = sig
    for i in range(ns.get()):
        a = var[i].get()
        sts.append(int(a))

    st = {}
    for i in sts:
        for j in inp:
            m = str(i)
            n = str(j)
            k = m + n
            st[k] = StringVar()

    for i in sts:
        for j in inp:
            m = str(i)
            n = str(j)
            k = m + n
            if (check.get() == 'Y') or (check.get() == 'y'):
                Label(text=f"enter transitions for state {i} with input {j} ").grid(row=row, column=2)
                Entry(root, textvariable=st[k]).grid(row=row, column=4)
                row = row + 1
            else:
                Label(text=f"enter transitions for state {i} with input  {chr(j)}").grid(row=row, column=2)
                Entry(root, textvariable=st[k]).grid(row=row, column=4)
                row = row + 1
    Button(text="OK", command=lambda: tranget(sts, inp, st)).grid(row=row - 1, column=6)


def gettrans():
    global row, ns, sig
    row = row + 1

    Label(text="enter the states values in digits(E.g:0 for q0):").grid(row=row, column=2)
    var = {}
    for i in range(ns.get()):
        var[i] = IntVar(value=0)
    for i in range(ns.get()):
        Entry(root, textvariable=var[i]).grid(row=row, column=4)
        row = row + 1
    Button(text="OK", command=lambda: delta(var)).grid(row=row - 1, column=6)


def gettran(var):  # gives sigma
    global row, sig
    if (check.get() == 'Y') or (check.get() == 'y'):
        for i in range(nk.get()):
            a = (var[i].get())
            sig.append(a)
    else:
        for i in range(nk.get()):
            a = (var[i].get())
            sig.append(ord(a))

    Label(text="Enter the total number of states including trap states").grid(row=row, column=2)
    Entry(root, textvariable=ns).grid(row=row, column=4)

    Button(text="OK", command=gettrans).grid(row=row, column=6)


def getinp():  # to get input
    global row
    var = {}
    if (check.get() == 'Y') or (check.get() == 'y'):
        for i in range(nk.get()):
            var[i] = IntVar()
        for i in range(nk.get()):
            Entry(root, textvariable=var[i]).grid(row=row, column=4)
            row = row + 1

    else:
        for i in range(nk.get()):
            var[i] = StringVar()  # initially set default values to a
        for i in range(nk.get()):
            Entry(root, textvariable=var[i]).grid(row=row, column=4)
            row = row + 1

    Button(text="submit", command=lambda: gettran(var)).grid(row=row - 1, column=6)


Button(text="submit", command=getinp).grid(row=2, column=6)

root.mainloop()
