from django.shortcuts import render,render_to_response,redirect
from django.views import generic
from .models import Post
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.utils.text import slugify
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required



class PostList(generic.ListView):
    queryset = Post.objects.order_by('-created_on')
    template_name = 'blog/index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

"""
class AddblogView(generic.FormView):
    template_name = 'blog/addblog2.html'
    success_url = '/blog/'
    """


def addblog(request):
    if request.user.is_authenticated:
        return render_to_response('blog/addblog2.html')
    else:
        return redirect('/login')


@csrf_exempt
def submit(request):
    newpost = Post()
    newpost.userid = request.POST['userid']
    newpost.title = request.POST['title']
    newpost.text = request.POST['text']
    newpost.created_on = datetime.datetime.now()
    newpost.slug = generate_unique_slug(Post,newpost.title)
    newpost.save()
    return redirect('/blog')
    


def generate_unique_slug(klass, field):
    origin_slug = slugify(field)
    unique_slug = origin_slug
    numb = 1
    while klass.objects.filter(slug=unique_slug).exists():
        unique_slug = '%s-%d' % (origin_slug, numb)
        numb += 1
    return unique_slug