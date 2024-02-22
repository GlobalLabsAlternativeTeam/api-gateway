import json
from flask import Flask, jsonify
from flask import request
from server.api import API
from flask_api import status

app = Flask(__name__)
api = API()

# Get all the patients by doctor ID 
@app.route("/v1/users/patients/<doctor_id>", methods=['GET'])
def get_patients(doctor_id):
    # doctor_id = request.args.get('doctor_id')

    # Get the response from the API
    response, error = api.get_patients(request.headers, doctor_id)

    if error!=None:
        response = {"error": error}
        return response, 404


    # Return the response as a json object
    return jsonify(response), 200


# For the patient_id get all the treatments: ID, name, status, comlete percentage (?)
@app.route("/v1/instances/<patient_id>", methods=['GET'])
def get_instances(patient_id):
    # Get the response from the API
    response, error  = api.get_instances(request.headers, patient_id)
    
    if error!=None:
        response = {"error": error}
        return response, 404
    

    # Convert TreatmentLight objects to dictionaries
    treatments = []
    for treatment_light in response:
        treatment_dict = {
            "treatment_id": treatment_light.treatment_id,
            "treatment_name": treatment_light.treatment_name,
            "status": treatment_light.treatment_status,
            "treatment_progress": treatment_light.treatment_progress
        }
        treatments.append(treatment_dict)

    # Create the final dictionary with patient_id and treatments
    json_response = {
        "patient_id": patient_id,
        "treatments": treatments
    }

    return jsonify(json_response), 200


# Get the full treatment
@app.route("/v1/instance/", methods=['GET'])
def get_instance():
    instance_id = request.args.get('id')
    response, error = api.get_instance(request.headers, instance_id)
    
    if error != None:
        response = {"error": error}
        return response, 404
    
    treatment_dict = {
        "treatment_id": response.treatment_id,
        "doctor_id": response.doctor_id,
        "patient_id": response.patient_id,
        "status": response.status,
        "pattern_instance": {
            "instance_id": response.pattern_instance.instance_id,
            "status": response.pattern_instance.status,
            "pattern_id": response.pattern_instance.pattern_id,
            "author_id": response.pattern_instance.author_id,
            "pattern_name": response.pattern_instance.pattern_name,
            "created_at": response.pattern_instance.created_at,
            "updated_at": response.pattern_instance.updated_at,
            "deleted_at": response.pattern_instance.deleted_at,
            "tasks": [
                {
                    "id": task.id,
                    "level": task.level,
                    "name": task.name,
                    "status": task.status,
                    "blocked_by": task.blocked_by,
                    "responsible": task.responsible,
                    "time_limit": task.time_limit,
                    "children": [child.id for child in task.children],
                    "comment": task.comment
                }
                for task in response.pattern_instance.tasks
            ]
        },
        "started_at": response.started_at,
        "finished_at": response.finished_at,
        "deleted_at": response.deleted_at
    }

    # Convert dictionary to JSON
    return jsonify(treatment_dict)

@app.route("/v1/instances/create", methods=["POST"])
def create_instance():
    try: 
         data = request.json
    except Exception as e:
        return {"error": "Message is not a JSON string"}, 400
    try:
        schema_id = data["schema_id"]
    except Exception as e:
        return {"error": "Message does not contain schema_id"}, 400
    
    try: 
        patient_id = data["patient_id"]
    except Exception as e:
        return {"error": "Message does not contain patient_id"}, 400
    
    try: 
        doctor_id = data["doctor_id"]
    except Exception as e:
        return {"error": "Message does not contain doctor_id"}, 400
    
    response, error = api.create_treatment(request.headers, schema_id, patient_id, doctor_id)
    if error != None:
         return jsonify(error)

    else:
        return jsonify(response)

@app.route("/v1/instance/tasks/complete", methods=["POST"])
def complete_task():
    try:
        data = request.json
    except Exception as e:
        return {"error": "Message is not a JSON string"}, 400

    try:
        instance_id = data["instance_id"]
    except Exception as e:
        return {"error": "Message does not contain instance"}, 400
    
    try: 
        task_ids = data["task_ids"]
    except Exception as e:
        return {"error": "Message does not contain tasks"}, 400
    
    response, error = api.complete_task(request.headers, instance_id, task_ids)
    
    if error != "":
        response = {"error": error}
        return response, 404

    else:
        return response, 200


@app.route("/v1/schemas", methods=["GET"])
def get_schemas():
    return "Not implemented"

@app.route("/v1/schema/<schema_id>", methods=["GET"])
def get_schema(schema_id):
    
    response, error = api.get_schema(request.headers, schema_id)

    if error != None:
        return jsonify(error), 404
    else:
        return jsonify(response)
    # return "Not implemented"



@app.route("/v1/schema/update", methods=["GET"])
def update_schema():
    return "Not implemented"

@app.route("/v1/schema/create", methods=["POST"])
def create_schema():
    try: 
         data = request.json
    except Exception as e:
        return {"error": "Message is not a JSON string"}, 400
    try:
        doctor_id = data["doctor_id"]
    except Exception as e:
        return {"error": "Message does not contain doctor_id"}, 400
    
    try: 
        schema_name = data["schema_name"]
    except Exception as e:
        return {"error": "Message does not contain schema_name"}, 400
    
    try: 
        tasks = data["tasks"]
    except Exception as e:
        return {"error": "Message does not contain tasks"}, 400
    
    response = api.create_schema(request.headers, tasks, doctor_id, schema_name)
    return jsonify(response)



if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=1818)