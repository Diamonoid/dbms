from django.contrib import admin
from .models import User
from .models import Patient

from .models import PatientSymptom

from .models import LabStaffDoctor
from .models import Migrant
from .models import AssetAvailability
from .models import SampleCollected
from .models import SampleType
from .models import CriticalCase
from .models import Guideline

admin.site.register(User)
admin.site.register(Patient)

admin.site.register(PatientSymptom)
admin.site.register(LabStaffDoctor)
admin.site.register(Migrant)
admin.site.register(AssetAvailability)
admin.site.register(SampleCollected)
admin.site.register(SampleType)
admin.site.register(CriticalCase)
admin.site.register(Guideline)
# Register your models here.
