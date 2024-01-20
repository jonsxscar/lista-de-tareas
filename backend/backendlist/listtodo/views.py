import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Task
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class TaskView(View):
    def get(self, request):
        try:
            tasks = list(Task.objects.values())
            return JsonResponse(tasks, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def post(self, request):
        try:
            data = json.loads(request.body)
            task = Task.objects.create(
                title=data.get('title'),
                description=data.get('description'),
                completed=data.get('completed')
            )
            return JsonResponse(model_to_dict(task), status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
    def put(self, request, id):
        try:
            data = json.loads(request.body)
            Task.objects.filter(id=id).update(
                title=data.get('title'),
                description=data.get('description'),
                completed=data.get('completed')
            )
            task = Task.objects.get(id=id)
            return JsonResponse(model_to_dict(task))
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def delete(self, request, id):
        try:
            task = Task.objects.get(id=id)
        except Task.DoesNotExist:
            return JsonResponse({'error': 'La tarea no existe'}, status=404)

        try:
            task.delete()
            return JsonResponse({'id': id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class TaskDetailView(View):
    def get(self, request, id):
        try:
            task = Task.objects.get(id=id)
            return JsonResponse(model_to_dict(task), safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def put(self, request, id):
        try:
            data = json.loads(request.body)
            Task.objects.filter(id=id).update(
                title=data.get('title'),
                description=data.get('description'),
                completed=data.get('completed') 
            )
            task = Task.objects.get(id=id)
            return JsonResponse(model_to_dict(task))
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def delete(self, request, id):
        try:
            task = Task.objects.get(id=id)
        except Task.DoesNotExist:
            return JsonResponse({'error': 'La tarea no existe'}, status=404)

        try:
            task.delete()
            return JsonResponse({'id': id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
