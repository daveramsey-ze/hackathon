from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from home.models import Question
# Create your views here.

def index(request):

    # Page from the theme
    return render(request, 'pages/dashboard.html')
def welcome(request):

    # Page from the theme
    return render(request, 'pages/welcome.html')



# def question_view(request, question_id):
#     question = get_object_or_404(Question, id=question_id)
#     return render(request, 'pages/question.html', {'question': question})

def question_view(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    options = question.options.all()
    return render(request, 'pages/question.html', {'question': question, 'options': options})