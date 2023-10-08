# 6 subjects were given a drug(treatment group) and an additional 6 subjects a placebo(control group).
# Their reaction time to stimulus was measured (in ms)
# We want ot perform 2-sample t-test for comparing the means of the treatment and control groups
# Control group: 91,87,99,77,88,91----#placebo effect
# Treatment group: 101,110,103,93,99,104.-------#drug effect
# Placebo effect: People thinks that when they take the medicine, the headache reduces.
import pandas as pd
import numpy as np
import stats
from scipy import stats
n=6# sample size
a=0.05
#creating the data frames
df_c= pd.Series([91,87,99,77,88,91])
df_t=pd.Series([101,110,103,93,99,104])
print(df_c)
print(df_t)
# Defining the hypothesis.
# Null hypothesis: Ho-> mean_df_c = mean_df_t, then no effect.
# Alternate Hypothesis: Ha-> mean_df_c != mean_df_t, then there is statistically significant difference.
# Thus the  medicine has real effect on the patient.

pvalue=stats.ttest_ind(df_c,df_t)[1]

print(pvalue)
if pvalue >= a:
    print("Here pvalue is greater than 0.05, so Accept Ho \n Inference: Accepting Ho-> (mean_df_c = mean_df_t), then no effect.")
else:
    print("Here, pvalue is lesser than 0.05, so Reject Ho \n Inference: Rejecting Ho-> (mean_df_c = mean_df_t), choose the alternate hypothesis Ha-> (mean_df_c != mean_df_t),\n then there is statistically significant difference. Thus the  medicine has real effect on the patient.")