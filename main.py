import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
emissions = pd.read_csv("co2_emissions.csv")
#--------------1---------------
'''emissions.tail(5)
print(emissions)'''

#--------------2---------------
'''world = emissions.groupby("year").sum.T
world

uzb = world ["Uzbekistan"]
uzb
 
afg = world ["Afghanistan"]
afg

plt.plot(uzb, color="Red", label="++++")
plt.plot(afg, color="Blue", label="----")
plt.legend()
plt.title("CO2 emissions")
plt.show()'''

#--------------3---------------
'''afghanistan = emissions.groupby(["country"]).get_group("Afghanistan")
uzbekistan = emissions.groupby(["country"]).get_group("Uzbekistan")
kazakhstan = emissions.groupby(["country"]).get_group("Kazakhstan")

a1 = emissions.groupby(["year"]).get_group("")

afghanistan_emis = afghanistan["co2_emission"]
uzbekistan_emis = uzbekistan["co2_emission"]
kazakhstan_emis = kazakhstan["co2_emission"]
plt.plot(afghanistan_emissions)
plt.show()

fig, ax = plt.subplots()

countries = ['afghanistan', 'uzbekistan', 'kazakhstan']
quan = ['afghanistan_emis', 'uzbekistan_emis', 'kazakhstan_emis']
bar_labels = ['red', 'blue', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red']

ax.bar(countries, quan, label=bar_labels, color=bar_colors)

ax.set_ylabel('Co2_emission in Central Asia')
ax.set_title('....')
ax.legend(title='CO2 emissions')
plt.show()'''

#--------------4---------------
'''emissions.tail(5)
zim = emissions['co2_emission']
year = emissions['year']
plt.scatter(year, zim)
plt.show()'''

#--------------5---------------
'''m1 = emissions[["co2_emission", "country"]].nlargest(5, ["co2_emission"]).set_index("country")
print(m1)'''

#------------6----------------
'''uzbekistan = emissions.groupby(["country"]).get_group("Uzbekistan")
uzbekistan_last_10 = uzbekistan.tail(10)
width = 0.5
df = uzbekistan_last_10[["year", 'co2_emission']]
ax = df.plot.bar(x="year", y = "co2_emission", width = width, rot=90)
plt.show()'''

#------------7----------------
plt.style.use('_mpl-gallery')

# make data
x = np.arange(0, 10, 2)
year = [2000, 2010, 2020]
co2 = {
    'uzbekistan' : [4021038044, 5209877785, 6310349345],
    'afghanistan' : [71679740, 100148964, 192848747],
    'kazakhstan' : [9076864154, 11100321718, 13908240442],
}
# plot
fig, ax = plt.subplots()

ax.stackplot(year, co2.values(), labels=co2.keys(), alpha=0.8)

ax.legend(loc = 'upper left')
ax.set_title("CO2")
ax.set_xlabel("Year")
ax.set_ylabel("CO2 by years")

plt.show()