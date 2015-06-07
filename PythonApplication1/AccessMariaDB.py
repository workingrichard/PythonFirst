#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Richard
#
# Created:     06/06/2015
# Copyright:   (c) Richard 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import mysql.connector
#from mysql.connector import (connection)
#import MySQLdb

#def main():
#    pass

#if __name__ == '__main__':
#    main()

def ReadURLTask():

    conn = mysql.connector.MySQLConnection(user = 'root', password = '12345', host = 'localhost', database = 'mytask')
    cursor = conn.cursor()
    cursor.execute("select version();")
    data = cursor.fetchone()
    print("DB version: " + data[0])

    cursor.execute("select * from urltask")
    for x in cursor.fetchall():
        for y in x:
            print(y)

    cursor.execute("select id, url from urltask")
    for (id, url) in cursor:
        print(str(id) + " : " + url)
    
    conn.close()

    return
