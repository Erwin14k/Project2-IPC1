from Medicine import Medicine

class Medicine_DAO:
    def __init__(self):
        self.medicines = []
        self.idm_counter = 0



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
