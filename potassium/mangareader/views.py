from email.policy import default
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views import View
from django.views.generic import TemplateView


from mangareader.forms import CreateCollectionForm

from .models import Collection, Question, Task

# Create your views here.
# Ajax2


class ResourcePage(TemplateView):
    template_name = 'mangareader/resources.html'


class DeleteQuestionFromCollection(View):
    model = Collection
    def post(self, request):
        question_id = self.request.POST['question_id']
        collection_id = self.request.POST['collection_id']
        collection = Collection.objects.all().get(id=collection_id)
        question = Question.objects.all().get(id=question_id)
        collection.questions.remove(question)

        view_format = self.request.POST['format']
        if view_format == 'list':
            order = self.request.POST['order']
            return redirect('collection-detail-list', col=collection_id, order=order)
        else:
            return redirect('collection-detail', col=collection_id)


class CollectionPostDb(View):
    model = Question
    def post(self, request):
        question_id = request.POST['id']
        question = Question.objects.get(id=question_id)
        question.complete = not question.complete
        question.save()
        return HttpResponse("")

class CollectionPostNamechange(View):
    model = Collection
    def post(self, request):
        collection_id = request.POST['id']
        collection_name = request.POST['newName']
        collection = Collection.objects.get(id=collection_id)
        collection.name = collection_name
        collection.save()
        return HttpResponse(collection_name)


class CustomLoginView(LoginView):
    template_name = 'mangareader/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')

class RegisterPage(FormView):
    template_name = 'mangareader/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('dashboard')
        return super(RegisterPage, self).get(*args, **kwargs)


class Dashboard(LoginRequiredMixin, ListView):
    model = Collection
    template_name = 'mangareader/dashboard.html'
    context_object_name = 'Data'
    
    def post(self, request):
        if 'delete-col' in request.POST:
            collection_id = request.POST['delete-col']
            collection = Collection.objects.get(id=collection_id)
            collection.delete()
        return redirect('dashboard')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['collections'] = Collection.objects.all().filter(user=self.request.user)
  
        return context

class CollectionDetail(LoginRequiredMixin, ListView):
    model = Collection
    template_name = 'mangareader/collection_detail.html'
    context_object_name = 'Data'

    def post(self, request, col, que):
        question = Question.objects.get(id=que)
        question.complete = not question.complete
        question.save()
        return redirect('collection-detail', col=col)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['collections'] = Collection.objects.all().filter(user=self.request.user)
        collection = Collection.objects.all().filter(user=self.request.user).get(id=self.kwargs['col'])
        

        setattr(collection, 'total', collection.get_question_count)
        setattr(collection, 'completed', collection.get_question_completed)
        topics = collection.initialize_topics()
        topics_data = {}
        for topic in topics:
            topics_data[topic] = {}
            topics_data[topic]['questions'] = collection.populate_topic(topic)
            topics_data[topic]['total'] = collection.get_topic_questions_total(topic)
            topics_data[topic]['complete'] = collection.get_topic_questions_complete(topic)
        setattr(collection, 'topics_data', topics_data)    
        context['collection'] = collection
        return context

class CollectionDetailList(LoginRequiredMixin, ListView):
    model = Collection
    template_name = 'mangareader/collection_detail_list.html'
    context_object_name = 'Data'

    def post(self, request, col, que, order):
        question = Question.objects.get(id=que)
        question.complete = not question.complete
        question.save()
        return redirect('collection-detail-list', col=col, order=order)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['collections'] = Collection.objects.all().filter(user=self.request.user)
        collection = Collection.objects.all().filter(user=self.request.user).get(id=self.kwargs['col'])
        order = self.kwargs['order']


        setattr(collection, 'total', collection.get_question_count)
        setattr(collection, 'completed', collection.get_question_completed)
        setattr(collection, 'questions_sorted_list', collection.questions.order_by(order))
        

        context['collection'] = collection
        context['order'] = order
        return context






class DashboardList(LoginRequiredMixin, ListView):
    model = Collection
    template_name = 'mangareader/dashboardlist.html'
    context_object_name = "Data"

    def post(self, request, pk, pk2):
        question = Question.objects.get(id=pk)
        if 'Delete' in request.POST:
            collection = Collection.objects.get(id=pk2)
            collection.questions.remove(question)
        else:
            question.complete = not question.complete
            question.save()
        return redirect('list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['collections'] = Collection.objects.all().filter(user=self.request.user)
        order_by = ''
        for collection in context['collections']:
            setattr(collection, 'total', collection.get_question_count)
            setattr(collection, 'completed', collection.get_question_completed)
            order_by = self.request.GET.get('dropdown') or ''
            if order_by:
                setattr(collection, 'questions_sorted_list', collection.questions.order_by(order_by))
            else:
                setattr(collection, 'questions_sorted_list', collection.questions.order_by('difficulty_level'))
        context['order'] = order_by

        return context



class CollectionCreate(LoginRequiredMixin, CreateView):
    model = Collection
    form_class = CreateCollectionForm
    template_name = 'mangareader/collection_create_form.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = Question.objects.all().filter(user=self.request.user)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['questions'] = context['questions'].filter(name__icontains=search_input)
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        custom_model = form.save(commit=False)
        custom_model.custom = True
        custom_model.save()
        new_collection = Collection.objects.filter(user=self.request.user).get(name=custom_model.name)
        self.success_url = reverse_lazy('collection-detail', kwargs={'col': new_collection.id})
        return super(CollectionCreate, self).form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super(CollectionCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    
class CollectionUpdate(LoginRequiredMixin, UpdateView):
    model = Collection
    fields = ['questions']
    success_url = reverse_lazy('dashboard')
    template_name = 'mangareader/collection_update_form.html'

    def get_success_url(self):
        col = self.request.POST['col']
        return reverse_lazy('collection-detail', kwargs={'col': col})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        collection_id = self.kwargs['pk']
        context['questions'] = Question.objects.all().filter(user=self.request.user)
        context['collection'] = Collection.objects.all().get(id=collection_id)
        return context


class CollectionDelete(LoginRequiredMixin, DeleteView):
    model = Collection
    context_object_name = "collection"
    template_name = 'mangareader/collection_delete.html'
    success_url = reverse_lazy('dashboard')

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'mangareader/tasklist.html'
    context_object_name = 'tasks'

    def post(self, request):
        task_name = request.POST['task_name']
        new_task = Task(user=self.request.user, description=task_name, complete=False)
        new_task.save()
        return redirect('tasklist')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user).order_by('-time')
        return context

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['description', 'complete']
    success_url = reverse_lazy('tasklist')
    template_name = 'mangareader/task_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
    

class TaskUpdate(LoginRequiredMixin, View):
    model = Task
    def get(self, request, pk):
        task = Task.objects.filter(id=pk).get()
        task.complete = not task.complete
        task.save()
        return redirect('tasklist')


class TaskDelete(LoginRequiredMixin, View):
    model = Task
    def get(self, request, pk):
        Task.objects.filter(id=pk).delete()
        return redirect('tasklist')
    




