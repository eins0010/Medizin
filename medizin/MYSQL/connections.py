from config import DB_config

db = {
        "user": DB_config.USERNAME,
        "password": DB_config.PASSWORD,
        "database": DB_config.DATABASE,
        "raise_on_warnings": True
    }