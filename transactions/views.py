from django.shortcuts import render, redirect
from .models import Category, Transaction, Goal
from .serializers import CategorySerializer, TransactionSerializer, GoalSerializer
from .forms import CategoryForm, RegisterForm, LoginForm
from django.views.generic import DetailView, UpdateView, DeleteView
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from transactions.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from transactions.paginations import CategoryAPIListPagination
from django.contrib.auth import login, logout, authenticate
from rest_framework_simplejwt.views import TokenObtainPairView
from django.views.generic import View


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'transactions/signup.html', {'form': form})


class LoginView(View):
    template_name = 'transactions/login.html'

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, self.template_name, {form: form})
    
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            print('ok')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                token_view = TokenObtainPairView.as_view()
                token_request_data = {
                    'username': username,
                    'password': password,
                }
                response = token_view(request, data=token_request_data)
            if response.status_code == 200:
                token_data = response.data
                request.session['access'] = token_data['access']
                request.session['refresh'] = token_data['refresh']

            return redirect('home')

        else:
            # Если пользователь не найден, добавляем ошибку в форму
            form.add_error(None, "Неверное имя пользователя или пароль.")
        
        
        return render(request, self.template_name, {'form': form})

def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('home')

class CategoryAPIList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = CategoryAPIListPagination


class CategoryAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #permission_classes = (IsOwnerOrReadOnly, )
    permission_classes = (IsAuthenticated, )


class CategoryAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly, )

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated, )


class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


#class CategoryViewSet(viewsets.ModelViewSet):
#    #queryset = Category.objects.all()
#    serializer_class = CategorySerializer
#
#    def get_queryset(self):
#        pk=self.kwargs.get('pk')
#        if not pk:
#            return Category.objects.all()[:3]
#        return Category.objects.filter(pk=pk)
#
#    @action(methods=['get'], detail=True)
#    def user(self, request, pk=None):
#        users = User.objects.get(pk=pk)
#        return Response({'users': users.id})


#class CategoryAPIList(generics.ListCreateAPIView):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer
#
#class CategoryAPIUpdate(generics.UpdateAPIView):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer
#
#class CategoryAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer



##class CategoryAPIView(generics.ListAPIView):
##    queryset = Category.objects.all()
##    serializer_class = CategorySerializer
#
#def categories(request):
#    categories = Category.objects.all()
#    return render(request, 'transactions/categories.html', {'categories': categories})
#
#class CategoryDetailView(DetailView):
#    model = Category
#    template_name='transactions/details_view.html'
#    context_object_name = 'category'
#
#class CategoryUpdateView(UpdateView):
#    model = Category
#    template_name = 'transactions/create.html'
#    
#    form_class = CategoryForm
#
#class CategoryDeleteView(UpdateView):
#    model = Category
#    success_url = '/categories/'
#    template_name = 'transactions/category_delete.html'
#
#    fields = ['name',]
#
#def create(request):
#    error = ''
#    if request.method == 'POST':
#        form = CategoryForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('categories')
#        else:
#            error = 'Форма заполнена неверно'
#
#    form = CategoryForm
#    data = {
#        'form': form,
#        'error': error
#    }
#
#    return render(request, 'transactions/create.html', data)
#
def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request, 'transactions/index.html', data)

def about(request):
    return render(request, 'transactions/about.html')

def contact(request):
    return render(request, 'transactions/contact.html')