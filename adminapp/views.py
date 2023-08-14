from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from django.urls import reverse
from mainapp.models import ProductCategory, Product


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'пользователи'

    users_list = ShopUser.objects.all().order_by('-is_active',
                                                 '-is_superuser',
                                                 '-is_staff',
                                                 'username')

    context = {
        'title': title,
        'users_list': users_list,
    }

    return render(request, 'admin_staff/users.html', context)


def user_create(request):
    title = 'пользователи | создать'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)

        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin_staff:users'))
    else:
        user_form = ShopUserRegisterForm()

    context = {
        'title': title,
        'user_form': user_form,
    }

    return render(request, 'admin_staff/user_create.html', context)


def user_update(request, pk):
    pass


def user_delete(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
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