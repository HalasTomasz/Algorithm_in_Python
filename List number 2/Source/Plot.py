import pandas as pd
import seaborn as sns

df = pd.read_json(r'C:\Users\denev\.spyder-py3\K100Hib') 
df['cmp'] = df.apply(lambda row: (row['Porownania'] / row.Tablica), axis=1)
df['c'] = df.apply(lambda row: (row['Zmiany'] / row.Tablica), axis=1)
df['Nazwa'] = df['Nazwa'].astype('category')
#%%
sns.lineplot(data = df, x = 'Tablica', y = 'Porownania', hue = 'Nazwa')
#%%
sns.lineplot(data = df, x = 'Tablica', y = 'Zmiany', hue = 'Nazwa')
#%%
sns.lineplot(data = df, x = 'Tablica', y = 'Czas', hue = 'Nazwa')
#%%
sns.lineplot(data = df, x = 'Tablica', y = 'cmp', hue = 'Nazwa')
#%%
sns.lineplot(data = df, x = 'Tablica', y = 'c', hue = 'Nazwa')

