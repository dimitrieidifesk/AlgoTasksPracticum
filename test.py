# import requests
#
# url = 'https://shafklj.ru/wh_bill/v1/transaction/wh/'
# headers = {
#     'Content-Type': 'application/json'
# }
# json_body = {
#     "id": ["20241123172602567"],
#     "sum": ["0.00"],
#     "orderid": ["43024149"],
#     "key": ["5723e592473147b0af1c32d6a50cc09e"],
#     "pk_hostname": ["https: //222330801184.server.paykeeper.ru"],
#     "ps_id": ["94"],
#     "client_email": ["LS 43024149"],
#     "client_phone": ["2094508856"],
#     "service_name": ["Услуга"],
#     "fop_receipt_key": ["Uo9AFN_J"],
#     "obtain_datetime": ["2024-10-29 16:08:59"]
# }
# response = requests.post(url, json=json_body, headers=headers, verify=False)
# print(response.status_code)
# resp = response.json()
# print(resp)


import phonenumbers
from phonenumbers import carrier, geocoder

def validate_phone_number(phone, region='RU'):
    try:
        # Проверяем, начинается ли номер с '7' или '8' и добавляем +7, если это так
        if phone.startswith('8') or phone.startswith('7'):
            phone = '+7' + phone[1:]

        # Пытаемся создать объект PhoneNumber
        parsed_phone = phonenumbers.parse(phone, region)

        # Проверяем, является ли номер действительным
        return phonenumbers.is_valid_number(parsed_phone)
    except phonenumbers.NumberParseException:
        return False

# Примеры использования
phone_numbers = [
    "+1-234-567-8901",
    "234-567-8901",
    "(234) 567-8901",
    "+91 98765 43210",
    "+7 (969) 722-40-20",
    "79697224020",
    "89697224020",
    "7 (969) 722 4020",
    "1234567",    # Ошибочный номер
    "abcd1234",   # Ошибочный номер
]

for number in phone_numbers:
    print(f"{number}: {validate_phone_number(number)}")