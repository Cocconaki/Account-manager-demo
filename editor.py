
class Edit:

    @staticmethod
    def edit_user_info(user_attr, user_instance):
        
        
        
        
        user = User(first_name, 
                    last_name, 
                    role, 
                    salary, 
                    phone_number, 
                    gender=user_instance.gender, 
                    dob=user_instance.dob, 
                    email_adress=user_instance.email_adress, 
                    user_id=user_instance.user_id)

