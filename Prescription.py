class Prescription:
    def __init__(self,id,name_patient,date,suffering,description):
        self.id = id 
        self.name_patient = name_patient
        self.date = date
        self.suffering = suffering
        self.description = description

    def dump(self):
        return {
            'id': self.id,
            'name_patient': self.name_patient,
            'date':  self.date,
            'suffering': self.suffering,
            'description': self.description,
        }