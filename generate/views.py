from django.shortcuts import render
import string
import random

characters = list(string.ascii_letters+string.digits+"!\";#$%&'()*+,-./:;<=>?@[]^_`{|}~") 

# Create your views here.
def generate_password(request):
    print("Password generator function is working...")
    
    random.shuffle(characters)
    password=[]
    
    if request.method=='POST':
        length = int(request.POST['password_length'])
        
        for i in range(length):
            password.append(random.choice(characters))
            
        random.shuffle(password)
        password = "".join(password)
    
    
    return render(request, 'home.html', {'password': password})