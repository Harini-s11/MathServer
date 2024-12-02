from django.shortcuts import render 
def power(request): 
    context={} 
    context['power'] = "0" 
    context['i'] = "0" 
    context['r'] = "0" 
    if request.method == 'POST': 
        print("POST method is used")
        i = int(request.POST.get('intensity','0'))
        r = int(request.POST.get('resistance','0'))
        print('request=',request) 
        print('Intensity=',i) 
        print('Resistance=',r) 
        power = i*i*r
        context['power'] = power
        context['i'] = i
        context['r'] = r
        print('Power=',power) 
    return render(request,'mathapp/math.html',context)
