def make_averager():
    series=[]
    def average(new_value):
        series.append(new_value)
        total=sum(series)
        return total/len(series)

    return average
avg=make_averager()
print(avg(10))
print(avg(11))
print(avg(13))
print(avg.__code__.co_varnames)
print(avg.__closure__[0].cell_contents)

b=6
def f2(a):
    print(a)
    print(b)
print(f2(3))
def adder(x,y):
    def wrapper(y):
        return x + y
    return wrapper
adder5 = adder(5,6)
print(adder5)
# print(adder5(10))
# print(adder5(6))