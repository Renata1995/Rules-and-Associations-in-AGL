import pandas
from scipy import stats
from statsmodels.formula.api import ols


letter = pandas.read_csv("csv files/letter.csv", sep=';', na_values=".")

# re_low = re.where("cs"==1)
# print (re_low)

model = ols("'Z(HR)-Z(FA)' ~ grammar", letter).fit()
print model.summary()




