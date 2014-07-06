from django.shortcuts import render, HttpResponse
from g2s.forms import G2SForm, G2STransactionForm


def g2s_index(request):
    # this is what user wants to buy
    items_list = [
        {
            'item_name': 'Test',
            'item_amount': 1.11,
            'item_quantity': 1,
        },
    ]

    # this data you can get from user profile or from custom user model
    payment_details = {
        'country': 'Russia',
        'city': 'Moscow',
        'address1': 'Moscow, Arbat',
        'zip': '121099',
        'first_name': 'Ivan',
        'last_name': 'Ivanov',
        'email': 'ivanov.ivan@yandex.ru',
        'phone1': '+79031234567',
        'total_amount': 1.11,
        'user_token_id': 1,
        'productId': 1,
    }

    form = G2SForm(items_list, initial=payment_details)
    return render(request, "g2s/order.html", {"form": form})


def g2s_success(request):
    form = G2STransactionForm(request.GET)
    if form.is_valid() and form.save():
        return HttpResponse("Success")
    return HttpResponse('Error')


def g2s_pending(request):
    return HttpResponse("Pending")


def g2s_error(request):
    return HttpResponse("Error")


def g2s_back(request):
    return HttpResponse("Back")
