import mysql.connector
import logging as log


class mysql_:
    def __init__(self, host, user, pass_, database):
        self.host = host
        self.user = user
        self.pass_ = pass_
        self.database = database
    
    def connect(self):
        self.mydb = mysql.connector.connect(
            host=f"{self.host}",
            user=f"{self.user}",
            passwd=f"{self.pass_}",
            database=f"{self.database}"
        )
        self.mycursor = self.mydb.cursor()
    
    def close(self):
        self.mycursor.close()
        self.mydb.close()

    def __connect(self, database):
        self.mydb = mysql.connector.connect(
            host=f"{self.host}",
            user=f"{self.user}",
            passwd=f"{self.pass_}",
            database=f"{database}"
        )
        self.mycursor = self.mydb.cursor()
     
    def reconnect_db(self):
        self.mydb.reconnect(attempts=1, delay=0)
    

    def insert(self, newtuple, tableObject):
        self.reconnect_db()
        table = tableObject.getColumes()
        tableS = tableObject.getColumesS()
        sql = f"INSERT INTO {tableObject.tableName} {table} VALUES {tableS}" 
        self.mycursor.execute(sql, newtuple)
        self.mydb.commit()
    

    def __valueInsert(self, newList):
        valueInsert = f"("
        for i, value in enumerate(newList):
            if(i < len(newList)):
                valueInsert = valueInsert +  f"{value},"
            else:
                valueInsert = valueInsert + f"{value})"
        return valueInsert

    def select(self, tableObject, selectColumes="*"):
        if(type(selectColumes) != str):
            columes = self.__valueInsert(selectColumes)
        else:
            columes = selectColumes
        sql = f"SELECT {columes} FROM {tableObject.tableName}"
        self.mycursor.execute(sql)
        myreasult = self.mycursor.fetchall()
        return myreasult
    
    def selectWhere(self, tableObject, whereList, selectColumes="*"):
        if(type(selectColumes) != str):
            columes = self.__valueInsert(selectColumes)
        else:
            columes = selectColumes
        where = self.__whereList(whereList)
        sql = f"SELECT {columes} FROM {tableObject.tableName} WHERE {where}"
        self.mycursor.execute(sql)
        myreasult = self.mycursor.fetchall()
        return myreasult

    def  __whereList(self, whereList):
        whereString = f""
        if(len(whereList) == 1):
            return f"{self.__setWhereString(whereList[0])}"
        for i, where in enumerate(whereList):
            if(i < len(whereList) -1):
                whereString = whereString + f"{self.__setWhereString(where)} AND "
            else:
                whereString = whereString + f"{self.__setWhereString(where)}"
        return whereString

    def __setWhereString(self, where):
        if(type(list(where.values())[0]) == int):
            return f"{list(where.keys())[0]}={list(where.values())[0]}"
        else:
            return f"{list(where.keys())[0]}=\'{list(where.values())[0]}\'"

    def delete(self, tableObject, whereList):
        where = self.__whereList(whereList)
        sql = f"DELETE FROM {tableObject.tableName} WHERE {where}"
        self.mycursor.execute(sql)
        self.mydb.commit()
    
    def update(self, tableObject, updateList, whereList):
        where = self.__whereList(whereList)
        update = self.__whereList(updateList)
        sql = f"UPDATE {tableObject.tableName} SET {update} WHERE {where}"
        self.mycursor.execute(sql)
        self.mydb.commit()
    
    def createDB(self, dbObject):
        try:
            sql = f"CREATE DATABASE {dbObject.dbName}"
            self.mycursor.execute(sql)
            self.__connect(dbObject.dbName)
            self.__createTables(dbObject)
        except Exception as e:
            print(log.ERROR(e))

    def  __createTables(self, dbObject):
        try:
            for table in dbObject.tablesObject:
                tableValues = table.getColumesAndValues()
                sql = "CREATE TABLE {table.tableName} {tableValues}"
                self.mycursor.execute(sql)
        except Exception as e:
            print(log.ERROR(e))
   
    @staticmethod
    def ConverteToJson(tableObject, tupleList):
        #this function will converte the output of the list of tuple of mysql
        # to json
        js = {}
        for j,tuple in enumerate(tupleList):
            line = {}
            coulumsName = tableObject.columesName
            for i, colum in enumerate(coulumsName):
                line[colum] = str(tuple[i])
            js[j] = line

        return js

    @staticmethod 
    def ConverteToTuple(json):
        #this function will converte the json obj into tuple
        lsVal = json.values()
        tp = tuple(lsVal)
        return tp
      
            
   
