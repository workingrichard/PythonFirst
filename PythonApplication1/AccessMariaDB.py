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


#def main():
#    pass

#if __name__ == '__main__':
#    main()

def ReadURLTask():
    config = {
        'user': 'root'
    }
    #conn= mysql.connector.connect(**config)
    conn = mysql.connector.MySQLConnection(user = 'root', pass = '12345', host = 'localhost', database = 'test')



    return
