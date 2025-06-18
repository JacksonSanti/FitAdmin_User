import grpc
import service_pb2_grpc
from concurrent import futures
from handlers import *

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))  
    service_pb2_grpc.add_AuthServiceServicer_to_server(AuthService(), server) 
    service_pb2_grpc.add_StudentServiceServicer_to_server(StudentService(), server)
    service_pb2_grpc.add_StateServiceServicer_to_server(StateService(),server)
    service_pb2_grpc.add_GenderServiceServicer_to_server(GenderService(),server)
    service_pb2_grpc.add_NivelServiceServicer_to_server(NivelService(), server)
    service_pb2_grpc.add_GoalServiceServicer_to_server(GoalService(),server)
    server.add_insecure_port('[::]:50051')  
    print("Servidor gRPC rodando na porta 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
