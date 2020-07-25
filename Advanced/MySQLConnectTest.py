import mysql.connector

def get_connection_sql():
    try:
        mydb = mysql.connector.connect(
            host="rtp-dbpl-mysql5",
            port="3306",
            database="osrcscan",
            user="osrcscan",
            passwd="Blackduck!234"
        )
    except mysql.connector.Error as err:
        print("In DB setup error")
        exit(err)
    return mydb


def query_db(my_query):
    try:
        print(my_query)
        mydb = mysql.connector.connect(
            host="rtp-dbpl-mysql5",
            port="3306",
            database="osrcscan",
            user="osrcscan",
            passwd="Blackduck!234"
        )
        cursor = mydb.cursor()
        #cursor = cnx.cursor()
        cursor.execute(my_query)
        result = cursor.fetchall()
        print("RES ::: ", result)
        return result
    except mysql.connector.Error as err:
        print("In connection error")
        exit(err)
    finally:
        print("In final")
        #cursor.close()

try:
    my_query = query_db("select * from queue_list")
    print(my_query)
except Exception as e:
    print("Exception :::", e)