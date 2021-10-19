import grpc;
from grpc_reflection.v1alpha import reflection
from concurrent import futures;

import agent_pb2;
import agent_pb2_grpc;

class AgentServicer(agent_pb2_grpc.AgentServicer):
    def GetPlan(self, request, context):
        """Gets a new plan from the agent.
        """
        print(request.numMissiles)
        return agent_pb2.Plan(targetDamageAssessment=[0,0,0,0,0,0,0])
        
def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    agent_pb2_grpc.add_AgentServicer_to_server(
        AgentServicer(), server)
    SERVICE_NAMES = (
        agent_pb2.DESCRIPTOR.services_by_name['Agent'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    port = "50051"
    print("Server started. Listening on port " + port)
    server.add_insecure_port('[::]:' + port)
    server.start()
    server.wait_for_termination()

main()
