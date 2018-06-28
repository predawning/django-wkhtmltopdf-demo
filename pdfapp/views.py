from django.shortcuts import render

# Create your views here.
from wkhtmltopdf.views import PDFTemplateView


class MyPDF(PDFTemplateView):
    show_content_in_browser = True
    filename = 'my_pdf1.pdf'

    template_name = 'sample.html'

    header_template = "header.html"
    footer_template = "footer.html"

    extra_context = {'title': 'Test KycPDF'}
    cmd_options = {
        'margin-top': 30,
        "header-spacing": 10,
        "margin-bottom": 15,
        "footer-spacing": 5,
        'margin-left': 21,
        'margin-right': 21
    }
