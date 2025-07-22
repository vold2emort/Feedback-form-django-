from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .form import ReviewForm
from .models import Review
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView

# Create your views here.

class AddFavouritView(View):
    def post(self, request):
        review_id = request.POST['review_id']
        fav_review = Review.objects.get(pk=review_id)
        # rev_txt = fav_review.review_text
        


class ReviewView(FormView):
    template_name = "reviews/review.html"
    success_url = "/thank_you"
    form_class = ReviewForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    # def get(self, request):
    #     form = ReviewForm()
    #     return render(request, "reviews/review.html", {"form": form})

    # def post(self, request):
    #     if request.method == 'POST':
    #         form = ReviewForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return HttpResponseRedirect("/thank_you")
    #         return render(request, "reviews/review.html", {"form": form})

# def review(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank_you")
#     else:
#         form = ReviewForm()
    
#     return render(request, "reviews/review.html", {"form": form})

class ThankyouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This doesn't work!"
        return context
    

class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews" # the name that goes to the template

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review = Review.objects.all() # imported from models.py
    #     context["reviews"] = review
    #     return context


class ReviewDetail(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs["id"]
    #     review = Review.objects.get(pk=review_id)
    #     context["review"] = review
    #     return context

# def thank_you(request):
#     return render(request, "reviews/thank_you.html")