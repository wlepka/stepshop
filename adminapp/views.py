from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    title = 'админка/главная'

    context = {
        'title': title,
    }

    return render(request, 'admin_staff/index.html', context)


class UsersListView(ListView):
    model = ShopUser
    template_name = 'admin_staff/users.html'
    context_object_name = 'users_list'
    paginate_by = 2

    def get_queryset(self):
        return ShopUser.objects.all().order_by('-is_active',
                                               '-is_superuser',
                                               '-is_staff',
                                               'username')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UsersListView, self).get_context_data()
        # context['title'] = 'пользователи'
        context.update({'title': 'пользователи'})
        return context


class UserCreateView(CreateView):
    model = ShopUser
    template_name = 'admin_staff/user_create.html'
    success_url = reverse_lazy('admin_staff:users')
    form_class = ShopUserRegisterForm

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'пользователи/создание'
        return context

    def form_valid(self, form):
        user = form.save()
        user.is_active = True
        user.save()
        return HttpResponseRedirect(self.get_success_url())


def user_update(request, pk):
    pass


def user_delete(request, pk):
    pass


def categories(request):
    title = 'категории'

    categories_list = ProductCategory.objects.all()

    context = {
        'title': title,
        'categories_list': categories_list,
    }

    return render(request, 'admin_staff/categories.html', context)


def category_create(request):
    pass


def category_update(request, pk):
    pass


def category_delete(request, pk):
    pass


def products(request, pk):
    title = 'продукты'

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    context = {
        'title': title,
        'category': category,
        'products_list': products_list,
    }

    return render(request, 'admin_staff/products.html', context)


def product_create(request, pk):
    pass


def product_read(request, pk):
    pass


def product_update(request, pk):
    pass


def product_delete(request, pk):
    pass
