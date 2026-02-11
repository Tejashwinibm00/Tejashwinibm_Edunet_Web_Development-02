<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.

def student_list(request):
    # sample data: usually its done by database query
    students = [
    {'name': 'John Doe', 'course': 'B.Sc Computer Science'},
    {'name': 'Jane Smith', 'course': 'B.A Economics'},
    {'name': 'Emily Johnson', 'course': 'B.Com Accounting'}

    ]
    # Context dictionary - keys will become variable names in template
    context ={'students':students}

    #Render the template and send the data
    return render(request, 'profiles/student_list.html',context)
=======
from django.shortcuts import render

# Create your views here.

def student_list(request):
    # sample data: usually its done by database query
    students = [
    {'name': 'John Doe', 'course': 'B.Sc Computer Science'},
    {'name': 'Jane Smith', 'course': 'B.A Economics'},
    {'name': 'Emily Johnson', 'course': 'B.Com Accounting'}

    ]
    # Context dictionary - keys will become variable names in template
    context ={'students':students}

    #Render the template and send the data
    return render(request, 'profiles/student_list.html',context)
>>>>>>> 86c0bec (Initial commit with large folder)
