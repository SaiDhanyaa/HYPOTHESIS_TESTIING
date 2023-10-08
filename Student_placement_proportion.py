## USE CASE: Is there a significant difference between the population proportions of state-1 and state-2
# who report that students have been placed immediately after education.
# Populations: All students who have completed the graduation and posst-graduation in both the states.
# PARAMETERS OF INTEREST: P1=state-1,   P-2=state-2.
# DATA: 247 students FROM STATE-1---P1, probability of 36.8%----student reports that they have got the job
#  308 students FROM STATE-1---P2, probability of 38.9%----student reports that they have got the job.
#

import pandas as pd
import numpy as np
import stats
from scipy import stats
import statsmodels.api as sm
from main import p

n1=247
n2=308
P1= 0.37
P2= 0.39
a=0.05
# we have the binomial distribution for state-1
print('the binomial distribution for state-1 :')
population1= np.random.binomial(1,P1,n1)
popu1_mean= population1.mean()
print(population1)
print('population mean of state-1:', popu1_mean)


# we have the binomial distribution for state-2
print('the binomial distribution for state-2:')
population2= np.random.binomial(1,P2,n2)
popu2_mean= population2.mean()
print(population2)
print('population mean of state-2:', popu2_mean)

# We have to conduct the proportion-t-test-2 sample
P= sm.stats.ttest_ind(population1,population2)   # ind--represents teh independent test
pvalue= P[1]
print('T-Test results:' ,P)
print('pvalue:',pvalue)


#  Hypothesis testing:
#  Defining the hypothesis:
#  NULL HYPOTHESIS: Ho-->>> if P1=P2-- State-1 and 2 are having no statistical difference in the students passing out.
#  ALTERNATE HYPOTHESIS: Ha-->>>> if P1 != P2.State-1 and 2 are having statistical difference in the students passing out and we can find thhe best college.


if pvalue >= a:
    print("Here pvalue is greater than 0.05, so Accept Ho \n Inference: Accepting Ho-> (P1=P2), State-1 and 2 are having no statistical difference in the students passing out.\n So both states are performing good")
else:
    print("Here, pvalue is lesser than 0.05, so Reject Ho \n Inference: Rejecting Ho-> (P1=P2), choose the alternate hypothesis Ha-> (P1 != P2), \n then State-1 and 2 are having statistical difference in the students passing out and we can find the best college.")