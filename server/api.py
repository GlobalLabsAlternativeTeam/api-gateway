from models.types.treatment_light import TreatmentLight
from service.instance import Instance
from google.protobuf.json_format import MessageToDict

class API():
    def __init__(self):
        pass

    def get_patients(self, context, request):
        pass

    def get_instances(self, context, patient_id):
        print("START get_instances API")
        instance = Instance()
        # patient_id = request.request.view_args('patient_id') 
        
        response = instance.GetInstances(patient_id)
        response_dict = MessageToDict(response)
        treatments_array =  response_dict['treatmentLight']
        
        treatment_lights = []
        for treatment_light_dict in treatments_array:
            
            treatment_light = TreatmentLight(
                treatment_id=treatment_light_dict['treatmentId'],
                treatment_name=treatment_light_dict['treatmentName'],
                treatment_status=treatment_light_dict['treatmentStatus'],
                treatment_progress=treatment_light_dict['treatmentProgress']
            )
            print(treatment_light)
            treatment_lights.append(treatment_light)
        print("END get_instances API")
        return treatment_lights

    def get_instance(self, context, request):
        pass
