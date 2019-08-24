from django.shortcuts import render, redirect,get_object_or_404
from .models import Cliente
from.forms import ClienteForm

# Create your views here.

def lista_de_clientes(request):
   clientes = Cliente.objects.all().order_by('-id')
   return render(request,"clientes/lista_de_clientes.html", {'clientes':clientes})

   def adicionar_cliente(request):
      form = ClienteForm(request.POST)
      if form.isvalid():
         obj = form.save()
         obj.save()
         form = ClienteForm()
         return redirect('lista_de_clientes')

      return render(request,"clientes/adcionar_cliente.html", {'form'})   

      def editar_cliente(request,id=None):
         cliente = get_object_or_404(Cliente,id=id)
         form - ClienteForm(reuest.POST or none, instance=cliente)
         if form.is_valid():
            obj.save()
            return redirect('lista_de_clientes')
         return render(request, "clientes/edita_cliente.html"), {'form'}:form})