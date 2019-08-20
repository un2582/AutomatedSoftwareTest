from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    #This is no longer a unit test, since it depends on post and blog to both work. So it depends on two things to work
    def test_create_post_in_blog(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', "Test Content")

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Test Post')
        self.assertEqual(b.posts[0].content, 'Test Content')

    def test_json_no_post(self):
        b = Blog('Test', 'Test Author')
        expected = {'title': 'Test', 'author':'Test Author', 'posts':[]}

    def test_json(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')

        expected = {'title': 'Test', 'author':'Test Author', 'posts': [{'title':'Test Post', 'content':"Test Content"}]}
        self.assertEqual(b.json(), expected)