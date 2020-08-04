import mysql.connector


class DBClass:
    def __init__(self, host, username, password, dbname):
        self.__dbname = dbname
        self.__mydb = mysql.connector.connect(
            host=host,
            user=username,
            passwd=password,
            database=dbname
        )

    def selectQuery(self, table):
        mycursor = self.__mydb.cursor()
        mycursor.execute("SELECT * FROM " + table)
        return mycursor.fetchall()

    def countrySort(self, table, country="Any"):
        mycursor = self.__mydb.cursor()
        if country == "Any":
            print("Any")
            mycursor.execute("SELECT * FROM " + table)
        else:
            mycursor.execute("SELECT * FROM " + table + " WHERE country=" +"'" + country + "'")
        return mycursor.fetchall()

#SELECT distinct country FROM `customers` ORDER by country
    def countryList(self):
        mycursor = self.__mydb.cursor()
        mycursor.execute("SELECT distinct country FROM customers ORDER by country")
        return mycursor.fetchall()

    def uniqueColumn(self, table, column):
        mycursor = self.__mydb.cursor()
        mycursor.execute("SELECT distinct "+column+" FROM "+table+" ORDER by " +column)
        return mycursor.fetchall()



