from flask import Flask
from flask_cors import CORS
from User_DAO import User_DAO
from Medicine_DAO import Medicine_DAO
from flask.globals import request

app = Flask(__name__)
CORS(app)
userHandler = User_DAO()
medicineHandler = Medicine_DAO()



userHandler = User_DAO()
userHandler.new_admin("Erwin","Vásquez","Master","1234","m","15/04/2001","12345678")
userHandler.new_patient("paciente","1","user1","1234","m","15/04/2001","12345678")
userHandler.new_patient("paciente","2","user2","1234","m","15/04/2001","12345678")
userHandler.new_patient("paciente","3","user3","1234","f","15/04/2001","12345678")
userHandler.new_patient("paciente","4","user4","1234","f","15/04/2001","12345678")
userHandler.new_patient("paciente","5","user5","1234","m","15/04/2001","12345678")

userHandler.new_doctor("doctor","1","user100","1234","m","15/04/2001","12345678","Cardiologo")
userHandler.new_doctor("doctor","2","user101","1234","m","15/04/2001","12345678","Pediatra")
userHandler.new_doctor("doctor","3","user102","1234","f","15/04/2001","12345678","Oncólogo")
userHandler.new_doctor("doctor","4","user103","1234","f","15/04/2001","12345678","Urólogo")
userHandler.new_doctor("doctor","5","user104","1234","m","15/04/2001","12345678","Cirugía General")


userHandler.new_nurse("enfermera", "1", "nurse1", "1234", "f", "15/04/2001", "12345678")
userHandler.new_nurse("enfermera", "2", "nurse2", "1234", "f", "15/04/2001", "12345678")
userHandler.new_nurse("enfermera", "3", "nurse3", "1234", "f", "15/04/2001", "12345678")
userHandler.new_nurse("enfermera", "4", "nurse4", "1234", "f", "15/04/2001", "12345678")
userHandler.new_nurse("enfermera", "5", "nurse5", "1234", "f", "15/04/2001", "12345678")


medicineHandler.new_medicine("Acetaminofen", 50.00, "medicina 1", 100)
medicineHandler.new_medicine("Ibuprofeno", 50.00, "medicina 2", 100)
medicineHandler.new_medicine("Ibersatán", 50.00, "medicina 3", 100)
medicineHandler.new_medicine("Paracetamol", 50.00, "medicina 4", 100)
medicineHandler.new_medicine("Omeprazol ", 50.00, "medicina 5", 100)


@app.route("/")
def index():
    return "<h1>Ruta Principal 14k</h1>"






@app.route('/saludar',methods=['POST'])
def saluda():
    response = {}
    name = request.json['name']
    response = {
        "state": "Hola "+name
    }
    return response

@app.route('/login',methods=['POST'])
def new_user():
    
    response = {}
    user_name = request.json['user_name']
    password = request.json['password']
    print("Intentanto iniciar sesión para:" + str(user_name))
    if(userHandler.login_validation(user_name,password)):
        response = {
            "state": "perfect",
            "message": "El usuario "+str(user_name)+ "ha iniciado sesión con éxito"
        }
        return response
    else:
        response = {
            "state": "error",
            "message": "El nombre de usuario o contraeña incorrectos"
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





if __name__ == "__main__":
    app.run(threaded=True, port=5000,debug=True)