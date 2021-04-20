from Medicine import Medicine
import json
class Medicine_DAO:
    def __init__(self):
        self.medicines = []
        self.idm_counter = 1000



    def new_medicine(self,name,price,description,amount):
        for medicine in self.medicines:
            if medicine.name == name:
                print('La medicina que desea ingresar ya existe!')
                return False
        new = Medicine(self.idm_counter,name,price,description,amount)
        self.medicines.append(new)
        self.idm_counter += 1
        print("Se ingresó una nueva medicina")
        return True

#Función que devuelve todos los medicamentos
    def get_medicines(self):
        return json.dumps([Medicine.dump() for Medicine in self.medicines if Medicine.amount!=0]) 
