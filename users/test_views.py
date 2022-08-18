from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Comment


class TestUsersViews(TestCase):
    """
    A class for testing the Users app views.
    """
    def test_get_create_user_page(self):
        response = self.client.get('/user/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login_register.html')

    def test_get_login_user_page(self):
        response = self.client.get('/user/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login_register.html')

    def test_get_redirected_by_logout_user_page(self):
        response = self.client.get('/user/logout/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/user/login/')

    def test_get_redirected_by_user_profile_page(self):
        response = self.client.get('/user/profile/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/user/login/')

    def test_get_redirected_by_edit_profile_page(self):
        response = self.client.get('/user/profile/edit/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/user/login/')

    def test_get_redirected_by_delete_profile_page(self):
        response = self.client.get('/user/profile/delete/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            '/user/login/'
        )

    def test_get_redirected_by_change_password_page(self):
        response = self.client.get('/user/profile/password/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            '/user/login/'
        )

    def test_get_approve_comments_page(self):
        password = 'mypassword'
        my_admin = User.objects.create_superuser(
            'myuser',
            'myemail@test.com',
            password
        )

        self.client.login(username=my_admin.username, password=password)

        response = self.client.get('/user/profile/approve_comments/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/approve_comments.html')

    def test_get_delete_comments_page(self):
        password = 'mypassword'
        my_admin = User.objects.create_superuser(
            'myuser',
            'myemail@test.com',
            password
        )

        self.client.login(username=my_admin.username, password=password)

        post = Post.objects.create(
            title='Lisbon Steak',
            author=User.objects.create(),
            featured_image='',
            excerpt='A Lisbon Beef Steak',
            meal_type=2,
            dish_type=4,
            content='Some ramdom content about this dish'
        )
        item = Comment.objects.create(
            email='john@email.com',
            author=post.author,
            post=post,
            body='some random comment',
        )

        response = self.client.get(f'/user/profile/delete_comment/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/delete_comment.html')

    def test_get_view_users_page(self):
        password = 'mypassword'
        my_admin = User.objects.create_superuser(
            'myuser',
            'myemail@test.com',
            password
        )

        self.client.login(username=my_admin.username, password=password)

        response = self.client.get('/user/profile/view_users')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_accounts.html')
