# from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from product.forms import BookForm
from product.models import Book
from user.models import CustomerUser


# Create your views here.
def index(request):
    context = {}
    context["users"] = CustomerUser.objects.all()
    return render(request, 'index.html', context)


# def index():
#     return "ju"


def products(request):
    context = {}
    context['books'] = Book.objects.all().order_by('-id')
    # context["yourname"] = "jaibhem2"
    # context["hello"] = "evening"
    # return render(request, 'products.html',{"yourname":"jaibhem"})
    return render(request, 'products.html', context)


def product_create(request):
    print("request -------->", request)

    print(" -------->")
    print("request method -------->", request.method),
    if request.method == "POST":
        print("--------------->  post data", request.POST)
        if "is_published" in request.POST:
            is_published_value = False
            if request.POST["is_published"] == "on":
                is_published_value = True
        else:
            is_published_value = False
        profile_pic = request.FILES.get("profile_pic")
        Book.objects.create(title=request.POST['title'], author=request.POST['author'],
                            num_pages=int(request.POST['num_pages']), description=request.POST['description'],
                            qualification=request.POST['qualification'], is_published=is_published_value,
                            profile_pic=profile_pic)

    return render(request, 'products_create.html')


def computer_products(request):
    return render(request, 'computer_products.html')


def cart_products(request):
    message = ""
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            form = BookForm()
            message = str(form.errors)
    else:
        form = BookForm()
    return render(request, 'cart_products.html', {"form": form, "message": message})


def cart_product_update(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm(instance=book)

    return render(request, 'cart_products.html', {"form": form})


def delete_book(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        book.delete()
        return redirect('index')
    return render(request, 'book_delete.html', {"book": book})
