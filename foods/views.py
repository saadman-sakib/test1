from django.shortcuts import redirect, render
from .models import Food

# Create your views here.
def foodView(request):
    allfoods = Food.objects.all()
    return render(request, 'foods/foods.html', {'allfoods': allfoods})


def rangeView(request):
    gt = request.GET.get('gt')
    lt = request.GET.get('lt')
    if gt == None or lt == None:
        return redirect('/foods/')
        
    foods = Food.objects.filter(calories__gt=gt, calories__lt=lt)
    return render(request, 'foods/foods.html', {'allfoods': foods})

# upload an xl file and save data to database
def upload(request):
    if request.method == 'POST':
        myfile = request.FILES.get('myfile')
        data = myfile.read().decode('utf-8').splitlines()
        #skip the first line
        data = data[1:]
        for line in data:
            name, calories = line.split(',')
            Food.objects.create(name=name, calories=calories)
        return redirect('/foodtb/')
    return render(request, 'foods/upload.html')