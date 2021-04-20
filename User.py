class User:
    def __init__(self,id,name,last_name,user_name,password,gender,date_of_birth,phone,speciality,user_role):
        self.id = id 
        self.name = name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password
        self.gender=gender
        self.date_of_birth=date_of_birth
        self.phone=phone
        self.speciality=speciality
        self.user_role = user_role


    def dump(self):
        return {
            'id': self.id,
            'name': self.name,
            'last_name':  self.last_name,
            'user_name': self.user_name,
            'password': self.password,
            'gender':self.gender,
            'date_of_birth':self.date_of_birth,
            'phone':self.phone,
            'speciality':self.speciality,
            'user_role':self.user_role,
        }