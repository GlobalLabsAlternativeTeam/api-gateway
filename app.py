from flask import Flask
from flask import request
from server.api import API

app = Flask(__name__)
api = API()

# Get all the patients by doctor ID 
@app.route("/v1/users/patients", methods=['GET'])
def get_patients():
    doctor_id = request.args.get('doctor_id')
    return "Hello, World!"

# For the patient_id get all the treatments: ID, name, status, comlete percentage (?)
@app.route("/v1/instances/<patient_id>", methods=['GET'])
def get_instances(patient_id):
    response  = api.get_instances(request.headers, patient_id)
    return response

# Get the full treatment
@app.route("/v1/instance", methods=['GET'])
def get_instance():
    instance_id = request.args.get('instance_id')
    return "Hello, World!"

# Dont' need
@app.route("/v1/instance/status", methods=['GET'])
def get_instance_status():
    instance_id = request.args.get('instance_id')
    return "Hello, World"


@app.route("/v1/instance/task", methods=['GET'])
def get_task():
    instance_id = request.args.get('instance_id')
    task_id = request.args.get('task_id')
    return "Hello, World"

@app.route("/v1/instance/task/is_locked", methods=['GET'])
def is_task_locked():
    instance_id = request.args.get('instance_id')
    task_id = request.args.get('task_id')
    return "Hello, World"

@app.route("/v1/instance/task/status", methods=['GET'])
def get_task_status():
    instance_id = request.args.get('instance_id')
    task_id = request.args.get('task_id')
    return "Hello, World"


@app.route("/v1/schemas" , methods=['GET'])
def get_schemas():
    return "Hello, World"


@app.route("/v1/schemas/doctor", methods=['GET'])
def get_schemas_by_doctor_id():
    return "Hello world"




if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=1818)