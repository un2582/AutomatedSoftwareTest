from blog import Blog
POST_TEMPLATE = '''
--- {} ---

{}
'''
MENU_PROMPT = 'Enter "c" to create a blog, "1" to list blogs, "r" to read one, "p" to create a post, or q to quit: '
blogs = dict() #blog_name : Blog object

def menu():
    #Show the user the avvailable blogs
    #Let the user make a choice
    #do something wit hthe choice
    #eventually exit
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)

def print_blogs():
    for key, blog in blogs.items(): #(blog name: blog) , (blog name: blog)
        print('- {}'.format(blog))

def ask_create_blog():
    title = input("Enter your title: ")
    author = input("Enter your name: ")

    blogs[title] = Blog(title,author)

def ask_read_blog():
    title = input("Enter the title of the blog you wish to read: ")

    print_posts(blogs[title])

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))

def ask_create_post():
    blog = input("Enter the blog title you wish to write a post in: ")
    title = input("Enter your post title: ")
    content = input("Enter your content title: ")

    blogs[blog].create_post(title,content)
