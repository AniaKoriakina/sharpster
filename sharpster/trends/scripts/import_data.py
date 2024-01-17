import pandas as pd
from django.utils import timezone
from django.utils.html import strip_tags
from bs4 import BeautifulSoup
from ..models import Vacancy

csv_file_path = 'media/vacancies.csv'
data = pd.read_csv(csv_file_path)

for index, row in data.iterrows():
    description = strip_tags(row['description'])
    description = BeautifulSoup(description, 'html.parser').get_text()
    Vacancy.objects.create(
        title=row['name'],
        description=description,
        salary_min=row['salary_from'],
        salary_max=row['salary_to'],
        currency=row['salary_currency'],
        publication_date=timezone.datetime.strptime(row['published_at'], "%Y-%m-%dT%H:%M:%S%z").date(),
        profession=row['area_name']
    )

print("Данные успешно импортированы в базу данных.")