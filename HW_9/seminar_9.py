"""##Домашнее задание
Дан файл california_housing_train.csv. Определить среднюю стоимость дома , где количество людей от 0 до 500 (population) и сохранить ее в переменную avg.
Используйте модуль pandas.
"""

import pandas as pd

df = pd.read_csv('/content/sample_data/california_housing_train.csv')
df.sample(5)

avg = df[(df['population'] > 0) & (df['population'] <= 500)]['median_house_value'].mean()
avg

"""Найти максимальное значение переменной "households" в зоне минимального значения переменной min_population и сохраните это значение в переменную max_households_in_min_population.
Используйте модуль pandas.
"""

min_population = df['population']. min()
min_population

max_households_in_min_population = df[df['population'] == min_population]['households'].max()
max_households_in_min_population