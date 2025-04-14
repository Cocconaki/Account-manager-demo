from store_user import *
from user import User
import os
from filter import Filter
import time

while True:
    
    flag = False
    os.system('cls')
    print("""Menu
          ______________
          1. Add user
          2. Delete user
          3. Show user data
          4. Enter filtering menu
          5. Exit program""")

    try:       
        choice = int(input(": "))
    except ValueError:
        print("Please enter a number from the list")
        flag = True
        time.sleep(2)

    match choice:
        case 1:
            os.system('cls')
            User.create_user()
        case 2:
            os.system('cls')
            userid_todel = int(input("Enter user's ID: "))
            User.delete_user(userid_todel)
        case 3:
            os.system('cls')
            userid_toshow = int(input("Enter user's ID: "))
            User.show_user_data(userid_toshow)
            input()
        case 4:

            while True:
                os.system('cls')
                print("""Menu
                        ______________
                        1. Filter by salary: 
                        2. Filter by salary range:
                        3. Filter salary ascending: 
                        4. Filter salary descending: 
                        5. Back to main menu: """)
                
                choice = int(input(": "))
                match choice:
                    case 1:
                        os.system('cls')
                        salary = int(input("Enter salary: "))
                        Filter.filter_by_salary(salary)
                        input()
                    case 2:
                        os.system('cls')
                        bottom = int(input("Bottom salary: "))
                        top = int(input("Top salary: "))
                        Filter.filter_by_salary_range(bottom, top)
                    case 3:
                        os.system('cls')
                        Filter.filter_salary_ascending()
                        input()
                    case 4: 
                        os.system('cls')
                        Filter.filter_salary_descending()
                        input()
                    
                    case 5:
                        os.system('cls')
                        print("Returning to main menu")
                        time.sleep(2)
                        break

        case 5:
            os.system('cls')
            exit = input("Are you sure you want to exit?: Y/N: ")
            
            var = "y" 
            if exit.lower() == var:
                print("Exiting")
                time.sleep(1)
                break
            else:
                continue    
        case _:

            if flag is False:
                os.system('cls')
                print("Invalid choice, please try again.")
                time.sleep(2)
            else:
                continue
                
                    
            
     
        

       
            

        