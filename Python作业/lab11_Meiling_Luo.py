from mysql.connector import MySQLConnection, Error

from mySqlDbConfig import readDbConfig

import webbrowser


def insertGrade(firstName,lastName,province,grade):
    try:
        dbconfig = readDbConfig()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO grades (FName, LName, Province, Grade)"
            "VALUES ('{}', '{}', '{}', '{}')".format(firstName, lastName, province, grade))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def deleteGrade(firstName,lastName,province,grade):
    try:
        dbconfig = readDbConfig()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM grades WHERE FName = '{}' AND LName = '{}' AND Province = '{}' AND Grade = '{}'".format(firstName, lastName, province, grade))
        conn.commit()
    except Error as e:
        print(e)


def displayGrade(firstName, lastName, province):
    try:
        dbconfig = readDbConfig()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM grades WHERE Fname LIKE '%{}%' AND LName LIKE'%{}%' AND province LIKE'%{}%'".format(firstName, lastName, province))
        rows = cursor.fetchone()
        print("<table border='1'>")
        while rows is not None:
            print("<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(rows[0], rows[1], rows[2], rows[3]))
            rows = cursor.fetchone()
        print("</table>")
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()



while True:
        print("\n"
              "1.Insert a grade\n"
              "2.Display a grade \n"
              "3.Delete a grade\n"
              "0.Exit\n"
             )
        try:
            choice = int(input())
            if choice in range(0, 4):
                if choice == 1:
                    firstName = input("Please enter first Name:")
                    lastName = input("Please enter last Name:")
                    province = input("Please enter province:")
                    grade = input("Please enter grade:")
                    insertGrade(firstName, lastName, province, grade)
                    print("The grade has been inserted.")
                    continue
                if choice == 2:
                    firstName = input("Please enter first Name:")
                    lastName = input("Please enter last Name:")
                    province = input("Please enter province:")
                    action = displayGrade(firstName, lastName, province)
                    continue
                if choice == 3:
                    firstName = input("Please enter first Name:")
                    lastName = input("Please enter last Name:")
                    province = input("Please enter province:")
                    grade = input("Please enter grade:")
                    action = deleteGrade(firstName, lastName, province, grade)
                    print("The grade has been deleted")
                    continue
                else:
                    print("THANK YOU")
                    break
            else:
                print("Please enter a number between 0 and 3.")
        except ValueError:
            print("Please enter a valid number.")