from django.contrib.auth import login,logout, authenticate
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .forms import ProductForm
from .models import Product
from django.views.generic import View
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

class Index(TemplateView):
    template_name = "index.html"

class AboutUs(TemplateView):
    template_name = "aboutUs.html"

class LoginView(View):
    template_name = "login.html"
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

class LogoutView(View):
    template_name = "logout.html"
    def get(self, request):
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return redirect('/')


class RegisterView(View):
    template_name = "register.html"
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, "Registration successful.")
            return redirect(reverse('/'))

        return render(request, 'register.html', { 'form': form })


class ProductListView(ListView):
    template_name = 'list_products.html'
    name = "list_products"
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        return data

class ProductAddView(CreateView):
    template_name = "products.html"
    name = "add_products"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("admin_panel:add_products")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _('Successfully product added'))
        return super(ProductAddView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, mark_safe(form.errors))
        return super(ProductAddView, self).form_invalid(form)


class ProductUpdateView(UpdateView):
    form_class = ProductForm
    model = Product
    template_name = "products.html"
    name = "update_products"
    success_url = reverse_lazy("admin_panel:update_products")
    dec_url = reverse_lazy("admin_panel:update_products")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Successfully products updated')
        return super(ProductUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return redirect(self.request.META.get('HTTP_REFERER', '/'))

class ProductDeleteView(DeleteView):
    name = "delete_products"
    success_url = reverse_lazy("admin_panel:delete_products")
    model = Product

    def get(self, request, pk, *args, **kwargs):
        obj = Product.objects.filter(id=pk)
        obj.delete()
        messages.success(request, _('Successfully product deleted'))
        return redirect('/')

