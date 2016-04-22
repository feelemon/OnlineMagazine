from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.views.generic.edit import FormView
from .forms import PostForm
from .models import Post
from paypal.standard.forms import PayPalPaymentsForm



def home(request):
     """
     Home page with auth links.
     """
     if request.user.is_authenticated():
         return HttpResponse("{0} <a href='/accounts/logout'>exit</a>".format(request.user))
     else:
         return HttpResponse("<a href='/login/vk-oauth2/'>login with VK</a>")

@login_required
def account_profile(request):
     """
     Show user greetings. ONly for logged in users.
     """
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

def action(request, pk):
    if request.user.pk == pk:
        return render(request, 'magazine/post_detail.html')
    else:
        return render(request,'magazine/post_list.html')

class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return render(request, 'magazine/post_list.html',)


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'magazine/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'magazine/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
        else:
            form = PostForm()
    return render(request, 'magazine/post_edit.html', {'form': form})

def post_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
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


def account_profile(request):
    return None


@csrf_exempt
def paypal_success(request):
     """
     Tell user we got the payment.
     """
     return HttpResponse("Money is mine. Thanks.")



@login_required
def paypal_pay(request):
     """
     Page where we ask user to pay with paypal.
     """
     paypal_dict = {
         "business": "acccko-facilitator@gmail.com",
         "amount": "100.00",
         "currency_code": "RUB",
         "item_name": "products in socshop",
         "invoice": "INV-00001",
         "notify_url": reverse('paypal-ipn'),
         "return_url": "http://localhost:8000/payment/success/",
         "cancel_return": "http://localhost:8000/payment/cart/",
         "custom": str(request.user.id)
     }

     # Create the instance.
     form = PayPalPaymentsуForm(initial=paypal_dict)
     context = {"form": form, "paypal_dict": paypal_dict}
     return render(request, "magazine/payment.html", context)