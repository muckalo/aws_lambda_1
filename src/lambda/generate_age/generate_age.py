from datetime import datetime


def lambda_handler(event, context):
    date_string = event.get('birth_date', {})

    birth_date = datetime.strptime(date_string, "%Y-%m-%d").date()
    today_date = datetime.today().date()
    age = today_date.year - birth_date.year - ((today_date.month, today_date.day) < (birth_date.month, birth_date.day))

    result_str = f'You are {age} age years old'
    result = {'result': result_str}

    return result
