from django.shortcuts import render,redirect
from .form import SubscriptionForm
def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about_us')
    else:
        form = SubscriptionForm()
    return render(request, 'subscribe.html', {'form': form})

# Create your views here.
