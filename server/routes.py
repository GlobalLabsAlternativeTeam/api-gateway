from flask import Flask
from flask import request
import api as API

app = Flask(__name__)

@app.route("/v1/users/patients", methods=['GET'])
def get_patients():
    return "Hello, World!"


@app.route("/v1/instances", methods=['GET'])
def get_instances():
    patient_id = request.args.get('patient_id') # Should be extracted from the context 
    return "Hello, World!"


@app.route("/v1/instance", methods=['GET'])
def get_instance():
    instance_id = request.args.get('instance_id')
    return "Hello, World!"


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
    app.run(debug=True, port=5000)