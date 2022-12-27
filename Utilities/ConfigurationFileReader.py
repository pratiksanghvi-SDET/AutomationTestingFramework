from jproperties import Properties


#-----------------------------------------------------------------
configs = Properties()
# Read file from Resources folder
with open('D:\Learn & Projects\SDET-AutomationFramework\Resources\FrameworkProperties.properties', 'rb') as config_file:
    configs.load(config_file)

class configurationFileReader:


    def getPropertyValue(propertyName):
        tup =configs.get(str(propertyName))
        return tup[0]

