from django.test import TestCase
from cinema.models import Movie


class ModelTest(TestCase):
    def test_movie_str(self):
        movie = Movie.objects.create(
            title="Test_title",
            description="Test description.",
            duration=100
        )
        self.assertEqual(str(movie), movie.title)
