from User import User


class User_DAO:
    def __init__(self):
        self.users = []
        self.id_counter = 0
        user_name_temp=""
        id_temp=""
        role_temp=""

#Función que nos indica el usuario en base a su id
    def user_by_id(self,id):
        for user in self.usuarios:
            if user.id == id:
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
            if user.id == id:
                return user
        return False

#Función que valida los datos de inicio de sesión
    def login_validation(self,user_name,password):
        for user in self.users:
            if user.user_name == user_name and user.password == password:
                print("Se inicio sesión exitosamente para el usuario: "+user.user_name)
                user_name_temp=user.user_name
                id_temp= user.id
                return True
        print("Usuario o contraseña incorrectos, intente de nuevo")
        
        return False
    
#Función para eliminar usuarios(enfermeras, doctores o pacientes)
    def delete_user(self,id):
        for user in self.users:
            if user.id == id:
                print(f'El usuario: "{user.user_name}" ha sido eliminado con éxito')
                self.users.remove(user)
                return True
        print(f'El usuario con id: "{ id }" no ha sido encontrado.')
        return False

#Función para crear nuevos admin(Esta función solo se utilizará una vez ya que solo hay un admin)
    def new_admin(self,name,last_name,user_name,password,gender,date_of_birth,phone):
        for user in self.users:
            if user.user_name == user_name:
                print('El nombre de usuario ya existe, intente de nuevo')
                return False
        new = User(self.id_counter,name,last_name,user_name,password,gender,date_of_birth,phone,"Paciente","patient")
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

#Función para actualizar datos de pacientes
    def update_patient(self,id , name ,last_name ,user_name ,password ,date_of_birth):
        for user in self.users:
            if user.user_role=="patient" and user.id==id:
                if user.user_name == user_name :
                    print('El nombre de usuario ya existe, intente de nuevo')
                    return False
                user.name=name
                user.last_name=last_name
                user.user_name=user_name
                user.password=password
                user.date_of_birth=date_of_birth
                return True

    

#Función para crear nuevos doctores
    def new_doctor(self,name,last_name,user_name,password,gender,date_of_birth,phone,specialty):
        for user in self.users:
            if user.user_name == user_name:
                print('El nombre de usuario ya existe, intente de nuevo')
                return False
        new = User(self.id_counter,name,last_name,user_name,password,gender,date_of_birth,phone,specialty,"doctor")
        self.users.append(new)
        self.id_counter += 1
        print("Se creo un nuevo doctor")
        return True


#Función para actualizar datos de los doctores
    def update_doctor(self,id,name,last_name,user_name,password,date_of_birth):
        for user in self.users:
            if user.user_role=="doctor" and user.id==id:
                if user.user_name == user_name:
                    print('El nombre de usuario ya existe, intente de nuevo')
                    return False
                user.name=name
                user.last_name=last_name
                user.user_name=user_name
                user.password=password
                user.date_of_birth=date_of_birth
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


#Función para actualizar datos de enfermeras
    def update_nurse(self,id,name,last_name,user_name,password,date_of_birth):
        for user in self.users:
            if user.user_role=="nurse"and user.id==id:
                if user.user_name == user_name:
                    print('El nombre de usuario ya existe, intente de nuevo')
                    return False
                user.name=name
                user.last_name=last_name
                user.user_name=user_name
                user.password=password
                user.date_of_birth=date_of_birth
                return True