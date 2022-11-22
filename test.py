import unittest
from main import add_movie
from main import movies


class TestMovies(unittest.TestCase):
    def test_add_movie(self):
        movies.clear()
        add_movie()
        count = len(movies)
        self.assertEqual(count, 1)


if __name__ == '__main__':
    unittest.main()
