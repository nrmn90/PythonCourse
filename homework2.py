import pandas as pd
import os
import numpy as np
import scipy
from scipy.stats import f
import matplotlib.pylab as plt
import wbdata
import datetime

os.chdir('C:/Users/Utente/Documents/KocPython2020-master/homework/homework2')

#scrapping world bank data
countries = [i['id'] for i in wbdata.get_country(incomelevel="UMC", display=False)]
indicators = {"IC.BUS.DFRN.XQ": "doing_business", "PAY.TAX.PRFT.CP.ZS": "Profit tax",
              "IC.CNST.PRMT.COST.WRH.VAL": "construction permits",
              "IC.REG.PRRT.COST.PRT.VAL": "Registering property", "IC.ELC.PRI.KH.DB1619": "Electricity price"}
data_date = (datetime.datetime(2019, 1, 1), datetime.datetime(2019, 12, 31))
df = wbdata.get_dataframe(indicators, country=countries, convert_date=True, data_date=data_date)
df.to_csv('wb_api.csv')
###########
data = pd.read_csv('wb_api.csv')
data = data[['doing_business', 'Profit tax', 'construction permits', 'Registering property',
             'Electricity price']]  # choosing columns
for i in data.columns:  # replacing nan with mean
    data[i] = data[i].fillna(data[i].median())
data = data.drop(index=58)
data = data.drop(index=59)# eliminating instance with large deviation
data = data.replace(0, data.median())  # replacing 0 values with mean
dt = np.array(data.values, 'float')  # transforming pandas frame to numpy array
Y = dt[:, 0]
X1 = dt[:,1]
X2 = dt[:,2]
X3 = dt[:,3]
X4 = dt[:,4]

# plotting variables
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(X1, Y, 'bo')
axs[0, 1].plot(X2, Y, 'bo', color='orange')
axs[1, 0].plot(X3, Y, 'bo', color='green')
axs[1, 1].plot(X4, Y, 'bo', color='red')
for ax in axs.flat:
    ax.set_ylabel('Doing business')
#############################
# calculating means
y_m = np.mean(Y)
x1_m = np.mean(X1)
x2_m = np.mean(X2)
x3_m = np.mean(X3)
x4_m = np.mean(X4)


y = Y - y_m
x1 = X1 - x1_m
x2 = X2 - x2_m
x3 = X3 - x3_m
x4 = X4 - x4_m

# calculation of estimates
b1 = np.sum(x1 * y) / np.sum(x1 ** 2)
b2 = np.sum(x2 * y) / np.sum(x2 ** 2)
b3 = np.sum(x3 * y) / np.sum(x3 ** 2)
b4 = np.sum(x4 * y) / np.sum(x4 ** 2)
b0 = y_m - (b1 * x1_m + b2 * x2_m + b3 * x3_m + b4 * x4_m)

#predicted model
Y_opt = b0 + X1 * b1 + X2 * b2 + X3 * b3 + X4 * b4

ESS = np.sum((Y_opt - y_m) ** 2)  # estimated sum of squares
RSS = np.sum((Y - Y_opt) ** 2)  # residual sum of squares
TSS = np.sum((Y - y_m) ** 2)  # total sum of squares
print('ESS=',ESS,',''RSS=',RSS,',','TSS=',TSS)

R_sqr = ESS / TSS  # R square - explanation of change by the model is nearly 70%
print('R square is',R_sqr)
R_sqr_adj = 1 - (1 - R_sqr) * ((len(data) - 1) / (len(data) - len(data.columns[1:]) - 1))  # adjusted R square

# testing model significance as a whole
F_test = (ESS / len(data.columns[1:])) / (RSS / (len(data) - len(data.columns[1:]) - 1))
F = scipy.stats.f.ppf(0.95, len(data.columns[1:]), len(data) - len(data.columns[1:]) - 1)
print(' The model fitness test is ', F_test, ' and it is greater than F value', F,'\n The model is significant as a whole')

variance = RSS / (len(data) - len(data.columns[1:]) - 1)
stnd_error = np.sqrt(variance)  # standard error of the model
stnd_error
# standard error of intercepts
str_error_b1 = stnd_error / np.sqrt(np.sum(x1 ** 2))
str_error_b2 = stnd_error / np.sqrt(np.sum(x2 ** 2))
str_error_b3 = stnd_error / np.sqrt(np.sum(x3 ** 2))
str_error_b4 = stnd_error / np.sqrt(np.sum(x4 ** 2))
print(str_error_b1,str_error_b2,str_error_b3,str_error_b4)

# testing model significance by individual variables X1 and X2
t1 = b1 / str_error_b1  # t value for b1
t2 = b2 / str_error_b2  # t value for b2
t3 = b1 / str_error_b3  # t value for b1
t4 = b2 / str_error_b4  # t value for b2
t = scipy.stats.t.ppf(0.975, len(data) - len(data.columns[1:]) - 1)  # t student value
print(' t value for X1',t1,'\n','t value for X2', t2,'\n','t value for X3', t3,'\n','t value for X4', t4,
      '\n', 't test -', t)
print('Only X1 is significant which is Profit tax')
