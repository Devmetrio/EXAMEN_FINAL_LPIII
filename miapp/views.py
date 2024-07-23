from django.shortcuts import render,get_object_or_404, redirect # type: ignore
from .models import AMES_Persona
from django.contrib import messages # type: ignore
# Create your views here.
def index(request):
    return render(request, 'index.html')

def personas(request):
    personaLis = AMES_Persona.objects.all()
    return render(request, 'index.html', {"persona": personaLis})

def agregar_persona(request):
    return render(request, 'agregar_persona.html')

def registrar_persona(request, persona_id=None):
    persona = None
    if persona_id:
        persona = get_object_or_404(AMES_Persona, id=persona_id)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        sexo = request.POST.get('sexo')
        if persona_id:
            persona.nombre = nombre
            persona.apellidos = apellidos
            persona.sexo = sexo
            persona.save()
            messages.success(request, 'Persona actualizada exitosamente.')
        else:
            AMES_Persona.objects.create(nombre=nombre, apellidos=apellidos, sexo=sexo)
            messages.success(request, 'Persona creada exitosamente.')
        return redirect('/personas/')
    return render(request, 'agregar_persona.html', {'persona': persona})

def eliminar_persona(request, persona_id):
    persona = get_object_or_404(AMES_Persona, id=persona_id)
    if request.method == 'POST':
        persona.delete()
        return redirect('/personas/')
    # Handle GET request (optional)
    return redirect('/')