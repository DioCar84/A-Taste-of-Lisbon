# Testing

## Django Testing (Unit Tests)

For testing Django functionality I used the built in Django TestCase class.

### A Taste of Lisbon Project:

#### Restaurant App:

##### Forms

- Tests developed for the Menu Form:

```python
class TestMenuForm(TestCase):
    """
    A class for testing the Menu form.
    """

    def test_form_data_input_is_valid(self):
        form = MenuForm(data={
            'title': 'Roast Lamb',
            'description': 'Roast Lamb',
            'dish_type': 2,
            'price': 12.99,
        })

        self.assertTrue(form.is_valid())

    def test_fields_user_has_access_to(self):
        form = MenuForm()
        self.assertEqual(
            form.Meta.fields,
            '__all__'
        )

    def test_title_field_cannot_be_empty(self):
        form = MenuForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_price_field_cannot_be_empty(self):
        form = MenuForm({'price': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0], 'This field is required.')

    def test_description_field_cannot_be_empty(self):
        form = MenuForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(
            form.errors['description'][0],
            'This field is required.'
        )

    def test_dish_type_field_cannot_be_empty(self):
        form = MenuForm({'dish_type': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('dish_type', form.errors.keys())
        self.assertEqual(
            form.errors['dish_type'][0],
            'This field is required.'
        )
```

- Tests results:

![result](./documentation/tests/Restaurant%20TestForms(Menu)%20Results.png)

- Tests developed for the Reservation Form:

```python
class TestReservationForm(TestCase):
    """
    A class for testing the Reservation form.
    """

    def test_form_data_input_is_valid(self):
        form = ReservationForm(data={
            'email': 'john@email.com',
            'table': 6,
            'number_of_clients': 4,
            'date': '08/22/2022',
            'time': 3,
        })

        self.assertTrue(form.is_valid())

    def test_fields_user_has_access_to(self):
        form = ReservationForm()
        self.assertEqual(
            form.Meta.fields,
            [
                'name',
                'email',
                'table',
                'number_of_clients',
                'date',
                'time'
            ]
        )

    def test_email_field_cannot_be_empty(self):
        form = ReservationForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_table_field_cannot_be_empty(self):
        form = ReservationForm({'table': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('table', form.errors.keys())
        self.assertEqual(form.errors['table'][0], 'This field is required.')

    def test_number_of_clients_field_cannot_be_empty(self):
        form = ReservationForm({'number_of_clients': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('number_of_clients', form.errors.keys())
        self.assertEqual(
            form.errors['number_of_clients'][0],
            'This field is required.'
        )

    def test_date_field_cannot_be_empty(self):
        form = ReservationForm({'date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors.keys())
        self.assertEqual(form.errors['date'][0], 'This field is required.')

    def test_time_field_cannot_be_empty(self):
        form = ReservationForm({'time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('time', form.errors.keys())
        self.assertEqual(form.errors['time'][0], 'This field is required.')
```

- Tests results:

![result](./documentation/tests/Restaurant%20TestForms(Reservation)%20Results.png)

##### Models

- Tests developed for the Restaurant app models:

```python
import datetime as date
from django.test import TestCase
from .models import Photo, Menu, Reservation


class TestRestaurantModels(TestCase):
    '''
    A class to test models in the Restaurant app.
    '''
    def test_reservation_item_created_now(self):
        item = Reservation.objects.create(
            email='john@email.com',
            table=6,
            number_of_clients=4,
            date='2022-08-22',
            time=3,
        )
        current_date = date.datetime.now()
        self.assertEqual(current_date.date(), item.created_on.date())

    def test_default_image_name(self):
        item = Photo.objects.create(
            title='random photo'
        )

        self.assertEqual(item.image, 'yleipz1gqfmdwpnbtx0v.jpg')

    def test_menu_item_created_now(self):
        item = Menu.objects.create(
            title='Roast Lamb',
            description='Roast Lamb',
            dish_type=2,
            price=12.99,
        )
        current_date = date.datetime.now()
        self.assertEqual(current_date.date(), item.created_on.date())

```

- Tests results:

![result](./documentation/tests/Restaurant%20TestModels%20Results.png)

##### Views

- Tests developed for the Restaurant app views:

```python
class TestRestaurantViews(TestCase):
    """
    A class for testing the Restaurant app views.
    """
    def test_get_home_page(self):
        hero_image = Photo.objects.create(title='Lisbon Tram')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant/home.html')

    def test_get_menu_page(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant/menu.html')

    def test_get_create_menu_item_page(self):
        item = Menu.objects.create(
            title='Roast Lamb',
            description='Roast Lamb',
            dish_type=2,
            price=12.99,
        )
        response = self.client.get('/create_menu/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant/menu_form.html')

    def test_get_edit_menu_item_page(self):
        item = Menu.objects.create(
            title='Roast Lamb',
            description='Roast Lamb',
            dish_type=2,
            price=12.99,
        )
        response = self.client.get(f'/edit_menu/{item.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant/menu_form.html')

    def test_get_delete_menu_item_page(self):
        item = Menu.objects.create(
            title='Roast Lamb',
            description='Roast Lamb',
            dish_type=2,
            price=12.99,
        )
        response = self.client.get(f'/delete_menu/{item.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant/delete_item.html')

    def test_get_reservations_page(self):
        open_image = Photo.objects.create(title='Open Times')
        open_banner = Photo.objects.create(title='Open Times Banner')
        response = self.client.get('/reservations/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant/reservations.html')

    def test_get_redirected_by_user_reservations_page(self):
        response = self.client.get('/reservations/user/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/user/login/?next=/reservations/user/')

    def test_get_redirected_by_edit_user_reservations_page(self):
        item = Reservation.objects.create(
            email='john@email.com',
            table=6,
            number_of_clients=4,
            date='2022-08-22',
            time=3,
        )
        response = self.client.get(f'/reservations/user/{item.id}')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            f'/user/login/?next=/reservations/user/{item.id}'
        )

    def test_get_redirected_by_delete_user_reservations_page(self):
        item = Reservation.objects.create(
            email='john@email.com',
            table=6,
            number_of_clients=4,
            date='2022-08-22',
            time=3,
        )
        response = self.client.get(f'/reservations/user/{item.id}/delete')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            f'/user/login/?next=/reservations/user/{item.id}/delete'
        )

    def test_get_about_page(self):
        map_image = Photo.objects.create(title='Map of London')
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant/about.html')
```

- Tests results:

![result](./documentation/tests/Restaurant%20TestViews%20Results.png)

#### Blog App:

##### Forms

- Tests developed for the Post Form:

```python
class TestPostForm(TestCase):
    """
    A class for testing the Post form.
    """

    def test_form_data_input_is_valid(self):
        form = PostForm(data={
            'title': 'Lisbon Steak',
            'featured_image': '',
            'excerpt': 'A Lisbon Beef Steak',
            'meal_type': 2,
            'dish_type': 4,
            'content': 'Some ramdom content about this dish'
        })

        self.assertTrue(form.is_valid())

    def test_fields_user_has_access_to(self):
        form = PostForm()
        self.assertEqual(
            form.Meta.fields,
            (
                'title',
                'featured_image',
                'excerpt',
                'meal_type',
                'dish_type',
                'content'
            )
        )

    def test_title_field_cannot_be_empty(self):
        form = PostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_content_field_cannot_be_empty(self):
        form = PostForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_meal_type_field_cannot_be_empty(self):
        form = PostForm({'meal_type': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('meal_type', form.errors.keys())
        self.assertEqual(
            form.errors['meal_type'][0],
            'This field is required.'
        )

    def test_dish_type_field_cannot_be_empty(self):
        form = PostForm({'dish_type': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('dish_type', form.errors.keys())
        self.assertEqual(
            form.errors['dish_type'][0],
            'This field is required.'
        )
```

- Tests results:

![result](./documentation/tests/Blog%20TestForms(Post)%20Results.png)

- Tests developed for the Comment Form:

```python
class TestCommentForm(TestCase):
    """
    A class for testing the Comment form.
    """

    def test_form_data_input_is_valid(self):
        form = CommentForm(data={
            'email': 'john@email.com',
            'body': 'some random comment',
        })

        self.assertTrue(form.is_valid())

    def test_fields_user_has_access_to(self):
        form = CommentForm()
        self.assertEqual(
            form.Meta.fields,
            ('body', )
        )

    def test_body_field_cannot_be_empty(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')
```

- Tests results:

![result](./documentation/tests/Blog%20TestForms(Comment)%20Results.png)

##### Models

- Tests developed for the Blog app models:

```python
class TestBlogModels(TestCase):
    '''
    A class to test models in the Blog app.
    '''
    def test_post_item_created_now(self):
        item = Post.objects.create(
            title='Lisbon Steak',
            author=User.objects.create(),
            excerpt='A Lisbon Beef Steak',
            meal_type=2,
            dish_type=4,
            content='Some ramdom content about this dish'
        )
        current_date = date.datetime.now()
        self.assertEqual(current_date.date(), item.created_on.date())

    def test_default_featured_image_name(self):
        item = Post.objects.create(
            title='Lisbon Steak',
            author=User.objects.create(),
            excerpt='A Lisbon Beef Steak',
            meal_type=2,
            dish_type=4,
            content='Some ramdom content about this dish'
        )

        self.assertEqual(item.featured_image, 'placeholder')

    def test_post_title_must_be_unique(self):
        item = Post.objects.create(
            title='Lisbon Steak',
            author=User.objects.create(),
            excerpt='A Lisbon Beef Steak',
            meal_type=2,
            dish_type=4,
            content='Some ramdom content about this dish'
        )

        password = 'mypassword'
        my_admin = User.objects.create_superuser(
            'myuser',
            'myemail@test.com',
            password
        )

        form = PostForm(data={
            'title': 'Lisbon Steak',
            'author': my_admin.username,
            'excerpt': 'A Lisbon Beef Steak',
            'meal_type': 2,
            'dish_type': 4,
            'content': 'Some ramdom content about this dish'
        })

        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(
            form.errors['title'][0],
            'Post with this Title already exists.'
        )

    def test_comment_item_created_now(self):
        post = Post.objects.create(
            title='Lisbon Steak',
            author=User.objects.create(),
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
        current_date = date.datetime.now()
        self.assertEqual(current_date.date(), item.created_on.date())
```

- Tests results:

![result](./documentation/tests/Blog%20TestModels%20Results.png)

##### Views

- Tests developed for the Blog app views:

```python
class TestBlogViews(TestCase):
    """
    A class for testing the Blog app views.
    """
    def test_get_blog_page(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_home.html')

    def test_get_blog_post_page(self):
        item = Post.objects.create(
            title='Lisbon Steak',
            author=User.objects.create(),
            featured_image='',
            excerpt='A Lisbon Beef Steak',
            meal_type=2,
            dish_type=4,
            content='Some ramdom content about this dish'
        )
        response = self.client.get(f'/blog/{item.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_post.html')

    def test_get_edit_blog_post_page(self):
        item = Post.objects.create(
            title='Lisbon Steak',
            author=User.objects.create(),
            featured_image='',
            excerpt='A Lisbon Beef Steak',
            meal_type=2,
            dish_type=4,
            content='Some ramdom content about this dish'
        )
        response = self.client.get(f'/blog/edit_post/{item.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/edit_post.html')

    def test_get_delete_blog_post_page(self):
        item = Post.objects.create(
            title='Lisbon Steak',
            author=User.objects.create(),
            featured_image='',
            excerpt='A Lisbon Beef Steak',
            meal_type=2,
            dish_type=4,
            content='Some ramdom content about this dish'
        )
        response = self.client.get(f'/blog/delete_post/{item.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/delete_post.html')

    def test_get_edit_blog_comment_page(self):
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
        response = self.client.get(f'/blog/edit_comment/{item.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/edit_comment.html')

    def test_get_delete_blog_comment_page(self):
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
        response = self.client.get(f'/blog/delete_comment/{item.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/delete_comment.html')

    def test_get_blog_meal_tag_page(self):
        item = Post.objects.create(
            title='Lisbon Steak',
            author=User.objects.create(),
            featured_image='',
            excerpt='A Lisbon Beef Steak',
            meal_type=2,
            dish_type=4,
            content='Some ramdom content about this dish'
        )
        response = self.client.get(f'/blog/meal_tag/{item.meal_type}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_home.html')

    def test_get_blog_dish_tag_page(self):
        item = Post.objects.create(
            title='Lisbon Steak',
            author=User.objects.create(),
            featured_image='',
            excerpt='A Lisbon Beef Steak',
            meal_type=2,
            dish_type=4,
            content='Some ramdom content about this dish'
        )
        response = self.client.get(f'/blog/meal_tag/{item.dish_type}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_home.html')
```

- Tests results:

![result](./documentation/tests/Blog%20TestViews%20Results.png)

#### Users App:

##### Forms

- Tests developed for the User Profile Form:

```python
class TestUserProfileForm(TestCase):
    """
    A class for testing the user profile form.
    """

    def test_form_data_input_is_valid(self):
        form = UserProfileForm(data={
            'name': 'John',
            'username': 'John123',
            'email': 'john@email.com'
        })

        self.assertTrue(form.is_valid())

    def test_fields_user_has_access_to(self):
        form = UserProfileForm()
        self.assertEqual(
            form.Meta.fields,
            ['username', 'name', 'email', 'profile_image']
        )

    def test_user_can_be_blank(self):
        form = UserProfileForm({'user': ''})
        self.assertTrue(form.is_valid())

    def test_username_can_be_blank(self):
        form = UserProfileForm({'username': ''})
        self.assertTrue(form.is_valid())

    def test_email_can_be_blank(self):
        form = UserProfileForm({'email': ''})
        self.assertTrue(form.is_valid())
```

- Tests results:

![result](./documentation/tests/Users%20TestForms%20Results.png)

##### Models

- Tests developed for the Users app models:

```python
class TestUsersModels(TestCase):
    '''
    A class to test models in the Users app.
    '''
    def test_user_profile_created_now(self):
        item = UserProfile.objects.create()
        current_date = date.datetime.now()
        self.assertEqual(current_date.date(), item.created_on.date())

    def test_default_profile_image_name(self):
        item = UserProfile.objects.create()
        self.assertEqual(item.profile_image, 'muoktj5dbjhygxwuu0v3.png')
```

- Tests results:

![result](./documentation/tests/Users%20TestModels%20Results.png)

##### Views

- Tests developed for the Users app views:

```python
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
```

- Tests results:

![result](./documentation/tests/Users%20TestViews%20Results.PNG)

## Validator Testing 
[PEP8 Python Validation](http://pep8online.com/)

### A Taste of Lisbon Project:

##### wsgi.py

![wsgi](./documentation/tests/ATOL%20Wsgi.png)

##### urls.py

![urls](./documentation/tests/ATOL%20Urls.png)

##### settings.py

![settings](./documentation/tests/ATOL%20Settings.png)

##### asgi.py

![asgi](./documentation/tests/ATOL%20Asgi.png)

#### Restaurant App:

##### widgets.py

![widgets](./documentation/tests/Restaurant%20Widgets.png)

##### views.py

![views](./documentation/tests/Restaurant%20Views.png)

##### urls.py

![urls](./documentation/tests/Restaurant%20Urls.png)

##### models.py

![models](./documentation/tests/Restaurant%20Models.png)

##### forms.py

![forms](./documentation/tests/Restaurant%20Forms.png)

##### apps.py

![apps](./documentation/tests/Restaurant%20Apps.png)

##### admin.py

![admin](./documentation/tests/Restaurant%20Admin.png)

##### test_forms.py

![test_forms](./documentation/tests/Restaurant%20TestForms.png)

##### test_models.py

![test_models](./documentation/tests/Restaurant%20TestModels.png)

##### test_views.py

![test_views](./documentation/tests/Restaurant%20TestViews.png)

#### Blog App:

##### views.py

![views](./documentation/tests/Blog%20Views.png)

##### urls.py

![urls](./documentation/tests/Blog%20Urls.png)

##### models.py

![models](./documentation/tests/Blog%20Models.png)

##### forms.py

![forms](./documentation/tests/Blog%20Forms.png)

##### apps.py

![apps](./documentation/tests/Blog%20Apps.png)

##### admin.py

![admin](./documentation/tests/Blog%20Admin.png)

##### test_forms.py

![test_forms](./documentation/tests/Blog%20TestForms.png)

##### test_models.py

![test_models](./documentation/tests/Blog%20TestModels.png)

##### test_views.py

![test_views](./documentation/tests/Blog%20TestViews.png)

#### Users App:

##### views.py

![views](./documentation/tests/Users%20Views.png)

##### urls.py

![urls](./documentation/tests/Users%20Urls.png)

##### signals.py

![signals](./documentation/tests/Users%20Signals.png)

##### models.py

![models](./documentation/tests/Users%20Views.png)

##### forms.py

![views](./documentation/tests/Users%20Models.png)

##### apps.py

![apps](./documentation/tests/Users%20Apps.png)

##### admin.py

![views](./documentation/tests/Users%20Admin.png)

##### test_forms.py

![test_forms](./documentation/tests/Users%20TestForms.png)

##### test_models.py

![test_models](./documentation/tests/Users%20TestModels.png)

##### test_views.py

![test_views](./documentation/tests/Users%20TestViews.PNG)



## [HTML Validation](https://validator.w3.org/)

### Home Page

![html](./documentation/tests/Home%20HTML.png)

### Menu Page

![html](./documentation/tests/Menu%20HTML.png)

### Blog Page

![html](./documentation/tests/Blog%20HTML.png)

### Blog Post Page

![html](./documentation/tests/Blog%20Post%20HTML.png)

- Errors are related to the Summernote text editor not this project's HTML code

### Reservations Page

![html](./documentation/tests/Reservations%20HTML.png)

### About Page

![html](./documentation/tests/About%20HTML.png)

### Login Page

![html](./documentation/tests/Login%20HTML.png)

### Register Page

![html](./documentation/tests/Register%20HTML.png)

- Error is related to Django's user creation form not this project's HTML code

### User Profile Page

![html](./documentation/tests/User%20Profile%20HTML.png)

## [CSS Validation](https://jigsaw.w3.org/css-validator/)

![CSS](./documentation/tests/styles%20css%20test.png)

## Lighthouse Score

### Mobile:

![LighthouseMobile](./documentation/tests/Home%20Mobile.png)

### Desktop:

![LighthouseDesktop](./documentation/tests/Home%20Desktop.png)

#### Best Practices

![LighthouseBestPractices](./documentation/tests/Best%20Practices.png)

- Yellow score due to JQuery library and not the project's code

## User Story Tests

### Site user:

    - As a site user I can register an account so that I can comment and like posts

![userregistration](./documentation/tests/user%20stories/User%20Registration.png)

    - As a site user I can view the menu so that I can determine if I want to eat at this restaurant

![menu](./documentation/tests/user%20stories/Menu.png)

    - As a site user I can view key information so that I know when the restaurant is open, or where it is located

![info](./documentation/tests/user%20stories/Info%201.png)
![info](./documentation/tests/user%20stories/Info%202.png)

    - As a site user I can view a paginated list of posts so that I can easily select a post to view

![paginatedposts](./documentation/tests/user%20stories/Paginated%20Posts.png)

    - As a site user I can make, edit and delete comments so that I have control over how I interact with the blog community

![crudcomments](./documentation/tests/user%20stories/CRUD%20Comments.png)

    - As a site user I can like a post so that the author knows I enjoyed the content

![likepost](./documentation/tests/user%20stories/Like%20Post.png)

    - As a site user I can make, edit, view and delete my reservations so that I can have control over when I will eat at the restaurant

![crudreservations](./documentation/tests/user%20stories/CRUD%20Reservations.png)

    - As a site user I can remove a like so that I can demonstrate that I am no longer interested in/agree with the post

![removelike](./documentation/tests/user%20stories/Unlike%20Post.png)

    - As a site user I can edit my account so that I can update any information as it changes

![crudprofile](./documentation/tests/user%20stories/CRUD%20Profile.png)

    - As a site user I can delete my account so that I can choose to no longer be a member of the site community

![deleteprofile](./documentation/tests/user%20stories/CRUD%20Profile.png)    

  ### Site admin:

    - As a site admin I can create, edit, view and delete posts so that I can be in total control of my sites content

![createpost](./documentation/tests/user%20stories/Create%20Post.png)
![editdeletepost](./documentation/tests/user%20stories/Edit%20Delete%20Post.png)

    - As a site admin I can approve comments so that I can filter out any unwanted comments

![approvecomments](./documentation/tests/user%20stories/Comment%20Approval.png)

    - As a site admin I can make, edit and remove comments so that I have total control over my interactions with the site community

![crudcomments](./documentation/tests/user%20stories/Admin%20CRUD%20Comments.png)

    - As a site admin I can view member accounts so that I know how many users have registered

![viewusers](./documentation/tests/user%20stories/Registered%20Users.png)

    - As a site admin I can view the number of reservations so that I can advise the kitchen of how customers are expected

![viewreservations](./documentation/tests/user%20stories/Admin%20Reservations.png)

    - As a site admin I can display key information so that users know where the restaurant is located and what's on the menu

![info](./documentation/tests/user%20stories/Info%201.png)
![info](./documentation/tests/user%20stories/Info%202.png)    

  ### Common stories:

    - As a site user|admin I can view the comments so that I can be aware of the conversation

![viewcomments](./documentation/tests/user%20stories/Admin%20CRUD%20Comments.png)

    - As a site user|admin I can view likes so that I am aware of which topics are trendy

![likepost](./documentation/tests/user%20stories/Like%20Post.png)    

## Manual Testing

Manual testing is the process of manually testing software for defects. It requires a tester to play the role of an end user where by they use most of the application's features to ensure correct behaviour.

- As I am using django-allauth, it handles the login / create an account functionality ensuring users only enter the correct infomration before they can progress. It ensures duplicate users cannot be created, passwords are not too similar / short as well as all information is validated before users can submit.

    ![allauth](docs/readme/manualtestlogin.png)

- When users try ADD a coin to a portfolio, the application will ensure the ticker they enter is valid. If it does not exist within the CoinMarketCap API then a Bootstrap message will display telling them that the ticker they entered does not exist. Furthermore, when submitting the inital form, all tickers must be entered in uppercase. If the user does not do this, it would cause the API call to fail, so I made sure that all valid tickers entered are transformed to uppercase before the next form can be submit.

    ![addcoin](docs/readme/addcointest.png)

- When trying to SELL a coin, user's should not be able to sell more than they hold. As a result I have put in code which checks if the quantity they are trying to sell is less or equal to the quantity they hold. If this check fails, then a Bootstrap message will appear letting the user know, and the form will not submit.

    ![sell](docs/readme/sellmanualtest.png)

- If a user tries to ADD a coin which they already hold in their portfolio, instead of creating a new instance of that coin, the updated quantity and price bought at should be appended to the existing assets fields. This is because you should not have mulitple instances of the same coin within a single portfolio.

    ![duplicatetest](docs/readme/duplicatetest.png)

- A user is unable to name a portfolio anything greater than nine characters, this is because on mobile, due to the portfolio information being stored on a ```<table>```, if the name is greater than nine chars it will cause an overflow error. As a result, in the model, I defined max_length = 9.

    ![9](docs/readme/manualtestcreate.png)

## Responsiveness Testing

### Homepage:

### 320px & 375px:

![homepage](docs/readme/hp320px.png)

### 425px:

![homepage](docs/readme/hp425px.png)

### 768px:

![homepage](docs/readme/hp768px.png)

### 1024px:

![homepage](docs/readme/hp1024px.png)

### 1440px:

![homepage](docs/readme/hp1440px.png)

### Login, Create Account & Logout:

### 320px & 375px:

![LILO](docs/readme/lilo320px.png)

### 425px:

![LILO](docs/readme/lilo425px.png)

### 768px, 1204px & 1440px:

![LILO](docs/readme/lilo768px.png)

### View Portfolio:

### 320px & 375px:

![vp](docs/readme/vp320px.png)

### 425px:

![vp](docs/readme/vp425px.png)

### 768px:

![vp](docs/readme/vp768px.png)

### 1024px & 1440px:

![vp](docs/readme/vp1024px.png)

### Create Portfolio:

### 320px, 375px, 425px:

![cp](docs/readme/cp320px.png)

### 768px:

![cp](docs/readme/cp768px.png)

### 1024px & 1440px:

![cp](docs/readme/cp1024px.png)

### Manage Portfolio Modal:

### 320px & 375px:

![mp](docs/readme/mp320px.png)

### 425px:

![mp](docs/readme/mp425px.png)

### 768px:

![mp](docs/readme/mp768px.png)

### 1024px & 1440px:

![mp](docs/readme/mp1024px.png)

### View Assets:

### 320px & 375px:

![va](docs/readme/va320px.png)

### 425px:

![va](docs/readme/va425px.png)

### 768px:

![va](docs/readme/va768px.png)

### 1024px & 1440px:

![va](docs/readme/va1024px.png)

### Add Coin Form:

### 320px & 375px:

![ac](docs/readme/ac320px.png)

### 425px:

![ac](docs/readme/ac425px.png)

### 768px and above:

![ac](docs/readme/ac768px.png)

## Browser Compatibility Tests 

I will test Cryptics on [Firefox](https://www.mozilla.org/en-GB/firefox/new/), [Microsoft Edge](https://www.microsoft.com/en-us/edge) and [Brave Browser](https://brave.com/):

### Firefox:

![firefox](docs/readme/firefox.png)

### Microsoft Edge:

![edge](docs/readme/microsoftedge.png)

### Brave Browser:

![Brave](docs/readme/bravebrowser.png)

## GitHub Issues

When developing the project, I used GitHub Issues as a way to track my work on GitHub, and make notes of any bugs or features that I needed to fix/implement.

- [Here](https://github.com/RiyadhKh4n/cryptics/issues?q=is%3Aopen+is%3Aissue) you can find a list of open issues, which are made up of various User Stories or Dvelopment tasks that needed completing.

- [Here](https://github.com/RiyadhKh4n/cryptics/issues?q=is%3Aissue+is%3Aclosed) you can find a list of all closed issues, which show any bugs I resolved.

## Bugs

- Not so much a bug but the API I am using only allows 333 calls per day as I am using the free version. Each time the user Adds or Buys a coin, as well as each time the [portfolio.html](portfolio/templates/portfolio/portfolio.html) template is rendered, 10 credits (calls) are used which means the program can be called 33 times a day before going over the limit. The limit is a soft limit meaning it does let you go over the 333 per day however after 10,000 calls (per month) the API will stop allowing calls meaning the program would not work if the limit is reached.

    ![apikey](docs/readme/apikeytest.png)

- A bug that is out of my control is if the CoinMarketCap data has been hacked or corrupted. This was not something I thought I had to worry about however on (14/12/21) the website got hacked causing all the coin data to be incorrect, meaning if the data my program produces will also be incorrect.

- If a user adds a coin whose price is very small e.g. SHIB (£0.00001852), the program will add the coin as price £0. This is because I round the price displayed to 3 decimal places in order to reduce how many decimal places display on the front-end making the site look cleaner. However, this will cause all other fields which depend on price (current_holdings, average_price, pnl) to also equal £0 as anything multiplied by zero equals zero. As a result, the asset will not display the correct data on the table in [assets.html](portfolio/templates/portfolio/assets.html)