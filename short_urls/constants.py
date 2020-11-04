URL_REGEX = r'((https?):((//)|(\\\\))+[\w\d:#@%/;$()~_?\+-=\\\.&]*)'

UUID4_REGEX = r'[0-9a-f]{12}4[0-9a-f]{3}[89ab][0-9a-f]{15}\Z'

# Дефолтное время жизни записи в БД до ее очистки
DEFAULT_CLEANUP_INTERVAL = 30

DEFAULT_CACHE_TTL = 60 * 10
