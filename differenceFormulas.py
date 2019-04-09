import math
import matplotlib.pyplot as plt
import pandas as pd

def f(x):
    return (math.sin(x) - math.cos(x))

def fttt(x):
    return ((-1 *  math.sin(x)) + math.cos(x))    

def table(s, ed):
    approx, erramt = [],[]
    for i in range(s,ed):
        ap = (f((0 + (10 ** -i))) - f((0 - (10 ** -i))))/(2 *(10 ** -i))
        err = (((10 ** -i) ** 2)/6) * fttt(0)
        res = ap - err
        approx.append(ap)
        erramt.append(err)
    return(approx, erramt)

data = pd.DataFrame({"Term": ["10^" + str(i) for i in range(1,13)],
                     "Formula": table(1,13)[0],
                     "Error":table(1,13)[1]})
print(data)
data.plot(secondary_y = ["Formula"])
plt.show()
        
        

