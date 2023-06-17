import configparser
config=configparser.RawConfigParser()
config.read("C:\\Users\\Suraj V. Chaudhari\\Desktop\\Orange\\Configuration\\config.ini")

class ReadFile:
    @staticmethod
    def getusername():
        username=config.get('login file','username')
        return username

    @staticmethod
    def getpassword():
        password=config.get('login file','password')
        return password


