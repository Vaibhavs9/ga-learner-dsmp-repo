# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
data['Gender'].replace('-','Agender',inplace=True)
gender_count = data.Gender.value_counts()
plt.bar(gender_count, align='center', height = 15, alpha=0.5)
plt.show()
#Code starts here 




# --------------
#Code starts here
alignment = data.Alignment.value_counts()
alignment.plot.pie(figsize=(5, 5))
plt.title('Character Alignment')
plt.tight_layout()
plt.show()


# --------------
#Code starts here
# pearson's correlation coefficient for Strength and Combat
sc_df = data[['Strength','Combat']].copy()
sc_covariance = sc_df['Strength'].cov(sc_df["Combat"]) 
print(sc_covariance)         
sc_strength = sc_df['Strength'].std(axis = 0)    
print(sc_strength)    
sc_combat = sc_df['Combat'].std(axis = 0)    
print(sc_combat)
sc_pearson = sc_covariance/(sc_strength*sc_combat)
print(sc_pearson)   

# pearson's correlation coefficient for Intelligence and Combat
ic_df = data[['Intelligence','Combat']].copy()
ic_covariance = ic_df['Intelligence'].cov(ic_df['Combat'])
print(ic_covariance)
ic_intelligence = ic_df['Intelligence'].std(axis = 0)  
print(ic_intelligence)
ic_combat = ic_df['Combat'].std(axis = 0)
print(ic_combat)
ic_pearson = ic_covariance/(ic_intelligence*ic_combat)
print(ic_pearson)




# --------------
#Code starts here
total_high = data.Total.quantile(.99) 
super_best = data.loc[data['Total'] > total_high]
super_best_names = list(super_best['Name'])
print(super_best_names)


# --------------
#Code starts here
fig, (ax_1, ax_2,ax_3,ax_4) = plt.subplots(1,4, figsize=(20,10))
ax_1.boxplot(super_best['Intelligence'])
ax_1.set_title('Intelligence')
ax_4.plot(super_best['Intelligence'])
ax_4.set_title('Intelligence')
ax_2.boxplot(super_best['Speed'])
ax_2.set_title('Speed')
ax_3.boxplot(super_best['Power'])
ax_3.set_title('Pntelligence')


