from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"base.html")

def WhatsappData(Ph,Message):
    import time
    import webbrowser as web
    import pyautogui as pg
    
    Phone = "+91"+Ph
    web.open('https://web.whatsapp.com/send?phone='+Phone+'&text='+Message)
    time.sleep(30)
    pg.press('enter')


def SendData(request):
    if request.method == 'POST':
        ph = request.POST['Phone']
        Message = request.POST['Message']
        print(ph,Message)
        WhatsappData(ph,Message)
        msg = "Message has successfully sent.."
        return render(request,"whatsapp_app/home.html",{'msg':msg})
    else:
        return HttpResponse("<h1>404 - Not Found : )</h1>")

    