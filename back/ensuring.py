from mySql import mysql_
from table import table


class ensuring():
    def __init__(self, db):
       self.db = db
       self.ensuringTable = table(['id', 'idUser', 'idCar', 'date', 'outTime', 'backTime'], 'ensuring', ['INT', 'INT', 'INT', 'DATE', 'TIME', 'TIME'])

    def insertToEnsuring(self, ensuringTableValue):
        #this function will insert new value into car table
        try:
            self.db.connect()
            ensuringTableValue = mysql_.ConverteToTuple(ensuringTableValue)
            self.db.insert(ensuringTableValue, self.ensuringTable)
            self.db.close()
            return "Insert To The Table"
        except Exception as e:
            return e
    def selectAllEnsuring(self):
        #this function will return a json of the ensuring table value
        try:
            self.db.connect()
            ensuringTable = self.db.select(self.ensuringTable)
            ensuringJsonTable = mysql_.ConverteToJson(self.ensuringTable, ensuringTable)
            self.db.close()
            return ensuringJsonTable
        except Exception as e:
            return e
    def upadateEnsuring(self, wereList, updateList):
        #this function will update a spesific colum in ensuring table
        try:
            self.db.connect()
            self.db.update(self.ensuringTable, updateList, wereList)
            self.db.close()
            return "Update The Table"
        except Exception as e:
            return e
    def deleteEnsuring(self, wereList):
        #this function will delete the ensuring from the table
        try:
            self.db.connect()
            self.db.delete(self.ensuringTable ,wereList)
            self.db.close()
            return "Delete From The Table"
        except Exception as e:
            return e
        
    def selectSpesificEnsuringr(self, wherelist):
        #this function will return a spesific ensuring
        try:
            self.db.connect()
            ensuringTable = self.db.selectWhere(self.ensuringTable , wherelist)
            ensuringJsonTable = mysql_.ConverteToJson(self.ensuringTable, ensuringTable)
            self.db.close()
            return ensuringJsonTable 
        except Exception as e:
            return e
