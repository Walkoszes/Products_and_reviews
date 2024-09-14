from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ReviewForm

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            review.product = product
            review.save()
            return redirect("product_detail", pk=product.pk)
    else:
        form = ReviewForm()
    
    return render(request, "product_detail.html", {
    "product": product, 
    "form": form,
    "reviews": product.review_set.all(),
})
