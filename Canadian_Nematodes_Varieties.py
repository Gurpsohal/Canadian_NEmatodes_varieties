import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/gursohal/Desktop/Pythong/checklist_of_canadian_nematodes__liste_des_nématodes_canadiens_2024.csv')
print(data.columns)
print(data.info())

#species_counts.plot(kind='barh', color='lightcoral', edgecolor='black')
#plt.xlabel('Frequency')
#plt.ylabel('Nematode Species')
#plt.title('Nematode Species Frequency')
#plt.show()
#New_Species = data['Province/Territory | Province/territoire']
#New_Species.plot(kind='hist')
#plt.xlabel('Frequency')
#plt.ylabel('Nematode Species')
#plt.show()


# Get counts of provinces/territories
province_counts = data['Province/Territory | Province/territoire'].value_counts()

# Plot bar chart
province_counts.plot(kind='barh', color='lightcoral', edgecolor='black')
#plt.xlabel('Frequency')
#plt.ylabel('Province/Territory')
#plt.title('Frequency of Nematodes by Province/Territory')
plt.show()