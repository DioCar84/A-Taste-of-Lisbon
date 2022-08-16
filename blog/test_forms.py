from django.test import TestCase
from .forms import PostForm, CommentForm


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
