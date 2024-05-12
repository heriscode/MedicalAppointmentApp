import datetime
from MedicalApp.allergy import Allergy
from ..user import User, MedicalPatient
from oracledb import IntegrityError
from ..appointments import Appointments



class FakeDB:

    def __init__(self):
        self.allergies = [Allergy(1,"Peanuts","Allergic reaction to peanuts causing hives and swelling."), Allergy(2,"Penicillin","Allergic reaction to penicillin causing difficulty breathing and rash.")]
        self.patients = []
        #                                  weight, email,              password,                                                                                                                                                            first_name, last_name, access_level, dob,              blood_type, height, allergies=None, avatar_path=None, id=None
        self.patients.append(MedicalPatient(68.0, "maddie@example.com","scrypt:32768:8:1$FGTAHUp5LISWRIg8$7353fe1b7e4599016f3dfd29dc2f478bb00fbb1ca016572a3c84e82b8866c4785958b4933ed90dc2fd01f1a217478843aa634f3cab2e97f7b1eb2c4ac8540e68", "Maddie", "Buckley", "PATIENT", datetime.date(1985,10,5), "O-", 168.0, allergies=[self.allergies[0]], id=6))
        self.patients.append(MedicalPatient(70.2, "chimney@example.com", "scrypt:32768:8:1$FGTAHUp5LISWRIg8$7353fe1b7e4599016f3dfd29dc2f478bb00fbb1ca016572a3c84e82b8866c4785958b4933ed90dc2fd01f1a217478843aa634f3cab2e97f7b1eb2c4ac8540e68", "Howard", "Han", "PATIENT", datetime.date(1985,10,5), "A+", 168.0, id=7))
        self.patients.append(MedicalPatient(75.2, "eddie@example.com", "scrypt:32768:8:1$FGTAHUp5LISWRIg8$7353fe1b7e4599016f3dfd29dc2f478bb00fbb1ca016572a3c84e82b8866c4785958b4933ed90dc2fd01f1a217478843aa634f3cab2e97f7b1eb2c4ac8540e68", "Eddie", "Diaz", "PATIENT", datetime.date(1985,10,5), "B+", 170.0, id=8))
        self.users = []
        self.users.append(User("maddie@example.com","scrypt:32768:8:1$FGTAHUp5LISWRIg8$7353fe1b7e4599016f3dfd29dc2f478bb00fbb1ca016572a3c84e82b8866c4785958b4933ed90dc2fd01f1a217478843aa634f3cab2e97f7b1eb2c4ac8540e68", "Maddie", "Buckley", "PATIENT"))
        self.users.append(User("chimney@example.com", "scrypt:32768:8:1$FGTAHUp5LISWRIg8$7353fe1b7e4599016f3dfd29dc2f478bb00fbb1ca016572a3c84e82b8866c4785958b4933ed90dc2fd01f1a217478843aa634f3cab2e97f7b1eb2c4ac8540e68", "Howard", "Han", "PATIENT"))
        self.users.append(User("eddie@example.com", "scrypt:32768:8:1$FGTAHUp5LISWRIg8$7353fe1b7e4599016f3dfd29dc2f478bb00fbb1ca016572a3c84e82b8866c4785958b4933ed90dc2fd01f1a217478843aa634f3cab2e97f7b1eb2c4ac8540e68", "Eddie", "Diaz", "PATIENT"))
        self.users.append(User("bobby@example.com", "scrypt:32768:8:1$FGTAHUp5LISWRIg8$7353fe1b7e4599016f3dfd29dc2f478bb00fbb1ca016572a3c84e82b8866c4785958b4933ed90dc2fd01f1a217478843aa634f3cab2e97f7b1eb2c4ac8540e68", "Bobby", "Nash", "DOCTOR"))
        self.appointments = []

    def get_appointment_by_id(self, appointment_id):
        for appointment in self.appointments:
            if appointment.id == appointment_id:
                return appointment
        return None

    def get_appointments(self):
        return self.appointments

    def add_appointment(self, appointment):
        if not isinstance(appointment, Appointments):
            raise TypeError("Invalid appointment type")
        self.appointments.append(appointment)
        
    def get_patient_allergies(self, patient_id):
        if (patient_id is None):
            raise ValueError("Parameters cannot be none")
        try:
            patient_id = int(patient_id)
        except:
            raise TypeError("Parameters of incorrect type")
        
        patient = self.get_patients_by_id(patient_id)
        return patient.allergies

    def get_patients_page_number(self, page, first_name, last_name):
        if (page is None):
            raise ValueError("Parameters cannot be none")
        if (first_name is not None and not isinstance(first_name, str) or last_name is not None and not isinstance(last_name, str)):
            raise TypeError("Parameters of incorrect type")
        
        try:
            page = int(page)
        except:
            raise TypeError("Parameters of incorrect type")
        
        patients = []
        offset=((page - 1)*2)
        count=2
        
        for i in range(offset, count+offset):
            print("i:", i)
            print("index:", i)
            patient = self.patients[i]
            print("Patient:", patient)
            if first_name is None and last_name is None:
                patients.append(patient)
            if first_name is not None and patient.first_name == first_name:
                patients.append(patient)
            if last_name is not None and patient.last_name == last_name:
                patients.append(patient)
        return patients
    
    def get_patients_by_id(self, patient_id):
        if (patient_id is None):
            raise ValueError("Parameters cannot be none")
        try:
            patient_id = int(patient_id)
        except:
            raise TypeError("Parameters of incorrect type")
        
        patient = None
        for patient in self.patients:
            if patient.id == patient_id:
                return patient
        return patient

    def run_file(self, file_path):
        pass

    def close(self):
        pass
