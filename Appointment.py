class Appointment:
    def __init__(self,id,id_patient,id_doctor,name_doctor,date,time,reason,status):
        self.id = id 
        self.id_patient= id_patient
        self.id_doctor= id_doctor
        self.name_doctor=name_doctor
        self.date = date
        self.time = time
        self.reason = reason
        self.status=status





    
    def dump(self):
        return {
            'id': self.id,
            'id_patient': self.id_patient,
            'id_doctor':  self.id_doctor,
            'name_doctor':  self.name_doctor,
            'status':self.status,
            'date': self.date,
            'time': self.time,
            'reason':self.reason,
            'status':self.status,
        }