from django.shortcuts import render 
def calculate_power(request):

    if request.method == "POST":
        Intensity = float(request.POST.get("Intensity"))
        Resistance = float(request.POST.get("Resistance"))
        Power = ((Intensity)**2 ) * Resistance 
        print(f"Intensity: {Intensity} I, Resistance: {Resistance} R, Power: {Power}")
    return render(request,'serverapp/server.html')
