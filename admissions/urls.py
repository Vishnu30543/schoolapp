from django.urls import path

from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('addadm/',views.addAdmission),
    path('admr/', views.admissionsReport),
    path('addven/', views.addVendor),
    path('delete/<int:id>', views.deletestudent),
    path('update/<int:id>', views.updatestudent),

    path('firstcbv/', login_required(views.FirstClassBasedView.as_view())),
    path('teacherslist/', login_required(views.TeacherRead.as_view()), name='listteachers'),
    path('getteacherdetails/<int:pk>', login_required(views.GetTeacher.as_view()), name='teacherdetails'),
    # pk primary key
    path('insertteacher/', login_required(views.AddTeacher.as_view())),
    path('updateteacher/<int:pk>', login_required(views.UpdateTeacher.as_view())),


]