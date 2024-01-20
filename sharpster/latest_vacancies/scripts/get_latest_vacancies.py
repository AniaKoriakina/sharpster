import requests
from datetime import datetime, timedelta
from dateutil import parser

def get_vacancies():
    current_datetime = datetime.utcnow()
    twenty_four_hours_ago = current_datetime - timedelta(hours=24)
    formatted_time_from = twenty_four_hours_ago.strftime("%Y-%m-%dT%H:%M:%S%z")
    formatted_time_to = current_datetime.strftime("%Y-%m-%dT%H:%M:%S%z")

    url = (
        'https://api.hh.ru/vacancies?clusters=true&only_with_salary=true&enable_snippets=true&st=searchVacancy'
        f'&text=C%23&search_field=name&per_page=10'
        f'&date_from={formatted_time_from}&date_to={formatted_time_to}'
    )

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        vacancies = []

        for vacancy in data.get('items', []):
            vacancy_data = get_vacancy_details(vacancy.get('id'))
            salary_info = vacancy.get('salary', {})
            average_salary = calculate_average_salary(salary_info)
            currency = salary_info.get('currency', 'Не указана')

            vacancies.append({
                "name": vacancy.get('name', 'Не указано'),
                "id": vacancy.get('id', 'Нет ID'),
                "salary": format_salary(average_salary, currency),
                "region": vacancy.get('area', {}).get('name', 'Не указано'),
                "published_at": format_published_date(vacancy.get('published_at', 'Не указана')),
                "company_name": vacancy.get('employer', {}).get('name', 'Не указана'),
                "key_skills": [skill.get('name', '') for skill in vacancy_data.get('key_skills', [])],
                "description": vacancy_data.get('description', 'Нет описания')
            })

        return vacancies
    else:
        print(f"Ошибка {response.status_code}: {response.text}")
        return []

def calculate_average_salary(salary_info):
    from_salary = salary_info.get('from')
    to_salary = salary_info.get('to')

    if from_salary is not None and to_salary is not None:
        return (from_salary + to_salary) / 2
    elif from_salary is not None:
        return from_salary
    elif to_salary is not None:
        return to_salary
    else:
        return 'Не указано'

def format_salary(salary, currency):
    if isinstance(salary, (int, float)):
        return "{:,.0f} {}".format(salary, currency)
    else:
        return salary

def format_published_date(published_date):
    parsed_date = parser.parse(published_date)
    return parsed_date.strftime("%Y-%m-%d %H:%M:%S")

def get_vacancy_details(vacancy_id):
    response_id = requests.get(f'https://api.hh.ru/vacancies/{vacancy_id}')
    if response_id.status_code == 200:
        return response_id.json()
    else:
        print(f"Ошибка {response_id.status_code}: {response_id.text}")
        return {}


