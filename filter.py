from user import calculate_age, User
from store_user import users
import os
import time


class Filter:

    @staticmethod
    def filter_by_salary(salary):
        flag = False
        for user in users:
            if user.salary == salary:
                flag = True
                user.show_user_data(user.user_id)
        if flag is False:
            print(f"No employee with {salary} salary was found")
    
    @staticmethod
    def filter_by_salary_range(start, stop):
        
        count = 0
        for user in users:
            if start <= user.salary <= stop:
                user.show_user_data(user.user_id)
                count += 1
                print("_______________________")
        if count == 0:
            print("There are no salaries in this range.")

    
    
    @staticmethod
    def filter_salary_desc_asc(order="asc"):
        reverse = True if order == "desc" else False
        users_sorted = sorted(users, key=lambda user: user.salary, reverse=reverse)
        for user in users_sorted:
            user.show_user_data(user.user_id)
    
    
    @staticmethod
    def filter_by_gender(gender):
        os.system('cls')
        genders = ['male', 'female']
        while True:
            if gender.lower() not in genders:
               print("Enter a valid gender")
               time.sleep(1)
            else:
                 break
        os.system('cls')
        found = False
        for user in users:
            if user.gender == gender:
                found = True
                user.show_user_data(user.user_id)
        if found == False:
            print("No one was found")
        input()
       

    @staticmethod
    def filter_by_age(age):
        count = 0
        for user in users:
            if calculate_age(user.dob) == age:
                count += 1
                user.show_user_data(user.user_id)
        if count == 0:
            print(f"No one at the age of {age} was found")
    
    @staticmethod
    def filter_by_age_range(bottom, top):
        count = 0
        for user in users:
            if bottom <= calculate_age(user.dob) <= top:
                count += 1
                user.show_user_data(user.user_id)
        if count == 0:
            print(f"No one at the range of {bottom}-{top} was found")

    @staticmethod
    def filter_age_des_asc(order = "asc"):
        reverse = True if order == "desc" else False
        sorted_users_byage = sorted(users, key=lambda user: user.dob, reverse=reverse)
        for user in sorted_users_byage: 
            user.show_user_data(user.user_id)
 
        
       

         