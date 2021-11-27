from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста
USER_POSTGRES = env.str("USER_POSTGRES")
PASSWORD_POSTGRES = env.str("PASSWORD_POSTGRES")
HOST_POSTGRES = env.str("HOST_POSTGRES")
BASE_POSTGRES = env.str("BASE_POSTGRES")

LIST_LANGUAGE_TRANSLATE = ['English', 'Russian']
LIST_LANGUAGE_PROGRAMMING = ['Python', '1C', 'Java']
