from environs import Env

env = Env()
env.read_env()


BOT_TOKEN = env("BOT_TOKEN")
ADMIN = env.int(("ADMIN"))
BOT_URL = env('BOT_URL')
BASE_URL = env('BASE_URL')