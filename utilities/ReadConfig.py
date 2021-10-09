import configparser
import os

config = configparser.RawConfigParser()
current_dir = os.getcwd()
os.chdir('..')
base_dir = os.getcwd()
config_dir = os.path.join(base_dir, "Configurations", "config.ini")
config.read(config_dir)


class ReadConfig:
    @staticmethod
    def getType():
        travel_type = config.get('search screen', 'type')
        return travel_type

    @staticmethod
    def getFromLoc():
        fromLoc = config.get('search screen', 'fromLoc')
        return fromLoc

    @staticmethod
    def getToLoc():
        toLoc = config.get('search screen', 'toLoc')
        return toLoc

    @staticmethod
    def getDepartDate():
        departDate = config.get('search screen', 'departure_date')
        return departDate

    @staticmethod
    def getReturnDate():
        returnDate = config.get('search screen', 'return_date')
        return returnDate
