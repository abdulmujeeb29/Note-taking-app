from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from noteapp.serializer import Noteserializer
from noteapp.models import Note 
from django.contrib.auth.models import User,auth 
from django.contrib import messages
from notebook import settings 
from django.core.mail import send_mail

# Create your views here.


@api_view(['GET', 'POST'])
def note_list(request):
    notes = Note.objects.all()
    if request.method == 'GET':
        serializer = Noteserializer(notes,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Noteserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else :
            return Response(serializer.errors)
        


# @api_view(['POST'])
# def note_create(request):
#     notes = Note.objects.all()
#     serializer = Noteserializer(data=request.data)
#     if serializer.is_valid:
#         serializer.save()
#         return Response(serializer.data)

#     else :
#         return Response(serializer.errors)



@api_view(['GET', 'PUT', 'DELETE'])
def note_particular(request,pk):
    notes = Note.objects.get(id=pk)

    if request.method == 'GET':
        serializer =Noteserializer(notes)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Noteserializer(notes, data=request.data)
        if serializer.is_valid() :
            return Response(serializer.data)

        else :
            return Response(serializer.errors)


    elif request.method == 'DELETE' :
        notes.delete()
        return Response('Succesfully deleted')





#Authentication

def signup(request):
    if request.method == 'POST':
        username =request.POST['username']
        fname =request.POST['fname']
        lname =request.POST['lname']
        email =request.POST['email']
        pass1 =request.POST['pass1']
        pass2 =request.POST['pass2']

        if pass1== pass2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('signup')


            elif User.objects.filter(username=username).exists() :
                messages.info(request,'Username already used')
                return redirect('signup')

            elif len(username) >10 :
                messages.info(request,'username must be less than 10 characters ')

            else:
                user = User.objects.create_user(username,email,pass1)
                user.save();
                #messages.success('Account has been succesfully created ')

                #welcome email activation
                subject = 'Welcome tO DJANGO notepad'     
                message = 'hello '+ user.username + 'Welcome to the notepad community '
                from_email = settings.EMAIL_HOST_USER 
                to_list = [user.email]
                send_mail(subject ,message ,from_email , to_list ,fail_silently=True  )


                return redirect('signin')

        else:
            messages.info(request,'Passwords does not correspond ')
            return redirect('signup')

    else:
        return render(request,'signup.html')




def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user =auth.authenticate(username=username,password=pass1)

        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            messages.info(request,'Invalid Credentials')
            return redirect ('signin')





    return render(request,'signin.html')


def signout(request):
    # auth.logout(request)
    # return redirect ('')
    return render(request,'signout.html')