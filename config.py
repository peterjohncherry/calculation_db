#!/usr/vin/python
from configparser import ConfigParser


def dbconfig(filename='/home/peter/PROJECTS/PGSQL_TEST/database.ini', section='postgresql'):
    parser = ConfigParser()
    print(filename)
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
        print ("db = ", db)
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

