# from asyncio import Task
from models.types.pattern_instance import PatternInstance
from models.types.task import Task
from models.types.treatment import Treatment
from models.types.treatment_light import TreatmentLight
from models.types.task_light import TaskLight
from service.instance import Instance
from service.schema import Schema
from google.protobuf.json_format import MessageToDict

class API():
    def __init__(self):
        pass

    def get_patients(self, context, doctor_id):
        print("START get_patients API")
        instance = Instance()

        response = instance.GetPatients(doctor_id)
        response_patients = response.get('patients','')
        response_error = response.get('error',"None")

        if response_error!=None:
            return None, response_error
        

        response_dict = MessageToDict(response_patients)
        patients_array = list(set(response_dict.get('patientIds', [])))
        
        print("END get_patients API")
        return patients_array, None

    def get_instances(self, context, patient_id):
        print("START get_instances API")
        instance = Instance()
        
        response = instance.GetInstances(patient_id)
        response_instances = response.get('instances','')
        response_error = response.get('error',None)

        if response_error!=None:
            return None, response_error
        
        response_dict = MessageToDict(response_instances)
        treatments_array = response_dict.get('treatmentLight', [])
        
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
        response_instance = response.get('instance', '')
        response_error = response.get("error", None)
        if response_error != None:
            return None, response_error
        
        instance_dict = MessageToDict(response_instance)['treatment']
        pattern_instance_data = instance_dict['patternInstance']

        tasks_data = pattern_instance_data.get('tasks', [])

        tasks = []
        for task_data in tasks_data:
            
            task = Task(
                id=task_data['id'],
                level=task_data.get('level'),
                name=task_data['name'],
                status=task_data.get('status', 'PATTERN_INSTANCE_STATUS_UNSPECIFIED'),
                blockedBy=task_data.get('blockedBy', []),
                responsible=task_data.get('responsible', ''),
                timeLimit=task_data.get('timeLimit', 0),
                children=[Task(**child) for child in task_data.get('children', [])],
                comment=task_data.get('comment', '')
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
            treatment_id=instance_dict['treatmentId'],
            doctor_id=instance_dict['doctorId'],
            patient_id=instance_dict['patientId'],
            status=instance_dict['status'],
            pattern_instance=pattern_instance,
            started_at=instance_dict['startedAt'],
            finished_at=instance_dict['finishedAt'],
            deleted_at=instance_dict['deletedAt']
        )

        print("END get_instances API")
        return treatment, None
        
    def complete_task(self, context, instance_id, task_ids):
        print("START complete_task API")
        instance = Instance()
        response = instance.CompleteTasks(instance_id, task_ids)
        response_tasks = response.get('tasks', '')
        response_error = response.get('error', None)
        
        if response_error!=None:
            return [], response_error
        
        response_dict = MessageToDict(response_tasks)
        tasks_array = response_dict.get('tasks_light', [])
        
        if not tasks_array:
            return [], "Instance not found"
        
        task_lights = []
        for task_light_dict in tasks_array:
            task_light = TaskLight(
                id = task_light_dict["id"],
                status = task_light_dict["status"]
            )
            task_lights.append(task_light)
        print("END complete_task API")
        return task_lights, None
    
    def create_treatment(self, context, schema_id, patient_id, doctor_id):
        # 1 get schema
        schema, error = self.get_schema(context, schema_id)
        if error != None:
            return None, error
        else: 
            instance = Instance()
            response = instance.CreateTreatment(schema, patient_id, doctor_id)
            response_treatment = response.get('treatment')
            response_error = response.get('error')
            if response_error != '':
                return None, response_error
            else:
                treatment_dict = MessageToDict(response_treatment)
                treatment = treatment_dict.get('treatment', '')
                return treatment, None
    

    def get_schema(self, context, schema_id):
        print("START get_schema API")
        schema = Schema()

        response = schema.GetSchema(context, schema_id)
        response_schema = response.get('schema')
        response_error = response.get('error')
        print(response_schema)

        print("END get_schema API")
        if response_error != '':
            return None, response_error
        else:
            schema_dict = MessageToDict(response_schema)
            schema = schema_dict.get('schema', '')
            return schema, None
        

    def create_schema(self, context, tasks, author_id, schema_name):
        print("START create_schema API")
        
        schema = Schema()

        # author_id = request.get('author_id'
        response = schema.CreateSchema(context, tasks, author_id, schema_name)
        response_schema = response.get('schema')
        response_error = response.get('error')


        print("END create_schema API")
        if response_error != '':
            return response_error
        else:
            schema_dict = MessageToDict(response_schema)
            schema = schema_dict.get('schema', '')
            return schema
