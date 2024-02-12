from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpRequest, request,Http404
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.signals import user_logged_out
from django.contrib import messages
from django.urls import reverse
from . forms import IconForm, ProfileForm, PortfolioForm
from . models import Icon, Portfolio, Profile, Testimony
from django.core.mail import send_mail
from django.forms import modelformset_factory
from django.views.generic import CreateView, ListView, DetailView, UpdateView
# Create your views here.




def AdminIndex(request):
    return render(request, 'adminindex.html')

def index(request):
    allic = Icon.objects.all()
    profile = Profile.objects.all()
    portfolio = Portfolio.objects.all()
    testimony = Testimony.objects.all()
    context = {}

    if allic.count() > 0:
        ic = Icon.objects.latest('id')
        icon_dict = {'ic':ic}
        context.update(icon_dict)
    
    if profile.count() > 0:
        prof = Profile.objects.latest('id')
        prof_dict = {'prof':prof}
        context.update(prof_dict)
    

    pf = {'portfolios':portfolio}
    tst = {'testimonies':testimony}
    context.update(pf)
    context.update(tst)
    return render(request, 'index.html', context)

    

# ALL CLASS BASED VIEWS 

class CreatePortfolioView(CreateView):
    model = Portfolio
    template_name = 'portfolio-create.html'
    fields = '__all__'

class UpdatePortfolioView(UpdateView):
    model = Portfolio
    template_name = 'update-portfolio.html'
    fields = '__all__'
    
class CreateTestimonyView(CreateView):
    model = Testimony
    template_name = 'adminindex.html'
    fields = '__all__'

class UpdateTestimonyView(UpdateView):
    model = Testimony
    template_name = 'update-testimony.html'
    fields = '__all__'
    



# AUTHENTICATION

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in."))
            return redirect('adminindex')
        else:
            messages.error(request, ("There was an error"))
            return redirect('index')
    else:
        return render(request, 'login.html', {})
    
def UserLoggedIn(request):
    if request.user.is_authenticated == True:
        username = request.user.username
    else:
        username = None
    return username

def logout_user(request):
    username = UserLoggedIn(request)
    if username != None:
        logout(request)
        messages.error(request, ("Logged out."))
        return redirect('index')
    else:
        return render(request, 'adminindex.html')



# UPLOADING
    
def profile_create(request):
    if request.method == 'POST':
        profForm = ProfileForm(request.POST, request.FILES)
        if profForm.is_valid():
            profForm.save()
            return redirect('adminindex')
    else:
        profForm = ProfileForm()
        context = {'profiles':profForm}
        return render(request, 'adminindex.html', context)
    
def upload_icon(request):
    if request.method == 'POST':
        icform = IconForm(request.POST, request.FILES)
        if icform.is_valid():
            icform.save()
            return render(request, 'adminindex.html')        
    else:
        icform = IconForm()
        context = {'icform':icform}   
    return render(request, 'adminindex.html', context)


# DISPLAYING

def portfolio_details(request,pk):
    try:
        portfolio_data = Portfolio.objects.get(id=pk)
        all_portfolio = Portfolio.objects.get(id=pk)
        ic = Icon.objects.latest('id')
    except portfolio_data.DoesNotExist:
        raise Http404('Portfolio does not exist.')
    else:
        images = []
        if portfolio_data.img:
            images.append(portfolio_data.img)
        if portfolio_data.img2:
            images.append(portfolio_data.img2)
        if portfolio_data.img3:
            images.append(portfolio_data.img3)
        if portfolio_data.img4:
            images.append(portfolio_data.img4)
        if portfolio_data.img5:
            images.append(portfolio_data.img5)
        if portfolio_data.img6:
            images.append(portfolio_data.img6)
        if portfolio_data.img7:
            images.append(portfolio_data.img7)
        if portfolio_data.img8:
            images.append(portfolio_data.img8)
        if portfolio_data.img9:
            images.append(portfolio_data.img9)
        if portfolio_data.img10:
            images.append(portfolio_data.img10)
        context = {'images':images, 'portfolio':all_portfolio, 'ic':ic}
    return render(request, 'portfolio-details.html', context)


def gallery(request):
    ic = Icon.objects.all()
    prof = Profile.objects.all()
    testimony = Testimony.objects.all()
    port = Portfolio.objects.all()
    context = {'ic':ic, 'prof':prof, 'port':port,'testimony':testimony}
    return render(request, 'gallery.html', context)

# DELETING

def deleteic(request, pk):
    ic = get_object_or_404(Icon, pk=pk)
    ic.delete()
    return redirect('gallery')

def deleteprof(request, pk):
    prof = get_object_or_404(Profile, pk=pk)
    prof.delete()
    return redirect('gallery')

def deletetest(request, pk):
    testi = get_object_or_404(Testimony, pk=pk)
    testi.delete()
    return redirect('gallery')

def deleteport(request, pk):
    port = get_object_or_404(Portfolio, pk=pk)
    port.delete()
    return redirect('gallery')

# MAIL SENDING

def contact(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message_name = request.POST['name']
        message_email = request.POST['email']
        message = request.POST['message']
        send_mail(
            subject + ' from ' + message_name,
            message,
            message_email,
            ['salmankfarisinfo@gmail.com',]
        )
        messages.success(request, (f'Sent! I will get back to you soon, {message_name}.'))
        return redirect('index')
    else:
        messages.error(request, ('There was an error.'))
        return render(request, 'index.html', {})