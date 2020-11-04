from django.urls.converters import StringConverter, UUIDConverter


class ShortUrlConverter(StringConverter):
    """
    Конвертер строки длинной 7 символов.
    """
    regex = r'[^/]{7}'


class CustomUUIDConverter(UUIDConverter):
    """
    Конвертер UUID4. Стандартный не работает полностью корректно с UUID 4 версии.
    """
    regex = r'[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}'