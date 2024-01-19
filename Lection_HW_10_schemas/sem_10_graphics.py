## Задача №63. Решение в группах
# 1. Изобразите отношение households к population с
# помощью точечного графика
# 2. Визуализировать longitude по отношения к
# median_house_value, используя линейный график
# 3. Представить гистограмму по housing_median_age
# 4. Изобразить гистограмму по median_house_value с
# оттенком housing_median_age


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/content/sample_data/california_housing_test.csv')
df.sample(5)

# 1. Изобразите отношение households к population с
# помощью точечного графика

plt.figure(figsize = (12,6))
sns.scatterplot(df, x = 'households', y = 'population')

# 2. Визуализировать longitude по отношения к
# median_house_value, используя линейный график



#1
sns.relplot(data = df, x = 'longitude', y = 'median_house_value', kind = 'line', aspect = 2, height = 4);



#2
plt.figure(figsize = (12,6))
sns.lineplot(data = df, x = 'longitude', y = 'median_house_value');

# 3. Представить гистограмму по housing_median_age



plt.figure(figsize = (12,5))
sns.histplot(df, x = 'housing_median_age', bins = 51)
plt.title('Average houses age')
plt.ylabel('Quantity')
plt.xlabel('Houses age')
plt.xticks(range(55))
plt.yticks(range(0, 200, 10))
plt.grid();

# 4. Изобразить гистограмму по median_house_value с
# оттенком housing_median_age


sns.displot(df, x = 'median_house_value', hue = 'housing_median_age', aspect = 2, legend = False  );

# ## Задача №65. Решение в группах
# Написать EDA для датасета про пингвинов
# Необходимо:
# 1. Использовать 2-3 точечных графика
# 2. Применить доп измерение в точечных графиках, используя
# аргументы hue, size, stile
# 3. Использовать PairGrid с типом графика на ваш выбор
# 4. Изобразить Heatmap
# 5. Использовать 2-3 гистограммы


df = sns.load_dataset('penguins')
df.sample(3)

plt.figure(figsize = (6,5))
sns.scatterplot(df, x = 'bill_length_mm', y = 'flipper_length_mm', hue = 'species', style = 'sex');

plt.figure(figsize = (6,5))
sns.scatterplot(df, x = 'bill_depth_mm', y = 'body_mass_g', hue = 'species', size = 'sex');

plt.figure(figsize = (6,5))
sns.scatterplot(df, x = 'flipper_length_mm', y = 'body_mass_g', hue = 'species', size = 'island');

g = sns.PairGrid(df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']])
g.map(sns.scatterplot);

g = sns.PairGrid(df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']])
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot);

g = sns.PairGrid(df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']])
g.map_diag(sns.histplot)
g.map_lower(sns.scatterplot)
g.map_upper(sns.kdeplot);

df_corr = df.corr().round(2)
df_corr

sns.heatmap(df_corr, annot = True, cmap = 'coolwarm', linewidths = 1);

plt.figure(figsize = (12,5))
sns.histplot(df, x = 'body_mass_g')
plt.title('Mass of pinguins')
plt.ylabel('Quantity')
plt.xlabel('Pinguin\'s mass')
plt.grid();

plt.figure(figsize = (12,5))
sns.histplot(df, x = 'flipper_length_mm')
plt.title('Flipper length of pinguins')
plt.ylabel('Quantity')
plt.xlabel('Flipper length')
plt.grid();

## Задача № 67

# Создать новый столбец в таблице с
# пингвинами, который будет отвечать за
# показатель длины клюва пингвина.
# high - длинный(от 42)
# middle - средний(от 35 до 42)
# low - маленький(до 35)


df.sample()

df.loc[df['bill_length_mm'] >= 42, 'heigth_group'] = 'high'
df.loc[(df['bill_length_mm'] >= 35) & (df['bill_length_mm'] < 42), 'heigth_group'] = 'middle'
df.loc[df['bill_length_mm'] < 35, 'height_group'] = 'low'
df.sample(45)

# ## Задача №69.
# Изобразить гистограмму по flipper_length_mm с оттенком height_group. Сделать анализ


plt.figure(figsize=(13,5))
sns.histplot(df, x = 'flipper_length_mm', hue = 'heigth_group');

