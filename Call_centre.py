### call center processing


import numpy as np
from scipy import stats

n = 50
t = (4.6- 4) / (3 / np.sqrt(n))
p = 2 * stats.t.cdf(-t, df=n - 1)
print(t)
print(p)
a = 0.05
# Ho= mean = 4
# Ha= mean != 4
if p < a:
    print("Reject Ho, because the p is less than alpha a. So, we accept the alternate hypothesis, mean!=4 which means \
    the process is out of control. There needs a managerial intervention")
else:
    print("Accept Ho, because p is greater than alpha. So, we accepting the null hypothesis and mean=4, which means \
    the process is under the control. So there is no managerial intervention required.")
# p value : In this case, p>a. 0.16>0.05 : so our decision is to accept the Ho.
# The p value implies that If I reject this decision, I might go wrong by 16% probability----
# P value less means, risk less
