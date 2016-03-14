from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.http import HttpResponse, Http404, HttpResponseRedirect
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse

def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit',10))
    except ValueError:
        limit = 10
  
    if limit > 100:
        limit = 10
 
    try:
        page = int(request.GET.get('page',1))
    except ValueError:
        raise Http404

    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)  
    return page, paginator

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def question(request, id):
    question = get_object_or_404(Question, pk=id)
    answers = Answer.objects.filter(question = question)
    user_q = question.author.get_username
    form = AnswerForm(initial={'question': str(id)})
    return render(request, 'question.html', {'user':user_q, 'question':question, 'answers':answers, 'form': form,})

@require_GET
def index(request):
    qa = Question.objects.all()
    qa = qa.order_by('-added_at')
    page, paginator = paginate(request,qa)
    paginator.baseurl = '/?page='
    return render(request,'quest_new.html', {'questions': page.object_list, 'paginator': paginator, 'page':page, })

@require_GET
def popular(request):
    qa = Question.objects.all()
    qa = qa.order_by('-rating')
    page, paginator = paginate(request,qa)
    paginator.baseurl = '/popular/?page='
    return render(request,'quest_pop.html', {'questions': page.object_list, 'paginator': paginator, 'page':page, })

def ask_add(request):
    if request.method == 'POST': 
        form = AskForm(request.POST)
        if form.is_valid():
            #form._user = request.user 
            question = form.save()
            url = reverse('question', args=[question.id])
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask.html', { 'form': form, } )


def answer_add(request):
    if request.method == 'POST': 
        form = AnswerForm(request.POST)
        if form.is_valid():
            #form._user = request.user 
            answer = form.save()
            url = answer.get_url()
            #url = reverse('question', args=[answer.question.id])
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm()
    return render(request, 'answer.html', { 'form': form, } )

