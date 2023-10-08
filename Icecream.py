##An outbreak of Salmonella related illness was attributed to icecream produced by the certain factory.
# Scientists meeasured the level of salmonella in 9 randomly sampled batches of icecream.
# The levels in (MPG/g) of salmonella : 0.593, 0.142,0.329, 0.691,0.231,0.793, 0.519, 0.392, 0.418
# Is there any evidence that mean level of salmonella in the icecream is greater than 0.3MPN/g?.


import pandas as pd
import numpy as np
import stats
from scipy import stats

from Call_centre import p

u=0.3
n=9  # sample size
a=0.05

# creating the data frame
Dataframe=pd.Series([0.593, 0.142,0.329, 0.691,0.231,0.793, 0.519, 0.392, 0.418])
print(Dataframe)
# Defining the hypothesis.
# Null hypothesis: Ho-> u<= 0.3, then no action required.
# Alternate Hypothesis: Ha-> u>0.3, then we need take action to control the bacteria.
P=stats.ttest_1samp(Dataframe,u)[1]
p_value=P/2
print(P, p_value)
if p_value >= a:
    print("Here pvalue is greater than 0.05, so Accept Ho \
    Inference: Accepting Ho-> u<= 0.3, then no action required to control the bacteria")
else:
    print("Here, pvalue is lesser than 0.05, so Reject Ho \
    Inference: Rejecting Ho->(u<= 0.3), choose the alternate hypothesis Ha-> u>0.3, then we need take action to control the bacteria")

