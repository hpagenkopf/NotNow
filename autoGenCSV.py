"""
Author @HannaPagenkopf
Feb 13, 2021

autoGenCSV is a program that autogenerates two .csv files
that contain information intended to be used inside of a fictional SQL database

The two .csv collections are donorList and emoloyeeList.
They both contain the following information for a prespecified number of people
donorList: DonorID, FirstName, LastName, Phone, Address, City, State, Zip
emoloyeeList: EmployeeID, FirstName, LastName, Phone, Address, City, State, Zip

Notes about this code:
    It could be made more efficient by rearanging when a csv file is created and
    lines are added to the file. 
    There are limited values for states, zipcodes, and phone area codes
    that could be expanded upon. 
    

"""

#---------------Libraries to be used in program---------------#
import names
import csv
import os.path
import pandas as pd
import os
import random
from faker import Faker

#---------------Values to be used in program---------------#
faker = Faker()
#donorNum is number of donors
donorNum = 20
#employNum is number of employees
employNum = 6
#Path to file, this is computer specific
path = r'C:/Users/owner/.spyder-py3/Matt' 

#---------------Functions relating to CSV---------------#
def addtoCSV(csv_File, data_Tuple):
    """
    Add data_Tuple information to an existing csv

    Parameters
    ----------
    csv_File : TYPE
        name of csv file and file path
    data_Tuple : TYPE
        collection of data about a person
        

    Returns
    -------
    None.

    """
    append_list_as_row(csv_File, data_Tuple)     
    #print("value added to existing CSV")
    
def newCSV(csv_File, df):
    """
    Parameters
    ----------
    csv_File : TYPE
        name of csv file and file path        
    df : TYPE
        Labels associated with the data entered along with random persons information in [1x8] format

    Returns
    -------
    None.

    """
    #opening the new file and creating the list       
    with open(csv_File, 'w'):
        df.to_csv(csv_File, index=False) 
        
def append_list_as_row(file_name, data_tuple): 
    """
    appends list to existing csv
    
    Parameters
    ----------
    file_name : TYPE
        
    data_tuple : TYPE
        collection of data about a person
        

    Returns
    -------
    None.

    """
    with open(file_name, 'a+', newline='') as csvfile:
    # Create a writer object from csv module
        csv_writer = csv.writer(csvfile)
    # Add contents of list as last row in the csv file
        csv_writer.writerow(data_tuple)

def addData(csv_File, data_Tuple, df):
    """
    Check if a file already exists, otherwise add new line

    Parameters
    ----------
    csv_File : TYPE
        name of csv file and file path
    data_Tuple : TYPE
        collection of data about a person
    df : TYPE
        Labels associated with the data entered along with random persons information in [1x8] format

    Returns
    -------
    None.

    """
    if os.path.exists(os.path.expanduser(csv_File)) == True:  
        #if there is a path there
         addtoCSV(csv_File, data_Tuple)
         print("csv data added")
    else:
        #create a new csv if it is not there 
        newCSV(csv_File, df)
        print("newCSV created")
        
#---------------Functions about generating data---------------#

def random_phone_num_generator(State):
    """
    randomly generates a phone number, with specific area codes

    Parameters
    ----------
    State : str
        State is used to assign phone area code

    Returns
    -------
    str representing a phone number
        a string representing a random phone number

    """
    if State == 'Idaho':
        first = 208
    elif State == 'Oregon':
        first = 458    
    #else:
        #this could be used for a random area code
        #first = str(random.randint(100, 999))
    second = str(random.randint(1, 888)).zfill(3)
    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))
    #returns the random generated phone number
    return '{}-{}-{}'.format(first, second, last)
    
def pickAState():
    """
    randomly chooses between Idaho and Oregon for a state

    Returns
    -------
    State : str
        Either 'Idaho' or 'Oregon'

    """
    x = bool(random.getrandbits(1))
    if x == 1:
        State = 'Idaho'
    else:
        State = 'Oregon'
    return State

def pickACity(State):
    """
    Sets a value for city and zip
    This is a very small list with only two cities per state
    One zip for each city

    Parameters
    ----------
    State : str
        Takes in assigned state

    Returns
    -------
    City : str
        Random City chosen based off state
    Zip : str
        Zip code assigned based on city

    """
    if  State == 'Idaho':
        #random city and zip for idaho
        x = bool(random.getrandbits(1))
        if x == 1:
            City = 'Boise'
            Zip = '83705'
        else:
             City = 'Hagerman'
             Zip = '83332'
    else:
        #random city and zip for idaho
        x = bool(random.getrandbits(1))
        if x == 1:
            City = 'Eugene'
            Zip = '97401'
        else:
             City = 'Salem' 
             Zip = '93701'
    return City, Zip
    
def donorGeneration(donorNum):
    """
    Randomly assigns values for a dataStructure containing:
    DonorID,FirstName,LastName,Phone,Address,City,State,Zip
    Creates or Adds data to a .csv

    Parameters
    ----------
    donorNum : int
        The number of employees preset in the begining of the code

    Returns
    -------
    None.

    """
    i = 1
    
    while i <= donorNum:
        
        #create formated DonorID starting at 5000 in sequential order
        num = 5000 + i
        converted_num = f'{num}'
        DonorID = str('0' + converted_num)
        
        State = pickAState()
        FirstName, LastName, Phone, Address, City, Zip = randomInfo(State)
        
        #creating the data frame and appropriate data
        row_contens = [DonorID,FirstName,LastName,Phone,Address,City,State,Zip]
        data_Tuple = tuple(row_contens)
        df = pd.DataFrame([data_Tuple], columns = ['DonorID','FirstName','LastName','Phone','Address','City','State','Zip'])
        
        #Naming of the file is 'donorList'
        csv_File = os.path.join(path, 'donorList')
    
        #either adding new person to a CSV or making a new file and adding it
        addData(csv_File, data_Tuple, df)
        
        #starts over generating/adding new person
        i = i+1

def employeeGeneration(employNum):
    """
    Randomly assigns values for a dataStructure containing:
    EmployeeID,FirstName,LastName,Phone,Address,City,State,Zip
    Creates or Adds data to a .csv

    Parameters
    ----------
    employNum : int
        The number of employees preset in the begining of the code

    Returns
    -------
    None.

    """

    j = 1
    
    while j <= employNum:
        #random generating employeeID
        EmployeeID = (str(random.randint(100, 999)).zfill(3))
        State = 'Idaho' #Employees all have the same state
        FirstName, LastName, Phone, Address, City, Zip = randomInfo(State)
        
        #creating the data frame and appropriate data
        row_contens = [EmployeeID,FirstName,LastName,Phone,Address,City,State,Zip]
        data_Tuple = tuple(row_contens)
        df = pd.DataFrame([data_Tuple], columns = ['EmployeeID','FirstName','LastName','Phone','Address','City','State','Zip'])
        
        #Naming of the file is 'employeeList'
        csv_File = os.path.join(path, 'employeeList')
    
        #either adding it to a CSV or making a new one
        addData(csv_File, data_Tuple, df)
        
        #starts over generating/adding new person
        j = j+1

def randomInfo(State):
    """
    Auto generates values for a fictional person

    Parameters
    ----------
    State : str
        Takes in assigned state

    Returns
    -------
    FirstName : str
        Random first name
    LastName : str
        Random last name
    Phone : str
        Phone number with area code dependant on state
    Address : str
        Random address generated useing faker library
    City : str
        City generated based on state
    Zip : str
        Zipcode generated based on city
        This list is very limited

    """
    FirstName = names.get_first_name()
    LastName = names.get_last_name()
    Phone = random_phone_num_generator(State)
    Address = faker.street_address()
    City, Zip = pickACity(State)
    return FirstName, LastName, Phone, Address, City, Zip

def generateCSV(): 
    #Generates two .csv files
    donorGeneration(donorNum)
    employeeGeneration(employNum)

def main():
    generateCSV()

if __name__ == "__main__":
    main()
    




