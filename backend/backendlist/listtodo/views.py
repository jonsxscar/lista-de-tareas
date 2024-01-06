from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Task
from django.forms.models import model_to_dict
# Create your views here.

class TaskView(View):
    def get(self, request):
        try:
            tasks = list(Task.objects.values())
            return JsonResponse(tasks, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def post(self, request):
        try:
            data = request.POST
            task = Task.objects.create(
                title=data.get('title'),
                description=data.get('description'),
                completed=data.get('completed') == 'true'
            )
            return JsonResponse(model_to_dict(task), status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    def put(self, request, id):
        try:
            data = request.POST
            Task.objects.filter(id=id).update(
                title=data.get('title'),
                description=data.get('description'),
                completed=data.get('completed') == 'true'
            )
            task = Task.objects.get(id=id)
            return JsonResponse(model_to_dict(task))
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def delete(self, request, id):
        try:
            Task.objects.get(id=id).delete()
            return JsonResponse({'id': id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
