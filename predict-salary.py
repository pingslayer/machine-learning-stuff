from scipy import stats

# x= years
x = [1,2,3,4,5]

# y = salary
y = [100000,200000,300000,500000,500000]


slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

#predict salasry for 5th year
salary = myfunc(6)

print(salary)