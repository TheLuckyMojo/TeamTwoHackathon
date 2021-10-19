# RPC client/server notes

[gRPC](https://grpc.io/docs/) helps you define a single service contract from .proto file(s) of your choice, then auto-generate client/server code in different languages that talk over HTTP/2.

## Regenerating the agent client/server

Assuming you have Python 3.8 and pip already installed, run the following:
```
python -m pip install --upgrade pip
# Installs plugins for building and generating client/server code.
python -m pip install grpcio grpcio-tools
```

Run the `generate_agent_server_client.py` script to auto-generate any client/server code to their respective frontend/backend directories.

## Smoke testing the agent server

There's extra proto files and Go plugins you have to setup to also be able to generate a REST API alongside the RPC interface. You can still hit gRPC services with human-friendly JSON inputs though with what currently gets generated out of the box with the help of [grpcurl](https://github.com/fullstorydev/grpcurl).

1. Install Go: https://golang.org/doc/install
1. Install grpcurl from command line 
    ```
    go install github.com/fullstorydev/grpcurl/cmd/grpcurl@latest
    ```
1. Run the generated agent server:
    ```
    cd Backend\agent-server
    python .\agent-server.py
    ```
1. From another terminal, run grpcurl with JSON inputs of choice against the RPC call you want to hit, and wait for response:
    ```
    grpcurl -plaintext -d '{\"numMissiles\": 50}' localhost:50051 agent.Agent/GetPlan
    ```

There's other grpcurl commands you can use to list all available methods from a server, pass in the JSON from a file, etc, but this so far is quickest way to sanity check the server by itself.