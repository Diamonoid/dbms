from django.shortcuts import render

def login(request):
    return render (request,'blog/HTML_FOR_FRONT_END.html')
def admin(request):
    return render (request,'blog/admin_dashboard.html')


def patient(request):
    return render (request,'blog/patient_dashboard.html')
def doctor(request):
    return render(request, 'blog/doctor_lab_dashboard.html')





from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .models import User

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User as uuser  # Assuming you have a CustomUser model with a role field
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Patient
def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            print(f"User found: {user}")  # Debugging print

            if user.password == password:  # In production, use password hashing
                if user.role == 'Doctor':
                    return redirect('Doctor')
                elif user.role == 'Patient':
                    # Use case-insensitive query for contact_info
                    patient = Patient.objects.filter(contact_info__iexact=email).first()
                    if patient:
                        print(f"Patient found: {patient}")  # Debugging print
                        return redirect('patient_dashboard', email=email)  # Pass email to redirect
                    else:
                        messages.error(request, "Patient information not found.")
                        return redirect('signin')
                else:
                    messages.error(request, "Invalid role assigned to user.")
                    return redirect('signin')
            else:
                messages.error(request, "Invalid email or password.")
                return redirect('signin')
                
        except User.DoesNotExist:
            messages.error(request, "User does not exist.")
            return redirect('signin')
        except Exception as e:
            messages.error(request, f"Error during sign in: {e}")
            return redirect('signin')

    return render(request, 'blog/HTML_FOR_FRONT_END.html')

def patient_dashboard(request, email):
    try:
        # Use case-insensitive lookup to retrieve patient data
        patient = Patient.objects.filter(contact_info__iexact=email).first()
        if not patient:
            messages.error(request, "Patient information not found.")
            return redirect('signin')

        print(f"Dashboard patient: {patient}")  # Debugging print

        lab_results = []  # Placeholder for actual lab results
        migrations = []   # Placeholder for actual migration data

        context = {
            'patient': {
                'id': f'P{patient.patient_id}',
                'name': patient.name,
                'dob': patient.dob,
                'gender': patient.gender,
                'address': patient.address,
                'registration_date': patient.registration_date,
                'status': patient.status,
                'contact_info': patient.contact_info
            },
            'lab_results': lab_results,
            'migrations': migrations
        }

        return render(request, 'blog/patient_dashboard.html', context)

    except Exception as e:
        messages.error(request, f"Error loading patient dashboard: {e}")
        return redirect('signin')


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Patient
from .models import User


def signup2(request):
    if request.method == 'POST':
        # Process the form data
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        registration_date = request.POST.get('registrationDate')
        status = request.POST.get('status')

        # Create a new Patient object
        patient = Patient(
            name=name,
            dob=dob,
            gender=gender,
            address=address,
            registration_date=registration_date,
            status=status,
            contact_info=email
        )
        patient.save()
        user=User(
            username=username,
            email=email,
            password=password,
            role='Patient'
        )
        user.save()


        messages.success(request, 'Patient registered successfully!')
        return redirect('signin')  # Redirect to a patient list view

    return render(request, 'blog/patient_reg.html')
from django.shortcuts import render
from .models import AssetAvailability, LabStaffDoctor, Guideline

def dashboard_view(request):
    """
    View to display all resources in the dashboard.
    Fetches all records from AssetAvailability, LabStaffDoctor, and Guideline models.
    """
    context = {
        'lab_staff_doctors': LabStaffDoctor.objects.all(),
        'assets': AssetAvailability.objects.all(),
        'guidelines': Guideline.objects.all(),
    }
    return render(request, 'blog/visitors_dashboard.html', context)

