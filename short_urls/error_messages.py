from collections import namedtuple

error_message = namedtuple('error_message', ('message', 'code', ))

WRONG_UUID = error_message(
    'Строка UUID не соответсует стандарту. Допустимы только строки UUID версии 4',
    'wrong_uuid',
)