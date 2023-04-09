import traceback

from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from .models import Order
from .forms import CreateOrder
from django.shortcuts import get_object_or_404
import json
from django.forms import model_to_dict


@require_GET
def order_detail(request, id):
    order = get_object_or_404(Order, id=id)
    return JsonResponse(model_to_dict(order), safe=False)


@require_POST
@csrf_exempt
def create_order(request):
    form = CreateOrder(json.loads(request.body))
    error_message = dict(message="Validation Error", code=400,
                         fields=dict(merchant_order_id=["order already exist"]))
    if not form.is_valid():
        error_message['fields'] = form.errors
        return JsonResponse(dict(error=error_message), status=400)
    values = form.cleaned_data

    if Order.objects.filter(merchant_id=values["merchant_id"],
                            merchant_order_id=values["merchant_order_id"]).count() > 0:
        return JsonResponse(dict(error=error_message), status=400)
    try:
        instance = form.save()
    except IntegrityError as e:
        traceback.print_exception(e)
        return JsonResponse(dict(error=error_message), status=400)
    return JsonResponse(model_to_dict(instance), safe=False)
