# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import pymongo

from database import Database
from menu import Menu
from models.blog import Blog

# from models.post import Post
__author__ = 'Jotham'

Database.initialize()

# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
# print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
# print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# uri = "mongodb://127.0.0.1:27017"
# client = pymongo.MongoClient(uri)
# database = client['fullstack']
# collection = database['students']

# students = collection.find({})
# student_list = []
#
# for student in students:
#     print(student)
#     student_list.append(student)

# students = [student for student in collection.find({})]
# print(students)

# students = [student['score'] for student in collection.find({})]
# print(students)

# students = [student['score'] for student in collection.find({}) if student['score'] == 100.0]
# print(students)

# post = Post("Post1 Title", "Post1 Content is here", "Post1 author")
# post2 = Post("Post2 Title", "Post2 Content is also here", "Post2 author")
# post2.content = "Different Content"

# print(post.content)
# print(post2.content)

# post = Post(blog_id="123",
#             title="Another great post",
#             content="This is a great content",
#             author="jotham")
#
# post.save_to_mongo()

# post = Post.from_mongo('fb827d996b4841f8a96e1dc7e6de43ba')
# print(post)

# posts = Post.from_blog('123')
# for post in posts:
#     print(post)

# blog = Blog(author="Jotham",
#             title="Sample title",
#             description="Sample description")
#
# blog.new_post()
#
# blog.save_to_mongo()
#
# from_database = Blog.from_mongo(blog.id)
#
# print(blog.get_posts())

menu = Menu()
menu.run_menu()
