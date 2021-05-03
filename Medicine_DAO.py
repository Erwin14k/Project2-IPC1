from Medicine import Medicine
import json
class Medicine_DAO:
    def __init__(self):
        self.medicines = []
        self.idm_counter = 1000


#Función para crear nueva medicina
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
        return json.dumps([Medicine.dump() for Medicine in self.medicines  ]) 

#Función que devuelve todos los medicamentos que tengan al menos una existencia
    def get_medicines2(self):
        return json.dumps([Medicine.dump() for Medicine in self.medicines if Medicine.status!=0 ]) 
#Función parecida a la anterior, en este caso nos servirá para traer los id de los medicamentos
    def id_of_all_medicines(self):
        return json.dumps([Medicine.dump() for Medicine in self.medicines ])

#Función que devuelve todos los datos de un medicamento en base a su id 
    def get_medicine_data_by_id(self,id):
        return json.dumps([Medicine.dump() for Medicine in self.medicines if Medicine.id == int(id)  ]) 


#Función para actualizar datos de cualquier medicamento
    def update_medicine(self,id ,price ,description):
        for medicine in self.medicines:
            if medicine.id ==int(id) :
                medicine.price=price
                medicine.description=description
                return True
        return False


#Función para eliminar usuarios(enfermeras, doctores o pacientes)
    def delete_medicine(self,id):
        for medicine in self.medicines:
            if medicine.id == int(id):
                print(f'El medicamento: "{medicine.name}" ha sido eliminado con éxito')
                self.medicines.remove(medicine)
                return True
        print(f'El medicamento con id: "{ id }" no ha sido encontrado.')
        return False
    
    def purchase_update(self,id,amount):
        for medicine in self.medicines:
            if medicine.id==int(id):
                if medicine.amount >=int(amount):
                    medicine.amount=medicine.amount-int(amount)
                    return True
                return False
