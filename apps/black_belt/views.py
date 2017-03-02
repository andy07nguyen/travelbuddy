from django.shortcuts import render, redirect, HttpResponse
from .models import User, Trip
from django.contrib import messages
# Create your views here.
def index(request):
    # request.session.delete()
    request.session['magic'] = 'nhgbhnv'
    return render(request, 'black_belt/index.html')

def process(request):
    if request.method == "GET":
        messages.success(request, "Nice try!")
        return redirect('/')
    user = User.objects.register(request.POST)
    if user[0] == True:
        messages.success(request, 'Successful Registration! Please Log in')
        request.session['id'] = user[1].id
        request.session['magic'] = 'registered'
    else:
        for i in user[1]:
            print i
            messages.success(request, i)
        return redirect('/')
    return redirect('/success')

def loginProcess(request):
    if request.method == "GET":
        messages.success(request, "Nice try!")
        return redirect("/")
    frogs = User.objects.login(request.POST['emailLogin'], request.POST['pwLogin'])
    if frogs[0] == True:
        messages.success(request, 'Successful Logged In!')
        request.session['id'] = frogs[2].id
        request.session['magic'] = 'loggedin'
    else:
        for i in frogs[1]:
            messages.success(request, i)
        return redirect('/')
    return redirect('/success')

def success(request):
    if "id" not in request.session:
        return redirect('/')
    else:
        print request.session['magic']
        user = User.objects.get(id=request.session['id'])
        context = {
            "currentUser": user,
            "trip": Trip.objects.filter(joiner__id=request.session['id']),
            "OtherUserTripData": Trip.objects.exclude(joiner__id=request.session['id']),
        }
    return render(request, 'black_belt/success.html', context)

def add(request):
    return render(request, 'black_belt/add.html')

def addprocess(request):
    usertrip = Trip.objects.addtrips(request.POST, request.session['id'])
    if usertrip[0] == True:
        print "#"*20, usertrip[2], "#"*20
        messages.info(request, "Successful Added A New Trip!")
    else:
        for i in usertrip[1]:
            messages.info(request, i)
        return redirect('/add')
    return redirect('/success')

def join(request, id):
    join = Trip.objects.join(id, request.session['id'])
    if join[0] == True:
        messages.info(request, "Successful Joined A Trip!")
        return redirect('/success')
    else:
        for i in join[1]:
            messages.info(request, i)
        return redirect('/success')
    return redirect('/success')

def show(request, id):
    context = {
        "user_trip": Trip.objects.filter(id = id),
        "other_users": User.objects.filter(join__id = id)
    }
    return render(request, 'black_belt/show.html', context)

def remove(request, id):
    context = {
        "trip": Trip.objects.filter(id=id)
    }
    return render(request, "black_belt/remove.html", context)

def delete(request, id):
    context = {
        "delete": Trip.objects.get(id=id).delete()
    }
    return redirect('/success', context)

def logout(request):
    if request.method == "GET":
        # messages.success(request, "Nice try!")
        return redirect("/")
    del request.session['id']
    return redirect('/')
