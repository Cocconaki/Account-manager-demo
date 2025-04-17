from store_user import *
from user import User

class Edit:
    
    @staticmethod
    def get_user_info(user_to_edit):
        while True:
                
                if not isinstance(user_to_edit, int):
                    print("Invalid format, please try again.")
                    continue
                

                if user_to_edit not in taken_ids:
                    print(f"ID {user_to_edit} not found.")
                    again = input("Want to try again? (y/n): ").strip().lower()
                    if again != "y":
                        break  
                    else:
                        continue  
                else:
                    print("""What do you want to edit?
                            1. First name
                            2. Last name
                            3. Role
                            4. Salary
                            5. Phone number""")
                    key = int(input("Enter: "))
                    break
        
        keys = {1:"first_name", 2:"last_name", 3:"role", 4:"salary", 5:"phone_number"}
        choice = None
        if key in keys:
            choice = keys[key]

        user_instance = next((user for user in users if user.user_id == user_to_edit), None) #we need this
       
        
        return user_instance, choice
    
    @staticmethod
    def edit_user_info(get_user_info):
        user_instance, choice = get_user_info()
        for attr, value in user_instance.__dict__.items():
            if attr == choice:
                new_value = input("Enter new value: ")
                setattr(user_instance, attr, new_value)
                break  
        return user_instance
    
    @staticmethod
    def replace_user(edit_user_info, get_user_info):
        old_instance = get_user_info()
        new_instance = edit_user_info()

        for i, user in enumerate(users):  
            if user.user_id == old_instance.user_id:
                users[i] = new_instance  
                break  



   

            
            
         
