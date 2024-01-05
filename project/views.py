from django.shortcuts import render


# Create your views here.
import requests
from django.http import HttpResponse




def index(request):
    return HttpResponse(
        """
    <body>
        <h1> Welcome to twin Tech AI powered job platform.</h1>
        <ul>
            <li><a href="/app">/app</a></li>
            <li><a href="/admin">/admin</a></li>
            
        </ul>
    </body>
    """)
