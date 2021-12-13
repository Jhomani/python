from mysql.connector import Error, connect
from mysql.connector.connection import MySQLConnection, MySQLCursor

from pyspeach.src.utils import formatResDict

class ConnectSQL:
  __connection: MySQLConnection
  __cursor: MySQLCursor
  __creadentials = {}

  def __init__(self, user: str, pss: str, db: str):
    self.__creadentials = {
      'host':'localhost',
      'database': db,
      'user': user,
      'password': pss,
      'port': 3306,
    }

    try:
      self.__connection = connect(**self.__creadentials)
    except Error as error:
      print("Error while connecting to MySQL", error)

  def connect(self):
    try:
      self.__connection.reconnect()
      self.__cursor = self.__connection.cursor()
    except Error as error:
      print("Error while reconnect to MySQL", error)

  def disconnect(self):
    if self.__connection.is_connected():
      self.__connection.close()
      self.__cursor.close()


  def getById(self, key: int, table: str):
    res = None

    try:
      self.connect()

      sqlQuery = f'SELECT * FROM {table} WHERE id={key} LIMIT 10'

      self.__cursor.execute(sqlQuery)
      record = self.__cursor.fetchone()
      if record is not None:
        colNames = self.__cursor.column_names
        res = formatResDict(colNames, record)

    except Error as e:
      print("Error while runing to MySQL", e)
    else:
      self.disconnect()

    return res

  def deleteById(self, key: int, table: str) -> bool:
    res = False

    try:
      self.connect()

      sqlQuery = f'DELETE FROM {table} WHERE id={key}'

      self.__cursor.execute(sqlQuery)
      self.__connection.commit()

      if self.__cursor.rowcount > 0: 
        res = True 

    except Error as e:
      print("Error while runing to MySQL", e)
    else:
      self.disconnect()

    return res

  def updateById(self, key: int, table: str, field: str, toVal): 
    res = False

    try:
      self.connect()

      toVal = f"'{toVal}'" if isinstance(toVal) == str else toVal

      sqlQuery = f'''
        UPDATE {table} SET {field}={toVal} 
        WHERE id={key}
      '''

      self.__cursor.execute(sqlQuery)
      self.__connection.commit()

      print(self.__cursor.rowcount, self.__cursor.statement)

      if self.__cursor.rowcount > 0:
        res = True 
    except Error as e:
      print("Error while runing to MySQL", e)
    else:
      self.disconnect()

    return res
