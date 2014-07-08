Django Gate2Shop
================

How to install
--------------
1. Using pip:

.. code-block:: bash

    $ pip install django-gate2shop


2. Edit "settings.py"
    - add "g2s" to your "INSTALLED_APPS"
    - add following settings:

.. code-block:: python

    G2S_MERCHANT_ID = "123456"
    G2S_SECRET_KEY = "YourSecretWord"
    G2S_MERCHANT_SITE_ID = "1234567"
    G2S_CURRENCY = 'USD'


3. Add to "urls.py" paths

.. code-block:: python

    urlpatterns = patterns('',
        url(r'^g2s/g2s_form/$', 'g2s_form', name='g2s-form'),
        url(r'^g2s/', include('g2s.urls')),
    )


4. Create table in your database

.. code-block:: bash

    $ python manage.py syncdb
    $ python manage.py migrate


5. Create/render form

Create an instance of the form in your "views.py" and make render in your template

.. code-block:: python

    from g2s.forms import G2SForm

    def g2s_form(request):
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


In "order.html":

.. code-block:: html

    {{ form.render }}


After payment G2S sends a signal to your server (DMN URL).
The transaction will be saved in the database, then will be send a signal.
You can use it to process your own actions (add amount to users account, etc..)

.. code-block:: python

    from django.forms.models import model_to_dict
    from g2s.signals import g2s_payment_was_successful
    from pprint import pprint


    def transaction_result(sender, **kwargs):
        if sender.Status == 'APPROVED':
            pprint(model_to_dict(sender))


    g2s_payment_was_successful.connect(
        transaction_result, dispatch_uid="demo.models.transaction_result")



Demo installation:
------------------

.. code-block:: bash

    $ pip install virtualenvwrapper
    $ source /usr/local/bin/virtualenvwrapper.sh
    $ mkvirtualenv django-gate2shop
    $ git clone https://github.com/gotlium/django-gate2shop.git
    $ cd django-gate2shop
    $ python setup.py develop
    $ cd demo
    $ pip install -r requirements.txt
    $ python manage.py syncdb --noinput && python manage.py migrate --noinput
    $ python manage.py runserver >& /tmp/runserver.log &
    $ xdg-open http://127.0.0.1:8000/g2s/



Full Gateway Specification available at: http://www.g2s.com/documentation/
