from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render

# views.py
from .models import Student

from .forms import StudentModelForm
from .forms import VendorForm

from django.views.generic import View
from django.http import HttpResponse


@login_required         # for function based we can give directly
def homepage(request):  # for returning to homepage purpose only
    return render(request, 'templates/index.html')


def logoutuser(request):
    return render(request, 'logout.html')

@login_required
def addAdmission(request):
    form = StudentModelForm
    studentform = {'form': form}
    #values = {'name':'Vishnu', 'age':'18', 'add':'India'}

    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
        return homepage(request)

    return render(request, 'admissions/addAdmission.html', studentform)

@login_required
def admissionsReport(request):
    #get records from the models table
    result = Student.objects.all()      #select * from Students
    #store it in a dictionay
    students = {'allstudents':result}   #{key : value}
    return render(request, 'admissions/admissionReport.html',students)

@login_required
@permission_required('admission.delete_student')    # ('appname.operation_modelname')
def deletestudent(request, id):
    s = Student.objects.get(id=id) #select * from admissions_student where id=idvalue
    s.delete()
    return admissionsReport(request)

@login_required
@permission_required('admissions.change_student')   # add, delete, change, view
def updatestudent(request,id):
    s = Student.objects.get(id=id)
    form = StudentModelForm(instance=s)
    dict = {'form': form}

    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=s)
        if form.is_valid():
            form.save()
        return admissionsReport(request)
        #return redirect('/ad/admr')        install redirect and check

    return render(request, 'admissions/updateadm.html',dict)

@login_required
def addVendor(request):
    form = VendorForm
    vform = {'form': form}

    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])    #prints in the terminal through cleaned data dictionary
            print(form.cleaned_data['address'])
        return homepage(request)

    return render(request, 'admissions/add vendor.html', vform)


#class based view       we need to give @login_required in urls
class FirstClassBasedView(View):
    def get(self,request):
        return HttpResponse('Hello, this is class based view')


from django.views.generic import ListView
from .models import Teacher
# reading from database through class based view
class TeacherRead(ListView):
    #It automatically creates ORM statement (result = Students.objects.all() )              LIKE admissionReport module
    #creates dictionary and sends it to the templates automatically
    #default context name ( object that receives all the objects from ORM) is modelname_list ; teacher_list is the context object name
    #you can also specify custom context object name by "  context_Obiect_name—'result'  "

    #By default it sends to the template teacher_list.html or custom -> template_name = 'tlist.html'
    model = Teacher


from django.views.generic import DetailView
#for Retriveing only single teacher
class GetTeacher(DetailView):
    model = Teacher


from django.views.generic import CreateView
#create operation
class AddTeacher(CreateView):
    model = Teacher     #model attribute = modelname
    fields = ('name', 'exp', 'subject', 'contact')

from django.views.generic import UpdateView
class UpdateTeacher(UpdateView):
    model = Teacher
    # Only the attributes which are mentioned in the fields
    fields = ('name', 'contact')
   # success_url = custom ; rather than using teacher_form.html


from django.views.generic import DeleteView
from django.urls import reverse_lazy
class DeleteTeacher(DeleteView):
    model = Teacher
    success_url = reverse_lazy('listteachers')
# while providing value to the success_url attribute we need to use reverse_lazy instead of reverse