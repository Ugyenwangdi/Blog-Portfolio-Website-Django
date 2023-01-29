from django.shortcuts import redirect, render, get_object_or_404
from .models import Post, Tag, Profile, Project, Banner  #, Comment
from django.contrib.auth.models import auth
# Django Q objects use to create complex queries
from django.db.models import Q
import random
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import time

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# from .forms import CommentForm

def home(request):
    # get query from request
    query = request.GET.get('query')
    # print(query)
    # Set query to '' if None
    if query == None:
        query = ''

    # posts = Post.postmanager.all()
    # search for query in headline, sub headline, body
    posts = Post.postmanager.filter(
        Q(headline__icontains=query) |
        Q(sub_headline__icontains=query) |
        Q(body__icontains=query)
    )

    # feature posts on the home page
    featured = Post.postmanager.filter(featured=True)[0:3]

    # To access latest updated profile image, Profile is a Profile table inside the models
    profiles = Profile.objects.latest('updated')
    profiles.profile_views = profiles.profile_views + 1
    profiles.save() 

    banner = Banner.objects.latest('date_added')
    # To display tags for searching categies
    tags = Tag.objects.all()

    listtags = list(tags)

    # To display tags randomly for searching by tags
    randomtags = random.sample(listtags, 4)

    category = request.GET.get('category')

    if category == None:
        projects = Project.objects.all()[0:3]

    else:
        projects = Project.objects.filter(category__name=category)

    categories = Tag.objects.all()

    "#Number of visits to this view, as counted in the session variable."
    # num_visits = request.session.get('num_visits', 1)
    # request.session['num_visits'] = num_visits + 1

    # Pass the context so that we can access inside the rendered template
    context = {
        'posts': posts,
        'featured': featured,
        'tags': tags,
        'randomtags': randomtags,
        'profiles': profiles,
        'banner': banner,
        'query': query,
        'projects': projects,
        'categories': categories,
        'categoryname': category,
    }  
    # 'count': num_visits,
    # 

    return render(request, 'index.html', context)


def post(request, post):

    post = get_object_or_404(Post, slug=post, status='published')
    post.post_views = post.post_views + 1
    post.save()
    # time.sleep(2)
    
    profiles = Profile.objects.latest('updated') 
    banner = Banner.objects.latest('date_added')
    

    context = {
        'post': post,
        'profiles': profiles,
        'banner': banner,
        
    }
    



    # if request.method == 'POST':
    #     form = CommentForm(request.POST)

    #     if form.is_valid():
    #         obj = form.save(commit=False)
    #         obj.post = post
    #         obj.save()
    #         context.update({'form': form, 'slug':post.slug})

    #         # return redirect('post', slug=post.slug)
    #         return render(request, 'Post.html', context)
    # else:
    #     form = CommentForm()
    #     context.update({'form': form})

    return render(request, 'Post.html', context)

def posts(request):
    # get query from request
    query = request.GET.get('query')
    # print(query)
    # Set query to '' if None
    if query == None:
        query = ''

    # posts = Post.postmanager.all()
    # search for query in headline, sub headline, body
    posts = Post.postmanager.filter(
        Q(headline__icontains=query) |
        Q(sub_headline__icontains=query) |
        Q(body__icontains=query)
    )

    # results = True
    # if posts == None:
    #     results = False

    profiles = Profile.objects.latest('updated') 
    banner = Banner.objects.latest('date_added')
    

    tags = Tag.objects.all()
    
    listtags = list(tags)

    # To display tags randomly for searching by tags
    randomtags = random.sample(listtags, 5)

    context = {
        'posts': posts,
        # 'slug': post.slug,
        'tags': tags,
        'query': query,
        'randomtags': randomtags,
        'profiles': profiles,
        'banner': banner,
        
    }

    return render(request, 'Posts.html', context)


def projects(request):
    # get query from request
    query = request.GET.get('query')
    # print(query)
    # Set query to '' if None
    if query == None:
        query = ''

    # posts = Post.postmanager.all()
    # search for query in headline, sub headline, body
    posts = Post.postmanager.filter(
        Q(headline__icontains=query) |
        Q(sub_headline__icontains=query) |
        Q(body__icontains=query)
    )

    # feature posts on the home page
    featured = Post.postmanager.filter(featured=True)[0:3]

    # To access latest updated profile image, Profile is a Profile table inside the models
    profiles = Profile.objects.latest('updated')
    profiles.profile_views = profiles.profile_views + 1
    profiles.save() 

    banner = Banner.objects.latest('date_added')
    # To display tags for searching categies
    tags = Tag.objects.all()

    listtags = list(tags)

    # To display tags randomly for searching by tags
    randomtags = random.sample(listtags, 4)

    category = request.GET.get('category')

    if category == None:
        projects = Project.objects.all()

    else:
        projects = Project.objects.filter(category__name=category)

    categories = Tag.objects.all()

    "#Number of visits to this view, as counted in the session variable."
    # num_visits = request.session.get('num_visits', 1)
    # request.session['num_visits'] = num_visits + 1

    # Pass the context so that we can access inside the rendered template
    context = {
        'posts': posts,
        'featured': featured,
        'tags': tags,
        'randomtags': randomtags,
        'profiles': profiles,
        'banner': banner,
        'query': query,
        'projects': projects,
        'categories': categories,
        'categoryname': category,
    }  
    # 'count': num_visits,
    # 

    return render(request, 'project.html', context)

def viewProject(request, pk):
    project = Project.objects.get(id=pk)
    profiles = Profile.objects.latest('updated') 
    banner = Banner.objects.latest('date_added')

    context = {
        'profiles': profiles,
        'banner': banner,
        'project': project
        
    }
    return render(request, 'projectDetail.html', context)
    
def about(request):

    profiles = Profile.objects.latest('updated') 
    banner = Banner.objects.latest('date_added')

    context = {
        'profiles': profiles,
        'banner': banner,
        
    }

    ## Allow Less secure app access on gmail

    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        # send_mail(
        #     'Contact form', 
        #     message, 
        #     settings.EMAIL_HOST_USER, 
        #     ['wulficode@gmail.com'], 
        #     fail_silently=False
        # )
    
        data = {
            'name': name,
            'email': email,
            'message': message
        }
        message = '''
        New message: {}
        By: {}
        From: {}
        '''.format(data['message'], data['name'], data['email'])

        # send an email
        try:
            if name is None or email is None or message is None:
                messages.info(request, 'Enter all the details')
                return render(request, 'about.html', context)

                
            else:
                send_mail(data['message'], message, '', ['email@gmail.com',], fail_silently=False)
                messages.info(request, 'Message sent')
                # context.update({'profiles': profiles})
                return render(request, 'about.html', context)
        except:
            messages.info(request, 'Could not sent your message')
            # context.update({'profiles': profiles})
            # return render(request, 'contact.html', context)
        
    return render(request, 'about.html', context)

# def contact(request):

#     profiles = Profile.objects.latest('updated') 

#     if request.method == "POST":

#         name = request.POST['name']
#         email = request.POST['email']
#         message = request.POST['message']
    
#         data = {
#             'name': name,
#             'email': email,
#             'message': message
#         }
#         message = '''
#         New message: {}
#         By: {}
#         From: {}
#         '''.format(data['message'], data['name'], data['email'])

#         # send an email
#         try:
#             send_mail(data['message'], message, '', ['wulficode@gmail.com'], fail_silently=False)
#             messages.info(request, 'Message sent')
#             context = {'profiles': profiles}
#             return render(request, 'contact.html', context)
#         except:
#             messages.info(request, 'Could not sent your message')
#             context = {'profiles': profiles}
#             return render(request, 'contact.html', context)
    
#     return render(request, 'contact.html', {'profiles': profiles})




############# API VIEWS ##################

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PostSerializer
from .models import Profile, Tag, Post, Project


@api_view(['GET']) # 'GET' decorator
def getRoutes(request):  # function based view 
    routes = [
        {
            'Endpoint': 'api/routes/',
            'method': 'Get',
            'body': None,
            'description': 'Return all the routes'
        },
        {
            'Endpoint': 'api/posts/id/',
            'method': 'Get',
            'body': None,
            'description': 'Return a single post'
        },
        {
            'Endpoint': 'api/posts/',
            'method': 'Get',
            'body': None,
            'description': 'Return all the posts'
        },
        {
            'Endpoint': 'api/posts/create',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new post with data sent in post request'
        },
        {
            'Endpoint': 'api/posts/id/update',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing post with data sent in PUT request'
        },
        {
            'Endpoint': 'api/posts/id/delete',
            'method': 'DELETe',
            'body': None,
            'description': 'Deletes an existing post'
        }
    ]
    return Response(routes)  # save false means we can turn any kinds of data into json data


@api_view(['GET'])
def getPosts(request):
    posts = Post.objects.all()

    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPost(request, pk):    
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, pk=pk)
    serializer = PostSerializer(post)
    return Response(serializer.data)


# @api_view(['POST'])
# def createPost(request):
#     if not request.user.is_authenticated:
#         return redirect('classifierApp:login')

#     data = request.data

#     note = Note.objects.create(
#         body = data['body']
#     )

#     serializer = NoteSerializer(note, many=False)
#     return Response(serializer.data)



# @api_view(['PUT'])
# def updateNote(request, pk):
#     data = request.data

#     note = Note.objects.get(id=pk)

#     serializer = NoteSerializer(note, data=request.data)
    
#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


# @api_view(['DELETE'])
# def deleteNote(reqest, pk):
#    note = Note.objects.get(id=pk)
#    note.delete()
   
#    return Response('Note was deleted')