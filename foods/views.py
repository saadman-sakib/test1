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
        print(request.FILES)
        # myfile = request.FILES['myfile']
        # data = myfile.read().decode('utf-8').splitlines()
        # for line in data:
        #     name, calories = line.split(',')
        #     # Food.objects.create(name=name, calories=calories)
        #     print(name, calories)
        return redirect('/foodtb/')
    return render(request, 'foods/upload.html')
        