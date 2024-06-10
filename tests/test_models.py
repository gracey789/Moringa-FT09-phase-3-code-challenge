import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")

    def test_author_invalid_name(self):
        with self.assertRaises(ValueError):
            author = Author(2, "")

    def test_article_invalid_title(self):
        with self.assertRaises(ValueError):
            article = Article(2, "Tiny", "Valid Content", 1, 1)

    def test_magazine_invalid_name(self):
        with self.assertRaises(ValueError):
            magazine = Magazine(2, "", "Technology")

if _name_ == "_main_":
    unittest.main()
