
#modo = 'produccion'
modo = 'desarrollo'


def getConfigDB():
    configDB = {}
    if (modo == 'desarrollo'):
        configDB['host'] = 'localhost'
        configDB['user'] = 'admingrc'
        configDB['password'] = '1234'
        configDB['database'] = 'bdgrc'
        configDB['auth_plugin'] = 'mysql_native_password'

    elif(modo == 'produccion'):
        configDB['host'] = 'grcunla.mysql.pythonanywhere-services.com'
        configDB['user'] = 'grcunla'
        configDB['password'] = 'mmyt1234'
        configDB['database'] = 'grcunla$grcdb'
        configDB['auth_plugin'] = 'mysql_native_password'
    else:
        configDB['host'] = None
        configDB['user'] = None
        configDB['password'] = None
        configDB['database'] = None
        configDB['auth_plugin'] = 'mysql_native_password'

    return configDB