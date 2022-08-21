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

![result](./documentation/tests/restaurant_testforms(menu)_results.png)

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

![result](./documentation/tests/restaurant_testforms(reservation)_results.png)

##### Models

- Tests developed for the Restaurant app models:

```python
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

![result](./documentation/tests/restaurant_testmodels_results.png)

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

![result](./documentation/tests/restaurant_testviews_results.png)

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
            'content': 'Some random content about this dish'
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

![result](./documentation/tests/blog_testforms(post)_results.png)

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

![result](./documentation/tests/blog_testforms(comment)_results.png)

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
            content='Some random content about this dish'
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
            content='Some random content about this dish'
        )

        self.assertEqual(item.featured_image, 'placeholder')

    def test_post_title_must_be_unique(self):
        item = Post.objects.create(
            title='Lisbon Steak',
            author=User.objects.create(),
            excerpt='A Lisbon Beef Steak',
            meal_type=2,
            dish_type=4,
            content='Some random content about this dish'
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
            'content': 'Some random content about this dish'
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
            content='Some random content about this dish'
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

![result](./documentation/tests/blog_testforms(post)_results.png)

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
            content='Some random content about this dish'
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
            content='Some random content about this dish'
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
            content='Some random content about this dish'
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
            content='Some random content about this dish'
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
            content='Some random content about this dish'
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
            content='Some random content about this dish'
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
            content='Some random content about this dish'
        )
        response = self.client.get(f'/blog/meal_tag/{item.dish_type}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_home.html')
```

- Tests results:

![result](./documentation/tests/blog_testviews_results.png)

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

![result](./documentation/tests/users_testforms_results.png)

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

![result](./documentation/tests/users_testmodels_results.png)

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
            content='Some random content about this dish'
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

![result](./documentation/tests/users_testviews_results.PNG)

## Validator Testing 
[PEP8 Python Validation](http://pep8online.com/)

### A Taste of Lisbon Project:

##### wsgi.py

![wsgi](./documentation/tests/pep8/atol_wsgi.png)

##### urls.py

![urls](./documentation/tests/pep8/atol_urls.png)

##### settings.py

![settings](./documentation/tests/pep8/atol_settings.png)

##### asgi.py

![asgi](./documentation/tests/pep8/atol_asgi.png)

#### Restaurant App:

##### widgets.py

![widgets](./documentation/tests/pep8/restaurant_widgets.png)

##### views.py

![views](./documentation/tests/pep8/restaurant_views.png)

##### urls.py

![urls](./documentation/tests/pep8/restaurant_urls.png)

##### models.py

![models](./documentation/tests/pep8/restaurant_models.png)

##### forms.py

![forms](./documentation/tests/pep8/restaurant_forms.png)

##### apps.py

![apps](./documentation/tests/pep8/restaurant_apps.png)

##### admin.py

![admin](./documentation/tests/pep8/restaurant_admin.png)

##### test_forms.py

![test_forms](./documentation/tests/pep8/restaurant_testforms.png)

##### test_models.py

![test_models](./documentation/tests/pep8/restaurant_testmodels.png)

##### test_views.py

![test_views](./documentation/tests/pep8/restaurant_testviews.png)

#### Blog App:

##### views.py

![views](./documentation/tests/pep8/blog_views.png)

##### urls.py

![urls](./documentation/tests/pep8/blog_urls.png)

##### models.py

![models](./documentation/tests/pep8/blog_models.png)

##### forms.py

![forms](./documentation/tests/pep8/blog_forms.png)

##### apps.py

![apps](./documentation/tests/pep8/blog_apps.png)

##### admin.py

![admin](./documentation/tests/pep8/blog_admin.png)

##### test_forms.py

![test_forms](./documentation/tests/pep8/blog_testforms.png)

##### test_models.py

![test_models](./documentation/tests/pep8/blog_models.png)

##### test_views.py

![test_views](./documentation/tests/pep8/blog_testviews.png)

#### Users App:

##### views.py

![views](./documentation/tests/pep8/users_views.png)

##### urls.py

![urls](./documentation/tests/pep8/users_urls.png)

##### signals.py

![signals](./documentation/tests/pep8/users_signals.png)

##### models.py

![models](./documentation/tests/pep8/users_models.png)

##### forms.py

![views](./documentation/tests/pep8/users_forms.png)

##### apps.py

![apps](./documentation/tests/pep8/users_apps.png)

##### admin.py

![views](./documentation/tests/pep8/users_admin.png)

##### test_forms.py

![test_forms](./documentation/tests/pep8/users_testforms.png)

##### test_models.py

![test_models](./documentation/tests/pep8/users_testmodels.png)

##### test_views.py

![test_views](./documentation/tests/pep8/users_testviews.PNG)


## [HTML Validation](https://validator.w3.org/)

### Home Page

![html](./documentation/tests/html/home_html.png)

### Menu Page

![html](./documentation/tests/html/menu_html.png)

### Blog Page

![html](./documentation/tests/html/blog_html.png)

### Blog Post Page

![html](./documentation/tests/html/blog_post_html.png)

- Errors are related to the Summernote text editor not this project's HTML code

### Reservations Page

![html](./documentation/tests/html/reservations_html.png)

### About Page

![html](./documentation/tests/html/about_html.png)

### Login Page

![html](./documentation/tests/html/login_html.png)

### Register Page

![html](./documentation/tests/html/register_html.png)

- Error is related to Django's user creation form not this project's HTML code

### User Profile Page

![html](./documentation/tests/html/user_profile_html.png)

## [CSS Validation](https://jigsaw.w3.org/css-validator/)

![CSS](./documentation/tests/css/styles_css_test.png)

## Lighthouse Score

### Mobile:

![LighthouseMobile](./documentation/tests/home_mobile.png)

### Desktop:

![LighthouseDesktop](./documentation/tests/home_mobile.png)

#### Best Practices

![LighthouseBestPractices](./documentation/tests/best_practices.png)

- Yellow score due to JQuery library and not the project's code

## User Story Tests

- ### Site user:

    - As a site user I can register an account so that I can comment and like posts

        ![userregistration](./documentation/tests/user_stories/user_registration.png)

    - As a site user I can view the menu so that I can determine if I want to eat at this restaurant

        ![menu](./documentation/tests/user_stories/menu.png)

    - As a site user I can view key information so that I know when the restaurant is open, or where it is located

        ![info](./documentation/tests/user_stories/info_1.png)
        ![info](./documentation/tests/user_stories/info_2.png)

    - As a site user I can view a paginated list of posts so that I can easily select a post to view

        ![paginatedposts](./documentation/tests/user_stories/paginated_posts.png)

    - As a site user I can make, edit and delete comments so that I have control over how I interact with the blog community

        ![crudcomments](./documentation/tests/user_stories/crud_comments.png)

    - As a site user I can like a post so that the author knows I enjoyed the content

        ![likepost](./documentation/tests/user_stories/like_post.png)

    - As a site user I can make, edit, view and delete my reservations so that I can have control over when I will eat at the restaurant

        ![crudreservations](./documentation/tests/user_stories/crud_reservations.png)

    - As a site user I can remove a like so that I can demonstrate that I am no longer interested in/agree with the post

        ![removelike](./documentation/tests/user_stories/unlike_post.png)

    - As a site user I can edit my account so that I can update any information as it changes

        ![crudprofile](./documentation/tests/user_stories/crud_profile.png)

    - As a site user I can delete my account so that I can choose to no longer be a member of the site community

        ![deleteprofile](./documentation/tests/user_stories/crud_profile.png)    

- ### Site admin:

    - As a site admin I can create, edit, view and delete posts so that I can be in total control of my sites content

        ![createpost](./documentation/tests/user_stories/create_post.png)
        ![editdeletepost](./documentation/tests/user_stories/edit_delete_post.png)

    - As a site admin I can approve comments so that I can filter out any unwanted comments

        ![approvecomments](./documentation/tests/user_stories/comment_approval.png)

    - As a site admin I can make, edit and remove comments so that I have total control over my interactions with the site community

        ![crudcomments](./documentation/tests/user_stories/crud_comments.png)

    - As a site admin I can view member accounts so that I know how many users have registered

        ![viewusers](./documentation/tests/user_stories/registered_users.png)

    - As a site admin I can view the number of reservations so that I can advise the kitchen of how customers are expected

        ![viewreservations](./documentation/tests/user_stories/admin_reservations.png)

    - As a site admin I can display key information so that users know where the restaurant is located and what's on the menu

        ![info](./documentation/tests/user_stories/info_1.png)
        ![info](./documentation/tests/user_stories/info_2.png)    

- ### Common stories:

    - As a site user|admin I can view the comments so that I can be aware of the conversation

        ![viewcomments](./documentation/tests/user_stories/admin_crud_comments.png)

    - As a site user|admin I can view likes so that I am aware of which topics are trendy

        ![likepost](./documentation/tests/user_stories/like_post.png)    

## Manual Testing

Manual testing is the process of manually testing software for defects. It requires a tester to play the role of an end user where by they use most of the application's features to ensure correct behaviour.

- User tries to register with a name already taken:

    ![registration](./documentation/tests/manual/user_already_taken.png)

- User tries to create username with invalid characters:

    ![registration](./documentation/tests/manual/invalid_username_char.png)

- User tries to register with two passwords that don't match:

    ![registration](./documentation/tests/manual/password_don't_match.png)

- User tries to register without filling in all the fields:

    ![registration](./documentation/tests/manual/blank_registration_field.png)

- User tries to login with a username that doesn't exist or is incorrect:

    ![login](./documentation/tests/manual/invalid_username.png)

- User tries to login without filling in all the fields:

    ![login](./documentation/tests/manual/blank_login_field.png)

- User tries to send a blank reservation form:

    ![reservation](./documentation/tests/manual/blank_reservation_form.png)

- User tries to send a blank comment:

    ![reservation](./documentation/tests/manual/blank_comment.png)

## Device Display Testing

### Home:

 - #### Mobile:

    ![home](./documentation/tests/devices/home_mobile.png)

- #### Tablet:

    ![home](./documentation/tests/devices/home_tablet.png)

- #### Desktop:

    ![home](./documentation/tests/devices/home_desktop.png)

### Menu:

- #### Mobile:

    ![menu](./documentation/tests/devices/menu_mobile.png)

- #### Tablet:

    ![menu](./documentation/tests/devices/menu_tablet.png)

- #### Desktop:

    ![menu](./documentation/tests/devices/menu_desktop.png)

### Blog:

- #### Mobile:

    ![blog](./documentation/tests/devices/blog_mobile.png)

- #### Tablet:

    ![blog](./documentation/tests/devices/blog_tablet.png)

- #### Desktop:

    ![blog](./documentation/tests/devices/blog_desktop.png)

### Blog Post:

- #### Mobile:

    ![blogpost](./documentation/tests/devices/blog_post_mobile.png)

- #### Tablet:

    ![blogpost](./documentation/tests/devices/blog_post_tablet.png)

- #### Desktop:

    ![blogpost](./documentation/tests/devices/blog_post_desktop.png)

### Reservations:

- #### Mobile:

    ![reservations](./documentation/tests/devices/reservations_mobile.png)

- #### Tablet:

    ![reservations](./documentation/tests/devices/reservations_tablet.png)

- #### Desktop:

    ![reservations](./documentation/tests/devices/reservations_desktop.png)

### About:

- #### Mobile:

    ![about](./documentation/tests/devices/about_mobile.png)

- #### Tablet:

    ![about](./documentation/tests/devices/about_tablet.png)

- #### Desktop:

    ![about](./documentation/tests/devices/about_desktop.png)

### Login:

- #### Mobile:

    ![login](./documentation/tests/devices/login_mobile.png)

- #### Tablet:

    ![login](./documentation/tests/devices/login_tablet.png)

- #### Desktop:

    ![login](./documentation/tests/devices/login_desktop.png)

### Register:

- #### Mobile:

    ![register](./documentation/tests/devices/register_mobile.png)

- #### Tablet:

    ![register](./documentation/tests/devices/register_tablet.png)

- #### Desktop:

    ![register](./documentation/tests/devices/register_desktop.png)

### Profile:

- #### Mobile:

    ![profile](./documentation/tests/devices/profile_mobile.png)

- #### Tablet:

    ![profile](./documentation/tests/devices/profile_tablet.png)

- #### Desktop:

    ![profile](./documentation/tests/devices/profile_desktop.png)

## Browser Compatibility Tests 

A Taste of Lisbon was tested on [Firefox](https://www.mozilla.org/en-GB/firefox/new/), [Google Chrome](https://www.google.com/intl/en_uk/chrome/) and [Brave Browser](https://brave.com/):

- ### Firefox:

    ![firefox](./documentation/tests/devices/browser_firefox.png)

- ### Google Chrome:

    ![chrome](./documentation/tests/devices/browser_chrome.png)

- ### Brave Browser:

    ![brave](./documentation/tests/devices/browser_brave.png)
