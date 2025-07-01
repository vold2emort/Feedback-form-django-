from django.shortcuts import render, HttpResponseRedirect
from .form import ReviewForm
from .models import Review
from django.views import View
from django.views.generic import TemplateView

# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {"form": form})

    def post(self, request):
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/thank_you")
            return render(request, "reviews/review.html", {"form": form})

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
    

class ReviewListView(TemplateView):
    template_name = "reviews/review_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review = Review.objects.all()
        context["reviews"] = review
        return context


class ReviewDetail(TemplateView):
    template_name = "reviews/review_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"]
        review = Review.objects.get(pk=review_id)
        context["review"] = review
        return context

# def thank_you(request):
#     return render(request, "reviews/thank_you.html")