from django.core.checks.messages import Error
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password , check_password
from Website.models.customer import Customer
from django.views import View

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        
        last_name = postData.get('lastname')
        phone_number = postData.get('phone_number')
        email = postData.get('email')
        password = postData.get('password')

        #validation
        value ={
            'first_name': first_name,
            'last_name': last_name,
            'phone_number': phone_number,
            'email': email
        }
        error_message = None

        customer = Customer(first_name=first_name,
                                last_name=last_name,
                                phone_number = phone_number,
                                email= email,
                                password=password)

        error_message = self.validateCustomer(customer)

        
        
        
        print(first_name, last_name, phone_number, email, password)
        
            
        
        if not error_message:
            

            customer.password = make_password(customer.password)
            customer.register()

            return redirect('storepage')
        else:
            data ={
                'error': error_message,
                'values' : value
            }
            return render(request, 'signup.html', data )

    def validateCustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message= "First name required"
        elif len(customer.first_name) < 4:
            error_message = "First Name must be 4 character long or more"
        elif not customer.last_name:
            error_message="Last name required"
        elif len(customer.last_name) < 4 :
            error_message="last name must be atleast 4 characters"
        elif not customer.phone_number:
            error_message="Phone number is required"
        elif len(customer.phone_number) > 10:
            error_message= "phone number should not exceed 10 characters"
        elif len(customer.password) < 6:
            error_message = "Password must be atleast 6 character long"
        elif len(customer.email) < 5:
            error_message = "Email must be atleast 5 character long"
        elif customer.isExists():
            error_message = 'Email Address already registered . . '
            
        return error_message