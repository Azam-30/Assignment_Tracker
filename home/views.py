from django.shortcuts import render, redirect, get_object_or_404
from .models import Student,DataStructuresStudent
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth import authenticate,login,logout
from django.db.models import Sum, Case, When, IntegerField
import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html')

# def load_data(request):
#     if request.method == 'POST':
#         roll_no = request.POST.get('roll_no')

#         python_data = list(Student.objects.filter(roll_no=roll_no).values())
#         data_structures_data = list(DataStructuresStudent.objects.filter(roll_no=roll_no).values())

#         def count_yes(assignments):
#             return sum(1 for assignment in assignments if assignment == 'yes')

#         python_counts = []
#         for data in python_data:
#             assignments = [data[f'assignment{i}'] for i in range(1, 7)]
#             python_counts.append(count_yes(assignments))

#         data_structures_counts = []
#         for data in data_structures_data:
#             assignments = [data[f'assignment{i}'] for i in range(1, 7)]
#             data_structures_counts.append(count_yes(assignments))

#         # Combine the counts into single values (assuming only one roll_no at a time)
#         python_count = python_counts[0] if python_counts else 0
#         data_structures_count = data_structures_counts[0] if data_structures_counts else 0

#         return JsonResponse({
#             'python_data': python_data,
#             'data_structures_data': data_structures_data,
#             'python_count': python_count,
#             'data_structures_count': data_structures_count,
#         })

#     return JsonResponse({'error': 'Invalid request'}, status=400)

def load_data(request):
    if request.method == 'POST':
        roll_no = request.POST.get('roll_no')
        if not roll_no:
            return JsonResponse({'error': 'Roll number is required'}, status=400)

        python_data = list(Student.objects.filter(roll_no=roll_no).values())
        data_structures_data = list(DataStructuresStudent.objects.filter(roll_no=roll_no).values())

        def count_yes(assignments):
            return sum(1 for assignment in assignments if assignment == 'yes')

        python_count = count_yes([data[f'assignment{i}'] for data in python_data for i in range(1, 7)]) if python_data else 0
        data_structures_count = count_yes([data[f'assignment{i}'] for data in data_structures_data for i in range(1, 7)]) if data_structures_data else 0

        return JsonResponse({
            'python_data': python_data,
            'data_structures_data': data_structures_data,
            'python_count': python_count,
            'data_structures_count': data_structures_count,
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)

def login_view(request):
    return render(request, 'login.html')


def validate_login(request):
    error_message = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('subject_selection')
        else:
            error_message = "Invalid credentials. Please try again."

    return render(request, "login.html", {"error_message": error_message})

@login_required(login_url='login')
def subject_selection_view(request):
    return render(request, 'subject_selection.html')

@login_required(login_url='login')
def python_assignments_view(request):
    # Redirect to the Python student list page
    return redirect('python_student_list')



"""def validate_login(request):
    error_message = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_list')
        else:
            error_message = "Invalid credentials. Please try again."

    return render(request, "login.html", {"error_message": error_message})"""


@login_required(login_url='login')
def LogoutPage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def python_student_list(request):
    students = Student.objects.all()
    return render(request, 'python_student_list.html', {'students': students})

@login_required(login_url='login')
def python_student_create(request):
    if request.method == 'POST':
        roll_no = request.POST['roll_no']
        assignment1 = request.POST['assignment1']
        assignment2 = request.POST['assignment2']
        assignment3 = request.POST['assignment3']
        assignment4 = request.POST['assignment4']
        assignment5 = request.POST['assignment5']
        assignment6 = request.POST['assignment6']
        
        student = Student(
            roll_no=roll_no, assignment1=assignment1, assignment2=assignment2,
            assignment3=assignment3, assignment4=assignment4, assignment5=assignment5,
            assignment6=assignment6
        )
        student.save()

        return redirect('python_student_list')

    return render(request, 'python_student_form.html')

@login_required(login_url='login')
def python_student_update(request, roll_no):
    student = get_object_or_404(Student, roll_no=roll_no)

    if request.method == 'POST':
        student.assignment1 = request.POST['assignment1']
        student.assignment2 = request.POST['assignment2']
        student.assignment3 = request.POST['assignment3']
        student.assignment4 = request.POST['assignment4']
        student.assignment5 = request.POST['assignment5']
        student.assignment6 = request.POST['assignment6']
        student.save()

        return redirect('python_student_list')

    return render(request, 'python_student_form.html', {'student': student})

@login_required(login_url='login')
def python_student_delete(request, roll_no):
    student = get_object_or_404(Student, roll_no=roll_no)

    if request.method == 'POST':
        student.delete()
        return redirect('python_student_list')

    return render(request, 'python_student_confirm_delete.html', {'student': student})

@login_required(login_url='login')
def python_student_search(request):
    no_records_found = False
    search_term = ''

    if request.method == 'POST':
        search_term = request.POST.get('search_term', '')

        # Filter the students based on the search term
        filtered_students = Student.objects.filter(
            roll_no__icontains=search_term
        )

        # Check if any records were found
        if not filtered_students.exists():
            no_records_found = True
        else:
            # Calculate total assignments submitted
            total_assignments_submitted = filtered_students.aggregate(
                total_submitted=Sum(
                    Case(
                        When(assignment1='yes', then=1),
                        When(assignment2='yes', then=1),
                        When(assignment3='yes', then=1),
                        When(assignment4='yes', then=1),
                        When(assignment5='yes', then=1),
                        When(assignment6='yes', then=1),
                        output_field=IntegerField()
                    )
                )
            )['total_submitted']

            # Prepare search results
            search_results = filtered_students

            return render(request, 'python_student_search.html', {
                'search_results': search_results,
                'search_term': search_term,
                'total_assignments_submitted': total_assignments_submitted,
            })

    return render(request, 'python_student_search.html', {'no_records_found': no_records_found})

@login_required(login_url='login')
def data_structures_student_list(request):
    students = DataStructuresStudent.objects.all()
    return render(request, 'data_structures_student_list.html', {'students': students})

@login_required(login_url='login')
def data_structures_student_create(request):
    if request.method == 'POST':
        roll_no = request.POST['roll_no']
        assignment1 = request.POST['assignment1']
        assignment2 = request.POST['assignment2']
        assignment3 = request.POST['assignment3']
        assignment4 = request.POST['assignment4']
        assignment5 = request.POST['assignment5']
        assignment6 = request.POST['assignment6']
        
        student = DataStructuresStudent(
            roll_no=roll_no, assignment1=assignment1, assignment2=assignment2,
            assignment3=assignment3, assignment4=assignment4, assignment5=assignment5,
            assignment6=assignment6
        )
        student.save()

        return redirect('data_structures_student_list')

    return render(request, 'data_structures_student_form.html')

@login_required(login_url='login')
def data_structures_student_update(request, roll_no):
    student = get_object_or_404(DataStructuresStudent, roll_no=roll_no)

    if request.method == 'POST':
        student.assignment1 = request.POST['assignment1']
        student.assignment2 = request.POST['assignment2']
        student.assignment3 = request.POST['assignment3']
        student.assignment4 = request.POST['assignment4']
        student.assignment5 = request.POST['assignment5']
        student.assignment6 = request.POST['assignment6']
        student.save()

        return redirect('data_structures_student_list')

    return render(request, 'data_structures_student_form.html', {'student': student})

@login_required(login_url='login')
def data_structures_student_delete(request, roll_no):
    student = get_object_or_404(DataStructuresStudent, roll_no=roll_no)

    if request.method == 'POST':
        student.delete()
        return redirect('data_structures_student_list')

    return render(request, 'data_structures_student_confirm_delete.html', {'student': student})

@login_required(login_url='login')
def data_structures_student_search(request):
    no_records_found = False
    search_term = ''

    if request.method == 'POST':
        search_term = request.POST.get('search_term', '')

        # Filter the students based on the search term
        filtered_students = DataStructuresStudent.objects.filter(
            roll_no__icontains=search_term
        )

        # Check if any records were found
        if not filtered_students.exists():
            no_records_found = True
        else:
            # Calculate total assignments submitted
            total_assignments_submitted = filtered_students.aggregate(
                total_submitted=Sum(
                    Case(
                        When(assignment1='yes', then=1),
                        When(assignment2='yes', then=1),
                        When(assignment3='yes', then=1),
                        When(assignment4='yes', then=1),
                        When(assignment5='yes', then=1),
                        When(assignment6='yes', then=1),
                        output_field=IntegerField()
                    )
                )
            )['total_submitted']

            # Prepare search results
            search_results = filtered_students

            return render(request, 'data_structures_student_search.html', {
                'search_results': search_results,
                'search_term': search_term,
                'total_assignments_submitted': total_assignments_submitted,
            })

    return render(request, 'data_structures_student_search.html', {'no_records_found': no_records_found})
