from django.shortcuts import render, HttpResponse, redirect
from discussion.models import Discussion, DiscussionComment
from django.contrib import messages
from django.contrib.auth.models import User
from discussion.templatetags import extras

# Create your views here.
def index(request): 
    # alldiscussions= discussion.objects.all()
    # context={'alldiscussions': alldiscussions}
    # return render(request, "blog/index.html", context)
    return render(request, "discussion/index.html")

def discussion(request, slug): 
    Discussion=Discussion.objects.filter(slug=slug).first()
    Discussion.views= Discussion.views +1
    Discussion.save()
    
    comments= DiscussionComment.objects.filter(Discussion=Discussion, parent=None)
    replies= DiscussionComment.objects.filter(Discussion=Discussion).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'Discussion':Discussion, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, "discussion/discussion.html", context)

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

