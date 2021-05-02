from Appointment import Appointment
import json
from User_DAO import User_DAO
from instances import userHandlerInstance
userHandler = userHandlerInstance

class Appointment_DAO:
    def __init__(self):
        self.appointments = []
        self.ida_counter = 20000


#Función para crear nuevas citas, recordando que el apartado de id doctor momentaneamente irá vacío
    def new_appointment(self,id_patient,date,time,reason):
        for appoi in self.appointments:
            if appoi.id_patient == int(id_patient):
                if appoi.status !="waiting" and appoi.status != "accepted":
                    new = Appointment(self.ida_counter,int(id_patient),0000000,"",date,time,reason,"waiting")
                    self.appointments.append(new)
                    print("Se ingresó una nueva cita programada para el paciente con el id: "+str(id_patient))
                    self.ida_counter += 1
                    return True
                elif appoi.status =="waiting" or appoi.status == "accepted":
                    print("No se pudo regitrar la cita, el paciente con el id: "+ str(id_patient)+ " Tiene una cita pendiente o alguna en proceso!")
                    return False
        new = Appointment(self.ida_counter,int(id_patient),0000000,"",date,time,reason,"waiting")
        self.appointments.append(new)
        print("Se ingresó una nueva cita programada para el paciente con el id: "+str(id_patient))
        self.ida_counter += 1
        return True


#Función que devuelve todas las citas pendientes
    def get_waiting_appointments(self,status):
        return json.dumps([Appointment.dump() for Appointment in self.appointments if Appointment.status == status ]) 

#Función que devuelve todas las citas aceptadas
    def get_accepted_appointments(self,status):
        return json.dumps([Appointment.dump() for Appointment in self.appointments if Appointment.status == status ]) 

#Función que devuelve todas las citas aceptadas por un doctor en especifico
    def get_accepted_appointments_by_doctor(self,status,id_doctor):
        return json.dumps([Appointment.dump() for Appointment in self.appointments if Appointment.status == status and Appointment.id_doctor==int(id_doctor) ]) 


#Función que muestra en consola todas las citas 
    def print_appoinments(self,id):
        for appoi in self.appointments:
            if appoi.id_patient == int(id):
                print(str(appoi.id)+" - "+str(appoi.id_patient)+" - "+str(appoi.reason)+" - "+str(appoi.status))
        
#Función que devuelve todas las citas dependiento el status de un paciente especifico
    def get_appointments_specific_patient_by_status(self,id,status):
        return json.dumps([Appointment.dump() for Appointment in self.appointments if Appointment.status == status and Appointment.id_patient==int(id) ]) 

#Función para rechazar citas
    def decline_appointment(self,id):
        for appointment in self.appointments:
            if appointment.id == int(id) :
                appointment.status="declined"
                print("Se ha rechazado con éxito la cita para el paciente con el id: "+str(appointment.id_patient))
                return True
        return False

#Función para finalizar citas
    def finish_appointment(self,id):
        for appointment in self.appointments:
            if appointment.id == int(id) :
                appointment.status="completed"
                userHandler.add_prescription(appointment.id_doctor)
                print("Se ha finalizado con éxito la cita para el paciente con el id: "+str(appointment.id_patient))
                return True
        return False

#Función para aceptar Citas
    def accept_appointment(self,id,doctor_id):
        for appointment in self.appointments:
            if appointment.id == int(id) :
                appointment.name_doctor=userHandler.get_name_of_user_by_id(doctor_id)
                appointment.status="accepted"
                appointment.id_doctor=int(doctor_id)
                print("Se ha aceptado con éxito la cita para el paciente con el id: "+str(appointment.id_patient))
                print(str(appointment.id_doctor))
                return True
        return False
    
    def accept_appointment2(self,id,doctor_username):
        for appointment in self.appointments:
            if appointment.id == int(id) :
                appointment.name_doctor=userHandler.get_name_of_user_by_user_name(doctor_username)
                appointment.status="accepted"
                appointment.id_doctor=int(userHandler.get_id_by_username(doctor_username))
                print("Se ha aceptado con éxito la cita para el paciente con el id: "+str(appointment.id_patient))
                print(str(appointment.id_doctor))
                return True
        return False

#Función que devuelve todos los datos de una cita en base a su id 
    def get_appointment_data_by_id(self,id):
        return json.dumps([Appointment.dump() for Appointment in self.appointments if Appointment.id == int(id)  ]) 
    
#Función que devuelve todos los id de las citas que estan pendientes
    def id_of_all_waiting_appointments(self):
        return json.dumps([Appointment.dump() for Appointment in self.appointments if Appointment.status != "accepted" and Appointment.status != "declined" and Appointment.status != "completed"  ]) 