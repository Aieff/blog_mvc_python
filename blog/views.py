from django.shortcuts import render
from django.shortcuts import redirect
from blog.forms import RegisterForm

from blog.forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.contrib.auth import logout
from django.urls import reverse


def home_view(request):
    return render(request, "home.html")

    
def register_view(request):
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            request.session['message'] = "Registro bem-sucedido!"
            return redirect('/')
    else:
        form = RegisterForm()
            
    return render(request, "register.html", {'form': form})


def user_login(request):
    user = None
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Logado com sucesso")
            return redirect('/home')
        else:
            messages.error(request, "Usuário ou Senha Inválidos")

    else:
        form = LoginForm()

    context = {'form': form}        
    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    # Após efetuar o logout, redireciona o usuário para a página de login ou homepage
    # Adiciona uma mensagem de sucesso 
    messages.success(request, "Deslogado com sucesso!")
    return redirect(reverse('blog:login'))