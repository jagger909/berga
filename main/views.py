from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from .forms import ZayavkaForm
from .models import sms_send


#class IndexPageView(TemplateView):
#    template_name = "index.html"
#    context_object_name = 'index'

#    zayavka_view(request)
    # def get_context_data(self, **kwargs):
    #    context = super(HomePageView, self).get_context_data(**kwargs)
    #    context['latest_articles'] = Article.objects.all()[:5]
    #    return context


def index_view(request):
    args = {}

    if request.method == 'POST':
        zayavka_form = ZayavkaForm(request.POST)

        if zayavka_form.is_valid():
            phone_number = zayavka_form.cleaned_data['phone_number']
            zayavka_text = zayavka_form.cleaned_data['zayavka_text']
            zayavka_name = zayavka_form.cleaned_data['zayavka_name']
            zayavka_msg = "zayavka ot %s %s %s" % (phone_number, zayavka_name, zayavka_text)
            sms_request = sms_send(zayavka_msg)
            args['sms_request'] = sms_request

        else:
            zayavka_msg = 'Не правильно заполнена форма!!'


    else:
        zayavka_form = ZayavkaForm()
        zayavka_msg = "Введите данные!"

    args['zayavka_form'] = zayavka_form
    args['title'] = 'BismIllah:'
    args['sms_text'] = zayavka_msg

    return render(request, 'index.html', args)
