from django.shortcuts import render

# Create your views here.
from wkhtmltopdf.views import PDFTemplateView


class MyPDF(PDFTemplateView):
    filename = 'my_pdf.pdf'
    template_name = 'sample.html'
    extra_context = {'title': 'Test KycPDF'}
    cmd_options = {
        'margin-top': 3,
    }
