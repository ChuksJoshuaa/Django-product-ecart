from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Product, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ProductForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,)
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.


class list_view(ListView):
    model = Product
    template_name = "prod_home.html"
    context_object_name = 'main'
    ordering = ['-created_at']
    paginate_by = 6

class detail_view(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "prod_detail.html"
    paginate_by = 3

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        return get_object_or_404(Product, id=id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs["id"]

        form = CommentForm()
        post = get_object_or_404(Product, id=id)
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form
        return context


    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        post = Product.objects.filter(id=self.kwargs['id'])[0]
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data['comment']
            comment = Comment.objects.create(commenter_name=name, comment=body, post=post)

        else:
            form = CommentForm()
            context['form'] = form
            return self.render_to_response(context=context)

        return self.render_to_response(context=context)

def delete_comment(request, pk):
    comment = Comment.objects.filter(post=pk).last()
    post_id = comment.post.id
    comment.delete()
    return redirect(reverse('prod-detail', args=[post_id]))

def search_view(request):
    query = request.GET['query']
    post = Product.objects.filter(name__icontains=query)
    context = {
        "post": post
    }
    return render(request, 'prod_search.html', context)

def aboutview(request):
    context = {

        "title": "About Page"
    }
    return render(request, "product_about.html", context)

@login_required
def createview(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('prod-home')
    else:
        form = ProductForm()

    context = {
        "form": form
    }

    return render(request, 'prod_form.html', context)


@login_required
def content_view(request):
    products = Product.objects.all()

    context = {
        "products": products
    }
    return render(request, "pdf_report.html", context)

def pdf_report_create(request):
    products = Product.objects.all()

    template_name = 'pdf_show_report.html'

    context = {'products': products}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="products_report.pdf"'

    template = get_template(template_name)

    html = template.render(context)

    pisa_status = pisa.CreatePDF(
       html, dest=response)

    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

class update_view(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = ProductForm
    template_name = "prod_form.html"
    queryset = Product.objects.all()

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        return get_object_or_404(Product, id=id)


    def test_func(self):
        Product = self.get_object()
        if self.request.user == Product.person:
            return True
        else:
            return False

    def get_success_url(self):
        return "/Product/home/"

class delete_view(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = "prod-delete.html"

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        return get_object_or_404(Product, id=id)

    def test_func(self):
        Product = self.get_object()
        if self.request.user == Product.person:
            return True
        else:
            return False

    def get_success_url(self):
        return "/Product/home/"

