class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def patient_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class MedicalRecord:
    def __init__(self, disease, medicine):
        self.disease = disease
        self.medicine = medicine

    def diagnosis(self):
        print(f"Disease: {self.disease}")

    def prescription(self):
        print(f"Medicine: {self.medicine}")

class Hospital(Patient, MedicalRecord):
    def __init__(self, name, age, disease, medicine):
        Patient.__init__(self, name, age)
        MedicalRecord.__init__(self, disease, medicine)

    def show_complete_record(self):
        self.patient_details()
        self.diagnosis()
        self.prescription()

h = Hospital("Rahul", 25, "Fever", "Paracetamol")
h.show_complete_record()


