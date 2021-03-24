from mySql import mysql_
from table import table

class cars:
    def __init__(self, db):
        #id = int, carsNumber= varchar(255) , carKind = varchar(255), carType = varchar(255) carWork = bool
        self.db = db
        self.carsTable = table(['id', 'carNumber', 'carKind', 'carType', 'carWork'], 'cars', ['INT', "VARCHAR(255)", "VARCHAR(255)", 'VARCHAR(255)', 'VARCHAR(255)', 'TINYINT'])
    
    def insertToCar(self, carTableValue):
        try:
            #this function will insert new value into car table
            self.db.connect()
            tupelCarValue = mysql_.ConverteToTuple(carTableValue)
            self.db.insert(tupelCarValue, self.carsTable)
            self.db.close()
            return "Insert To The Car"
        except Exception as e:
            return e
            
    def selectAllCar(self):
        #this function will return a json of the car table value
        try:
            self.db.connect()
            carsTable = self.db.select(self.carsTable)
            carsJsonTable = mysql_.ConverteToJson(self.carsTable, carsTable)
            self.db.close()
            return carsJsonTable
        except Exception as e:
            return e
    
    def upadateCar(self, wereList, updateList):
        #this function will update a spesific colum in car table
        try:
            self.db.connect()
            self.db.update(self.carsTable, updateList, wereList)
            self.db.close()
            return "Update The Table"
        except Exception as e:
            return e
    
    def deleteCar(self, wereList):
        #this function will delete the car from the table
        try:
            self.db.connect()
            self.db.delete(self.carsTable ,wereList)
            self.db.close()
            return "Delete From The Table"
        except Exception as e:
            return e

    def selectSpesificCar(self, wherelist):
        #this function will return a spesific car
        try:
            self.db.connect()
            carsTable = self.db.selectWhere(self.carsTable ,wherelist)
            carsJsonTable = mysql_.ConverteToJson(self.carsTable ,carsTable)
            self.db.close()
            return carsJsonTable
        except Exception as e:
            return e
