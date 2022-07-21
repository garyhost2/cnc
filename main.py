
import data_2020
import data_2022
from matplotlib import pyplot as plt 

x1 = data_2020.results_2020
x2 = data_2022.results_2022
y1 = [*range(len(x1))]
y2 = [*range(len(x2))]

plt.plot(x1,y1)
plt.plot(x2,y2)
plt.xlabel('2020-2022')
plt.ylabel('taux')
plt.title('difference entre resultat 2022-2020')
plt.show()