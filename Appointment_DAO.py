from Appointment import Appointment
from User import User
from User_DAO import User_DAO
class Appointment:
    def __init__(self):
        self.appointments = []
        self.ida_counter = 0

    userHandler = User_DAO()

    def new_appointment(self,id_patient,date,time,reason):
        for appointment in self.appointments:
            new = Appointment()(self.ida_counter,id_patient,date,time,reason)
            self.medicines.append(new)
            self.ida_counter += 1
            print("Se ingresó una nueva cita programada para el paciente: "+userHandler.user_by_id(id_patient))
            return True