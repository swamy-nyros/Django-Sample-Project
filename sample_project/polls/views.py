#!/usr/bin/python
# -*- coding: ascii -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from .models import Question, Choice, Comment, Post_Comment, File_Upload
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, FileUploadForm
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
import json
#import simplejson
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import logging
from django.utils import timezone
from rest_framework import status

logger = logging.getLogger(__name__)

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):        
        return Question.objects.order_by('-pub_date')[:5]
    def get_queryset(self):       
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

def detail(request, question_id):
    question_name = get_object_or_404(Question, pk=question_id)    
    comment_list = Comment.objects.filter(question_id=question_id).order_by('-id')   
    paginator  = Paginator(comment_list, 10)    
    page = request.GET.get('page', 1)

    try:
        comments = paginator.page(page)        
    except PageNotAnInteger:        
        comments = paginator.page(1)
    except EmptyPage:        
        comments = paginator.page(paginator.num_pages)
    
    tmpl_vars = {      
        'all_posts': comments,
        'form': CommentForm(),
        'question': question_name,
    }
    return render(request, 'polls/detail.html', tmpl_vars, )

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):        
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()        
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

@login_required
def comment(request, question_id):
    if request.method == 'POST':        
        p = get_object_or_404(Question, pk=question_id)
        form = CommentForm(request.POST)             
        post_comment = request.POST.get('the_post')
        response_data = {}
        comment = Comment(user=request.user,question_id=question_id,comment=post_comment)
        comment_data = comment.save()
        response_data['comment'] = comment.comment            
        response_data['user'] = comment.user.username

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def post_comment(request, question_id):
    if request.method == 'POST':
        logger.error("something went wrong !!!!!!!!!")
        p = get_object_or_404(Question, pk=question_id)        
        form = PostCommentForm(request.POST)
        if request.session.get('has_commented', False):
            return HttpResponse("you have already commented")
        c = Post_Comment(comment=new_comment, user=request.user,question_id=question_id)
        c.save()
    request.session['has_commented'] = True
    return HttpResponse("Thanks for your comment !")

def file_upload(request):
    if request.method == 'POST':        
        form = FileUploadForm(request.POST, request.FILES)        
        if form.is_valid():            
            data = form.cleaned_data['upload_file']
            file_data = File_Upload.objects.create(upload_file=request.FILES['upload_file'])           
            file_data.save()               
            return HttpResponseRedirect('/') 
    else:
        form = FileUploadForm()        
        upload_files = File_Upload.objects.all()        
        return render_to_response('polls/file_upload.html', {'form': form, 'upload_files':upload_files}, 
            context_instance=RequestContext(request))

class DetailView(generic.DetailView):    
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())
