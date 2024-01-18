import pandas as pd
from django.utils import timezone
from django.utils.html import strip_tags
from bs4 import BeautifulSoup
from ..models import Vacancy

csv_file_path = 'media/vacancies.csv'
data = pd.read_csv(csv_file_path)

for index, row in data.iterrows():
    key_skills = strip_tags(row['key_skills'])
    description = BeautifulSoup(key_skills, 'html.parser').get_text()
    Vacancy.objects.create(
        title=row['name'],
        key_skills=row['key_skills'],
        salary_min=row['salary_from'],
        salary_max=row['salary_to'],
        currency=row['salary_currency'],
        publication_date=timezone.datetime.strptime(row['published_at'], "%Y-%m-%dT%H:%M:%S%z").date(),
        area_name=row['area_name']
    )

print("Данные успешно импортированы в базу данных.")