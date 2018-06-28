import time
from django.core.management.base import BaseCommand, CommandError
from pdfapp.views import MyPDF
from django.template import loader, RequestContext
from django.test.client import RequestFactory
from wkhtmltopdf.utils import (_options_to_args, make_absolute_paths,
                               wkhtmltopdf, render_pdf_from_template,
                               render_to_temporary_file, RenderedFile)


class Command(BaseCommand):

    def handle(self, *args, **options):
        output_name = '/tmp/time-{}.pdf'.format(str(time.time()))
        cmd_options = MyPDF.cmd_options.copy()
        cmd_options.update({'output': output_name})
        extra_context = MyPDF.extra_context.copy()
        extra_context.update({'title':'this a report by dump script'})

        view = MyPDF.as_view(
            cmd_options=cmd_options,
            extra_context=extra_context
        )

        request = RequestFactory().get('/')
        response = view(request)
        response.render()
