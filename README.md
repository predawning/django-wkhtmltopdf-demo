# Django Wkhtmltopdf demo


Requirements
------------

Install the [wkhtmltopdf static binary](http://wkhtmltopdf.org/downloads.html).

This requires libfontconfig (on Ubuntu: ``sudo aptitude install libfontconfig``).

Python 2.6+ and 3.3+ are supported.


Installation
------------

```shell
    pip install -r requirements.txt
```

Demostration
------------

Run `./manage.py runserver`, then open `http://localhost:8080/pdf/` to open pdf, or `http://localhost:8080/pdf/?as=html` to see the html page
