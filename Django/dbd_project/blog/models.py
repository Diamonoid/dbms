from django.db import models

class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    registration_date = models.DateField()
    status = models.CharField(max_length=50)
class LabStaffDoctor(models.Model):
    lab_staff_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    def __str__(self):
        return self.name
class AssetAvailability(models.Model):
    asset_id = models.AutoField(primary_key=True)
    asset_type = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    available_units = models.IntegerField()
    lab_staff = models.ForeignKey(LabStaffDoctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Asset {self.asset_type} at {self.location}"





class PatientSymptom(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.CharField(max_length=255)

    class Meta:
        unique_together = (('patient', 'symptom'),)

    def __str__(self):
        return f"{self.patient.name} - {self.symptom}"





class SampleCollected(models.Model):
    sample_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    collection_date = models.DateField()
    test_result = models.CharField(max_length=255)
    test_date = models.DateField()
    lab_staff = models.ForeignKey(LabStaffDoctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Sample {self.sample_id} for {self.patient.name}"


class SampleType(models.Model):
    sample = models.ForeignKey(SampleCollected, on_delete=models.CASCADE)
    sample_type = models.CharField(max_length=255)

    class Meta:
        unique_together = (('sample', 'sample_type'),)

    def __str__(self):
        return f"Sample {self.sample.sample_id} - {self.sample_type}"


class Migrant(models.Model):
    migrant_id = models.AutoField(primary_key=True)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    date_of_movement = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f"Migrant {self.migrant_id} from {self.origin} to {self.destination}"


class CriticalCase(models.Model):
    case_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    p_condition = models.CharField(max_length=255)
    critical_date = models.DateField()
    treatment_status = models.CharField(max_length=100)

    def __str__(self):
        return f"Critical Case {self.case_id} for {self.patient.name}"


class Guideline(models.Model):
    guideline_id = models.AutoField(primary_key=True)
    symptom = models.CharField(max_length=255)
    description = models.TextField()
    date_effective = models.DateField()
    critical_case = models.ForeignKey(CriticalCase, on_delete=models.CASCADE)

    def __str__(self):
        return f"Guideline for {self.symptom}"







class User(models.Model):
    ROLE_CHOICES = [
        ('Patient', 'Patient'),
        ('Doctor', 'Doctor'),
        ('Admin', 'Admin'),
    ]

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} - {self.role}"
