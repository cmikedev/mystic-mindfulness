# Mystic Mindfulness

## 1. Introduction

Mystic Mindfulness is a fictional ecommerce site offering for sale healing crystals. The premise of the site is to not only appeal to customers already specifically interested in healing crystals but, also potential customers who subscribe to the umbrella 'wellness' lifestyle which, through various marketing strategies discussed below, can be pursuaded to incorporate crystals into their various practices and become paying customers.

### 1.1 Deployed Website
A link to the deployed project via the Heroku app can be found [here](https://mystic-mindfulness.herokuapp.com/).


### 1.2 Repository
The GitHub repository can be found [here](https://github.com/cmikedev/mystic-mindfulness).

____
</br>

## 2. Business Case

Mystic Mindfulness is a business-to-customer (B2C) ecommerce website selling healing crystals directly to online consumers. The site specializes in the main three types of healing crystals; Amethyst, Calcite and Quartz.
</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/amiresponsive-light.png?raw=true)</br>
</br>

Image created using [Am I Responsive?](https://ui.dev/amiresponsive)
</br></br>

### 2.1 Marketing Strategy

Social media

#### Search Engines

#### Facebook Business Page

The Facebook page can be found [here](https://www.facebook.com/profile.php?id=100092204265600). Please note that Facebook does not allow business pages to remain in perpetuity and the aforementioned link may be made inactive at any time. Should that occur at time of reading, the below screenshots have been provided to illustrate the active Mystic Mindfulness Facebook business page.
</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/facebook-top.png?raw=true)</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/facebook-bottom.png?raw=true)</br>
</br>

#### The Blog

The Mystic Mindfulness website contains a blog with posts written by the site admin. The purpose of the blog is twofold. Firstly, to provide education and guidance to any visitors who may be unsure of what crystals to purchase. By providing such a visitor with guidance they will be more sure of their needs and more likely to make a purchase. Secondly, by extolling the benefits of the crystals within the post topic, the blog itself becomes a marketing tool to drive up sales from visitors.

____
</br>

## 3. Planning

The goal of the Mystic Mindfulness ecommerce site is to provide the potential customer with a clear, intuitive interface which allows them to immediately understand the services being offered, navigate easily through the various pages, sign-up for a newsletter, interact via comments and reviews and ultimately make a purchase. To achieve this, Agile methodology was used within the planning and design process. Github's Kanban board was implemented to design and track user stories which were vital in developing a user-focused experience:

1. As a Site User I can register an account so that I can add items to my cart
2. As a Site User I can view a list of products for sale so that I can select one to view
3. As a Site User I can open up a product page so that I can view more details
4. As a Site User I can leave a review of a product so that other users can decide whether to buy or not
5. As a Site User I can select an item to add to my shopping cart so that I can purchase the product now or later
6. As a Site User I can use the integrated Strype button so that I can purchase products
7. As a Superuser I can add a product to the main product page so that the inventory is kept up to date
8. As a Superuser I can edit a product so that I can correct any errors or make changes to the details
9. As a Superuser I can delete a product so that I can keep the inventory up to date
10. As a Site User I can sign up to a newsletter so that I can receive correspondence from the site
11. As a Superuser I can create a blog post so that site users can learn more about the products and their uses
12. As a Superuser I can edit or delete a post so that I can correct any errors or remove a post entirely
13. As a Site User I can view blog entries relating so that I can learn more about the products on the site

The completed Kanban Board can be found [here](https://github.com/users/cmikedev/projects/9).

____
</br>



## 4. Design

Font-Family used was Bilbo. LOTR is a recognisable cultural reference and reinforces the mystical/fantastical element of the site. The expectation is that the font will create that connection in users head.

Design - background to be somewhat ethereal/cosmic. 

Large use of white colours to denote health, emptiness, clean-living. No clutter.


____
</br>



## 5. Testing

This section focuses on testing the website from the point of view of the user in line with the user stories utilised in this project's Kanban. The testing is spread across three areas, with authentication testing taking place as part of them:

- 5.1 User Story Testing
- 5.2 Admin / Superuser CRUD Capability Testing
- 5.3 Code and Responsiveness Testing
</br>

### 5.1 User Story Testing

___

User Story:

As a Site User I can sign up to a newsletter so that I can receive correspondence from the site.
* Acceptance Criteria:
    * Unauthenticated user can sign-up to a newsletter
    * Sign-up is not displayed for logged-in users
___

</br>
If an unauthenticated site-visitor navigates to the page footer, they will be presented with a form to sign-up to the Mystic Mindfulness newsletter. Note that the visitor's login status is shown as "Guest".</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/newsletter-test-1.png?raw=true)</br>
</br>

Clicking "subscribe" will add the users email to the "SubscribedUsers" model. 
</br></br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/newsletter-test-2.png?raw=true)</br>
</br>

The form will not appear for users who are already logged in. 
</br></br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/newsletter-test-8.png?raw=true)</br>
</br>

A visitor who either doesn't have an account or has but has yet to sign-in but has already subscribed to the newsletter will not be able to subscribe again as their email will already be in the "SubscribedUsers" model.

Subscribing does not create an account for the user (and no cookie is created) so the newsletter subscription form will still appear but the user will not be able to re-subscribe using the same details. 
</br></br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/newsletter-test-3.png?raw=true)</br>
</br>

Switching to the site admin account, the login status changes from "Guest" to "admin" and the administrator is able to access a drop-down menu which with a link to create the newsletter.
</br></br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/newsletter-test-4.png?raw=true)</br>
</br>

An unregistered site visitor or a registered and signed-in user without the correct permissions is not shown these options nor can they access the newsletter creation page even if they know the link at [https://mystic-mindfulness.herokuapp.com/newsletter](https://mystic-mindfulness.herokuapp.com/newsletter).

</br></br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/newsletter-test-9.png?raw=true)</br>
</br>

On the newsletter creation page, the "Receivers" field, which is editable, comes pre-populated with all visitors who subscribed to the newsletter. Once the administrator has drafted the letter and clicks send, it will automatically go to all emails in the "Receivers" field.
</br></br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/newsletter-test-5.png?raw=true)</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/newsletter-test-6.png?raw=true)</br>
</br>

Finally, we can see that the test newsletter has arrived in our test user's inbox.
</br></br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/newsletter-test-7.png?raw=true)</br>
</br>

___

User Story:

As a Site User I can register an account so that I can add items to my cart.
* Acceptance Criteria:
    * User can register an account
    * User can login
    * User is made aware of their login status
    * User can logout
    * User is made aware of their logout status
___

</br>
When a user clicks on the profile icon a drop-down will be activated which gives the user the option to login or register an account.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/registration-test-1.png?raw=true)</br>
</br>

The user needs to fill in their details and select Sign Up</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/registration-test-2.png?raw=true)</br>
</br>

If the user already exists or if a required field has not been filled out, the form will not be submitted and the user will be notified of the problem.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/registration-test-11.png?raw=true)</br>
</br>

Once their details have been entered correctly and the form submitted, the user will be informed that an email requiring confirmation has been sent to the email address that they provided.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/registration-test-3.png?raw=true)</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/registration-test-4.png?raw=true)</br>
</br>

When the user clicks on the confirmation link in their email, they will be redirected back to the Mystic Mindfulness website and asked the confirm their details.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/registration-test-5.png?raw=true)</br>
</br>

Once confirmed, the user will be notified that their confirmation has been accepted and they will be invited to log into their newly created account. Once logged in, the user will be notified of their login status.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/registration-test-6.png?raw=true)</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/registration-test-7.png?raw=true)</br>
</br>

To logout, the user simply needs to click on the profile icon and select "Logout" from the drop-down menu.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/registration-test-8.png?raw=true)</br>
</br>

The user will be asked to confirm that they wish to logout.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/registration-test-9.png?raw=true)</br>
</br>

Again, the user will be made aware of their login status.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/registration-test-10.png?raw=true)</br>
</br>

___

User Story:

As a Site User I can view a list of products for sale so that I can select one to view.
* Acceptance Criteria:
    * User can view and browse all available products
    * User can select a product and view further details
___

</br>
Regardless of their login status, a visitor has several pathways to the product page from the home page. Shown below, the user has selected "All Products" from the header menu which allows them to view all products sorted by price, category or alphabetically.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/products-test-1.png?raw=true)</br>
</br>

The user is then brought to the main products page. Their choice which in this case is "All Crystals", the number of products and the current sorting is visible to the user.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/products-test-2.png?raw=true)</br>
</br>

___

User Story:

As a Site User I can open up a product page so that I can view more details.
* Acceptance Criteria:
    * User can select a product and be directed to a details page
    * User is presented with expanded details of the product on a dedicated page
___

</br>
The user can then click on any product they wish (in this case, Green Calcite) and they will be redirected to a page showing the product's details including its rating (if any), price and detailed description.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/products-test-3.png?raw=true)</br>
</br>

___

User Story:

As a Site User I can leave a review of a product so that other users can decide whether to buy or not.
* Acceptance Criteria:
    * User can select a rating for a product
    * User can leave a review of the product
    * User can update their review
___

</br>
A product's rating is based off the average of the rating's given by authenticated users. If a user is authenticated, the form shown below, along with any posted reviews, will render on the page of the product they are viewing. In this instance, no reviews have been posted yet. The rating default is set at 3 out of 5.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/products-test-4.png?raw=true)</br>
</br>

Here, our user is already familiar with this product and so has decided to leave a rating.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/products-test-5.png?raw=true)</br>
</br>

Their rating of 5 now appears with the rest of the product's details.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/products-test-6.png?raw=true)</br>
</br>

On reflection, the user has now decided that the rating is a little high and so wants to reduce it to 4. As long as they are signed in, the form will render and they can simply leave another review. This will overwrite their previous review.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/products-test-7.png?raw=true)</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/products-test-8.png?raw=true)</br>
</br>

The review has been overwritten with the user's new review.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/products-test-9.png?raw=true)</br>
</br>

If the user then logs out and returns to the page, their review will be visible but the form to post a review will not be displayed.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/products-test-10.png?raw=true)</br>
</br>

___

User Story:

As a Site User I can select an item to add to my shopping cart so that I can purchase the product now or later.
* Acceptance Criteria:
    * User can select a product and add it to their cart
    * User can edit their cart
___

</br>
Text</br>
</br>

![image]()</br>
</br>

The cart icon has been assigned a Bootstrap 5 class to bring the user's attention to the fact that there are items in it. The user will also receive a notification message showing what has been added to the cart, the price and how much more they will need to spend in order to be eligible for free shipping.</br>
</br>

![image]()</br>
</br>

___

User Story:

As a Site User I can use the integrated Strype button so that I can purchase products.
* Acceptance Criteria:
    * User can add details at checkout
    * User can pay for the product using a credit card
    * User can see the items they are ordering
    * User receives a confirmation email containing their order details
___

</br>
Text</br>
</br>

![image]()</br>
</br>



### 5.2 Admin / Superuser CRUD Capability Testing

### 5.3 Code and Responsiveness Testing


W3C HTML:

Form error - thinks there's 2 id's but the widget replaces the old image with the new. So the old image is given an id and the new image's actual id is put in instead. When converted to HTML on the page it looks like there's 2 id's included.


Meta keywords ![Wordtracker](https://www.wordtracker.com/search)

Facebook Page ![Mystic Mindfulness Facebook Page](https://www.facebook.com/profile.php?id=100092204265600)

Privacy Policy ![Privacy Policy Generator](https://www.privacypolicygenerator.info/)

https://github.com/Code-Institute-Solutions/boutique_ado_v1


https://www.youtube.com/watch?v=wl4Yxo5_Cgw&t=386s

https://dev.to/themodernweb/how-to-make-an-e-commerce-website-with-html-css-and-js-3aon

Blog posts

https://www.healthline.com/health/healing-with-rose-quartz

https://tinyrituals.co/blogs/tiny-rituals/amethyst-meaning-healing-properties-and-everyday-uses

https://www.thespruce.com/calcite-feng-shui-4153035



site design 

https://www.thepsychictree.co.uk/

