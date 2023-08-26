# python code to retrieve data from config.ini file

import os
from configparser import ConfigParser

path = os.path.dirname(os.path.abspath(__file__))

def configuration(section = 'mariaDB'):
    '''
    Collect details in the config.ini by
    passing the section 
        input:
            section:string
        return:
            config: dict(string)
    '''

    parser = ConfigParser()
    file = path + '/config.ini'
    parser.read(file)
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception(f"Section {section} not found in the {file} file")
    return config
