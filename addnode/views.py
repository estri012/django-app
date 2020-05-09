from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from rest_framework.response import Response


# Create your views here.
def add_node(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f'Permintaan menambah node baru dari {form.cleaned_data["username"]}'
            message = f'Pemohon: {form.cleaned_data["email"]}\nLokasi node: {form.cleaned_data["lokasi_pemasangan_node"]}\nPJ: {form.cleaned_data["penanggung_jawab_pemasangan"]}\nKontak PJ: {form.cleaned_data["no_telp_penanggung_jawab"]}\nTanggal pemasangan: {form.cleaned_data["tanggal_pemasangan_node"]}\nSensor node: {form.cleaned_data["sensor_yang_digunakan_pada_node"]}'
            sender = form.cleaned_data["email"]
            recipients = ['gmlews.ugm@gmail.com']
            try:
                send_mail(subject, message, sender, recipients, fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect(add_node)
    return render(request, 'addnode.html', {'form':form})
