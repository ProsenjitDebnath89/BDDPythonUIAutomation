from jproperties import Properties
def ReadDataFromPropertiesFile(KeyItem):
    configs = Properties()
    with open('C:/Users/prodebna/PycharmProjects1/BDD/ReadProperties/Config.properties', 'rb') as config_file:
        configs.load(config_file)
        print(configs.get("DB_User"))
        Value_From_PropertiesFile = configs.get(KeyItem)
        Value = str(configs.get(KeyItem).data)
        print(Value)
        return Value
































