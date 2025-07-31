
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Review, TeamMember
from .forms import ReviewForm

def review_list(request):
    reviews = Review.objects.filter(is_approved=True)
    team = TeamMember.objects.all()
    return render(request, 'reviews/review_list.html', {
        'reviews': reviews,
        'team': team
    })

@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()  # is_approved reste False par défaut
            return redirect('review_list')
    else:
        form = ReviewForm()
    return render(request, 'reviews/add_review.html', {'form': form})

