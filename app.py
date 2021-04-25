from flask import Flask
from flask_cors import CORS
from User_DAO import User_DAO
from Medicine_DAO import Medicine_DAO
from Appointment_DAO import Appointment_DAO
from flask.globals import request
from instances import userHandlerInstance

app = Flask(__name__)
CORS(app)
userHandler = userHandlerInstance
medicineHandler = Medicine_DAO()
appointmentHandler = Appointment_DAO()



userHandler.new_admin("Erwin","Vásquez","Master","1234","m","15/04/2021","12345678")
userHandler.new_patient("paciente","1","user1","1234","m",'15/04/2021',"12345678")
userHandler.new_patient("paciente","2","user2","1234","m","15/04/2021","12345678")
userHandler.new_patient("paciente","3","user3","1234","f","15/04/2021","12345678")
userHandler.new_patient("paciente","4","user4","1234","f","15/04/2021","12345678")
userHandler.new_patient("paciente","5","user5","1234","m","15/04/2021","12345678")

userHandler.new_doctor("doctor","1","user100","1234","m","15/04/2021","12345678","Cardiologo")
userHandler.new_doctor("doctor","2","user101","1234","m","15/04/2021","12345678","Pediatra")
userHandler.new_doctor("doctor","3","user102","1234","f","15/04/2021","12345678","Oncólogo")
userHandler.new_doctor("doctor","4","user103","1234","f","15/04/2021","12345678","Urólogo")
userHandler.new_doctor("doctor","5","user104","1234","m","15/04/2021","12345678","Cirugía General")


userHandler.new_nurse("enfermera", "1", "nurse1", "1234", "f", "15/04/2021", "12345678")
userHandler.new_nurse("enfermera", "2", "nurse2", "1234", "f", "15/04/2021", "12345678")
userHandler.new_nurse("enfermera", "3", "nurse3", "1234", "f", "15/04/2021", "12345678")
userHandler.new_nurse("enfermera", "4", "nurse4", "1234", "f", "15/04/2021", "12345678")
userHandler.new_nurse("enfermera", "5", "nurse5", "1234", "f", "15/04/2021", "12345678")


medicineHandler.new_medicine("Acetaminofen", 50.00, "medicina 1", 100)
medicineHandler.new_medicine("Ibuprofeno", 50.00, "medicina 2", 100)
medicineHandler.new_medicine("Ibersatán", 50.00, "medicina 3", 100)
medicineHandler.new_medicine("Paracetamol", 50.00, "medicina 4", 100)
medicineHandler.new_medicine("Omeprazol ", 50.00, "medicina 5", 100)

appointmentHandler.new_appointment(1,"22/04/2021","9:00 am","Dolor de estómago")
appointmentHandler.new_appointment(2,"22/04/2021","9:00 am","Dolor de cabeza")
appointmentHandler.new_appointment(3,"22/04/2021","9:00 am","Dolor de pierna")
appointmentHandler.new_appointment(4,"22/04/2021","9:00 am","Dolor de muela")
appointmentHandler.new_appointment(5,"22/04/2021","9:00 am","Dolor de cuello")

#print(appointmentHandler.appointments[0].id_doctor+" "+appointmentHandler.appointments[0].name_doctor)
#print(appointmentHandler.appointments[1].name_patient)
#print(userHandler.get_name_of_user_by_id(1))
#print(userHandler.get_id_by_username("user100"))
#print(userHandler.get_user_data_by_id(1))

print(userHandler.update_user(11,"Lidia","Vásquez","lidia123","12345","21/07/2000" ))
print(userHandler.users[11].user_name)
@app.route("/")
def index():
    return "<h1>Ruta Principal 14k</h1>"







@app.route('/login',methods=['POST'])
def login():
    
    response = {}
    user_name = request.json['user_name']
    password = request.json['password']
    print("Intentanto iniciar sesión para:" + str(user_name))
    if(userHandler.login_validation(user_name,password)):
        response = {
            "state": "perfect",
            "message": "El usuario "+str(user_name)+ " ha iniciado sesión con éxito",
            "id":str(userHandler.get_id_by_username(user_name)),
            "role":str(userHandler.get_user_role_by_username(user_name))
        }
        return response
    else:
        response = {
            "state": "error",
            "message": "El nombre de usuario o contraeña incorrectos",
            "role" : "error"
        }
        return response



@app.route('/register',methods=['POST'])
def r_egister():
    
    response = {}
    name = request.json['name']
    last_name = request.json['last_name']
    user_name = request.json['user_name']
    password = request.json['password']
    gender  = request.json['gender']
    date_of_birth  = request.json['date_of_birth']
    phone = request.json['phone']
    print("Intentanto crear para:" + str(user_name))
    if(userHandler.new_patient(name,last_name,user_name,password,gender,date_of_birth,phone)):
        response = {
            "state": "perfect",
            "message": "El usuario ha sido creado con éxito"
        }
        return response
    else:
        response = {
            "state": "error",
            "message": "El nombre de usuario ya esta en uso"
        }
        return response


@app.route('/adminView',methods=['GET','POST','DELETE'])
def get_user_by_id():
    response = {}
    id = request.args.get("name", None)
    user_response = userHandler.get_user_by_id(id)
    if (user_response != False):
        response = {
            "name": str(user_response.name),
            "last_name": str(user_response.last_name),
            "user_name": str(user_response.user_name),
            "password": str(user_response.password),
            "date_of_birth": str(user_response.date_of_birth)
        }
        return  response
    response = {
        "state": "error",
    }
    return  response


@app.route('/get-patients',methods=['GET'])
def get_patients():
    return  userHandler.get_users_by_role("patient")

@app.route('/get-doctors',methods=['GET'])
def get_doctors():
    return  userHandler.get_users_by_role("doctor")

@app.route('/get-nurses',methods=['GET'])
def get_nurses():
    return  userHandler.get_users_by_role("nurse")

@app.route('/get-medicines',methods=['GET'])
def get_medicines():
    return  medicineHandler.get_medicines()


@app.route('/get-id_users',methods=['GET'])
def get_id_users():
    return  userHandler.id_of_all_users_except_admin()

@app.route('/get-id_appointments',methods=['GET'])
def get_id_waiting():
    return  appointmentHandler.id_of_all_waiting_appointments()    

@app.route('/get-doctor-list',methods=['GET'])
def get_doctor_lisst():
    return  userHandler.get_users_by_role("doctor")

@app.route('/get-accepted-appointments',methods=['GET'])
def get_accepted_a():
    return  appointmentHandler.get_accepted_appointments("accepted")


@app.route('/get-waiting-appointments',methods=['GET'])
def get_waiting_a():
    return  appointmentHandler.get_waiting_appointments("waiting")



@app.route('/waiting-patients',methods=['POST'])
def get_waiting_p():
    id = request.json['id']
    return  appointmentHandler.get_appointments_specific_patient_by_status(id,"waiting")

@app.route('/accepted-patients',methods=['POST'])
def get_accepted_p():
    id = request.json['id']
    return  appointmentHandler.get_appointments_specific_patient_by_status(id,"accepted")

@app.route('/declined-patients',methods=['POST'])
def get_declined_p():
    id = request.json['id']
    return  appointmentHandler.get_appointments_specific_patient_by_status(id,"declined")

@app.route('/completed-patients',methods=['POST'])
def get_completed_p():
    id = request.json['id']
    return  appointmentHandler.get_appointments_specific_patient_by_status(id,"completed")


@app.route('/get-data-patients-by-id',methods=['POST'])
def get_user_dats_by_id():
    id = request.json['id']
    print("Intentanto obtener datos para el usuario con el id: " + str(id))
    return userHandler.get_user_data_by_id(id)

@app.route('/get-data-appointments-by-id',methods=['POST'])
def get_appointment_dats_by_id():
    id = request.json['id']
    print("Intentanto obtener datos para la cita con el id: " + str(id))
    return appointmentHandler.get_appointment_data_by_id(id)

@app.route('/get-id-specific-nurse',methods=['POST'])
def get_nurse_dats_by_id():
    id = request.json['id']
    return userHandler.get_user_data_by_id(id)

@app.route('/get-data-nurse-by-id',methods=['POST'])
def get_data_nurse_by_id():
    id = request.json['id']
    print("Intentanto obtener datos para la enfermera con el id: " + str(id))
    return userHandler.get_user_data_by_id(id)
    

@app.route('/accept-appointments',methods=['POST'])
def accept_appointment_():
    response = {}
    id = request.json['id']
    username_doctor = request.json['doctor']
    print("Intentanto aceptar la cita con el id: " + str(id))
    if(appointmentHandler.accept_appointment(id,username_doctor)):
        response = {
            "state": "perfect",
            "message": "La cita se ha aceptado con éxito!"
        }
        return response
    else:
        response = {
            "state": "error",
            "message": "La cita con el id especificado no exite, o puede que ya haya sido aceptado!, intente de nuevo"
        }
        return response





@app.route('/delete-user',methods=['POST'])
def delete_userr():
    
    response = {}
    id = request.json['id']
    print("Intentanto eliminar el ususario con el id: " + str(id))
    if(userHandler.delete_user(id)):
        response = {
            "state": "perfect",
            "message": "El usuario ha sido eliminado con éxito"
        }
        return response
    else:
        response = {
            "state": "error",
            "message": "El usuario no existe, intente de nuevo"
        }
        return response

@app.route('/decline-appointment',methods=['POST'])
def decline_appointment_():
    
    response = {}
    id = request.json['id']
    print("Intentanto rechazar la cita con el id: " + str(id))
    if(appointmentHandler.decline_appointment(id)):
        response = {
            "state": "perfect",
            "message": "El usuario ha sido eliminado con éxito"
        }
        return response
    else:
        response = {
            "state": "error",
            "message": "El usuario no existe, intente de nuevo"
        }
        return response

@app.route('/update-user-admin',methods=['POST'])
def update_user_admin_():
    response = {}
    id = request.json['id']
    name = request.json['name']
    last_name = request.json['last_name']
    user_name = request.json['user_name']
    password = request.json['password']
    date_of_birth = request.json['date_of_birth']
    print("Intentanto actualizar los datos del ususario con el id: " + str(id))
    if(userHandler.update_user(id,name,last_name,user_name,password,date_of_birth)):
        response = {
            "state": "perfect",
            "message": "Los datos del usuario han sido actualizados con éxito!"
        }
        return response
    else:
        response = {
            "state": "error",
            "message": "El usuario no existe, intente de nuevo"
        }
        return response


@app.route('/update-nurse',methods=['POST'])
def update_nurse_():
    response = {}
    id = request.json['id']
    name = request.json['name']
    last_name = request.json['last_name']
    user_name = request.json['user_name']
    password = request.json['password']
    date_of_birth = request.json['date_of_birth']
    print("Intentanto actualizar los datos de la enfermera con el id: " + str(id))
    if(userHandler.update_user(id,name,last_name,user_name,password,date_of_birth)):
        response = {
            "state": "perfect",
            "message": "Los datos de la enfermera han sido actualizados con éxito!"
        }
        return response
    else:
        response = {
            "state": "error",
            "message": "La enfermera no existe, intente de nuevo"
        }
        return response


@app.route('/bulk-load-patient',methods=['POST'])
def bulk_patients():
    
    response = {}
    name = request.json['name']
    last_name = request.json['last_name']
    birth = request.json['user_name']
    gender = request.json['password']
    user_name  = request.json['gender']
    password  = request.json['date_of_birth']
    phone = request.json['phone']
    print("Intentanto crear para:" + str(user_name))
    if(userHandler.new_patient(name,last_name,user_name,password,gender,birth,phone)):
        response = {
            "state": "perfect",
            "message": "El usuario ha sido creado con éxito"
        }
        return response
    else:
        response = {
            "state": "error",
            "message": "El nombre de usuario ya esta en uso"
        }
        return response


if __name__ == "__main__":
    app.run(threaded=True, port=5000,debug=True)


    