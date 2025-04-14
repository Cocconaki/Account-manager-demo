from user import User, calculate_age
from store_user import users


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
    def filter_salary_ascending():
        
        users_sorted = sorted(users, key=lambda user: user.salary)
        for user in users_sorted:
            user.show_user_data(user.user_id)

    @staticmethod
    def filter_salary_descending():
        users_sorted = sorted(users, key=lambda user: user.salary, reverse=True)
        for user in users_sorted:
            user.show_user_data(user.user_id)
    
    @staticmethod
    def filter_by_gender(users, gender):
        for user in filter(lambda u: u.gender == gender, users): user.show_user_data(user.user_id)

    @staticmethod
    def filter_by_age(users,age):
        count = 0
        for user in users:
            if calculate_age(user.dob) == age:
                count += 1
                user.show_user_data(user.user_id)
        if count == 0:
            print(f"No one at the age of {age} was found")
    
    @staticmethod
    def filter_by_age_range(bottom, top, users):
        count = 0
        for user in users:
            if bottom <= calculate_age(user.dob) <= top:
                count += 1
                user.show_user_data(user.user_id)
        if count == 0:
            print(f"No one at the range of {bottom}-{top} was found")

    @staticmethod
    def filter_age_descending(users):
        sorted_users_byage = sorted(users, key=lambda user: user.dob)
        for user in sorted_users_byage:
            user.show_user_data(user.user_id)

    @staticmethod
    def filter_age_descending(users):
        sorted_users_byage = sorted(users, key=lambda user: user.dob, reverse=True)
        for user in sorted_users_byage:
            user.show_user_data(user.user_id)

        