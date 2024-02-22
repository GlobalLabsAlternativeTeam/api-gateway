# API Gateway

Gateway service that is in charge of redirecting the requests to the different microservices to complete the user original request.

## Dependencies

In order to generate the interfaces using `proto`, you will need to install some previous dependencies:
```bash
python3 -m pip install --upgrade pip
python3 -m pip install grpcio
python3 -m pip install grpcio-tools

```

In order to run the server, you will also need `Flask`:
```bash
python3 -m pip install --upgrade pip
python3 -m pip install flask
```

## Usage

### Generating proto interfaces

In order to run the service, we first need to **generate the interfaces** using protoc.

To do this, run the following command from the root directory:

```bash
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. proto/process_execution_service/service.proto
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. proto/schema_service/schema_service.proto
```

### Running the service

You can now launch the server using:

```bash
python3 app.py
```
