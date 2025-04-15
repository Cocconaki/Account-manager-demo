from store_user import *
from datetime import date, datetime

def calculate_age(dob):
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age


class User:

    def __init__(self, first_name, last_name, dob, gender, role, salary, phone_number, email_adress, user_id):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.gender = gender
        self.role = role
        self.salary = salary
        self.email_adress = email_adress
        self.phone_number = phone_number
        self.user_id = user_id
    
    @property
    def age(self):
        return calculate_age(self.dob)
    
    def __str__(self):
        return (f"User: {self.first_name} {self.last_name}\n"
                f"ID: {self.user_id}\n"
                f"Age: {self.age}\n"
                f"Gender: {self.gender}\n"
                f"Role: {self.role}\n"
                f"Salary: ${self.salary:,.2f}\n"
                f"Email: {self.email_adress}\n"
                f"Phone: {self.phone_number}")
    
    @classmethod
    def show_user_data(cls, user_id_show):
        for user in users:
            if user.user_id == user_id_show:
                print(f"User: {user.first_name} {user.last_name}\n"
                        f"ID: {user.user_id}\n"
                        f"Age: {user.age}\n"
                        f"Gender: {user.gender}\n"
                        f"Role: {user.role}\n"
                        f"Salary: ${user.salary:,.2f}\n"
                        f"Email: {user.email_adress}\n"
                        f"Phone: {user.phone_number}")
                return
        print("User not found")
    
    @classmethod
    def create_user(cls):
                first_name = str(input("Enter first name: "))
                last_name = str(input("Enter last name: "))

                while True:
                    try:
                        dob = datetime.strptime(input("Enter date of birth (YYYY-MM-DD): "), "%Y-%m-%d").date()
                        break
                    except ValueError:
                        print("Invalid format, please try again.")
                while True:
                    
                    genders = ["male", "female"]
                    gender = str(input("Enter gender: (Male or Female)"))
                    if gender.lower() not in genders:
                        print("Invalid gender, please try again.")
                    elif gender.lower() in genders:
                        break
                
                role = str(input("Enter users role: "))
                while True:
                    try:
                        salary = int(input("Enter users salary: (USD)"))
                        break
                    except ValueError:
                        print("Please enter a number!")
                phone_number = str(input("Enter phone number: "))

                def generate_id():
                    if len(taken_ids) == 0:
                        taken_ids.append(1)
                        return 1
                    else:
                        if len(deleted_ids) == 0:
                            user_id = max(taken_ids) + 1
                            taken_ids.append(user_id)
                            return user_id
                        else:
                            user_id = deleted_ids.pop()  
                            taken_ids.append(user_id)
                            return user_id

                
                generated_id = generate_id()
                
                def generate_work_email():
                
                    if len(user_email_adress_ids) == 0:
                        user_email_adress_ids.append(1)
                        company_email = f"{first_name.lower()}1{last_name.lower()}@aswomecompany.com"
                        return company_email
                        
                    else: 
                        code = user_email_adress_ids[-1] + 1
                        user_email_adress_ids.append(code)
                        company_email = f"{first_name.lower()}{code}{last_name.lower()}@aswomecompany.com"
                        return company_email
                    
                
                
                generated_email = generate_work_email()

                user = User(first_name, last_name, dob, gender, role, salary, phone_number, email_adress=generated_email, user_id=generated_id)
                users.append(user)
    
    @classmethod
    def delete_user(cls, user_id_del):
        
        for user in users:
            if user.user_id == user_id_del:
                print(f"User number {user.user_id} was deleted")
                users.remove(user)
                taken_ids.remove(user_id_del)
                deleted_ids.append(user_id_del)

            else:
                print(f"User with id:{user_id_del} not found ")
    
    @classmethod
    def edit_user_data(cls):
        pass

  

 



