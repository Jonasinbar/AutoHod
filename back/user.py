from mySql import mysql_
from table import table
import asyncio

class users:
    def __init__(self, db):
        self.db = db
        self.usersTable = table(['id', 'name', 'userId', 'team', 'carType', 'phoneNumber', 'password'], 'users', ['INT', "VARCHAR(255)", 'INT', "VARCHAR(255)","VARCHAR(255)", "VARCHAR(255)"])
        
    def insertUsers(self, userTableValue):
        #this function will inseret to user new value
        try:
            self.db.connect()
            userTableValue = mysql_.ConverteToTuple(userTableValue)
            self.db.insert(userTableValue, self.usersTable)
            self.db.close()
            return "Insert To The Users"
        except Exception as e:
            return e
    
    def selectUsers(self):
        #this function will return a table of json of all users
        try:
            self.db.connect()
            usersTable = self.db.select(self.usersTable)
            usersJsonTable = mysql_.ConverteToJson(self.usersTable, usersTable)
            self.db.close()
            return usersJsonTable
        except Exception as e:
            return e
    def updateUser(self, updateList, wereList):
        #this function will update the table
        try:
            self.db.connect()
            self.db.update(self.usersTable, updateList, wereList)
            self.db.close()
            return "Update The Table"
        except Exception as e:
            return e

    def deleteUser(self, wereList):
        #this function will delete the value from the table
        try:
            self.db.connect()
            self.db.delete(self.usersTable, wereList)
            self.db.close()
            return "Delete From The Table"
        except Exception as e:
            return e
            
    def selectSpesificUser(self, wereList):
        #this function return a spesific users in the table
        try:
            self.db.connect()
            userstable = self.db.selectWhere(self.usersTable, wereList)
            usersJsonTable = mysql_.ConverteToJson(self.usersTable ,userstable)
            self.db.close()
            if(usersJsonTable == {}):
                return "False"
            return usersJsonTable
        except Exception:
            return "False"