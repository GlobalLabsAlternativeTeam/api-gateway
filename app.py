import json
from flask import Flask, jsonify
from flask import request
from server.api import API

app = Flask(__name__)
api = API()

# Get all the patients by doctor ID 
@app.route("/v1/users/patients/<doctor_id>", methods=['GET'])
def get_patients(doctor_id):
    # doctor_id = request.args.get('doctor_id')

    # Get the response from the API
    response = api.get_patients(request.headers, doctor_id)

    # Return the response as a json object
    return jsonify(response)


# For the patient_id get all the treatments: ID, name, status, comlete percentage (?)
@app.route("/v1/instances/<patient_id>", methods=['GET'])
def get_instances(patient_id):
    # Get the response from the API
    response = api.get_instances(request.headers, patient_id)
    
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

    return jsonify(json_response)


# Get the full treatment
@app.route("/v1/instance/", methods=['GET'])
def get_instance():
    instance_id = request.args.get('id')
    response = api.get_instance(request.headers, instance_id)
    
    # Assuming response is a Treatment object
    treatment = response

    # Convert Treatment object to a dictionary
    treatment_dict = {
        "treatment_id": treatment.treatment_id,
        "doctor_id": treatment.doctor_id,
        "patient_id": treatment.patient_id,
        "status": treatment.status,
        "pattern_instance": {
            "instance_id": treatment.pattern_instance.instance_id,
            "status": treatment.pattern_instance.status,
            "pattern_id": treatment.pattern_instance.pattern_id,
            "author_id": treatment.pattern_instance.author_id,
            "pattern_name": treatment.pattern_instance.pattern_name,
            "created_at": treatment.pattern_instance.created_at,
            "updated_at": treatment.pattern_instance.updated_at,
            "deleted_at": treatment.pattern_instance.deleted_at,
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
                for task in treatment.pattern_instance.tasks
            ]
        },
        "started_at": treatment.started_at,
        "finished_at": treatment.finished_at,
        "deleted_at": treatment.deleted_at
    }

    # Convert dictionary to JSON
    return jsonify(treatment_dict)

@app.route("/v1/instances/create", methods=["POST"])
def create_instance():
    try: 
         data = request.json
    except Exception as e:
        return {"error": "Message is not a JSON string"}
    try:
        schema_id = data["schema_id"]
    except Exception as e:
        return {"error": "Message does not contain schema_id"}
    
    try: 
        patient_id = data["patient_id"]
    except Exception as e:
        return {"error": "Message does not contain patient_id"}
    
    try: 
        doctor_id = data["doctor_id"]
    except Exception as e:
        return {"error": "Message does not contain doctor_id"}
    
    response, error = api.create_instance(request.headers, schema_id, patient_id, doctor_id)
    if error != "":
        return {"error": error}

    else:
        return response

@app.route("/v1/instance/tasks/complete", methods=["POST"])
def complete_task():
    try:
        data = request.json
    except Exception as e:
        return {"error": "Message is not a JSON string"}

    try:
        instance_id = data["instance_id"]
    except Exception as e:
        return {"error": "Message does not contain instance"}
    
    try: 
        task_ids = data["task_ids"]
    except Exception as e:
        return {"error": "Message does not contain tasks"}
    
    response, error = api.complete_task(request.headers, instance_id, task_ids)
    
    if error != "":
        return {"error": error}

    else:
        return response


@app.route("/v1/schemas", methods=["GET"])
def get_schemas():
    return "Not implemented"

@app.route("/v1/schema/<schema_id>", methods=["GET"])
def get_schema(schema_id):
    print(schema_id)
    return "Not implemented"



@app.route("/v1/schema/update", methods=["GET"])
def update_schema():
    return "Not implemented"

@app.route("/v1/schema/create", methods=["GET"])
def create_schema():
    return "Not implemented"



if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=1818)