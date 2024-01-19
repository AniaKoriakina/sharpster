import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from unidecode import unidecode

def has_skill(skill_list, target_skill):
    return target_skill in skill_list

def standardize_csharp(name):
    return name.replace('С#', 'C#')

def is_csharp_vacancy(name):
    csharp_keywords = ['c#', 'c sharp', 'шарп', 'с#', 'C#', 'С#', 'C Sharp', 'C SHARP']
    normalized_name = unidecode(name.lower())
    return any(keyword in normalized_name for keyword in csharp_keywords)

df = pd.read_csv('sharpster/media/main/vacancies.csv', dtype={'key_skills': str})

df['name'] = df['name'].apply(standardize_csharp)

df_csharp = df[df['name'].apply(is_csharp_vacancy)]
df_csharp = df_csharp.dropna(subset=['key_skills', 'published_at'])

if not pd.api.types.is_datetime64_any_dtype(df_csharp['published_at']):
    df_csharp['published_at'] = pd.to_datetime(df_csharp['published_at'])

df_csharp['year'] = df_csharp['published_at'].dt.year

df_csharp['has_csharp'] = df_csharp['key_skills'].apply(lambda x: has_skill(x.lower(), 'c#'))

all_skills_csharp = df_csharp.groupby('year')['key_skills'].apply(lambda x: '\n'.join(x)).reset_index(name='all_skills')
skills_count_by_year_csharp = all_skills_csharp['all_skills'].str.split('\n').explode().value_counts().head(21)

table_data_csharp = {'Год': all_skills_csharp['year']}
for skill in skills_count_by_year_csharp.index:
    table_data_csharp[skill] = all_skills_csharp['all_skills'].apply(lambda x: x.count(skill))

table_df_csharp = pd.DataFrame(table_data_csharp)

table_df_csharp.replace(to_replace={"С#": "C#"}, inplace=True)

if 'С#' in table_df_csharp.columns:
    table_df_csharp['C#'] = table_df_csharp[['C#', 'С#']].sum(axis=1)
    table_df_csharp.drop(columns=['С#'], inplace=True)

html_table = table_df_csharp.to_html(index=False)

with open('skills_table.html', 'w', encoding='utf-8') as f:
    f.write(html_table)



plt.style.use('dark_background')
plt.figure(figsize=(12, 8))

colors_csharp = plt.cm.tab20(np.linspace(0, 1, len(skills_count_by_year_csharp.index)))

sorted_skills = skills_count_by_year_csharp.sort_values(ascending=False).index

bar_width = 0.08
index = np.arange(len(table_df_csharp['Год']))

combined_skill = 'С#'
combined_count = table_df_csharp.get('C#', 0) + table_df_csharp.get('С#', 0)

plt.bar(index, combined_count, bar_width, label=combined_skill, color=colors_csharp[0])

for i, skill in enumerate(sorted_skills):
    if ('С#' in skill) or ('C#' in skill):
        continue

    plt.bar(index + i * bar_width, table_df_csharp.get(skill, 0), bar_width, label=skill, color=colors_csharp[i % len(colors_csharp)])

plt.xticks(index + (len(skills_count_by_year_csharp.index) / 2) * bar_width, table_df_csharp['Год'])

handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))

plt.title('ТОП 20 навыков по годам для вакансий C#')
plt.xlabel('Год')
plt.xticks(index, table_df_csharp['Год'], rotation=45, ha="right")
plt.ylabel('Частота навыков')
plt.legend(by_label.values(), by_label.keys())

plt.savefig('skills_bar_plot_from_table_csharp.png')

plt.show()










