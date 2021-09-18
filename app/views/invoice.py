from flask import Blueprint, render_template, request
from flask.views import MethodView, View


task = Blueprint(
    'invoice',
    __name__,
    url_prefix='/invoice'
)


class GenerateInvoiceView(MethodView):
    """
    Generate a new invoice
    """
    def get(self):
        pass

    def post(self):
        pass


class InvoiceHistory(View):
    """
    List all generated invoice history
    """
    def dispatch_request(self):
        pass


task.add_url_rule("/", view_func=GenerateInvoiceView.as_view('invoice_view'))
task.add_url_rule("/history", view_func=InvoiceHistory.as_view('invoice_history'))
