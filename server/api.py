# from asyncio import Task
from models.types.pattern_instance import PatternInstance
from models.types.task import Task
from models.types.treatment import Treatment
from models.types.treatment_light import TreatmentLight
from service.instance import Instance
from google.protobuf.json_format import MessageToDict

class API():
    def __init__(self):
        pass

    def get_patients(self, context, doctor_id):
        print("START get_patients API")
        instance = Instance()
        
        response = instance.GetPatients(doctor_id)
        response_dict = MessageToDict(response)
        patients_array = response_dict['patients']

        print("END get_patients API")
        return patients_array

    def get_instances(self, context, patient_id):
        print("START get_instances API")
        instance = Instance()
        
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
            treatment_lights.append(treatment_light)
        print("END get_instances API")
        return treatment_lights

    def get_instance(self, context, instance_id):
        print("START get_instances API")
        instance = Instance()
        
        response = instance.GetInstance(instance_id)
        response_dict = MessageToDict(response)
        treatment_data = response_dict['treatment']

        pattern_instance_data = treatment_data['patternInstance']

        tasks_data = pattern_instance_data.get('tasks', [])



        tasks = []
        for task_data in tasks_data:
            task = Task(
                id=task_data['id'],
                level=task_data.get('level'),
                name=task_data['name'],
                status=task_data['status'],
                blockedBy=task_data.get('blockedBy', []),
                responsible=task_data['responsible'],
                timeLimit=task_data['timeLimit'],
                children=[Task(**child) for child in task_data.get('children', [])],
                comment=task_data.get('comment')
            )
            tasks.append(task)
        
        pattern_instance = PatternInstance(
            instance_id=pattern_instance_data['instanceId'],
            status=pattern_instance_data['status'],
            pattern_id=pattern_instance_data['patternId'],
            author_id=pattern_instance_data['authorId'],
            pattern_name=pattern_instance_data['patternName'],
            created_at=pattern_instance_data['createdAt'],
            updated_at=pattern_instance_data['updatedAt'],
            deleted_at=pattern_instance_data['deletedAt'],
            tasks=tasks
        )

        treatment = Treatment(
            treatment_id=treatment_data['treatmentId'],
            doctor_id=treatment_data['doctorId'],
            patient_id=treatment_data['patientId'],
            status=treatment_data['status'],
            pattern_instance=pattern_instance,
            started_at=treatment_data['startedAt'],
            finished_at=treatment_data['finishedAt'],
            deleted_at=treatment_data['deletedAt']
        )

        print("END get_instances API")
        return treatment
        
