from django.shortcuts import render




def Home(request):
    return render(request, 'index.html',)


def Calculate(request):
    Monthly_Slary = float(request.GET['Monthly_Slary'])
    Bonifications = float(request.GET['Bonifications'])
    Extra_Hours = float(request.GET['Extra_Hours'])

   # ?calcular el Descuentos salarial
    Total = Monthly_Slary + Bonifications + Extra_Hours
    AFP = Total * 2.87/100
    SFS = Total * 3.04/100
    if Total >= 34685.00:
        ISR = Total * 27/100
    else:
        ISR = 0

    Total_descuento = Total - (AFP+SFS+ISR)

    contents = {
        'Total': f'{Total:.2f}',
        'AFP': f'{AFP:.2f}',
        'SFS': f'{SFS:.2f}',
        'ISR': f'{ISR:.2f}',
        'descuento': f'{Total_descuento:.2f}'

    }
    return render(request, 'resultado.html', contents)
