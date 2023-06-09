# import psycopg2


# def DataUpdate(name_entry, phone_number_entry, account_number_entry):
#     '''
#     Pushes Descriptive Analytics Data to the Database
#     '''
#     db = psycopg2.connect(
#                 host="localhost",
#                 # port="5432",
#                 database="data",
#                 user="postgres",
#                 password="admin@!123"
#                 )

#     mycursor = db.connect()
    
#     postgres_insert_query = """INSERT INTO rasainfo(name,phone_number,account_number) VALUES (%s,%s,%s);""".format(name_entry,phone_number_entry, account_number_entry)
    
#     mycursor.execute(postgres_insert_query)
    
#     db.commit()

#     print("Record inserted successfully into table")



import mysql.connector

# from getpass import getpass
def DataUpdate(name_entry, phone_number_entry, account_number_entry):

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="pass123",
        database="rasa"

    )

    mycursor = mydb.cursor()
    sql = "CREATE TABLE customers(name VARCHAR(255), phone_number INT, account_number);"
    # sql= 'INSERT INTO customers (name, phone_number, account_number) VALUES ("{0}","{1}", "{2}");'.format(name_entry,phone_number_entry, account_number_entry)
    mycursor.execute(sql)

    mydb.commit()

    print("Record inserted successfully into table")

if __name__=="__main__":
    DataUpdate("hari", "9899999999", "12222222")    
