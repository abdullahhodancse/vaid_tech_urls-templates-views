# from django.shortcuts import render,redirect

# from app1.forms import UserRegistrationForm
# from django.contrib import messages


# from django.views.generic.edit import FormView
# from django.http import HttpResponseNotFound
# from django.http import HttpResponse
# from datetime import date
# # from django.urls import reverse_lazy



#   #  function based view
# def singup(request):
#     if request.method == 'POST':   #request method
#         form = UserRegistrationForm(request.POST)  
#         if form.is_valid():  #validtion check
#             user = form.save()  
#             roll = form.cleaned_data.get('roll')
#             reg = form.cleaned_data.get('reg')
#             department = form.cleaned_data.get('department')
#             session = form.cleaned_data.get('session')

#             messages.success(request,f"login success")
#             return HttpResponseNotFound("<h1>Page not found</h1>")
#             return HttpResponse(status=201)

#             return redirect('login')    #Response((extara))
            
        
        
#         else:
#             messages.error(request,f"login unsuccess")

        

            
            
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'app.html', {'form': form, 'type': 'Signup'})    #redirecting templates




# # class singup(FormView):
# #     template_name = 'app.html'
# #     form_class = UserRegistrationForm

# #     def form_valid(self, form):
        
# #         user = form.save()
# #         roll = form.cleaned_data.get('roll')
# #         reg = form.cleaned_data.get('reg')
# #         department = form.cleaned_data.get('department')
# #         session = form.cleaned_data.get('session')

       
# #         return render(self.request, self.template_name, {
# #             'form': self.form_class(),
# #             'message': "Signup successful!"
# #         })


# # from django.views.generic import TemplateView
# # from django.shortcuts import render, redirect
# # from forms import UserRegistrationForm

# # class SignupTemplateView(TemplateView):
# #     template_name = "app.html"

# #     def get_context_data(self, **kwargs):
# #         context = super().get_context_data(**kwargs)
# #         context['form'] = UserRegistrationForm()
# #         context['type'] = 'Signup'
# #         return context

# #     def post(self, request, *args, **kwargs):
# #         form = UserRegistrationForm(request.POST)
# #         if form.is_valid():  # form validation check
# #             form.save()       # valid হলে save করা
# #             return redirect('success')  # success page এ redirect
# #         context = self.get_context_data()
# #         context['form'] = form  # error message সহ form
# #         return self.render_to_response(context)


    
# # from django.http import HttpResponse

# # def my_custom_page_not_found_view(request, exception):
# #     return HttpResponse("পেজটি পাওয়া যায়নি!", status=404)



# # @require_http_methods(["GET", "POST"])
# # def my_view(request):
# #     # এখানে কেবল GET বা POST request প্রক্রিয়াকৃত হবে
# #     pass





# # @require_GET
# # def my_get_view(request):
# #     # কেবল GET request অনুমোদিত
# #     pass



# # from django.views.decorators.http import condition
# # from django.http import HttpResponse
# # import datetime

# # def my_etag(request):
# #     return "v1"  # Resource version

# # def my_last_modified(request):
# #     return datetime.datetime(2025, 9, 13)  # Resource এর শেষ পরিবর্তন তারিখ

# # @condition(etag_func=my_etag, last_modified_func=my_last_modified)
# # def my_view(request):
# #     return HttpResponse("এই ভিউতে conditional processing ব্যবহার করা হয়েছে।")


# # from django.views.decorators.cache import cache_control
# # from django.http import HttpResponse

# # @cache_control(public=True, max_age=3600)
# # def my_view(request):
# #     return HttpResponse("এই ভিউ ১ ঘণ্টা পর্যন্ত cache হতে পারবে।")


# # from django.views.decorators.cache import never_cache
# # from django.http import HttpResponse

# # @never_cache
# # def my_secret_view(request):
# #     return HttpResponse("এই পেজ কখনও cache হবে না।")


# # from django.http import HttpResponseRedirect
# # from django.shortcuts import render
# # from .forms import UploadFileForm

# # # Imaginary function to handle an uploaded file.
# # from somewhere import handle_uploaded_file


# # def upload_file(request):
# #     if request.method == "POST":
# #         form = UploadFileForm(request.POST, request.FILES)
# #         if form.is_valid():
# #             handle_uploaded_file(request.FILES["file"])
# #             return HttpResponseRedirect("/success/url/")
# #     else:
# #         form = UploadFileForm()
# #     return render(request, "upload.html", {"form": form})



# # def signup(request):
# #     if request.method == 'POST':
# #         form = UserRegistrationForm(request.POST, request.FILES)  # Important: include request.FILES
# #         if form.is_valid():
# #             user = form.save()
# #             profile_picture = form.cleaned_data.get('profile_picture')
            
# #             # Optional: save profile picture to your Account model if needed
# #             Account.objects.create(
# #                 user=user,
# #                 roll=form.cleaned_data.get('roll'),
# #                 reg=form.cleaned_data.get('reg'),
# #                 department=form.cleaned_data.get('department'),
# #                 session=form.cleaned_data.get('session'),
# #                 # profile_picture=profile_picture  # if you have this field in Account
# #             )

# #             return redirect('login')  # redirect after successful signup
# #     else:
# #         form = UserRegistrationForm()

# #     return render(request, 'app.html', {'form': form, 'type': 'Signup'})



# from django.views.decorators.csrf import csrf_exempt, csrf_protect


# # @csrf_exempt
# # def upload_file_view(request):
# #     request.upload_handlers.insert(0, ProgressBarUploadHandler(request))
# #     return _upload_file_view(request)


# # @csrf_protect
# # def _upload_file_view(request):
# #     # Process request
# #     ...


# # from django.utils.decorators import method_decorator
# # from django.views import View
# # from django.views.decorators.csrf import csrf_exempt, csrf_protect


# # @method_decorator(csrf_exempt, name="dispatch")
# # class UploadFileView(View):
# #     def setup(self, request, *args, **kwargs):
# #         request.upload_handlers.insert(0, ProgressBarUploadHandler(request))
# #         super().setup(request, *args, **kwargs)

# #     @method_decorator(csrf_protect)
# #     def post(self, request, *args, **kwargs):
# #         # Process request
# #         ...



# # def my_view(request):
# #     obj = MyModel.objects.get(pk=1)
# #     return redirect(obj, permanent=True)


# # from django.shortcuts import get_object_or_404

# # def my_view(request):
# #     obj = get_object_or_404(MyModel, pk=1)


# # from django.shortcuts import get_list_or_404

# # def my_view(request):
# #     my_objects = get_list_or_404(MyModel, published=True)


from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib import messages
from .forms import UserRegistrationForm  # Make sure this is your form
from datetime import date
from django.contrib.auth.decorators import login_required
from app1.models import Account


def signup(request):
    if request.method == 'POST':  # If form is submitted
        form = UserRegistrationForm(request.POST)
        if form.is_valid():  # Validation check
            user = form.save()
            
            # Extract extra data if needed
            Account.objects.create(
            user=user,    
               
            roll = form.cleaned_data.get('roll'),
            reg = form.cleaned_data.get('reg'),
            department = form.cleaned_data.get('department'),
            session = form.cleaned_data.get('session') ),

            # Success message
            messages.success(request, f"Account created successfully! Please log in.")
            
            # Redirect to login page (preferred)
            return redirect('login')
        else:
            # Show error message
            messages.error(request, f"Signup unsuccessful. Please correct the errors below.")
    else:
        # GET request, show empty form
        form = UserRegistrationForm()

    # Render signup page with form
    return render(request, 'app1.html', {'form': form, 'type': 'Signup', 'my_date': date.today()})
    

# @login_required
# def login_view(request):
#      account=request.user.account
#      return render(request, 'login.html',{'account': account})



@login_required
def login_view(request):
    try:
        account = request.user.account
    except Account.DoesNotExist:
        account = None  # অথবা নতুন Account create করতে পারেন

    return render(request, 'login.html', {'account': account})
   