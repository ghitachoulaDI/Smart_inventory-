from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum, F
from django.utils import timezone

from .models import Product, Customer, Order, OrderItem
from .forms import ProductForm, CustomerForm, OrderForm, OrderItemFormSet


# -------------------------
# Dashboard
# -------------------------
def dashboard(request):
    total_products = Product.objects.count()
    total_customers = Customer.objects.count()
    total_orders = Order.objects.count()

    stock_value = (
        Product.objects.aggregate(total=Sum(F("price") * F("quantity_in_stock")))
        .get("total")
        or 0
    )

    # Revenu total (si unit_price existe, sinon product.price)
    try:
        revenue_total = (
            OrderItem.objects.aggregate(total=Sum(F("unit_price") * F("quantity")))
            .get("total")
            or 0
        )
    except Exception:
        revenue_total = (
            OrderItem.objects.aggregate(total=Sum(F("product__price") * F("quantity")))
            .get("total")
            or 0
        )

    context = {
        "total_products": total_products,
        "total_customers": total_customers,
        "total_orders": total_orders,
        "stock_value": stock_value,
        "revenue_total": revenue_total,
    }
    return render(request, "inventory/dashboard.html", context)


# -------------------------
# Products CRUD
# -------------------------
def product_list(request):
    products = Product.objects.all().order_by("name")
    return render(request, "inventory/product_list.html", {"products": products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "inventory/product_detail.html", {"product": product})


def product_create(request):
    title = "Add Product"
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()

    return render(request, "inventory/product_form.html", {"form": form, "title": title})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    title = "Edit Product"

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_detail", pk=product.pk)
    else:
        form = ProductForm(instance=product)

    return render(request, "inventory/product_form.html", {"form": form, "title": title})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.delete()
        return redirect("product_list")

    return render(request, "inventory/product_confirm_delete.html", {"product": product})


# -------------------------
# Customers CRUD
# -------------------------
def customer_list(request):
    customers = Customer.objects.all().order_by("name")
    return render(request, "inventory/customer_list.html", {"customers": customers})


def customer_create(request):
    title = "Add Customer"
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("customer_list")
    else:
        form = CustomerForm()

    return render(request, "inventory/customer_form.html", {"form": form, "title": title})


def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    title = "Edit Customer"

    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customer_list")
    else:
        form = CustomerForm(instance=customer)

    return render(request, "inventory/customer_form.html", {"form": form, "title": title})


def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    if request.method == "POST":
        customer.delete()
        return redirect("customer_list")

    return render(request, "inventory/customer_confirm_delete.html", {"customer": customer})


# -------------------------
# Orders
# -------------------------
def order_list(request):
    orders = Order.objects.all().order_by("-order_date")
    return render(request, "inventory/order_list.html", {"orders": orders})


def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    items = OrderItem.objects.filter(order=order)
    return render(request, "inventory/order_detail.html", {"order": order, "items": items})


def order_create(request):
    title = "Create Order"

    if request.method == "POST":
        order_form = OrderForm(request.POST)
        formset = OrderItemFormSet(request.POST)

        if order_form.is_valid() and formset.is_valid():
            order = order_form.save(commit=False)
            order.order_date = timezone.now()
            order.save()

            items = formset.save(commit=False)
            for item in items:
                item.order = order

                # Vérification stock
                if item.quantity > item.product.quantity_in_stock:
                    order.delete()
                    return render(
                        request,
                        "inventory/order_form.html",
                        {
                            "order_form": order_form,
                            "formset": formset,
                            "title": title,
                            "error": f"Stock insuffisant pour {item.product.name}",
                        },
                    )

                # Déduction stock
                item.product.quantity_in_stock -= item.quantity
                item.product.save()
                item.save()

            return redirect("order_list")
    else:
        order_form = OrderForm()
        formset = OrderItemFormSet()

    return render(
        request,
        "inventory/order_form.html",
        {"order_form": order_form, "formset": formset, "title": title},
    )