
import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection(host_name,user_name,user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password
        )
        print("Database Connected Succesfully")
    except Error as e:
        print(f'Error: {e}')
        
    return connection


def create_db_connection(host_name,user_name,password,db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = password,
            database = db_name
        )
        print(f'Database {db_name} Connected Succesfully')
    except Error as e:
        print(f'Error: {e}')
        
    return connection
    


def create_database(connection,query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database Created Succesful")
    except Error as e:
        print(f'Error {e}')
        
def execute_query(connection,query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('Query Exceuted Succesfully')
    except Error as e:
        print(f'Error {e}' )
    
def read_query(connection,query):
    cursor = connection.cursor()
    results = None
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except Error as e:
        print(f'Error {e}')
        


def insert(connection):
    roll  = int(input("Enter the roll:"))
    name = input("Enter the name:")
    class_sec = input("Enter the Class & Sec:")
    father_name= input("Enter the Father name:")
    

    
    marks_term1 = []
    print("MARKS OF TERM I")
    marks_term1.append(int(input('Enter the marks Accounts:')))
    marks_term1.append(int(input('Enter the marks Economics:')))
    marks_term1.append(int(input('Enter the marks English:')))
    marks_term1.append(int(input('Enter the marks Business:')))
    marks_term1.append(int(input('Enter the marks IP:')))

    marks_term2 = []
    print("MARKS OF TERM II")
    marks_term2.append(int(input('Enter the marks Accounts:')))
    marks_term2.append(int(input('Enter the marks Economics:')))
    marks_term2.append(int(input('Enter the marks English:')))
    marks_term2.append(int(input('Enter the marks Business:')))  
    marks_term2.append(int(input('Enter the marks IP:')))
    
    insert_values = f"""INSERT INTO student_info VALUES ({roll},
    "{name}",
    "{class_sec}",
    "{father_name}",
    {marks_term1[0]},{marks_term1[1]},{marks_term1[2]},{marks_term1[3]},{marks_term1[4]},
    {marks_term2[0]},{marks_term2[1]},{marks_term2[2]},{marks_term2[3]},{marks_term2[4]});"""
    execute_query(connection,insert_values)


def delete(connection):
    roll_num = int(input("Enter the roll number for deletion:"))
    delete_data = f"""DELETE FROM student_info WHERE Roll_Id = {roll_num}"""
    execute_query(connection,delete_data)


def convert_to_dataframe(results):
    
    
    columns_list=['Roll_Id', 'Name', 'Class_Sec', 'Father_Name', 'Acc1', 'Eco1', 'Eng1', 'B1', 'IP1', 'Acc2', 'Eco2', 'Eng2', 'B2', 'IP2']
    print()
    df = pd.DataFrame(results,columns=columns_list)
    print(df)
    print()
    
    return df


def update_record(connection,df):
    index_to_modify = int(input("Enter the index to be modified:"))
    #print(df.loc[index_to_modify,"Roll_Id"])
    roll  = int(input("Enter the roll:"))
    name = input("Enter the name:")
    class_sec = input("Enter the Class & Sec:")
    father_name= input("Enter the Father name:")
    
    
    marks_term1 = []
    print("MARKS OF TERM I")
    marks_term1.append(int(input('Enter the marks Accounts:')))
    marks_term1.append(int(input('Enter the marks Economics:')))
    marks_term1.append(int(input('Enter the marks English:')))
    marks_term1.append(int(input('Enter the marks Business:')))
    marks_term1.append(int(input('Enter the marks IP:')))

    marks_term2 = []
    print("MARKS OF TERM II")
    marks_term2.append(int(input('Enter the marks Accounts:')))
    marks_term2.append(int(input('Enter the marks Economics:')))
    marks_term2.append(int(input('Enter the marks English:')))
    marks_term2.append(int(input('Enter the marks Business:')))  
    marks_term2.append(int(input('Enter the marks IP:')))
    update_query = f"""UPDATE student_info SET
    Roll_Id = {roll},
    Name = "{name}",
    Class_Sec="{class_sec}",
    Father_Name="{father_name}",
    Acc1= {marks_term1[0]},
    Eco={marks_term1[1]},
    Eng1 ={marks_term1[2]},
    B1={marks_term1[3]},
    IP1 ={marks_term1[4]},
    Acc2 ={marks_term2[0]},
    Eco2 ={marks_term2[1]},
    Eng2= {marks_term2[2]},
    B2 ={marks_term2[3]},
    IP2 ={marks_term2[4]}
    WHERE Roll_Id = {df.loc[index_to_modify,"Roll_Id"]}
    """
    
    execute_query(connection ,update_query)

    

    

if __name__ == "__main__":
    print("""        CHOICES
1.To Add a Records
2. To Search a record
3.To delete a records
4.To view all the records
5.Update
    """)
    connection = create_db_connection('localhost','root','nitinmadass','student_repo')
    #create_database_query = "CREATE DATABASE Student_Repo"
    #create_database(connection,create_database_query)
    
    create_table_student_info = """
    CREATE TABLE Student_info(
        Roll_Id INT PRIMARY KEY,
        Name VARCHAR(20) NOT NULL,
        Class_Sec VARCHAR(10) NOT NULL,
        Father_Name VARCHAR(20) NOT NULL,
        Acc1 INT DEFAULT 0,
        Eco1 INT DEFAULT 0,
        Eng1 INT DEFAULT 0,
        B1 INT DEFAULT 0,
        IP1 INT DEFAULT 0,
        Acc2 INT DEFAULT 0,
        Eco2 INT DEFAULT 0,
        Eng2 INT DEFAULT 0,
        B2 INT DEFAULT 0,
        IP2 INT DEFAULT 0
    
        )"""
    

    #execute_query(connection,create_table_student_info)
    while True:
        choice = int(input("Enter the choice(1-5):"))
        if choice == 1:#insert data
            insert(connection)
        
        elif choice == 2: #search for data
            
            roll_num = int(input("Enter the roll number:"))
            search_query = f"SELECT * FROM student_info WHERE Roll_Id = {roll_num};"
            results = read_query(connection ,search_query)
            convert_to_dataframe(results)
        
        elif choice == 3: # delete from database
            delete(connection)
            
        elif choice == 4:# Read  from database
            retrieve = "SELECT * FROM student_info;"
            results = read_query(connection,retrieve)
            df = convert_to_dataframe(results)
        elif choice == 5:
            print(":::::Before Update:::::")
            retrieve = "SELECT * FROM student_info;"
            results = read_query(connection,retrieve)
            df = convert_to_dataframe(results)
            
            update_record(connection,df)
        
        else:
            quit()

        
    
    
    
    
    





