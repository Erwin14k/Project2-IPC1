from User import User
import json 
from datetime import datetime

class User_DAO:
    def __init__(self):
        self.users = []
        self.id_counter = 0
        self.coincidences = 0
        self.user_name_temp=""
        self.id_temp=99999
        self.role_temp=""

#Función que nos indica el usuario en base a su id
    def user_by_id(self,id):
        for user in self.users:
            if user.id == int(id):
                return user.dump()
        return {}

#Función que nos devuelve el rol que tiene el usuario
    def get_user_role_by_username(self,user_name):
        for user in self.users:
            if user.user_name == user_name:
                return user.user_role
        return False

#Función que nos devuelve el usuario en base su id
    def get_user_by_id(self,id):    
        for user in self.users:
            if user.id == int(id):
                return user
        return False

    def coincidence_of_user_name(self,username):
        for user in self.users:
            if user.user_name==username:
                self.coincidences += 1
                if self.coincidences==0:
                    return True

#Función que nos devuelve el nombre y apellido del usuario en base a su id
    def get_name_of_user_by_id(self,id):    
        for user in self.users:
            if user.id == int(id):
                return user.name+" "+user.last_name
        return False

    def get_name_of_user_by_user_name(self,user_name):    
        for user in self.users:
            if user.user_name == user_name:
                return user.name+" "+user.last_name
        return False

#Función que nos devuelve el id del usuario en base a su nombre de usuario
    def get_id_by_username(self,username):   
        for user in self.users:
            if user.user_name == username:
                return int(user.id)
        return False

#Función que valida los datos de inicio de sesión
    def login_validation(self,user_name,password):
        for user in self.users:
            if user.user_name == user_name and user.password == password:
                print("Se inicio sesión exitosamente para el usuario: "+user.user_name)
                self.user_name_temp=user.user_name
                self.id_temp= user.id
                self.role_temp=user.user_role
                return True
        print("Usuario o contraseña incorrectos, intente de nuevo")
        
        return False
    
#Función para eliminar usuarios(enfermeras, doctores o pacientes)
    def delete_user(self,id):
        for user in self.users:
            if user.id == int(id):
                print(f'El usuario: "{user.user_name}" ha sido eliminado con éxito')
                self.users.remove(user)
                return True
        print(f'El usuario con id: "{ id }" no ha sido encontrado.')
        return False
    
    #Función para actualizar datos de cualquier usuario (Paciente, Doctor, enfermera)
    def update_user(self,id , name ,last_name ,user_name ,password ,date_of_birth):
        for user in self.users:
            if user.user_name != user_name :
                self.coincidences=0
                if user.id==int(id):
                    #if self.coincidences==0 or self.coincidences==1:
                    print("hola-------------------------------")
                    user.name = name
                    user.last_name = last_name
                    user.user_name = user_name
                    user.password = password
                    user.date_of_birth = date_of_birth
                    print("Se han actualizado con éxito los datos para el paciente con el id: "+str(id))
                    self.coincidences=0
                    return True
            elif user.user_name == user_name :
                self.coincidences+=1
                if user.id==int(id):
                    if self.coincidences==0:
                        print("hola-------------------------------")
                        user.name = name
                        user.last_name = last_name
                        user.user_name = user_name
                        user.password = password
                        user.date_of_birth = date_of_birth
                        print("Se han actualizado con éxito los datos para el paciente con el id: "+str(id))
                        self.coincidences=0
                        return True
        return False


    """def update_user2(self,id , name ,last_name ,username ,password ,date_of_birth):
        self.coincidences=0
        for user in self.users:
            if user.id==int(id) and user.user_name==username:
                print("hola-------------------------------")
                user.name = name
                user.last_name = last_name
                user.password = password
                user.date_of_birth = date_of_birth
                print("Se han actualizado con éxito los datos para el paciente con el id: "+str(id))
                return True
            elif user.id==int(id) and user.user_name != username:
                if (User_DAO.coincidence_of_user_name(username)):
                    print("hola-------------------------------")
                    user.name = name
                    user.last_name = last_name
                    user.user_name = username
                    user.password = password
                    user.date_of_birth = date_of_birth
                    print("Se han actualizado con éxito los datos para el paciente con el id: "+str(id))
                    self.coincidences=0
                    return True
            self.coincidences=0
            return False"""


#Función para crear nuevos admin(Esta función solo se utilizará una vez ya que solo hay un admin)
    def new_admin(self,name,last_name,user_name,password,gender,date_of_birth,phone):
        for user in self.users:
            if user.user_name == user_name:
                print('El nombre de usuario ya existe, intente de nuevo')
                return False
        new = User(self.id_counter,name,last_name,user_name,password,gender,date_of_birth,phone,"Administrador","admin")
        self.users.append(new)
        self.id_counter += 1
        print("Se creo un nuevo admin")
        return True

#Función para crear nuevos pacientes
    def new_patient(self,name,last_name,user_name,password,gender,date_of_birth,phone):
        for user in self.users:
            if user.user_name == user_name:
                print('El nombre de usuario ya existe, intente de nuevo')
                return False
        new = User(self.id_counter,name,last_name,user_name,password,gender,date_of_birth,phone,"Paciente","patient")
        self.users.append(new)
        self.id_counter += 1
        print("Se creo un nuevo paciente")
        return True

#Función que devuelve todos los usuarios excepto el admin
    def id_of_all_users_except_admin(self):
        return json.dumps([User.dump() for User in self.users if User.id != 0  ])

#Función que devuelve todos los usuarios en base a su rol 
    def get_users_by_role(self,role):
        return json.dumps([User.dump() for User in self.users if User.user_role == role  ]) 

#Función que devuelve todos los datos de un usuario en base a su id 
    def get_user_data_by_id(self,id):
        return json.dumps([User.dump() for User in self.users if User.id == int(id)  ]) 



    

#Función para crear nuevos doctores
    def new_doctor(self,name,last_name,user_name,password,gender,date_of_birth,speciality,phone):
        for user in self.users:
            if user.user_name == user_name:
                print('El nombre de usuario ya existe, intente de nuevo')
                return False
        new = User(self.id_counter,name,last_name,user_name,password,gender,date_of_birth,phone,speciality,"doctor")
        self.users.append(new)
        self.id_counter += 1
        print("Se creo un nuevo doctor")
        return True



    

#Función para crear nuevas enfermeras
    def new_nurse(self,name,last_name,user_name,password,gender,date_of_birth,phone):
        for user in self.users:
            if user.user_name == user_name:
                print('El nombre de usuario ya existe, intente de nuevo')
                return False
        new = User(self.id_counter,name,last_name,user_name,password,gender,date_of_birth,phone,"Enfermera","nurse")
        self.users.append(new)
        self.id_counter += 1
        print("Se creo una nueva enfermera")
        return True


