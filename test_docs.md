# Testing

## Django Testing (Unit Tests)

For testing Django functionality I used the built in Django TestCase class.

### A Taste of Lisbon Project:

### Restaurant App:

#### Forms

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

![result](docs/readme/formtestres.png)

#### Models

#### Views

### Blog App:

#### Forms

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

![result](docs/readme/formtestres.png)

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

![result](docs/readme/formtestres.png)

#### Models

#### Views

### Users App:

#### Forms

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

![result](docs/readme/formtestres.png)

#### Models

#### Views

## Validator Testing 
[PEP8 Python Validation](http://pep8online.com/)

### A Taste of Lisbon Project:

#### wsgi.py

![wsgi](./documentation/tests/ATOL%20Wsgi.png)

#### urls.py

![urls](./documentation/tests/ATOL%20Urls.png)

#### settings.py

![settings](./documentation/tests/ATOL%20Settings.png)

#### asgi.py

![asgi](./documentation/tests/ATOL%20Asgi.png)

### Restaurant App:

#### widgets.py

![widgets](./documentation/tests/Restaurant%20Widgets.png)

#### views.py

![views](./documentation/tests/Restaurant%20Views.png)

#### urls.py

![urls](./documentation/tests/Restaurant%20Urls.png)

#### models.py

![models](./documentation/tests/Restaurant%20Models.png)

#### forms.py

![forms](./documentation/tests/Restaurant%20Forms.png)

#### apps.py

![apps](./documentation/tests/Restaurant%20Apps.png)

#### admin.py

![admin](./documentation/tests/Restaurant%20Admin.png)

### Blog App:

#### views.py

![views](./documentation/tests/Blog%20Views.png)

#### urls.py

![urls](./documentation/tests/Blog%20Urls.png)

#### models.py

![models](./documentation/tests/Blog%20Models.png)

#### forms.py

![forms](./documentation/tests/Blog%20Forms.png)

#### apps.py

![apps](./documentation/tests/Blog%20Apps.png)

#### admin.py

![admin](./documentation/tests/Blog%20Admin.png)

### Users App:

#### views.py

![views](./documentation/tests/Users%20Views.png)

#### urls.py

![urls](./documentation/tests/Users%20Urls.png)

#### signlas.py

![signals](./documentation/tests/Users%20Signals.png)

#### models.py

![models](./documentation/tests/Users%20Views.png)

#### forms.py

![views](./documentation/tests/Users%20Models.png)

#### apps.py

![apps](./documentation/tests/Users%20Apps.png)

#### admin.py

![views](./documentation/tests/Users%20Admin.png)

### Django Test Files

#### test_forms.py

![test_forms](docs/readme/testviewspep8.png)

#### test_urls.py

![test_urls](docs/readme/testurlspep8.png)

#### test_views.py

![test_views](docs/readme/testviewspypep8.png)

### Settings.py

![settings](docs/readme/pep8settings.png)

## [HTML Validation](https://validator.w3.org/)

![html](docs/readme/w3chtml.png)

## [CSS Validation](https://jigsaw.w3.org/css-validator/)

The errors which can be seen on the screen shot below are coming from Front-Awesome, not my project, so can be ignored.

![CSS](docs/readme/w3ccss.png)

## Lighthouse Score

### Mobile:

![LighthouseMobile](docs/readme/lighthousemobile.png)

### Desktop:

![LighthouseDesktop](docs/readme/lighthousedesktop.png)

## User Story Tests

1. As a **Site User** I will be **directed to the Home Page** so that **I can understand the website**

    When the user loads the site, they are taken to this page which is the homepage. Here they are able to get an understanding of what Cryptics is and the aim of the website, they are also prompted to Create an Account, which allows them to use the Portfolio Tracking features. 

    ![homepage](docs/readme/hp768px.png)

2. As a **Site User** I can **create an account** so that **I can create a portfolio**

    Once the user has created an account, they are able to create and view their portfolios, as well as add assets to them.

    ![create](docs/readme/cp768px.png)

3. As a **Site User** I can **log in to my account** so that **I can view my portfolios**

    Once an account has been created, users are able to login to their account on any device and view their portfolios as well as individual assets

    ![view](docs/readme/lilo768px.png)

4. As a **Site User** I can **create a Portfolio** so that **I can track my crypto holdings**

    Cryptics provides full portfolio tracking functionality, meaning once a portfolio has been created, they are then able to add assets to them, allowing them to track their crypto holdings.

    ![track](docs/readme/va768px.png)


5. As a **Site User** I can **view all Portfolios** so that **I can see the total valuation**

    As well as being able to view individual assets within a portfolio, Cryptics also allows user to view all portfolios and see the total USD valuation of them.

    ![usdvalue](docs/readme/ustest.png)

6. As a **Site User** I can **delete my Portfolio** so that **I can remove my portfolio**

    Cryptics has full CRUD functionality meaning users have full control over the creation, reading, updating and deletion of their portfolios and assets.

    ![delete](docs/readme/mp768px.png)

7. As a **Site User** I can **search for a token** so that **I can add it to my portfolio**

    Cryptics harnesses the power of the CoinMarketCap API allowing users to search for and add over 2000 cryptocurrencies to their portfolios with live price data.

    ![search](docs/readme/ac425px.png)


8. As a **Site User** I can **Sell a token** so that **I can remove it from portfolio**

    Users have the ability to Buy and Sell thousands of coins and track their holdings all in one platform.

    ![buy/sell](docs/readme/buyselluserstory.png)

9. As a **Site User** I can **Buy a token** so that **I can add to my portfolio**

    Users have the ability to Buy and Sell thousands of coins and track their holdings all in one platform.

    ![buy/sell](docs/readme/buyselluserstory.png)

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