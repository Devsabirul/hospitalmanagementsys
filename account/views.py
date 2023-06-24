from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout


User = get_user_model()


class Signin(View):
    template_name = ''

    def get_context_data(self, **kwargs):
        context = {
            "error_msg": ""
        }
        context['is_admin'] = kwargs.get('is_admin')
        context['is_doctor'] = kwargs.get('is_doctor')
        context['is_reception'] = kwargs.get('is_reception')
        return context

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            is_admin = kwargs.get('is_admin')
            is_doctor = kwargs.get('is_doctor')
            is_reception = kwargs.get('is_reception')
            context = self.get_context_data(is_admin=is_admin,
                                            is_doctor=is_doctor, is_reception=is_reception)
            return render(request, self.template_name, context)
        else:
            return redirect("home")

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        is_admin = kwargs.get('is_admin')
        is_doctor = kwargs.get('is_doctor')
        is_reception = kwargs.get('is_reception')
        context = self.get_context_data(is_admin=is_admin,
                                        is_doctor=is_doctor, is_reception=is_reception)

        if is_admin == True:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")
            else:
                context['error_msg'] = "Invalid Username and Password!!"

        # if is_doctor == True:
        #     user = authenticate(username=username, password=password)
        #     if user:
        #         login(request, user)
        #         return redirect("home")
        #     else:
        #         context['error_msg'] = "Invalid Username and Password!!"

        # if is_reception == True:
        #     if user:
        #         login(request, user)
        #         return redirect("home")
        #     else:
        #         context['error_msg'] = "Invalid Username and Password!!"
        return render(request, self.template_name, context)


def logout_(request):
    logout(request)
    return redirect('home')
