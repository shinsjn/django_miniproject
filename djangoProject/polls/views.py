from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import  Choice,Question
from django.http import Http404
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}

    return render(request,'polls/index.html',context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk= question_id)

    return render(request, 'polls/detail.html',{'question':question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/results.html',{'question':question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:

        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):

        return render(request, 'polls/detail.html', {

            'question': question,

            'error_message': "You didn't select a choice.",

        })

    else:

        selected_choice.votes += 1

        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


