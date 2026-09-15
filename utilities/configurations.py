import configparser

def get_config():
    config = configparser.ConfigParser()
    config.read("utilities/properties.ini")
    return config