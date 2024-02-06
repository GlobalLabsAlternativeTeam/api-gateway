from flask import Flask, jsonify
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
@app.route("/v1/instance", methods=['GET'])
def get_instance():
    instance_id = request.args.get('instance_id')
    return "Hello, World!"





if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=1818)