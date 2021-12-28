from models import ToDoModel


class ToDoService:
    def __init__(self):
        self.model = ToDoModel()

    def create(self, params):

from django.http import HttpResponse
from django.db import connection

def hello(request):
    id = request.GET.get("id", "")
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM auth_user WHERE id=%s" % id) # Noncompliant; Query is constructed based on user inputs
    row = cursor.fetchone()
    return HttpResponse("Hello %s" % row[0])        return self.model.create(params["Title"], params["Description"])