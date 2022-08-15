from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Post(models.Model):
    """
    The Post model class. Defines all the fields in the class.
    Creates a table in the database which stores each objects data.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    meal_type = models.PositiveSmallIntegerField(choices=(
        (1, 'starter'),
        (2, 'main'),
        (3, 'dessert'),
    ), null=True)
    dish_type = models.PositiveSmallIntegerField(choices=(
        (1, 'soup'),
        (2, 'salad'),
        (3, 'bread'),
        (4, 'meat'),
        (5, 'fish'),
        (6, 'seafood'),
        (7, 'sweet'),
        (8, 'tangy'),
    ), null=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        """
        The Post model Meta class. Defines how each instance is ordered.
        Also, defines the string represenation of the Post class.
        """
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def datepublished(self):
        """
        A function that retuns a string formatted representation,
        of when the Post was published.
        """
        return self.created_on.strftime('%b %d')

    def number_of_likes(self):
        """
        A function that returns the total number of likes a post has.
        """
        return self.likes.count()

class Comment(models.Model):
    """
    The Comment model class. Defines all the fields in the class.
    Creates a table in the database which stores each objects data.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments_author"
    )
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        The Comment model Meta class. Defines how each instance is ordered.
        Also, defines the string represenation of the Comment class.
        """
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
