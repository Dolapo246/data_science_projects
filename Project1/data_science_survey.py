import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("kaggle_survey_2022_responses.csv")

education_nigeria = df[
    (df['Q4'] == 'Nigeria') &
    (df['Q8'] != 'I prefer not to answer') & (df['Q8'] != 'Professional doctorate') & (df['Q8'] != 'No formal education past high school')
]['Q8'].value_counts().reset_index()

education_nigeria.columns = ['Level of Education', 'Frequency']
print('Nigeria')
print (education_nigeria)
print ('\n')

education_south_korea = df[
    (df['Q4'] == 'South Korea') &
    (df['Q8'] != 'I prefer not to answer') & (df['Q8'] != 'Professional doctorate') & (df['Q8'] != 'No formal education past high school')
]['Q8'].value_counts().reset_index()

education_south_korea.columns = ['Level of Education', 'Frequency']

print('South Korea')
print (education_south_korea)
print('\n')


education_brazil= df[
    (df['Q4'] == 'Brazil') &
    (df['Q8'] != 'I prefer not to answer') & (df['Q8'] != 'Professional doctorate') & (df['Q8'] != 'No formal education past high school')
]['Q8'].value_counts().reset_index()

education_brazil.columns = ['Level of Education', 'Frequency']
print('Brazil')
print (education_brazil)
print('\n')

education_argentina= df[
    (df['Q4'] == 'Argentina') &
    (df['Q8'] != 'I prefer not to answer') & (df['Q8'] != 'Professional doctorate') & (df['Q8'] != 'No formal education past high school')
]['Q8'].value_counts().reset_index()


education_argentina.columns = ['Level of Education', 'Frequency']

print('Argentina')
print (education_argentina)
print('\n')

countries = ['Nigeria', 'South Korea', 'Brazil', 'Argentina']

education_df = df[
    (df['Q4'].isin(countries)) &
    (df['Q8'] != 'I prefer not to answer') & (df['Q8'] != 'Professional doctorate') & (df['Q8'] != 'No formal education past high school')
]

frequency_table = pd.crosstab(
    education_df['Q4'],
    education_df['Q8']
)

frequency_table




import matplotlib.pyplot as plt

frequency_table.plot(
    kind='bar',
    figsize=(12, 7),
    colormap='tab10',
    width=0.8
)

plt.title('Level of Education Across Countries')
plt.xlabel('Countries')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.legend(title='Level of Education', bbox_to_anchor=(1.05, 1))
plt.tight_layout()

plt.show()