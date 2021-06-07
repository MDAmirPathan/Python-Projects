import pandas as pd
from pandas.core.groupby.generic import DataFrameGroupBy

def add():
    add_more = 'y'
    while add_more == 'y' or add_more =='Y':
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
        
        df = pd.read_csv('Results.csv')
        r = df.shape[0]
        data_lst = [roll,name,class_sec,father_name]
        data_lst.extend([marks for marks in marks_term1])
        data_lst.extend([marks for marks in marks_term2])
        df[r,:] = data_lst
        df.to_csv("Results.csv",index=False)  
        print("Record Added Succesfully")
        
 
        add_more = input("Do you want add more?(y/n):")
        if add_more.lower() == 'n':
            break
    
def delete():
    
    df = pd.read_csv("Results.csv")
    
    print("::::::::::Before Deletion::::::::::")
    if df.shape[0]== 0:
        print("No record found")
    else:
        print(df)
    print()
        
    idx = int(input("Enter the index to delete:"))
    df.drop(idx,axis=0,inplace =True)
    df.to_csv("Results.csv",index=False)
    
    print("::::::::::After Deletion::::::::::")
    if df.shape[0] == 0:
        print("No record found")
    else:
        print(df)
    print()
    
def search():
    df =pd.read_csv("Results.csv")
    roll = int(input("Enter the roll number:"))
    print(df[df.loc[:,'roll'] == roll])
        
def update():
    
    df = pd.read_csv("Results.csv")
    
    print("::::::::::Before Update::::::::::")
    print(df)
    print()
    
    idx = int(input("Enter the index for update:"))
    
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
    
    data_lst = [roll,name,class_sec,father_name]
    data_lst.extend([marks for marks in marks_term1])
    data_lst.extend([marks for marks in marks_term2])
    df[idx,:] = data_lst
    df.to_csv("Results.csv",index=False)  
    print("Record Updated Succesfully")
    
    print("::::::::::After Update::::::::::")
    print(df)
    print()
    
def show_data():
    df= pd.read_csv("Results.csv")
    if df.shape[0] == 0:
        print("No record found")
    else:
        print(df)
    print()
    
    
    
if __name__ =='__main__':
    print("""        CHOICES
1.To Add a Records
2. To Search a record
3.To delete a records
4.To view all the records
5.Update
6. Generate the report
    """)
    
    
    while True:
        choice = int(input("Enter the choice(1-5):"))
        if choice == 1:#insert data
            add()
        
        elif choice == 2: #search for data
            search()
        
        elif choice == 3: # delete from database
            delete()
            
        elif choice == 4:# Read  from database
            show_data()
        
        elif choice == 5:
            update()
        else:
            quit()

         