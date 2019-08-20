from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from post import Post

class AppTest(TestCase):
    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_blog') as mocked_ask_create_blog:
                mocked_input.side_effect = ('c','test','test title','q')
                app.menu()
                mocked_ask_create_blog.assert_called()

    def test_menu_prompt(self):
        with patch('builtins.input', return_value = 'q') as mocked_input:
           app.menu()
           mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value = 'q'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 posts)')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            #side effect is like the method show in return_value for test_menu_calls_print_blogs
            #however, side effect can be used to return multiple values
            #i.e, first time input is called, return 'test', 2nd time input is triggered return 'test author'
            mocked_input.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))

    def test_ask_read_blog(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.input', return_value = 'Test') as mocked_input:
            with patch('app.print_posts') as mocked_print:

                app.ask_read_blog()
                mocked_input.assert_called_with("Enter the title of the blog you wish to read: ")
                mocked_print.assert_called_with(blog)

    def test_print_posts(self):
        blog = Blog('Test', 'Test Author')
        blog.create_post('Test', 'Test Content')
        app.blogs = {'Test':blog}
        with patch('app.print_post') as mocked_print_post:
            app.print_posts(app.blogs['Test'])
            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        post = Post('Test', 'Test Content')
        expected = app.POST_TEMPLATE.format('Test', 'Test Content')
        with patch('builtins.print') as mock_print:
            app.print_post(post)
            mock_print.assert_called_with(expected)

    def test_create_post(self):
        blog = Blog('Test', 'Test Title')
        app.blogs = {'Test': blog}
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Title', 'Test Content')
            app.ask_create_post()
            self.assertEqual('Test Title', app.blogs['Test'].posts[0].title)
            self.assertEqual('Test Content', app.blogs['Test'].posts[0].content)





