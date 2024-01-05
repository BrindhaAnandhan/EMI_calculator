from django.shortcuts import render

# Create your views here.

def EMI(request):
    d1 = {'amount': 0 }
    if request.method == 'POST':
        loan = int(request.POST.get('loan'))
        ROI = int(request.POST.get('ROI'))
        year = int(request.POST.get('year'))

        monthly_interest_rate= ROI / 1200
        amount_of_month=  year*12
        Monthly_payment = loan * monthly_interest_rate / (1 -(1+ monthly_interest_rate)**(- amount_of_month) )

        d = {'amount': "%.0f" %Monthly_payment}

        return render(request, 'index.html', d)
    return render(request, 'index.html', d1)