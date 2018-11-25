from config import DB_MYSQL_config, DB_MSSQL_config


mssql_db = {
    "driver": DB_MSSQL_config.DRIVER,
    "server": DB_MSSQL_config.SERVER,
    "database": DB_MSSQL_config.DATABASE,
    "UID": DB_MSSQL_config.UID,
    "PWD": DB_MSSQL_config.PWD

}

mysql_db = {
        "user": DB_MYSQL_config.USERNAME,
        "password": DB_MYSQL_config.PASSWORD,
        "database": DB_MYSQL_config.DATABASE,
        "raise_on_warnings": True
    }
