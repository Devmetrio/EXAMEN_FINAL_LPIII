from django.shortcuts import render, redirect
from .models import AMES_Persona
# Create your views here.
# Create your views here.
def index(request):
    return render(request, 'index.html')

def personas(request):
    personaLis = AMES_Persona.objects.all()
    return render(request, 'index.html', {"persona": personaLis})

def agregar_persona(request):
    return render(request, 'agregar_persona.html')

def registrar_persona(request):
    nombre = request.POST.get('nombre')
    apellidos = request.POST.get('apellidos')
    sexo = request.POST.get('sexo')
    AMES_Persona.objects.create(
    nombre=nombre, apellidos=apellidos, sexo=sexo)
    return redirect('/personas/')

def eliminar_persona(request, persona_id):
    persona = get_object_or_404(AMES_Persona, id=persona_id)
    if request.method == 'POST':
        persona.delete()
        return redirect('/agregar_persona/')  # Redirect to a suitable URL after deletion
    # Handle GET request (optional)
    return redirect('/')