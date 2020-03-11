from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

from django.template import loader

from django.shortcuts import render, get_object_or_404

from django.http import Http404

# Create your views here.
def index(request):
   
    question_list = Question.objects.order_by('-pub_date')
    # output = ', '.join([q.question_text for q in question_list])
    # return HttpResponse(output)

    # 使用template
    # template = loader.get_template('knw1/index.html')
    # context = {
    #     'question_list': question_list
    # }
    # return HttpResponse(
    #     template.render(context, request)
    # )

    context = {
        'question_list': question_list
    }
    return render(request, 'knw1/index.html', context)

    # return HttpResponse('from index of knw1')

def detail(request, question_id):
    
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')
    
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'knw1/detail.html', {
        'question': question
    })
        
    # return HttpResponse('deatil -> 问题id：%s' % question_id)

def results(request, question_id):
    return HttpResponse('results -> 问题id：%s' % question_id)

def vote(request, question_id):
    return HttpResponse('vote -> 问题id：%s' % question_id)