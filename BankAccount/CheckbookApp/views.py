from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import AccountForm
from .models import Account
from .forms import TransactionForm
from .models import Transaction

# Create your views here.
def homepage(request):#ADD WILDCARDS BELOW (AFTER INDEX.HTML)
    return render(request, 'CheckbookApp/index.html')

def addTransaction(request):#ADD WILDCARDS BELOW (AFTER INDEX.HTML)
    form = TransactionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('homepage')
    else:
        print(form.errors)
        form = TransactionForm
    context = {
        'form': form
    }
    return render(request, 'CheckbookApp/AddTransaction.html', context)


def balanceSheet(request):#ADD WILDCARDS BELOW (AFTER INDEX.HTML)
    return render(request, 'CheckbookApp/BalanceSheet.html')

def createNewAccount(request):#ADD WILDCARDS BELOW (AFTER INDEX.HTML)
    form = AccountForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('homepage')
    else:
        print(form.errors)
        form = AccountForm
    context = {
        'form': form
    }
    return render(request, 'CheckbookApp/CreateNewAccount.html', context)