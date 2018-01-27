import pandas as pd #data processing
import numpy as np #calculate stuff
import seaborn as sns #visualization
import matplotlib.pyplot as plt #visualization


#IMPORTING

pokemon_df = pd.read_csv('data/pokemon.csv')
combats_df = pd.read_csv('data/combats.csv')
test_df = pd.read_csv('data/tests.csv')
prediction_df = test_df.copy()

print pokemon_df.info()


#CLEANING

pokemon_df['Type 2'] = pokemon_df['Type 2'].fillna('None')
pokemon_df['Name'] = pokemon_df['Name'].fillna('Primeape')

#some type is named 'Fight', and some named 'Fighting'. This code is to clean it up.
pokemon_df['Type 1'] = pokemon_df['Type 1'].replace('Fighting', 'Fight')
pokemon_df['Type 2'] = pokemon_df['Type 2'].replace('Fighting', 'Fight')

#changing true/false to 1/0 in Legendary column
pokemon_df['Legendary'] = pokemon_df['Legendary'].map({False: 0, True:1})

print pokemon_df.info()


#changing winner to 0 and 1, each corresponds to first and second pokemon respectively
combats_df.Winner[combats_df.Winner == combats_df.First_pokemon] = 0
combats_df.Winner[combats_df.Winner == combats_df.Second_pokemon] = 1

print(combats_df.head(5))

stats_df = pokemon_df.drop( ['Name'], axis=1)
stats_dict = stats_df.set_index('#').T.to_dict('list')

print(stats_dict[1])

stats_list = []
stats_col = ['1Type1', '1Type2', '1HP', '1Attack',
             '1Defence', '1Sp.Attack','1Sp.Def',
             '1Speed', '1Generation', '1Legendary',
             '2Type1', '2Type2', '2HP', '2Attack',
             '2Defence', '2Sp.Attack','2Sp.Def',
             '2Speed', '2Generation', '2Legendary',
             'Winner'];
for row in combats_df.itertuples():
    first_pokemon_stats = stats_dict[row.First_pokemon]
    second_pokemon = stats_dict[row.Second_pokemon]
    winner = row.Winner
    battle = np.append(first_pokemon_stats, np.append(second_pokemon, winner))
    stats_list.append(battle.tolist())

print stats_list[:1]

stats_df = pd.DataFrame(stats_list, columns=stats_col)

print (stats_df.head(1));

#stats_df = stats_df.sample(frac=1).reset_index(drop=True);

#train_data, test_data = stats_df[:35000, :], stats_df[35000:, :]

#train_data.to_csv("train_data.csv")
#test_data.to_csv("test_data.csv")

#stats_df = stats_df.sample(frac=1).reset_index(drop=True);
train=stats_df.sample(frac=0.75,random_state=42).reset_index(drop=True)
test=stats_df.drop(train.index).reset_index(drop=True)
test_u=test.drop("Winner", axis=1)

train.to_csv("train_data.csv")
test.to_csv("test_data.csv")
test_u.to_csv("test_data_u.csv")
