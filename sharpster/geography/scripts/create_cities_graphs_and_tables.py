import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dateutil.parser import parse

df = pd.read_csv('../../media/vacancies_updated.csv', dtype={'key_skills': str})

df['published_at'] = pd.to_datetime(df['published_at'], utc=True)

def extract_year(date):
    return date.year

df['year'] = df['published_at'].apply(extract_year)

df_2023 = df[df['year'] == 2023]

def extract_avg_salary(row):
    currency = row['salary_currency']
    from_salary = row['salary_from']
    to_salary = row['salary_to']

    if pd.notna(currency):
        if pd.notna(from_salary) and pd.notna(to_salary):
            return (from_salary + to_salary) / 2
        elif pd.notna(from_salary):
            return from_salary
        elif pd.notna(to_salary):
            return to_salary

    return None

df_2023['avg_salary'] = df_2023.apply(lambda row: extract_avg_salary(row), axis=1)

df_2023 = df_2023.dropna(subset=['avg_salary', 'salary_currency', 'salary_from', 'salary_to', 'area_name']) #Закомментить если нужна доля вакансий

def is_csharp_vacancy(name):
    csharp_keywords = ['c#', 'c sharp', 'шарп', 'с#', 'C#', 'С#', 'C Sharp', 'C SHARP']
    if any(keyword.lower() in name.lower() for keyword in csharp_keywords):
        return True
    return False

top_n = 10

# уровень зарплат по городам в 2023 году для профессии C#
avg_salary_by_area_csharp = df_2023[df_2023['name'].apply(lambda x: is_csharp_vacancy(x) if pd.notna(x) else False)].groupby('area_name')['avg_salary'].mean().sort_values(ascending=False)
avg_salary_by_area_csharp = avg_salary_by_area_csharp.drop_duplicates()
avg_salary_by_area_csharp = avg_salary_by_area_csharp.round(2)
top_avg_salary_csharp = avg_salary_by_area_csharp.head(top_n)
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(15, 6))
top_avg_salary_csharp.plot(kind='bar', color='purple', alpha=0.8)
plt.title(f'Top {top_n} уровень зарплат по городам в 2023 году для профессии C# (в порядке убывания)')
plt.xlabel('Город')
plt.ylabel('Средняя зарплата')
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(f'top_salary_by_city_2023_csharp.png')
plt.show()


# доля вакансий по городам в 2023 году для профессии C#
vacancies_by_area_csharp = df_2023[df_2023['name'].apply(lambda x: is_csharp_vacancy(x) if pd.notna(x) else False)]['area_name'].value_counts()
percentage_by_area_csharp = (vacancies_by_area_csharp / vacancies_by_area_csharp.sum()) * 100
top_n = 10
top_percentage_csharp = percentage_by_area_csharp.head(top_n)
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(15, 6))
top_percentage_csharp.plot(kind='bar', color='purple', alpha=0.8)
plt.title(f'Top {top_n} доля вакансий по городам в 2023 году для профессии C# (в порядке убывания)')
plt.xlabel('Город')
plt.ylabel('Доля вакансий (%)')
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(f'top_percentage_by_city_2023_csharp.png')
plt.show()

# уровень зарплат по городам в 2023 году
avg_salary_by_area = df_2023.groupby('area_name')['avg_salary'].mean().sort_values(ascending=False)
avg_salary_by_area = avg_salary_by_area.drop_duplicates()
avg_salary_by_area = avg_salary_by_area.round(2)
top_n = 10

top_avg_salary = avg_salary_by_area.head(top_n)
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(15, 6))
top_avg_salary.plot(kind='bar', color='purple', alpha=0.8)
plt.title(f'Top {top_n} уровень зарплат по городам в 2023 году (в порядке убывания)')
plt.xlabel('Город')
plt.ylabel('Средняя зарплата')
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(f'top_salary_by_city_2023_1.png')
plt.show()

# доля вакансий по городам в 2023 году
vacancies_by_area = df_2023['area_name'].value_counts()
percentage_by_area = (vacancies_by_area / vacancies_by_area.sum()) * 100
top_n = 10
top_percentage = percentage_by_area.head(top_n)
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(15, 6))
top_percentage.plot(kind='bar', color='purple', alpha=0.8)
plt.title(f'Top {top_n} доля вакансий по городам в 2023 году (в порядке убывания)')
plt.xlabel('Город')
plt.ylabel('Доля вакансий (%)')
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(f'top_percentage_by_city_2023.png')
plt.show()

rounded_percentage_by_area_csharp = percentage_by_area_csharp.round(2)
rounded_percentage_by_area = percentage_by_area.round(2)

rounded_percentage_by_area_csharp.to_frame().reset_index().to_html('top_percentage_csharp.html', index=False)
rounded_percentage_by_area.to_frame().reset_index().to_html('top_percentage.html', index=False)
top_avg_salary_csharp.to_frame().reset_index().to_html('top_avg_salary_csharp.html', index=False)
top_avg_salary.to_frame().reset_index().to_html('top_avg_salary.html', index=False)




