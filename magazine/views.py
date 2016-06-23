from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.views.generic.edit import FormView
from paypal.standard.forms import PayPalPaymentsForm
from .forms import PostForm
from django.contrib.auth.models import Permission, User
from django.shortcuts import get_object_or_404
from .models import *
from django.contrib import messages
from django.core.mail import send_mail

@csrf_exempt
def paypal_success(request):
    """
    Tell user we got the payment.
   """
    return HttpResponse("Money is mine. Thanks.")


@login_required
def paypal_pay(request, sum):
     paypal_dict = {
         "business": "feelemon@bk.ru",
         "amount": 'sum',
         "currency_code": "RUB",
         "item_name": "Products in Soundfilch",
         "invoice": "INV-00001",
         "notify_url": reverse('paypal-ipn'),
         "return_url": "http://localhost:8000/payment/success/",
         "cancel_return": "http://localhost:8000/payment/cart/",
         "custom": str(request.user.id)
     }

     paypal_dict['amount'] = sum
     # Create the instance.
     print(paypal_dict['amount'])
     form = PayPalPaymentsForm(initial=paypal_dict)
     # user = User.objects.filter(last_name=)
     # user = get_object_or_404(User)
     context = {"form": form, "paypal_dict": paypal_dict}
     return render(request, "magazine/payment.html", context)

def summa():
    return str()



def home(request):
     if request.user.is_authenticated():
         return HttpResponse("{0} <a href='/accounts/logout'>exit</a>".format(request.user))
     else:
         return HttpResponse("<a href='/login/vk-oauth2/'>login with VK</a>")

@login_required
def account_profile(request):
     return HttpResponse("Hi, {0}! Nice to meet you.".format(request.user.first_name))


class RegisterFormView(FormView):
    form_class = UserCreationForm
    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/magazine.login.html/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "magazine/register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)
# Create your views here.

def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)

# Опять же, спасибо django за готовую форму аутентификации.


# class LoginFormView(FormView):
#     form_class = AuthenticationForm
#
#     # Аналогично регистрации, только используем шаблон аутентификации.
#     template_name = "magazine/login.html"
#
#     # В случае успеха перенаправим на главную.
#     success_url = "/"
#
#     def form_valid(self, form):
#         # Получаем объект пользователя на основе введённых в форму данных.
#         self.user = form.get_user()
#
#         # Выполняем аутентификацию пользователя.
#         login(self.request, self.user)
#         return super().form_valid(form)
#
#

# def action(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.user.pk == pk:
#         return render(request, 'magazine/post_list.html', {'post': post})
#     else:
#         return render(request, 'magazine/post_list.html', {'post': post})

class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return render(request, 'magazine/post_list.html',)


def backet_view(request):
    order = Order.objects.filter(owner=request.user, payment=False).latest("time_add")
    items = order.item_set.all()
    return render(request, 'magazine/backet.html', {'items': items, 'order': order})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'magazine/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'magazine/post_detail.html', {'post': post})


def post_new(request):
    form = PostForm()
    # if request.method == "POST":
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
    else:
        form = PostForm()
    return render(request, 'magazine/post_edit.html', {'form': form})


def post_edit(request, pk = None):
        post = get_object_or_404(Post, pk = pk)
        # if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('magazine.views.post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'magazine/post_edit.html', {'form': form})

def locus(request):
    return render(request, 'magazine/locus.html',)

def category_rock(request):
    posts = Post.objects.filter(category__alias='Rock').order_by('-published_date')
    return render(request, 'magazine/post_list.html', {'posts': posts})

def rap(request):
    posts = Post.objects.filter(category__alias='Rap').order_by('-published_date')
    return render(request, 'magazine/post_list.html', {'posts': posts})

def dance(request):
    posts = Post.objects.filter(category__alias='Dance').order_by('-published_date')
    return render(request, 'magazine/post_list.html', {'posts': posts})

def electro(request):
    posts = Post.objects.filter(category__alias='Electro').order_by('-published_date')
    return render(request, 'magazine/post_list.html', {'posts': posts})

#     return None
def backet(request):
    return render(request, "magazine/backet.html",)
