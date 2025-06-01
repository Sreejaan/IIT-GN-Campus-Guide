from django.shortcuts import get_object_or_404, render
from core.models import Person, Department, Role

def faculty_index(request):
    directors = Role.objects.filter(designation__code='director').select_related('person', 'designation')
    deans = Role.objects.filter(designation__code='dean').select_related('person', 'designation')
    departments = Department.objects.all()

    context = {
        'directors': directors,
        'deans': deans,
        'departments': departments,
    }
    return render(request, 'faculty/index.html', context)

def faculty_detail(request, slug):
    person = get_object_or_404(Person, slug=slug)
    roles = person.roles.select_related('department', 'designation')
    map_steps = person.map_steps.all()  # This will already be ordered by step_number due to Meta

    return render(request, 'faculty/detail.html', {
        'person': person,
        'roles': roles,
        'map_steps': map_steps,
    })

def department_detail(request, code):
    department = get_object_or_404(Department, code=code)
    # Exclude director and dean roles here, as you said
    roles = Role.objects.select_related('person', 'designation').filter(department=department).exclude(designation__code__in=['director', 'dean'])
    return render(request, 'faculty/department.html', {'department': department, 'roles': roles})
