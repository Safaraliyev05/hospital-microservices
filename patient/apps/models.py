from django.db.models import Model, CharField, DateField, TextField, DateTimeField, UUIDField


class Patient(Model):
    user = UUIDField()
    full_name = CharField(max_length=255)
    date_of_birth = DateField()
    gender = CharField(max_length=10, choices=[("male", "Male"), ("female", "Female"), ("other", "Other")])
    contact_number = CharField(max_length=15, blank=True, null=True)
    address = TextField(blank=True, null=True)
    emergency_contact = CharField(max_length=255, blank=True, null=True)
    medical_history = TextField(blank=True, null=True)
    allergies = TextField(blank=True, null=True)
    blood_group = CharField(max_length=3, blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
