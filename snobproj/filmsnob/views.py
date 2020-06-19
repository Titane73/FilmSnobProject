from django.shortcuts import render, get_object_or_404
from .models import Movies, Review
from .forms import AddMovie, AddReview
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'filmsnob/index.html')

def getMovies(request):
    movie_list = Movies.objects.all()
    return render(request, 'filmsnob/movies.html', {'movie_list' : movie_list})

def getReview(request, id):
    this_movie = Movies.objects.get(pk=id)
    review = Review.objects.filter(movie = id)
    context = {
        'this_movie' : this_movie,
        'review' : review,
    }
    return render(request, 'filmsnob/review.html', context = context)

@login_required
def newMovie (request):
    form = AddMovie
    if request.method=='POST':
          form=AddMovie(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=AddMovie()
    else:
          form=AddMovie()
    return render(request, 'filmsnob/newmovie.html', {'form': form})

@login_required
def newReview (request):
    form = AddReview
    if request.method=='POST':
          form=AddReview(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=AddReview()
    else:
          form=AddReview()
    return render(request, 'filmsnob/newreview.html', {'form': form})

def loginmessage(request):
    return render(request, 'filmsnob/loginmessage.html')

def logoutmessage(request):
    return render(request, 'filmsnob/logoutmessage.html')
