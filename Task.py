import requests
import json
import datetime


# Блок пользовательских вводов работает, но я не понимаю, как сделать, чтобы полученные от пользователя данные
# использовались дальше. Получилась какаято мешанина




URL = 'https://api.exchangerate.host/convert'


def symbols():
    with open('symbols.json', 'r') as file:
        symbols_file = json.load(file)
    return symbols_file


def currency_inputs():
    currency_from = input('Exchange from(default USD) - ')
    if currency_from == '':
        currency_from = 'USD'
    currency_to = input('Exchange to(default UAH) - ')
    if currency_to == '':
        currency_to = 'UAH'
    currency_amount = input('Enter the amount to be exchanged(default 100.00) - ')
    if currency_amount == '':
        currency_amount = 100.00
    currency_date = input('Enter date in format ''dd/MM/YYYY'' - ')
    if currency_date == '':
        currency_date = datetime.datetime.now()
    data = {'from': currency_from, 'to': currency_to, 'amount': currency_amount,
            'date': currency_date.strftime('%d-%m-%Y')}
    print(data)
    r = requests.get(URL, params=data)
    print(r.json())


currency_inputs()


def convert(currency_from, currency_to, amount, start_date):
    result = [['date', 'from', 'to', 'amount', 'rate', 'result']]
    while start_date <= datetime.datetime.now():
        request = requests.get('https://api.exchangerate.host/convert',
                               params={'from': currency_from, 'to': currency_to,
                                       'amount': amount, 'date': start_date})
        data = request.json()
        result.append([data['date'],
                       data['query']['from'],
                       data['query']['to'],
                       data['query']['amount'],
                       data['info']['rate'],
                       data['result']])
        start_date += datetime.timedelta(days=1)
        return result
    print(result)

# if __name__ == '__main__':
# parser = argparse.ArgumentParser(description='Exchange rates')
# parser.add_argument('currency_from')
# parser.add_argument('currency_to')
# parser.add_argument('amount')
# parser.add_argument("--start_date")
# arguments = parser.parse_args()
# print(arguments)
