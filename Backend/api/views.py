from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def echo(request):  # Renamed to 'echo' to match your api/urls.py
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            text = data.get('text', 'No text provided')
            return JsonResponse({'reply': f'Backend received: {text}'})
        except Exception as e:
            return JsonResponse({'reply': f'Error: {str(e)}'}, status=500)
    return JsonResponse({'reply': 'Only POST allowed'}, status=405)