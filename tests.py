from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.


class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title='sq', description='sqlith')

    def test_instance(self):
        post = Post.objects.get(title='sq')
        excepted_object_title = f"{post.title}"
        self.assertEqual(excepted_object_title, 'sq')


class hompageTest(TestCase):
    def setUp(self):
        Post.objects.create(title='python', description='python is good')


    def test_view_url_locations(self):
        response = self.client.get('/post/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_name(self):
        response = self.client.get(reverse('post'))
        self.assertEqual(response.status_code, 200)


    def test_view_template(self):
        response = self.client.get(reverse('post'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task/task.html')

