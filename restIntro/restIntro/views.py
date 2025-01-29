from django.http import HttpRequest, HttpResponse
import json
from .models import User
from django.shortcuts import get_object_or_404

def users(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        users = User.objects.all()
        serialized_users = [user.name for user in users]
        return HttpResponse(json.dumps(serialized_users))

    if request.method == "POST":
        body = json.loads(request.body)
        user = User(name=body['name'], email=body['email'], age=body['age'])
        user.save()
        return HttpResponse(json.dumps({'id': user.id, 'name': user.name}))

def get_update_or_delete_user(request: HttpRequest, id:int) -> HttpResponse:
    if request.method == "GET":
        user=get_object_or_404(User, id=id)
        return HttpResponse(json.dumps({'id': user.id, 'name': user.name, 'age': user.age, 'email': user.email}))

    if request.method == "PUT":
        body = json.loads(request.body)
        user = get_object_or_404(User, id=id)
        user.name = body['name']
        user.age = body['age']
        user.email = body['email']
        user.save()
        return HttpResponse(json.dumps({'id': user.id, 'name': user.name, 'age': user.age, 'email': user.email}))

    if request.method == "DELETE":
        user = get_object_or_404(User, id=id)
        user.delete()
        return HttpResponse(json.dumps({'id': id, 'deleted': True}))

