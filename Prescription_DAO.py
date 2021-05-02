from Prescription import Prescription
import json


class Prescription_DAO:
    def __init__(self):
        self.prescriptions = []
        self.idp_counter = 500000


#Función para crear nuevas citas, recordando que el apartado de id doctor momentaneamente irá vacío
    def new_prescription(self,name_patient,date,suffering,description):
        new= Prescription(self.idp_counter,name_patient,date,suffering.lower(),description)
        self.prescriptions.append(new)
        self.idp_counter += 1
        print("Se creó una nueva receta médica")
        return True