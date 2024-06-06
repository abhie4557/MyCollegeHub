from django.shortcuts import render, HttpResponse, redirect
from discussion.models import Discussion, DiscussionComment
from django.contrib import messages
from django.contrib.auth.models import User
from discussion.templatetags import extras
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request): 
    alldiscussions= Discussion.objects.all()
    context={'alldiscussions': alldiscussions}
    print(context)
    return render(request, "discussion/index.html", {'alldiscussions': alldiscussions})


def discussion(request, slug): 
    print(slug)
    discussion=Discussion.objects.filter(slug=slug).first()
    print(discussion)
    # discussion.views= Discussion.views +1
    discussion.save()
    
    comments= DiscussionComment.objects.filter(Discussion=discussion, parent=None)
    replies= DiscussionComment.objects.filter(Discussion=discussion).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'Discussion':discussion, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, "discussion/threads.html")



def DiscussionComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        DiscussionSno =request.POST.get('DiscussionSno')
        Discussion= Discussion.objects.get(sno=DiscussionSno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            comment=DiscussionComment(comment= comment, user=user, Discussion=Discussion)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= DiscussionComment.objects.get(sno=parentSno)
            comment=DiscussionComment(comment= comment, user=user, Discussion=Discussion , parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
        
    return redirect(f"/discussion/{discussion.slug}")

