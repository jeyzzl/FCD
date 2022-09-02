import pandas as pd
import matplotlib.pyplot as plt

songs = pd.read_csv('./database.csv')

#top danceability
########################
dance = songs[['danceability','uri']].sort_values(by="danceability", ascending=False).head(10).plot.hist()
print('Top 10 danceability songs \n')
print(dance)
plt.show()


#most energy by key
########################
print('\nKeys sorted by average energy \n')
total_avrg = []
key_energy_table = songs[['energy','key']]
for x in range(0,12):
    key = key_energy_table[key_energy_table.key == x]
    avrg_key = key['energy'].sum()/len(key['energy'])
    total_avrg.append(avrg_key)

k_avrg = pd.Series(total_avrg)
k_avrg_df = pd.DataFrame({"energy":k_avrg})
final = k_avrg_df.sort_values(by='energy', ascending=False).plot.hist()
print(final)
plt.show()

#most energy by tempo
########################
print('\nTempo sorted by average energy \n')
energy_avrg = []
tempo_energy_table = songs[['tempo','energy']]
for x in range(0,223):
    tempo = tempo_energy_table[tempo_energy_table.tempo == x]
    avrg_energy = tempo['energy'].sum()/len(tempo['energy'])
    energy_avrg.append(avrg_energy)

e_avrg = pd.Series(energy_avrg)
e_avrg_df = pd.DataFrame({'energy':e_avrg})
final_t = e_avrg_df.sort_values(by='energy', ascending=False).head(10).plot.hist()
print(final_t)
plt.show()