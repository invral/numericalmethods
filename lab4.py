import numpy as np

# 10^3 10^6 10^9
# [0,10]

eps = [0.001, 1e-6, 1e-9]
a = 0
b = 10

def f(x):
    return x**5-x**4-3*x-1

def dif_f(x):
    return 5*x**4-4*x**3-3

def dih_method(a,b,eps):
    # assert f(a) != 0, 'a равно 0'
    # assert f(b) != 0, 'b равно 0'
    l = []
    count = 0
    while (b-a)>eps:
        mid = (b+a)/2
        if f(mid) == 0:
            return mid, count
        if f(a)*f(mid)<0:
            b = mid
        if f(b)*f(mid)<0:
            a = mid
        count += 1
        if count>2000:
            break
        l.append(mid)
    return mid, count, l

def newton_method(a,b,eps):
    # assert f(a) != 0, 'a равно 0'
    # assert f(b) != 0, 'b равно 0'
    l = []
    count = 0
    mid = (b-a)/2

    while abs(f(mid))>eps:
        mid = mid - f(mid)/dif_f(mid)
        count +=1
        if count>2000:
            break
        l.append(mid)
    return mid, count, l

def hord_method(a,b,eps):
    # assert f(a) != 0, 'a равно 0'
    # assert f(b) != 0, 'b равно 0'

    count = 0
    a=0
    b=10
    x =[a,b]
    i = len(x)-1
    while (abs(f(x[i]))) > eps:
        chisl = f(x[i-1])*(x[i]-x[i-1])
        znam = f(x[i])-f(x[i-1])
        x0 = x[i-1] - chisl/znam
        # if x0 < a:
        #     x0+=2
        x.append(x0)
        i +=1
        if count>2000:
            break
    return x[-1], i-1, x

def convergenceRate(l):
    x1 = abs((l[-1]-l[-2])/(l[-2]-l[-3]))
    x2 = abs((l[-2]-l[-3])/(l[-3]-l[-4]))
    speed = np.log(x1)/np.log(x2)

    return speed


func_list = [dih_method,newton_method,hord_method]

for e in eps:
    for func in func_list:
        x, count, l = func(a=a,b=b,eps=e)
        print(f"root is {x}, amount of iterations = {count}"+" "+func.__name__+"\n")
        print(f"convergence rate is {convergenceRate(l)}"+"\n")






# сделать скорость сходимости по формуле, что
