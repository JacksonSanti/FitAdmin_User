import service_pb2
import service_pb2_grpc
import sqlite3
import database

DATABASE = "./database.db"

class AuthService(service_pb2_grpc.AuthServiceServicer):

    def AuthenticateUser(self, request, context):

        email = request.email
        password = request.password        

        conn = sqlite3.connect(DATABASE)

        user_status = database.authenticate_user(conn, email, password)

        conn.close()

        return service_pb2.AuthenticateUserResponse(success=bool(user_status))

class StudentService(service_pb2_grpc.StudentServiceServicer):

    def GetStudentData(self, request, context):

        conn = sqlite3.connect(DATABASE)

        data = database.get_all_student(conn)

        conn.close()

        students = []

        for row in data:
            student = service_pb2.Student(
                id=row[0],
                name=row[1],
                ###gender_id=int(row[2]),
                gender_id=GenderService.GetGenderById(int(row[2])),
                birthday=row[3],
                email=row[4],
                phone=row[5],
                ###state_id=int(row[6]),
                state_id=StateService.GetStateById(int(row[6])),
                city=row[7],
                neighborhood=row[8],
                address=row[9],
                number=row[10],
                plan_id=int(row[11]),
                payment_id=int(row[12])
            )
            students.append(student)

        return service_pb2.StudentDataResponse(student=students)
    
class StateService(service_pb2_grpc.StateServiceServicer): 

    def GetStateData(self, request, context):

        conn = sqlite3.connect(DATABASE)

        data = database.get_all_state(conn)

        conn.close()

        states = []

        for row in data:
            state = service_pb2.State(
                id=row[0],
                name=row[1],
                abbreviation=row[2]
            )
            states.append(state)

        return service_pb2.StateService(states=states) 
    
    def GetStateById(state_id):

        conn = sqlite3.connect(DATABASE)

        data = database.get_state_by_id(conn, state_id)

        return data[1]   
    
    

class GenderService(service_pb2_grpc.GenderServiceServicer):
    
    def GetGenderData(self, request, context):

        conn = sqlite3.connect(DATABASE)

        data = database.get_all_gender(conn)

        conn.close()

        genders = []

        for row in data:
            gender = service_pb2.Gender(
                id=row[0],
                name=row[1],
            )
            genders.append(gender)

        return service_pb2.GenderService(genders=genders)
    
    def GetGenderById(gender_id):

        conn = sqlite3.connect(DATABASE)

        data = database.get_gender_by_id(conn, gender_id)

        return data[1]
        


