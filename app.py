from blog import Blog

MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, "q" to quit.'
POST_TEMPLATE = '\n\t--- Post title ---\n\nPost content\n'
blogs = dict() # blog_name : Blog object


def menu():

    # Show the user the available blogs
    # Let the user make a choice
    # Do something with that choice
    # Eventually exit

    # print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            create_post()
        selection = input(MENU_PROMPT)


def print_blogs():
    for key, blog in blogs.items():  # [(blog_name, Blog), (blog_name, Blog)]
        print('- {}'.format(blog))

def ask_create_blog():
    title = input('Input blog title to create: ')
    author = input('Input blog author to create: ')

    blogs[title] = Blog(title, author)

def ask_read_blog():
    title = input('Input blog title to read: ')
    print_posts(blogs[title])

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))

def create_post():
    # ask for blog title
    # ask for post title
    # ask for post content
    # create new post in the blog
    blog_title = input('Input blog title to work with: ')
    post_title = input('Input post title to create: ')
    post_content = input('Input post content to create: ')
    blogs[blog_title].create_post(post_title, post_content)


