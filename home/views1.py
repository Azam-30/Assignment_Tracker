from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
import pandas as pd
from django.http import Http404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, 'index.html')

# @login_required(login_url='login')
# def student_list(request):
#     excel_file_path = 'static/assignmentData(1).xlsx'  # Update with the actual file path
#     df = pd.read_excel(excel_file_path)
#     students = []

#     for _, student_row in df.iterrows():
#         # Convert roll_no to string and add to the list
#         roll_no = str(student_row['roll_no'])
#         students.append(student_row.to_dict())

#     return render(request, 'student_list.html', {'students': students})
@login_required(login_url='login')
def student_list(request):
    excel_file_path = 'static/assignmentData(1).xlsx'
    df = pd.read_excel(excel_file_path)
    print(df)
    students = df.to_dict(orient='records')
    return render(request, 'student_list.html', {'students': students})



# @login_required(login_url='login')
# def student_create(request):
#     if request.method == 'POST':
#         roll_no = request.POST['roll_no']
#         assignment1 = request.POST['assignment1']
#         assignment2 = request.POST['assignment2']
#         assignment3 = request.POST['assignment3']
#         assignment4 = request.POST['assignment4']
#         assignment5 = request.POST['assignment5']
#         assignment6 = request.POST['assignment6']
#         # Repeat for other assignments
#         student = Student(roll_no=roll_no, assignment1=assignment1, assignment2=assignment2, assignment3=assignment3,assignment4=assignment4,assignment5=assignment5,assignment6=assignment6)
#         student.save()

#         # Update Excel file
#         data = pd.read_excel("static/assignmentData(1).xlsx")
#         new_row = {'roll_no': roll_no, 'assignment1': assignment1, 'assignment2': assignment2, 'assignment3': assignment3, 'assignment4': assignment4,'assignment5': assignment5, 'assignment6': assignment6,}
#         data = data.append(new_row, ignore_index=True)
#         data.to_excel("static/assignmentData(1).xlsx", index=False)

#         return redirect('student_list')
#     return render(request, 'student_form.html')

# @login_required(login_url='login')

@login_required(login_url='login')
def student_create(request):
    if request.method == 'POST':
        roll_no = request.POST['roll_no']
        assignment1 = request.POST['assignment1']
        assignment2 = request.POST['assignment2']
        assignment3 = request.POST['assignment3']
        assignment4 = request.POST['assignment4']
        assignment5 = request.POST['assignment5']
        assignment6 = request.POST['assignment6']
        
        # Save to database
        student = Student(
            roll_no=roll_no, assignment1=assignment1, assignment2=assignment2,
            assignment3=assignment3, assignment4=assignment4, assignment5=assignment5,
            assignment6=assignment6
        )
        student.save()

        # Update Excel file
        data = pd.read_excel("static/assignmentData(1).xlsx")
        new_row = {
            'roll_no': roll_no, 'assignment1': assignment1, 'assignment2': assignment2,
            'assignment3': assignment3, 'assignment4': assignment4, 'assignment5': assignment5,
            'assignment6': assignment6
        }
        new_row_df = pd.DataFrame([new_row])
        data = pd.concat([data, new_row_df], ignore_index=True)
        data.to_excel("static/assignmentData(1).xlsx", index=False)

        return redirect('student_list')
    return render(request, 'student_form.html')



# def student_update(request, roll_no):
#     # Convert roll_no to a string to match Excel data format
#     roll_no_str = str(roll_no)

#     # Check if a student with the given roll number exists in Excel data
#     excel_file_path = 'static/assignmentData(1).xlsx'
#     df = pd.read_excel(excel_file_path)

#     if roll_no_str in df['roll_no'].astype(str).values:
#         # Student exists in Excel data, update the existing data

#         if request.method == 'POST':
#             # Update Excel data
#             df.loc[df['roll_no'].astype(str) == roll_no_str, ['assignment1', 'assignment2', 'assignment3', 'assignment4', 'assignment5', 'assignment6']] = [
#                 request.POST['assignment1'], request.POST['assignment2'], request.POST['assignment3'],
#                 request.POST['assignment4'], request.POST['assignment5'], request.POST['assignment6'],
#             ]
#             df.to_excel(excel_file_path, index=False)

#             return redirect('student_list')

#         # Render the update form with the existing student data
#         student_data = df[df['roll_no'].astype(str) == roll_no_str].to_dict(orient='records')[0]
#         return render(request, 'student_form.html', {'student': student_data})
    
#     # If the roll number doesn't exist in the Excel data, raise a 404 error
#     raise Http404("Student not found in Excel data")

@login_required(login_url='login')
def student_update(request, roll_no):
    roll_no_str = str(roll_no)
    excel_file_path = 'static/assignmentData(1).xlsx'
    df = pd.read_excel(excel_file_path)

    if roll_no_str in df['roll_no'].astype(str).values:
        if request.method == 'POST':
            # Update Excel data
            df.loc[df['roll_no'].astype(str) == roll_no_str, ['assignment1', 'assignment2', 'assignment3', 'assignment4', 'assignment5', 'assignment6']] = [
                request.POST['assignment1'], request.POST['assignment2'], request.POST['assignment3'],
                request.POST['assignment4'], request.POST['assignment5'], request.POST['assignment6'],
            ]
            df.to_excel(excel_file_path, index=False)

            # Update database
            Student.objects.filter(roll_no=roll_no_str).update(
                assignment1=request.POST['assignment1'],
                assignment2=request.POST['assignment2'],
                assignment3=request.POST['assignment3'],
                assignment4=request.POST['assignment4'],
                assignment5=request.POST['assignment5'],
                assignment6=request.POST['assignment6']
            )

            return redirect('student_list')

        student_data = df[df['roll_no'].astype(str) == roll_no_str].to_dict(orient='records')[0]
        return render(request, 'student_form.html', {'student': student_data})

    raise Http404("Student not found in Excel data")



# @login_required(login_url='login')

# def student_delete(request, roll_no):
#     # Convert roll_no to a string to match Excel data format
#     roll_no_str = str(roll_no)
    
#     # Check if a student with the given roll number exists in Excel data
#     excel_file_path = 'static/assignmentData(1).xlsx'
#     df = pd.read_excel(excel_file_path)
    
#     if roll_no_str not in df['roll_no'].astype(str).values:
#         # Student not found in Excel data, handle the error
#         raise Http404("Student not found")
    
#     if request.method == 'POST':
#         # Delete from Excel data
#         df = df[df['roll_no'].astype(str) != roll_no_str]
#         df.to_excel(excel_file_path, index=False)

#         return redirect('student_list')
    
#     # Render the confirmation page
#     return render(request, 'student_confirm_delete.html', {'roll_no': roll_no_str})

@login_required(login_url='login')
def student_delete(request, roll_no):
    # Convert roll_no to a string to match Excel data format
    roll_no_str = str(roll_no)
    
    # Check if a student with the given roll number exists in Excel data
    excel_file_path = 'static/assignmentData(1).xlsx'
    df = pd.read_excel(excel_file_path)
    
    if roll_no_str not in df['roll_no'].astype(str).values:
        # Student not found in Excel data, handle the error
        raise Http404("Student not found")
    
    if request.method == 'POST':
        # Delete from database
        student = get_object_or_404(Student, roll_no=roll_no)
        student.delete()

        # Delete from Excel data
        df = df[df['roll_no'].astype(str) != roll_no_str]
        df.to_excel(excel_file_path, index=False)

        return redirect('student_list')
    
    # Render the confirmation page
    return render(request, 'student_confirm_delete.html', {'roll_no': roll_no_str})



# @login_required(login_url='login')

# def student_search(request):
#     no_records_found = False  # Initialize a variable to track if no records are found
#     search_term = '' 

#     if request.method == 'POST':
#         # Get the search term from the form
#         search_term = request.POST.get('search_term', '')

#         # Load the Excel data
#         excel_file_path = 'static/assignmentData(1).xlsx'
#         df = pd.read_excel(excel_file_path)

#         # Filter the data based on the search term (assuming the search term is part of the roll number)
#         filtered_data = df[df['roll_no'].astype(str).str.contains(search_term, case=False)]

#         if filtered_data.empty:
#             # No records found for the search term
#             no_records_found = True
#         else:
#             # Calculate the number of assignments submitted for each matching record
#             filtered_data['assignments_submitted'] = filtered_data.apply(
#                 lambda row: sum(1 for assignment in ['assignment1', 'assignment2', 'assignment3', 'assignment4', 'assignment5', 'assignment6'] if row[assignment] == 'yes'),
#                 axis=1
#             )

#             # Calculate the total number of assignments submitted
#             total_assignments_submitted = filtered_data['assignments_submitted'].sum()

#             # Convert the filtered data to a list of dictionaries for rendering
#             search_results = filtered_data.to_dict(orient='records')

#             return render(request, 'student_search.html', {
#                 'search_results': search_results,
#                 'search_term': search_term,
#                 'total_assignments_submitted': total_assignments_submitted,
#             })

#     return render(request, 'student_search.html', {'no_records_found': no_records_found})


@login_required(login_url='login')
def student_search(request):
    no_records_found = False  # Initialize a variable to track if no records are found
    search_term = ''

    if request.method == 'POST':
        # Get the search term from the form
        search_term = request.POST.get('search_term', '')

        # Load the Excel data
        excel_file_path = 'static/assignmentData(1).xlsx'
        df = pd.read_excel(excel_file_path)

        # Filter the data based on the search term (assuming the search term is part of the roll number)
        filtered_data = df[df['roll_no'].astype(str).str.contains(search_term, case=False)]

        if filtered_data.empty:
            # No records found for the search term
            no_records_found = True
        else:
            # Calculate the number of assignments submitted for each matching record
            filtered_data['assignments_submitted'] = filtered_data.apply(
                lambda row: sum(1 for assignment in ['assignment1', 'assignment2', 'assignment3', 'assignment4', 'assignment5', 'assignment6'] if row[assignment] == 'yes'),
                axis=1
            )

            # Convert the filtered data to a list of dictionaries for rendering
            search_results = filtered_data.to_dict(orient='records')
            total_assignments_submitted = filtered_data['assignments_submitted'].sum()

            return render(request, 'student_search.html', {
                'search_results': search_results,
                'search_term': search_term,
                'total_assignments_submitted': total_assignments_submitted,
            })

    return render(request, 'student_search.html', {'no_records_found': no_records_found})


def login_view(request):
    return render(request, 'login.html')


def validate_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username,password)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('student_list')
       
        else:
            # Invalid credentials, display an error message
            error_message = "Invalid credentials. Please try again."

    return render(request, "login.html", {"error_message": error_message})


@login_required(login_url='login')
def LogoutPage(request):
    logout(request)
    return redirect('login')