

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import AccountForm
from .models import Account
from .forms import TransactionForm
from .models import Transaction


# Create your views here.
def homepage(request):#ADD WILDCARDS BELOW (AFTER INDEX.HTML)
    allAccounts = Account.accounts.all()
    return render(request, 'CheckbookApp/index.html', {'accounts': allAccounts})

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


def balanceSheet(request,pk):#ADD WILDCARDS BELOW (AFTER INDEX.HTML)
    pk = int(pk)
    item = get_object_or_404(Account, pk=pk)
    trans = Transaction.transactions.filter(account=pk)
    total = []
    total1 = item.startingBalance
    for i in trans:
        if i.type == 'Deposit':
            total1 = total1 + i.amount
            total.append(total1)
        elif i.type == 'Withdrawal':
            total1 = total1 - i.amount
            total.append(total1)
    data = zip(total,trans)
    return render(request, 'CheckbookApp/BalanceSheet.html', {'item': item, 'data': data, 'trans': trans, 'total': total, 'total1': total1})

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