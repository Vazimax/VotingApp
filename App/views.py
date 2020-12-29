from django.shortcuts import render , get_object_or_404
from .models import *
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def Home(request):
    latest_question_list = Question.objects.order_by('-published_at')
    
    context = {
        'latest_question_list':latest_question_list
    }

    return render(request,'app/home.html',context)

def Detail(request,pk):
    try :
        question = Question.objects.get(id=pk)
    except Question.DoesNotExist:
        raise Http404("Sorry We can't find what you want =)")
    context  = {
        'question':question
    }
    return render(request,'app/detail.html',context)

def Results(request,pk):
    question =  get_object_or_404(Question,id=pk)
    context = {
        'question':question
    }
    return render(request,'app/result.html',context)

def Vote(request,pk): 
    question = get_object_or_404(Question,id=pk)
    try:
        selected_choice = question.choice_set.get(id=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))

    return render(request,'')
    
