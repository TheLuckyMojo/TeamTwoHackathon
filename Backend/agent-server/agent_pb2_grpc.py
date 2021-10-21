# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import agent_pb2 as agent__pb2


class AgentStub(object):
    """Interface for talking to the trained agent.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPlanAssessment = channel.unary_unary(
                '/agent.Agent/GetPlanAssessment',
                request_serializer=agent__pb2.OperatingPicture.SerializeToString,
                response_deserializer=agent__pb2.PlanAssessment.FromString,
                )


class AgentServicer(object):
    """Interface for talking to the trained agent.
    """

    def GetPlanAssessment(self, request, context):
        """Gets a new plan/assessment from the agent.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AgentServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetPlanAssessment': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPlanAssessment,
                    request_deserializer=agent__pb2.OperatingPicture.FromString,
                    response_serializer=agent__pb2.PlanAssessment.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'agent.Agent', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Agent(object):
    """Interface for talking to the trained agent.
    """

    @staticmethod
    def GetPlanAssessment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/agent.Agent/GetPlanAssessment',
            agent__pb2.OperatingPicture.SerializeToString,
            agent__pb2.PlanAssessment.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
