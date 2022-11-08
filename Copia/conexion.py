import cx_Oracle
from datetime import datetime
import logging

def conLect():
    file = open('D:\ProLect\sql\consulta.txt', 'r')
    quuery = file.read()
    rowarray_list = []
    logging.warning('conexión base de datos!')  # will print a message to the console
    year = str(datetime.today().year)
    month = str(datetime.today().month)
    date = year + '' + month
    logging.info('consulta de base de datos!')  # will print a message to the console
    dsn_tns = cx_Oracle.makedsn('metrolinkeu-db3.crbx1lexeh51.us-east-1.rds.amazonaws.com', '1521', service_name='ORCL') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
    conn = cx_Oracle.connect(user=r'calvarado', password='Bquilla##2022', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'
    querystring = quuery
    c = conn.cursor()
    logging.info('Ejecución de query!')  # will print a message to the console
    c.execute(querystring)
    for row in c:
        rowarray_list.append(row)
    logging.info('Finalizada extracción de datos!')  # will print a message to the console
    return rowarray_list
    conn.close()