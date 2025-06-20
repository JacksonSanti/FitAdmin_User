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
                gender_id=str(row[2]),
                birthday=row[3],
                email=row[4],
                phone=row[5],
                state_id=str(row[6]),
                city=row[7],
                neighborhood=row[8],
                address=row[9],
                number=row[10],
                cep = row[11],
                payment_id=str(row[12]),
                nivel_id=str(row[13]),
                goal_id=str(row[14])
            )
            students.append(student)

        return service_pb2.StudentDataResponse(student=students)

    def UpdateStudentData(self, request, context):

        conn = sqlite3.connect(DATABASE)

        id = request.id
        name = request.name
        gender_id = request.gender_id
        birthday = request.birthday
        email = request.email
        phone = request.phone
        state_id = request.state_id
        city = request.city
        neighborhood = request.neighborhood
        address = request.address
        number = request.number
        cep = request.cep
        payment_id = request.payment_id
        nivel_id = request.nivel_id
        goal_id = request.goal_id

        data = database.update_student_by_id(conn,id,name,gender_id,birthday,email,phone,state_id,city,neighborhood,address,number,cep,payment_id,nivel_id,goal_id)

        conn.close()

        return service_pb2.StudentUpdateResponse(success=data)
    
    def CreateStudentData(self, request, context):
        
        conn = sqlite3.connect(DATABASE)

        name = request.name
        gender_id = request.gender_id
        birthday = request.birthday
        email = request.email
        phone = request.phone
        state_id = request.state_id
        city = request.city
        neighborhood = request.neighborhood
        address = request.address
        number = request.number
        cep = request.cep
        payment_id = request.payment_id 
        nivel_id = request.nivel_id
        goal_id = request.goal_id

        id = database.create_student(
            conn, name, gender_id, birthday, email, phone, state_id, city,
            neighborhood, address, number, cep, payment_id, nivel_id, goal_id
        )

        conn.close()

        return service_pb2.StudentCreateResponse(id=id)

    
    def UpdateStudentPaymentId(self, request, context):

        conn = sqlite3.connect(DATABASE)

        student_id = request.student_id

        financial_id = request.financial_id

        status = database.update_payment_id_by_student_id(conn, student_id, financial_id)

        return service_pb2.StudentUpdateResponse(success = status)
    
    def DeleteStudentById(self, request, context):

        conn = sqlite3.connect(DATABASE)

        student_id = request.student_id

        status = database.delete_student_by_id(conn, student_id)

        return service_pb2.StudentUpdateResponse(success = status)
    
    def GetStudentByName(self, request, context):

        conn = sqlite3.connect(DATABASE)

        name = request.student_name

        data = database.get_student_by_name(conn,name)

        conn.close()

        students = []

        for row in data:
            student = service_pb2.Student(
                id=row[0],
                name=row[1],
                gender_id=str(row[2]),
                birthday=row[3],
                email=row[4],
                phone=row[5],
                state_id=str(row[6]),
                city=row[7],
                neighborhood=row[8],
                address=row[9],
                number=row[10],
                cep = row[11],
                payment_id=str(row[12])
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
            state = service_pb2.StateResponse(
                id=row[0],
                name=row[1],
                abbreviation=row[2]
            )
            states.append(state)

        return service_pb2.StatesListDataResponse(state=states)
    
    def GetStateDataById(self, request, context):

        conn = sqlite3.connect(DATABASE)

        state_id = request.state_id

        data = database.get_state_by_id(conn, state_id)

        return service_pb2.StateResponse(
                id=data[0],
                name=data[1],
                abbreviation=data[2]
        ) 

class GenderService(service_pb2_grpc.GenderServiceServicer):
    
    def GetGenderData(self, request, context):

        conn = sqlite3.connect(DATABASE)

        data = database.get_all_gender(conn)

        conn.close()

        genders = []

        for row in data:
            gender = service_pb2.GenderResponse(
                id=row[0],
                name=row[1],
            )
            genders.append(gender)

        return service_pb2.GenderListDataResponse(gender=genders)
    
    def GetGenderDataById(self, request, context):

        conn = sqlite3.connect(DATABASE)

        gender_id = request.gender_id

        data = database.get_gender_by_id(conn, gender_id)

        return service_pb2.GenderResponse(
            id=data[0],
            name=data[1],
        )
        
class NivelService(service_pb2_grpc.NivelServiceServicer):

    def GetNivelData(self, request, context):

        conn = sqlite3.connect(DATABASE)

        data = database.get_all_nivel(conn)

        conn.close()

        nivels = []

        for row in data:
            nivel = service_pb2.NivelResponse(
                id=row[0],
                name=row[1],
            )
            nivels.append(nivel)

        return service_pb2.NivelListDataResponse(nivel=nivels)
    
    def GetNivelDataById(self, request, context):

        conn = sqlite3.connect(DATABASE)

        nivel_id = request.nivel_id

        data = database.get_nivel_by_id(conn, nivel_id)

        return service_pb2.NivelResponse(
            id=data[0],
            name=data[1],
        )

class GoalService(service_pb2_grpc.GoalServiceServicer):

    def GetGoalsData(self, request, context):

        conn = sqlite3.connect(DATABASE)

        data = database.get_all_goals(conn)

        conn.close()

        goals = []

        for row in data:
            goal = service_pb2.GoalResponse(
                id=row[0],
                name=row[1],
            )
            goals.append(goal)

        return service_pb2.GoalListDataResponse(goal=goals)
    
    def GetGoalDataById(self, request, context):

        conn = sqlite3.connect(DATABASE)

        goal_id = request.goal_id

        data = database.get_goal_by_id(conn, goal_id)

        return service_pb2.GoalResponse(
            id=data[0],
            name=data[1],
        )

