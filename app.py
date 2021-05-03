from flask import Flask
from flask_cors import CORS
from User_DAO import User_DAO
from Medicine_DAO import Medicine_DAO
from Appointment_DAO import Appointment_DAO
from Prescription_DAO import Prescription_DAO
from flask.globals import request
from instances import userHandlerInstance

app = Flask(__name__)
CORS(app)
userHandler = userHandlerInstance
medicineHandler = Medicine_DAO()
appointmentHandler = Appointment_DAO()
prescriptionHandler= Prescription_DAO()



userHandler.new_admin("Ariel","Bautista","admin","1234","m","15/04/2021","12345678")
userHandler.new_patient("Jaime","Cardozo","user1","1234","m",'15/04/2021',"12345678")
userHandler.new_patient("Juan","Fernandez","user2","1234","m","15/04/2021","12345678")
userHandler.new_patient("Adriana","Santizo","user3","1234","f","15/04/2021","12345678")
userHandler.new_patient("Ericka","Márquez","user4","1234","f","15/04/2021","12345678")
userHandler.new_patient("Pedro","DeMarcos","user5","1234","m","15/04/2021","12345678")

userHandler.new_doctor("Oscar","Mingueza","user100","1234","m","15/04/2021","Cardiologo","12345678")
userHandler.new_doctor("Javier","Ordoñez","user101","1234","m","15/04/2021","Pediatra","12345678")
userHandler.new_doctor("Jorge","Lopez","user102","1234","f","15/04/2021","Oncólogo","12345678")
userHandler.new_doctor("Matias","Hernandez","user103","1234","f","15/04/2021","Urólogo","12345678")
userHandler.new_doctor("Julian","Castillo","user104","1234","m","15/04/2021","Cirugía General","12345678")


userHandler.new_nurse("Jessica", "Rodriguez", "nurse1", "1234", "f", "15/04/2021", "12345678")
userHandler.new_nurse("Angélica", "Nuñez", "nurse2", "1234", "f", "15/04/2021", "12345678")
userHandler.new_nurse("Bárbara", "García", "nurse3", "1234", "f", "15/04/2021", "12345678")
userHandler.new_nurse("Celia", "Martinez", "nurse4", "1234", "f", "15/04/2021", "12345678")
userHandler.new_nurse("Allison", "DiLaurentis", "nurse5", "1234", "f", "15/04/2021", "12345678")


medicineHandler.new_medicine("locamedicina1", 50.00, "medicina 1", 100)
medicineHandler.new_medicine("locamedicina2", 50.00, "medicina 2", 100)
medicineHandler.new_medicine("locamedicina3", 50.00, "medicina 3", 100)
medicineHandler.new_medicine("locamedicina4", 50.00, "medicina 4", 100)
medicineHandler.new_medicine("locamedicina5 ", 50.00, "medicina 5", 100)

appointmentHandler.new_appointment(1,"22/04/2021","9:00","Dolor de estómago")
appointmentHandler.new_appointment(2,"22/04/2021","9:00","Dolor de cabeza")
appointmentHandler.new_appointment(3,"22/04/2021","9:00","Dolor de pierna")
appointmentHandler.new_appointment(4,"22/04/2021","9:00","Dolor de muela")
appointmentHandler.new_appointment(5,"22/04/2021","9:00","Dolor de cuello")

#print(appointmentHandler.appointments[0].id_doctor+" "+appointmentHandler.appointments[0].name_doctor)
#print(appointmentHandler.appointments[1].name_patient)
#print(userHandler.get_name_of_user_by_id(1))
#print(userHandler.get_id_by_username("user100"))
#print(userHandler.get_user_data_by_id(1))

#print(userHandler.update_user(11,"Lidia","Vásquez","lidia123","12345","21/07/2000" ))
#print(userHandler.users[11].user_name)



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
            "role":str(userHandler.get_user_role_by_username(user_name)),
            "name":str(userHandler.get_name_of_user_by_user_name(user_name))
        }
        return response
    else:
        response = {
            "state": "error",
            "message": "El nombre de usuario o contraeña incorrectos",
            "role" : "error"
        }
        return response

@app.route('/total-bill',methods=['POST'])
def calc_total():
    totalfac=0
    response = {}
    consulta = request.json['consulta']
    operacion = request.json['operacion']
    internado = request.json['internado']
    print("Intentanto calcular el total de factura..........")
    
    if(operacion != "" and internado != ""):
        totalfac=float(consulta)+float(operacion)+float(internado)
        print(str(totalfac))
        response = {
            "state": "perfect",
            "totalbill":str(totalfac)
        }
        return response
    elif(operacion != "" and internado == ""):
        totalfac=float(consulta)+float(operacion)
        print(str(totalfac))
        response = {
            "state": "perfect",
            "totalbill":str(totalfac)
        }
        return response
    elif(operacion == "" and internado != ""):
        totalfac=float(consulta)+float(internado)
        print(str(totalfac))
        response = {
            "state": "perfect",
            "totalbill":str(totalfac)
        }
        return response
    else:
        totalfac=float(consulta)
        print(str(totalfac))
        response = {
            "state": "perfect",
            "totalbill":str(totalfac)
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



@app.route('/new-prescription',methods=['POST'])
def new_presc():
    patient = request.json['name_patient']
    date = request.json['date']
    suffering = request.json['suffering']
    description = request.json['description']
    id = request.json['doctor']
    print("Intentanto crear la receta para el paciente: " + str(patient))
    if(prescriptionHandler.new_prescription(patient,date,suffering,description)):
        return userHandler.get_user_data_by_id(int(id))

@app.route('/request-appointment',methods=['POST'])
def r_equest():
    
    response = {}
    id = request.json['id_patient']
    time = request.json['time']
    date = request.json['date']
    reason = request.json['reason']
    print("Intentanto crear una cita para el paciente con el id:" + str(id))
    if(appointmentHandler.new_appointment(id,date,time,reason)):
        response = {
            "state": "perfect",
            "message": "La cita ha sido creada con éxito"
        }
        return response
    else:
        response = {
            "state": "error",
            "message": "Tienes una cita en proceso!"
        }
        return response

"""
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
"""

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

@app.route('/get-medicines2',methods=['GET'])
def get_medicines2_():
    return  medicineHandler.get_medicines2()

@app.route('/generate-purchase',methods=['POST'])
def get_purchase_():
    id = request.json['id']
    return  medicineHandler.get_medicine_data_by_id(id)


@app.route('/get-id_users',methods=['GET'])
def get_id_users():
    return  userHandler.id_of_all_users_except_admin()

@app.route('/get-id_medicines',methods=['GET'])
def get_id_medicines():
    return  medicineHandler.id_of_all_medicines()

@app.route('/get-id_appointments',methods=['GET'])
def get_id_waiting():
    return  appointmentHandler.id_of_all_waiting_appointments()    

@app.route('/get-doctor-list',methods=['GET'])
def get_doctor_lisst():
    return  userHandler.get_users_by_role("doctor")

@app.route('/get-accepted-appointments',methods=['GET'])
def get_accepted_a():
    return  appointmentHandler.get_accepted_appointments("accepted")

@app.route('/get-appointments-of-a-doctor',methods=['POST'])
def get_accepted_doctor():
    id = request.json['id']
    return  appointmentHandler.get_accepted_appointments_by_doctor("accepted",int(id))

@app.route('/get-finished-appointments-of-a-doctor',methods=['POST'])
def get_finished_doctor():
    id = request.json['id']
    return  appointmentHandler.get_accepted_appointments_by_doctor("completed",int(id))




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

@app.route('/get-data-medicines-by-id',methods=['POST'])
def get_medicine_dats_by_id():
    id = request.json['id']
    print("Intentanto obtener datos para el medicamento con el id: " + str(id))
    return medicineHandler.get_medicine_data_by_id(id)

@app.route('/get-data-appointments-by-id',methods=['POST'])
def get_appointment_dats_by_id():
    id = request.json['id']
    print("Intentanto obtener datos para la cita con el id: " + str(id))
    return appointmentHandler.get_appointment_data_by_id(id)

@app.route('/get-id-specific-nurse',methods=['POST'])
def get_nurse_dats_by_id():
    id = request.json['id']
    return userHandler.get_user_data_by_id(id)


@app.route('/get-id-specific-doctor',methods=['POST'])
def get_doctor_dats_by_id():
    id = request.json['id']
    return userHandler.get_user_data_by_id(id)

@app.route('/get-id-specific-patient',methods=['POST'])
def get_patient_dats_by_id():
    id = request.json['id']
    return userHandler.get_user_data_by_id(id)

@app.route('/get-data-nurse-by-id',methods=['POST'])
def get_data_nurse_by_id():
    id = request.json['id']
    print("Intentanto obtener datos para la enfermera con el id: " + str(id))
    return userHandler.get_user_data_by_id(id)

@app.route('/get-data-doctor-by-id',methods=['POST'])
def get_data_doctor_by_id():
    id = request.json['id']
    print("Intentanto obtener datos para la enfermera con el id: " + str(id))
    return userHandler.get_user_data_by_id(id)



@app.route('/generate-bill',methods=['POST'])
def get_data_doctor_for_bill():
    id = request.json['id']
    print("Intentanto obtener datos para el doctor con el id: " + str(id))
    return userHandler.get_user_data_by_id(id)

@app.route('/get-data-patient-by-id',methods=['POST'])
def get_data_patient_by_id():
    id = request.json['id']
    print("Intentanto obtener datos para el paciente con el id: " + str(id))
    return userHandler.get_user_data_by_id(id)
    

@app.route('/accept-appointments',methods=['POST'])
def accept_appointment_():
    response = {}
    id = request.json['id']
    id_doctor = request.json['doctor']
    print("Intentanto aceptar la cita con el id: " + str(id))
    if(appointmentHandler.accept_appointment(id,id_doctor)):
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




@app.route('/accept-appointments-doctor',methods=['POST'])
def accept_appointment_D():
    response = {}
    id = request.json['id']
    id_doctor = request.json['doctor']
    print("Intentanto aceptar la cita con el id: " + str(id))
    if(appointmentHandler.accept_appointment(int(id),int(id_doctor))):
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

@app.route('/delete-medicine',methods=['POST'])
def delete_medicineee():
    
    response = {}
    id = request.json['id']
    print("Intentanto eliminar el medicamento con el id: " + str(id))
    if(medicineHandler.delete_medicine(int(id))):
        response = {
            "state": "perfect",
            "message": "El medicamento ha sido eliminado con éxito"
        }
        return response
    else:
        response = {
            "state": "error",
            "message": "El medicamento no existe, intente de nuevo"
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

@app.route('/finish-appointment',methods=['POST'])
def finish_appointment_():
    
    response = {}
    id = request.json['id']
    print("Intentanto finalizar la cita con el id: " + str(id))
    if(appointmentHandler.finish_appointment(int(id))):
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

@app.route('/update-medicine-admin',methods=['POST'])
def update_medicine_admin_():
    response = {}
    id = request.json['id']
    price = request.json['price']
    description = request.json['description']
    print("Intentanto actualizar los datos del medicamento con el id: " + str(id))
    if(medicineHandler.update_medicine(int(id),float(price),description)):
        response = {
            "state": "perfect",
            "message": "Los datos del medicamento han sido actualizados con éxito!"
        }
        return response
    else:
        response = {
            "state": "error",
            "message": "El medicamento no existe, intente de nuevo"
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

@app.route('/less-amount',methods=['POST'])
def less_amount():
    response = {}
    id_medicine = request.json['id']
    amount = request.json['amount']
    if(medicineHandler.purchase_update(id_medicine,amount)):
        response = {
            "state": "perfect",
            "message": "La cantidad de la medicina ha sido actualizada con éxito!!"
        }
        return response
    else:
        response = {
            "state": "error",
            "message": "La medicina no tiene suficiente cantidad para ser despachada"
        }
        return response

@app.route('/update-doctor',methods=['POST'])
def update_doctor_():
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
            "message": "Los datos del doctor han sido actualizados con éxito!"
        }
        return response
    else:
        response = {
            "state": "error",
            "message": "El doctor no existe, intente de nuevo"
        }
        return response


@app.route('/update-patient',methods=['POST'])
def update_patient_():
    response = {}
    id = request.json['id']
    name = request.json['name']
    last_name = request.json['last_name']
    user_name = request.json['user_name']
    password = request.json['password']
    date_of_birth = request.json['date_of_birth']
    print("Intentanto actualizar los datos del paciente con el id: " + str(id))
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

@app.route('/bulk-load-patients',methods=['POST'])
def bulk_patients():
    
    response = {}
    name = request.json['name']
    last_name = request.json['last_name']
    birth = request.json['date']
    gender = request.json['gender']
    user_name  = request.json['user_name']
    password  = request.json['password']
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

@app.route('/bulk-load-doctors',methods=['POST'])
def bulk_doctors():
    
    response = {}
    name = request.json['name']
    last_name = request.json['last_name']
    birth = request.json['date']
    gender = request.json['gender']
    user_name  = request.json['user_name']
    password  = request.json['password']
    speciality = request.json['speciality']
    phone = request.json['phone']
    
    print("Intentanto crear para:" + str(user_name))
    if(userHandler.new_doctor(name,last_name,user_name,password,gender,birth,speciality,phone)):
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


@app.route('/bulk-load-nurses',methods=['POST'])
def bulk_nurses():
    
    response = {}
    name = request.json['name']
    last_name = request.json['last_name']
    birth = request.json['date']
    gender = request.json['gender']
    user_name  = request.json['user_name']
    password  = request.json['password']
    phone = request.json['phone']
    print("Intentanto crear para:" + str(user_name))
    if(userHandler.new_nurse(name,last_name,user_name,password,gender,birth,phone)):
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

@app.route('/bulk-load-medicines',methods=['POST'])
def bulk_medicines():
    
    response = {}
    name = request.json['name']
    price = request.json['price']
    description = request.json['description']
    ammount = request.json['ammount']
    print("Intentanto crear para:" + str(name))
    if(medicineHandler.new_medicine(name,float(price),description,int(ammount))):
        response = {
            "state": "perfect",
            "message": "El medicamento ha sido ingresado con éxito"
        }
        return response
    else:
        response = {
            "state": "error",
            "message": "La medicina ya existe, intente de nuevo!"
        }
        return response

if __name__ == "__main__":
    app.run(threaded=True, port=5000,debug=True)


    