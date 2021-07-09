from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login,logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate

from nsepy import get_history
from datetime import date
import plotly.graph_objects as go
from plotly.offline import plot

# data = get_history(symbol="SBIN", start=date(2021,3,1), end=date.today())
# print(data.head(6))

# Create your views here.
def index(request):
    '''This is the sign-in view'''
    if request.method == 'POST':
        print(request.POST.get('password'))
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('main:home')
        else:
            return HttpResponse('Invalid User Details')
    return render(request,'index.html')

def signup(request):
    form = NewUserForm()
    if(request.method == 'POST'):
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("main:index")
        else:
            print(form.errors)
            messages.error(request, "Unsuccessful registration. Invalid information.")
            return HttpResponse(f"Unsuccessful registration. Invalid information.{form.errors}")
    else:
        return render(request,'signup.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('main:index')

def homepage(request):
    return render(request,'homepage.html')

def predict(request):
    if request.method == 'POST':
        ticker = request.POST.get('ticker')
        ticker = get_history(symbol=ticker, start=date(2021,3,1), end=date.today()) #pd df
        print(ticker.head(6))

        def candlestick():
            figure = go.Figure(
                data = [
                        go.Candlestick(
                        x = ticker.index,
                        high = ticker['High'],
                        low = ticker['Low'],
                        open = ticker['Open'],
                        close = ticker['Close'],
                        )
                    ]
            )
            candlestick_div = plot(figure, output_type='div')
            return candlestick_div

        last_candle = ticker.iloc[-1]
        buy = 0
        if(last_candle['Close']>last_candle['Open']):
            buy = 1

        
        return render(request,'homepage.html',{'candlestick':candlestick(),'ticker':request.POST.get('ticker'),'buy':buy})
        