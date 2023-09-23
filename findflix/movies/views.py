from django.shortcuts import render
from .models import Movie

def genre(request):
    return render(request, 'genre.html')

def movie(request):
    selected_genre = request.GET.get('genre')
    if selected_genre:
        movies = Movie.objects.filter(genre=selected_genre)
    else:
        movies = Movie.objects.all()
    
    return render(request, 'movie.html', {'movies': movies})

