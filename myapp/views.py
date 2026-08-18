
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def login(request):
    return render(request, "login.html")
def login_post(request):

    username = request.POST['username']
    password = request.POST['password']
    usertype = request.POST['type']
    try:
        obj = Login.objects.get(
            username=username,
            password=password,
            usertype=usertype
        )

        request.session['lid'] = obj.id

        if obj.usertype == "admin":
           return redirect('/admin_home/')
        elif obj.usertype == "student":
            student = Student.objects.get(LOGIN=obj)
            request.session['sid'] = student.id
            return redirect('/student_home/')
    except:

        return HttpResponse("""<script>alert("Invalid Username or Password"); window.location="/";</script>""")
def admin_home(request):
    return render(request, "adminhome.html")
def add_teacher(request):
    return render(request, "add_teacher.html")
def add_teacher_post(request):
    name = request.POST['name']
    department = request.POST['department']
    email = request.POST['email']
    teacher = Teacher()
    teacher.name = name
    teacher.department = department
    teacher.email = email
    teacher.save()
    return HttpResponse("""<script>alert("Teacher Added Successfully");window.location="/add_teacher/";</script>""")
def view_teacher(request):
    data = Teacher.objects.all()
    return render(request,"view_teacher.html",{'data': data})
def edit_teacher(request, id):
    data = Teacher.objects.get(id=id)
    return render(request,"edit_teacher.html",{'data': data})
def edit_teacher_post(request):
    id = request.POST['id']
    teacher = Teacher.objects.get(id=id)
    teacher.name = request.POST['name']
    teacher.department = request.POST['department']
    teacher.email = request.POST['email']
    teacher.save()
    return HttpResponse("""<script>alert("Teacher Updated Successfully"); window.location="/view_teacher/";</script>""")
def delete_teacher(request, id):
    Teacher.objects.get(id=id).delete()
    return HttpResponse("""<script>alert("Teacher Deleted Successfully");window.location="/view_teacher/";</script>""")
def logout(request):
    request.session.flush()
    return redirect("/")
def student_register(request):
    return render(request, "student_register.html")
def student_register_post(request):
    name = request.POST['name']
    rollno = request.POST['rollno']
    department = request.POST['department']
    semester = request.POST['semester']
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    if Login.objects.filter(username=username).exists():
        return HttpResponse("""<script>alert("Username Already Exists");window.location="/student_register/";</script>""")
    log = Login()
    log.username = username
    log.password = password
    log.usertype = "student"
    log.save()
    student = Student()
    student.LOGIN = log
    student.name = name
    student.rollno = rollno
    student.department = department
    student.semester = semester
    student.email = email
    student.save()
    return HttpResponse("""<script>alert("Registration Successful");window.location="/";</script>""")
def student_home(request):
    student = Student.objects.get(id=request.session['sid'])
    return render(request,"student_home.html",{'student': student})
def student_profile(request):
    student = Student.objects.get(id=request.session['sid'])
    return render(request,"student_profile.html",{'student': student})
def send_complaint(request):
    teacher = Teacher.objects.all()
    return render(request,"send_complaint.html", {'teacher': teacher})
def send_complaint_post(request):
    student = Student.objects.get(id=request.session['sid'])
    complaint_type = request.POST['complaint_type']
    title = request.POST['title']
    complaint = request.POST['complaint']
    obj = Complaint()
    obj.STUDENT = student
    if complaint_type == "Faculty":
        teacher = Teacher.objects.get(id=request.POST['teacher'])
        obj.TEACHER = teacher
    obj.complaint_type = complaint_type
    obj.title = title
    obj.complaint = complaint
    obj.status = "Pending"
    obj.reply = "Waiting for Reply"
    obj.save()
    return HttpResponse("""<script>alert("Complaint Submitted Successfully"); window.location="/student_home/";</script>""")
def complaint_history(request):
    student = Student.objects.get(id=request.session['sid'])
    data = Complaint.objects.filter(STUDENT=student)
    return render(request,"complaint_history.html",{'data': data})
def view_complaints(request):
    data = Complaint.objects.all().order_by('-id')
    return render(request,"view_complaints.html",{'data': data})
def reply(request, id):
    data = Complaint.objects.get(id=id)
    return render(request,"reply.html",{'data': data})
def reply_post(request):
    id = request.POST['id']
    reply = request.POST['reply']
    obj = Complaint.objects.get(id=id)
    obj.reply = reply
    obj.status = "Replied"
    obj.save()
    return HttpResponse("""<script>alert("Reply Sent Successfully");window.location="/view_complaints/";</script>""")
def view_students(request):
    data = Student.objects.all()
    return render(request,"view_students.html",{'data': data})
def view_students(request):
    data = Student.objects.all()
    return render(request,"view_students.html", {'data': data})
def edit_student(request, id):
    data = Student.objects.get(id=id)
    return render(request,"edit_student.html",{'data': data})
def edit_student_post(request):
    id = request.POST['id']
    student = Student.objects.get(id=id)
    student.name = request.POST['name']
    student.rollno = request.POST['rollno']
    student.department = request.POST['department']
    student.semester = request.POST['semester']
    student.email = request.POST['email']
    student.LOGIN.username = request.POST['username']
    student.LOGIN.password = request.POST['password']
    student.LOGIN.save()
    student.save()
    return HttpResponse("""<script>alert("Student Updated Successfully");window.location="/view_students/";</script>""")
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.LOGIN.delete()
    return HttpResponse("""<script>alert("Student Deleted Successfully");window.location="/view_students/";</script>""")