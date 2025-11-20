from django.http import HttpResponse

def menu_list(request):
    return HttpResponse("LISTA DE MENÚ")

def menu_create(request):
    return HttpResponse("CREAR PLATO")

def menu_edit(request, pk):
    return HttpResponse(f"EDITAR PLATO {pk}")

def menu_delete(request, pk):
    return HttpResponse(f"ELIMINAR PLATO {pk}")
