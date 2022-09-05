# import necessary libraries and modules
import pymysql
from app.config import mysql

# get all the usecases from the database
def get_usecases():
    """
    Function to fetch all the usecases from the database
    
    Args--> None
    
    Returns--> Usecases (List)
    """
    usecases, connection = None, None
    try:
        # establish connection with the database
        connection = mysql.connect()
        # initialize cursor object
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        # execute stored procedure to get all the usecases
        cursor.callproc('get_usecase')
        usecases = cursor.fetchall()

        # close the cursor
        cursor.close()
    except Exception as e:
        # handle execption and print the error in case of any problem
        print(e)
    finally:
        # if established close the connection
        if connection != None:
            connection.close()
    return usecases

# get all the entities and departments from the database
def get_data():
    """
    Function to fetch all the entities and departments from the database
    
    Args--> None
    
    Returns--> Entities (List), Departments (List)
    """
    entities, departments, connection = None, None, None
    try:
        # establish connection with the database
        connection = mysql.connect()
        # initialize cursor object for fetching entity list
        cursor_entity = connection.cursor(pymysql.cursors.DictCursor)
        # execute stored procedure to get all the business entities
        cursor_entity.callproc('get_entity')
        entities = cursor_entity.fetchall()
        # close the cursor
        cursor_entity.close()

        # initialize cursor object for fetching department list
        cursor_dept = connection.cursor(pymysql.cursors.DictCursor)
        # execute stored procedure to get all the departments
        cursor_dept.callproc('get_department')
        departments = cursor_dept.fetchall()
        # close the cursor
        cursor_dept.close()
    except Exception as e:
        # handle execption and print the error in case of any problem
        print(e)
    finally:
        # if established close the connection
        if connection != None:
            connection.close()
    return entities, departments

# push a usecase to the database
def insert_usecase(name, entity, department, descr):
    """
    Function to insert a usecase into the database

    Args--> name (str): Usecase Name
            entity (int): Entity ID
            department (int): Department ID
            descr (str): Usecase Description
    
    Returns--> None
    """
    connection = None
    try:
        # establish connection with the database
        connection = mysql.connect()
        # initialize cursor object
        cursor = connection.cursor()
        # execute stored procedure to insert usecase data in database
        cursor.callproc('insert_usecase',(name, entity, department, descr))
        # commit changes
        connection.commit()
        # close the cursor
        cursor.close()
        print("Usecase Uploaded Succesfully.")
    except Exception as e:
        # handle execption and rollback changes if any
        if connection != None:
            connection.rollback()
        # handle execption and print the error in case of any problem
        print(e)
    finally:
        # if established close the connection
        if connection != None:
            connection.close()

# update a usecase in the database
def update_usecase(id, name, entity, department, descr):
    """
    Function to update a usecase entry in the database

    Args--> id (int): Usecase ID
            name (str): Usecase Name
            entity (int): Entity ID
            department (int): Department ID
            descr (str): Usecase Description
    
    Returns--> None
    """
    connection = None
    try:
        # establish connection with the database
        connection = mysql.connect()
        # initialize cursor object
        cursor = connection.cursor()
        # execute stored procedure to update the usecase entry in the database
        cursor.callproc('update_usecase',(id, name, entity, department, descr))
        # commit changes
        connection.commit()
        # close the cursor
        cursor.close()
        print("Usecase Updated Succesfully.")
    except Exception as e:
        # handle execption and rollback changes if any
        if connection != None:
            connection.rollback()
        # handle execption and print the error in case of any problem
        print(e)
    finally:
        # if established close the connection
        if connection != None:
            connection.close()

# delete a usecase in the database
def delete_usecase(id):
    """
    Function to delete a usecase from the database based on usecase id

    Args--> id (int): Usecase ID
    
    Returns--> None
    """
    connection = None
    try:
        # establish connection with the database
        connection = mysql.connect()
        # initialize cursor object
        cursor = connection.cursor()
        # execute stored procedure to delete a particular usecase from the database
        cursor.callproc('delete_usecase',(id,))
        # commit changes
        connection.commit()
        # close the cursor
        cursor.close()
        print("Usecase Deleted Succesfully.")
    except Exception as e:
        # handle execption and rollback changes if any
        if connection != None:
            connection.rollback()
        # handle execption and print the error in case of any problem
        print(e)
    finally:
        # if established close the connection
        if connection != None:
            connection.close()