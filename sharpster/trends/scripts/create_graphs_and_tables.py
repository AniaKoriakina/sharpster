import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dateutil.parser import parse

df = pd.read_csv('../../media/vacancies_updated.csv', dtype={'key_skills': str})

df['published_at'] = pd.to_datetime(df['published_at'], utc=True)


def extract_year(date):
    return date.year


df['year'] = df['published_at'].apply(extract_year)


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


df['avg_salary'] = df.apply(extract_avg_salary, axis=1)

# df = df.dropna(subset=['avg_salary', 'salary_currency', 'salary_from', 'salary_to'])  # Закомментить если нужны таблицы по количеству вакансий

def is_csharp_vacancy(name):
    csharp_keywords = ['c#', 'c sharp', 'шарп', 'с#', 'C#', 'С#', 'C Sharp', 'C SHARP']
    if any(keyword.lower() in name.lower() for keyword in csharp_keywords):
        return True
    return False

csharp_df = df[df['name'].apply(lambda x: is_csharp_vacancy(x) if pd.notna(x) else False)]


# Динамика уровня зарплат по годам для C# программистов
csharp_avg_salary_by_year = csharp_df.groupby('year')['avg_salary'].mean()

plt.style.use('dark_background')

fig, ax = plt.subplots(figsize=(10, 6))
plt.plot(csharp_avg_salary_by_year.index, csharp_avg_salary_by_year.values, marker='o', color='blue', alpha=0.8)
plt.title('Динамика средних зарплат для C# программистов по годам')
plt.xlabel('Год')
plt.ylabel('Средняя зарплата')
plt.grid(True)
plt.xticks(csharp_avg_salary_by_year.index, rotation=45)
plt.yticks(np.arange(csharp_avg_salary_by_year.min(), csharp_avg_salary_by_year.max(), step=10000))
plt.savefig('csharp_avg_salary_by_year.png')
plt.show()

# Динамика количества вакансий по годам для C# программистов
csharp_vacancies_by_year = csharp_df.groupby('year').size()
plt.style.use('dark_background')

fig, ax = plt.subplots(figsize=(10, 6))
csharp_vacancies_by_year.plot(kind='bar', color='green', alpha=0.8)
plt.title('Динамика количества вакансий для C# программистов по годам')
plt.xlabel('Год')
plt.ylabel('Количество вакансий')
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.yticks(np.arange(0, csharp_vacancies_by_year.max(), step=500))
plt.savefig('csharp_vacancies_by_year.png')
plt.show()

# Динамика уровня зарплат по годам
avg_salary_by_year = df.groupby('year')['avg_salary'].mean()
plt.style.use('dark_background')

fig, ax = plt.subplots(figsize=(10, 6))
plt.plot(avg_salary_by_year.index, avg_salary_by_year.values, marker='o', color='red', alpha=0.8)
plt.title('Динамика средних зарплат по годам')
plt.xlabel('Год')
plt.ylabel('Средняя зарплата')
plt.grid(True)
plt.xticks(avg_salary_by_year.index, rotation=45)
plt.yticks(np.arange(avg_salary_by_year.min(), avg_salary_by_year.max(), step=10000))
plt.savefig('avg_salary_by_year.png')
plt.show()


# Динамика количества вакансий по годам
vacancies_by_year = df.groupby('year').size()
plt.style.use('dark_background')

fig, ax = plt.subplots(figsize=(10, 6))

vacancies_by_year.plot(kind='bar', color='orange', alpha=0.8)
plt.title('Динамика количества вакансий по годам')
plt.xlabel('Год')
plt.ylabel('Количество вакансий')
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.yticks(np.arange(0, vacancies_by_year.max(), step=50000))
plt.savefig('vacancies_by_year.png')
plt.show()


dark_styles = """
<style>
body {
    color: #fff;
    background-color: #333;
}

table {
    border-collapse: collapse;
    width: 15%;
}

th, td {
    border: 1px solid #555;
    padding: 8px;
    text-align: left;
}

th {
    background-color: #555;
    color: #fff;
}
</style>
"""

avg_salary_by_year_df = avg_salary_by_year.to_frame().reset_index()
avg_salary_by_year_df['avg_salary'] = avg_salary_by_year_df['avg_salary'].round(2)
avg_salary_html = avg_salary_by_year_df.to_html(index=False, classes='table table-striped', escape=False)

with open('avg_salary_by_year.html', 'w', encoding='utf-8') as f:
    f.write(f'<h2>Динамика уровня зарплат по годам</h2>{dark_styles}{avg_salary_html}')

vacancies_by_year_df = vacancies_by_year.to_frame().reset_index()
vacancies_html = vacancies_by_year_df.to_html(index=False, classes='table table-striped', escape=False)

with open('vacancies_by_year.html', 'w', encoding='utf-8') as f:
    f.write(f'<h2>Динамика количества вакансий по годам</h2>{dark_styles}{vacancies_html}')

csharp_avg_salary_by_year_df = csharp_avg_salary_by_year.to_frame().reset_index()
csharp_avg_salary_by_year_df['avg_salary'] = csharp_avg_salary_by_year_df['avg_salary'].round(2)
csharp_avg_salary_html = csharp_avg_salary_by_year_df.to_html(index=False, classes='table table-striped', escape=False)

with open('csharp_avg_salary_by_year.html', 'w', encoding='utf-8') as f:
    f.write(f'<h2>Динамика уровня зарплат по годам для C# программистов</h2>{dark_styles}{csharp_avg_salary_html}')

csharp_vacancies_by_year_df = csharp_vacancies_by_year.to_frame().reset_index()
csharp_vacancies_html = csharp_vacancies_by_year_df.to_html(index=False, classes='table table-striped', escape=False)

with open('csharp_vacancies_by_year.html', 'w', encoding='utf-8') as f:
    f.write(f'<h2>Динамика количества вакансий по годам для C# программистов</h2>{dark_styles}{csharp_vacancies_html}')

print("HTML files generated successfully!")






