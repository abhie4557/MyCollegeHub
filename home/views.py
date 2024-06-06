from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from resources.models import Paper
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout
from discussion.models import Discussion

def index(request): 
    return render(request, "home/index.html")

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc =request.POST['desc']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(desc)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, desc=desc)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "home/contact.html")

def search(request):
    query=request.GET['query']
    print(query)
    if len(query)>78:
        allDiscussions=Paper.objects.none()
    else:
        allDiscussionsTitle= Paper.objects.filter(subject__icontains=query)
        allDiscussionsAuthor= Paper.objects.filter(course__icontains=query)
        allDiscussionsContent =Paper.objects.filter(semester__icontains=query)
        allDiscussions=  allDiscussionsTitle.union(allDiscussionsContent, allDiscussionsAuthor)
    if allDiscussions.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allDiscussions': allDiscussions, 'query': query}
    print(params)
    print(allDiscussions)
    return render(request, 'home/search.html', params)

def searchdiscussion(request):
    query=request.GET['query']
    print(query)
    if len(query)>78:
        Result=Discussion.objects.none()
    else:
        allDiscussionsTitle= Discussion.objects.filter(title__icontains=query)
        allDiscussionsAuthor= Discussion.objects.filter(author__icontains=query)
        allDiscussionsContent =Discussion.objects.filter(content__icontains=query)
        allDiscussions=  allDiscussionsTitle.union(allDiscussionsContent, allDiscussionsAuthor)
    if allDiscussions.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allDiscussions': allDiscussions, 'query': query}
    print(params)
    print(allDiscussions)
    return render(request, 'home/search.html', params)

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        print(username)
        # check for errorneous input
        if len(username)>20:
            messages.error(request, " Your username must be under 20 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your MyCollegeHub account has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")


def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        print(loginusername)
        print(loginpassword)
        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")
    return render(request, 'home/login.html')
   

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')


def about(request): 
    return render(request, "home/about.html")
