python -m grpc_tools.protoc -I./ --python_out=../Backend/agent-server --grpc_python_out=../Backend/agent-server agent.proto

# TODO generate JS client from same proto file into frontend directory