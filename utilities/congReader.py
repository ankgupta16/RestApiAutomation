import configparser,os

def properties_to_dict():
    config = configparser.ConfigParser()
    project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    properties_file_path = os.path.join(project_path, "conf.properties")
    config.read(properties_file_path)
    properties_dict = {}
    for section in config.sections():
        properties_dict[section] = {}
        for option in config.options(section):
            properties_dict[section][option] = config.get(section, option)
    return properties_dict


properties_dict = properties_to_dict()
print(properties_dict)