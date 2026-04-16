from django.shortcuts import render
from django.http import HttpResponse

nav = """
    <nav>
        <a href='/'>Home</a> |
        <a href='/services/'>Services</a> |
        <a href='/staff/'>Staff</a> |
        <a href='/contact/'>Contact</a>
    </nav>
"""
name = "Tim"
age = 24
gains = 234.5634224

home_body = f"""
    <ol>
        <li>Name: {name}</li>
        <li>Age: {age}</li>
        <li>Gains: {gains:.2f}</li>
    </ol>
    
"""

services_provided = [
    "web development",
    "react development",
    "frontend",
    "backend",
    "UI/UX design"
]

members = {
    "Tim Lee": 2,
    "Jonathan Greenfield": 5,
    "Quentin Larry": 7,
    "Mario Lopez": 4,
}

def home(request):
    content= """
            <h1>Welcome to my Page</h1>
            <h2>Visit around</h2>
            <p>Enjoy the content</p>
    """
    
    return HttpResponse(nav + content + home_body)

def contact(request):
    message = "Please contact us at"
    number = "521-123-5231"
    contact_info = f"<h3>{message}</h3>\n<h4>{number}</h4>"
    div = f"<div>{contact_info}</div>"
    
    return HttpResponse(nav + div)

def services(request):
    string = ""
    for service in services_provided:
        string += f"<h3>{service}</h3>"
        
    div = f"<div>{string}</div>"
    
    return HttpResponse(nav + div)

def staff(request):
    string = ""
    for name, experience in members.items():
        string += f"<h3>{name}</h3>\n<h3>Experience: {str(experience)} years</h3>"
    
    div = f"<div>{string}</div>"
    
    return HttpResponse(nav + div)