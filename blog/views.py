from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlogComment
from django.contrib import messages
from blog.templatetags import extras
from django.shortcuts import get_object_or_404, redirect






def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/blogHome.html', context)

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)  
    context = {'post': post, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, 'blog/blogPost.html', context)

def postComment(request):
    if request.method == "POST":
        postSno = request.POST.get("postSno")
        if postSno:
            post_obj = Post.objects.get(sno=postSno)
            if postSno:
                comment_content = request.POST.get("comment")
                user = request.user
                BlogComment.objects.create(comment=comment_content, user=user, post=post_obj)
                messages.success(request, "Your comment has been posted successfully")
                return redirect(f"/blog/")
    return HttpResponse("Invalid request")

def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect(f"/blog/")
