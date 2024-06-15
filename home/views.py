from django.shortcuts import render, get_object_or_404, redirect
from home.models import Question, Option, Response
import uuid
def index(request):

    # Page from the theme
    return render(request, 'pages/dashboard.html')
def welcome(request):

    # Page from the theme
    return render(request, 'pages/welcome.html')
def about(request):

    # Page from the theme
    return render(request, 'pages/about.html')


def question_view(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    options = question.options.all()

    if request.method == 'POST':
        session_id = request.session.get('session_id', str(uuid.uuid4()))
        request.session['session_id'] = session_id
        answer = request.POST.get('answer')

        Response.objects.create(session_id=session_id, question=question, answer=answer)

        if question.next_question:
            return redirect('question', question_id=question.next_question.id)
        else:
            return redirect('results')

    return render(request, 'pages/question.html', {'question': question, 'options': options})


def calculate_risk_score(responses):
    # Implement your logic to calculate the risk score based on responses
    score = 0
    for response in responses:
        if response.answer in ['Yes', 'Daily', "No, I Don't"]:
            score += 2
        elif response.answer in ['Weekly/Monthly', 'Occasionally', 'Less Frequently']:
            score += 1
    return score

def results_view(request):
    session_id = request.session.get('session_id')
    responses = Response.objects.filter(session_id=session_id)
    risk_score = calculate_risk_score(responses)
    responses.delete()
    return render(request, 'pages/results.html', {'risk_score': risk_score})
