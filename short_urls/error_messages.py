from collections import namedtuple

error_message = namedtuple('error_message', ('message', 'code', ))

WRONG_UUID = error_message(
    'Строка UUID не соответсует стандарту. Допустимы только строки UUID версии 4',
    'wrong_uuid',
)
WRONG_URL_CODE_LEN = error_message(
    'Длинна "url_code" должна быть ровно 7 символов',
    'wrong_url_code_len',
)
WRONG_FULL_URL = error_message(
    'URL не корректно отформатированн',
    'wrong_full_url',
)
UNIQUE_URL_CODE = error_message(
    'Такой "url_code" уже существует. Придумайте другой',
    'unique_url_code',
)