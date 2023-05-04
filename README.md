# Mystic Mindfulness

## 1. Introduction

Mystic Mindfulness is a fictional ecommerce site offering for sale healing crystals. The premise of the site is to not only appeal to customers already specifically interested in healing crystals but, also potential customers who subscribe to the umbrella 'wellness' lifestyle which, through various marketing strategies discussed below, can be pursuaded to incorporate crystals into their various practices and become paying customers.

### 1.1 Deployed Website
A link to the deployed project via the Heroku app can be found [here](https://mystic-mindfulness.herokuapp.com/).


### 1.2 Repository
The GitHub repository can be found [here](https://github.com/cmikedev/mystic-mindfulness).

____
</br>

## 2. Business Rationale

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
</br>

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
Once a user, registered and logged in, or a guest, finds a product that they are interested in puchasing, they can add it to their cart using the plus and minus buttons to decide on the quantity.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/purchase-test-1.png?raw=true)</br>
</br>

The cart icon has been assigned a Bootstrap 5 class to bring the user's attention to the fact that there are items in it. The user will also receive a notification message showing what has been added to the cart, the price and how much more they will need to spend in order to be eligible for free shipping.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/purchase-test-2.png?raw=true)</br>
</br>

If the user clicks on the cart icon, they will be brought to their shopping cart. Here they will be shown what they have purchased, the quantity, price, the total price, the shipping cost and how much more they will need to spend in order to receive free shipping. We can change our mind and decide we no longer wish to purchase the Amethyst Dragon's Egg. By clicking on "remove" the item will be deleted from the cart.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/purchase-test-3.png?raw=true)</br>
</br>

As there was only one item in the cart, the cart is now completely empty.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/purchase-test-4.png?raw=true)</br>
</br>

Another item has been added. Once in the cart, a user may decide to increase the quantity. Here, one item was added but once in the cart the quantity was increased to 3.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/purchase-test-5.png?raw=true)</br>
</br>

In order to make the change in quantity take effect, the user must click on "update". Once done, the bag total and shipping cost change to reflect the change in quantity.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/purchase-test-6.png?raw=true)</br>
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

Once happy with the order the user can navigate to the checkout and fill out their details.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/purchase-test-7.png?raw=true)</br>
</br>

A guest can do the same, however the option to select save the delivery information will only render for an authenticated user.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/purchase-test-16.png?raw=true)</br>
</br>

As shown, the Stripe form will automatically render an error message if the user inputs an incorrect credit card number.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/purchase-test-8.png?raw=true)</br>
</br>

Once a correct number has been entered, the user can proceed with the payment.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/purchase-test-9.png?raw=true)</br>
</br>

By electing to complete the order, an order is generated, the user is provided with a reference number, the details of their order, confirmation by way of email and their cart is cleared.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/purchase-test-10.png?raw=true)</br>
</br>

An email confirmation containing details of the user's order is sent to the email that they provided when they registered.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/purchase-test-11.png?raw=true)</br>
</br>

Navigating to their profile, a user can see all of their past orders and their current information.

A user must be logged in to view this. If an unregistered user knows the url they will autiomatically be redirected to the sign-in page.</br>
<br/>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/purchase-test-17.png?raw=true)</br>
</br>

Here, we've changed the City/Town to "middle earth".</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/purchase-test-12.png?raw=true)</br>
</br>

Clicking "Update Information" saves the changes. The user is notified of the same.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/purchase-test-13.png?raw=true)</br>
</br>

To check that the changes are also reflected in the checkout form, some more items have been added to the cart and navigating to the checkout we can see that the change made to the town has been carried over.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/purchase-test-14.png?raw=true)</br>
</br>

Going to the Mystic Mindfulness Stripe account we can see that the payment from user pp5-test was successful.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/purchase-test-15.png?raw=true)</br>
</br>

___

User Story:

As a Site User I can view blog entries so that I can learn more about the products on the site.
* Acceptance Criteria:
    * User can see a list of blog entries
    * User can select an entry to view
    * A verified user can leave a comment
___

</br>
Any user, authenticated or not can browse the blog section of the website. A visitor can view a preview of each blog entry and by access the full post by clicking on the image or any of the other two links.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/blog-test-1.png?raw=true)</br>
</br>

Scrolling down, a visitor can view any comments that have been posted. If the visitor isn't authenticated, links to sign-in or register will be displayed.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/blog-test-2.png?raw=true)</br>
</br>

If the visitor is authenticated, links to post a comment will be rendered.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/blog-test-3.png?raw=true)</br>
</br>

Following the link, an authenticated user can post a comment.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/blog-test-4.png?raw=true)</br>
</br>

If an unauthenticated user knows the url of the comment page and tries to access it, they will be redirected back to the sign-in page.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/blog-test-7.png?raw=true)</br>
</br>

Once submitted, the user will be informed that their comment has been posted successfully.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/blog-test-5.png?raw=true)</br>
</br>

Browsing back to the page, the user's comment will appear.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/blog-test-6.png?raw=true)</br>
</br>

</br>

### 5.2 Admin / Superuser CRUD Capability Testing
</br>

A Superuser has different rights than a regular user. In addition, when a Superuser signs in to their account, different options in the form of a drop-down from their profile icon and edit/delete links on the Product and Blog pages will be rendered.</br>

___

User Story:

As a Superuser I can add a product to the main product page so that the inventory is kept up to date.
* Acceptance Criteria:
    * An authenticated user can access a page to upload a product
    * All uploads are done at the front-end
    * The authenticated user is presented with additional options when logged in than regular users ie - an 'add product button'
    * User is notified that the product has been successfully added
___

</br>
A Superuser can access the Product Management section from the drop-down that appears by clicking on the profile icon.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/add-product-test-1.png?raw=true)</br>
</br>

If an unauthenticated user knows the url of the Product Management page and tries to access it, they will be redirected back to the sign-in page.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/add-product-test-2.png?raw=true)</br>
</br>

The Superuser will be directed to a form which allows them to upload a product, selecting the category, name, description, price and if required, an image.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/add-product-test-3.png?raw=true)</br>
</br>

Once all required fields have been filled out, the Superuser selects "Add Product". If the addition is successful, the Superuser will be redirected to the product detail page and a success message will be displayed.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/add-product-test-4.png?raw=true)</br>
</br>

___

User Story:

As a Superuser I can edit a product so that I can correct any errors or make changes to the details.
* Acceptance Criteria:
    * Authenticated user can edit a products details
    * User is notified of the changes that are made
___

</br>
If a Superuser has logged into their account, "Edit Product" and "Delete Product" links will render on both the main Product and Product Detail pages. </br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/edit-product-test-1.png?raw=true)</br>
</br>

Clicking the "Edit Product" link will allow the Superuser to access a form which overwrites the current details recorded for the selected product including the photo. Here, the price has been changed.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/edit-product-test-2.png?raw=true)</br>
</br>

If an unauthenticated user knows the url of the edit product page and tries to access it, they will be redirected back to the sign-in page.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/edit-product-test-3.png?raw=true)</br>
</br>

Once submitted, the Superuser is directed back to the page of the product they were viewing. A message confirming that the changes were successful renders and the price has also changed.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/edit-product-test-4.png?raw=true)</br>
</br>

___

User Story:

As a Superuser I can delete a product so that I can keep the inventory up to date.
* Acceptance Criteria:
    * Authenticated user can select a product to delete
    * Once deleted, user is redirected
___

</br>
Text</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/delete-product-test-1.png?raw=true)</br>
</br>

Text</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/delete-product-test-2.png?raw=true)</br>
</br>

___

User Story:

As a Superuser I can create a blog post so that site users can learn more about the products and their uses.
* Acceptance Criteria:
    * Authenticated user can add a blog post
    * User is notified that the post has been added
___

</br>
When signed into their account, a Superuser can add a blog post by selecting "Blog Management" from the drop-down which renders when they click on the profile icon. This will bring the Superuser to a page where they can add a blog entry.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/add-blog-test-1.png?raw=true)</br>
</br>

If an unauthenticated user knows the url of the add a blog post page and tries to access it, they will be redirected back to the sign-in page.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/add-blog-test-2.png?raw=true)</br>
</br>

The Superuser can create an entry by filling out the form. The photo is optional. Here, we won't select one and a default image should render. To submit the form the Superuser selects the "Add Post" button.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/add-blog-test-3.png?raw=true)</br>
</br>

Once submitted, the Superuser is redirected to the post entry. The default image has rendered in place of a selected image.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/add-blog-test-4.png?raw=true)</br>
</br>

When the Superuser navigates back to the Blog page they will see their post appear.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/add-blog-test-5.png?raw=true)</br>
</br>

___

User Story:

As a Superuser I can edit or delete a post so that I can correct any errors or remove a post entirely.
* Acceptance Criteria:
    * Authenticated user can edit a blog post or delete it entirely
___

</br>
To edit the post that was just created, the Superuser selects the "Edit Post" link which renders when they are signed into their account.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/edit-blog-test-1.png?raw=true)</br>
</br>

If an unauthenticated user knows the url of the edit blog post page and tries to access it, they will be redirected back to the sign-in page.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/edit-blog-test-2.png?raw=true)</br>
</br>

The Superuser will be redirected to a form which allows them to edit the blog post. Here, a photo is added. Clicking the "Edit Post" button will submit the changes.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/edit-blog-test-3.png?raw=true)</br>
</br>

The Superuser will be redirected back to the Blog page and a message informing them that the edit was successful will render.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/edit-blog-test-4.png?raw=true)</br>
</br>

To delete the test entry, the Superuser selects the "Delete Post" link. This will direct the Superuser to a page where they will be asked to confirm that the post should be deleted.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/delete-blog-test-1.png?raw=true)</br>
</br>

If an unauthenticated user knows the url of the delete a blog post page and tries to access it, they will be redirected back to the sign-in page.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/delete-blog-test-2.png?raw=true)</br>
</br>

Clicking "Delete" confirms that the Superuser wants the post deleted.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/delete-blog-test-3.png?raw=true)</br>
</br>

The Superuser is then redirected back to the main Blog page. The entry has been deleted and no longer appears on the Blog page.</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/delete-blog-test-4.png?raw=true)</br>
</br>

</br>

## 5.3 Code and Responsiveness Testing

</br>

### CSS

The main project CSS and CSS where present in each app was tested using W3C's ![CSS Validation Service.](https://jigsaw.w3.org/css-validator/#validate_by_input) In all instances, the CSS was validated by direct input. No warnings or errors were returned.

### JavaScript

All pieces of JavaScript were tested using the ![JSHint](https://jshint.com/) validator tool. No errors were returned. 

### Python

The Python Code used throughout the project was tested using Code Institute's ![Python Linter](https://pep8ci.herokuapp.com/#). Where required, the code has been reformatted to remove empty spaces or reduce line length. There are no errors being returned.

### HTML

All of the HTML was tested using W3C's ![Markup Validation Service](https://validator.w3.org/#validate_by_input). The HTML was validated by direct input by viewing each page source and pasting the code into the validator. This prevented errors being returned which would have been the result of Django syntax being present had the HTML been copied directly from the development environment.

The HTML passed validation with no errors being returned. However, there were a number of warnings:

The Mystic Mindfulness ![homepage](https://mystic-mindfulness.herokuapp.com/) returns four "Empty heading". The first warning relates to a h4 element that is initially empty but is populated with a random quote on page load. This h4 element is contained in the base.html file in the project template's folder and so this warning will be returned on every html page that extends the base.html.

The next three are h6 elements that contain Font-Awesome icons.
</br>

![image]()</br>
</br>




W3C HTML:

Form error - thinks there's 2 id's but the widget replaces the old image with the new. So the old image is given an id and the new image's actual id is put in instead. When converted to HTML on the page it looks like there's 2 id's included.


## 6. Bugs
</br>

### 6.1 Bugs - Fixed
</br>

#### Django-ckeditor Error code: exportpdf-no-token-url

When posting a blog post, an "exportpdf-no-token-url" error was returned to the console. This related to the CKEditor plugin which is utilised in the Blog post and comment sections to use Rich Text forms.
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/export-pdf-error.png?raw=true)</br>
</br>

The fix was to remove the "exportpdf" plugin from the CKEDITOR_CONFIGS in the project's settings.py file.
</br>

#### Python Bare Except Error

The "Post" model in the blog app contained a function with a Try/Except statement which would attempt to call the image contained within the model or, if none existed, call a default. A "bare except" error was discovered when the code was put through Code Institute's ![Python Linter](https://pep8ci.herokuapp.com/#).
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/blog-models-pyerror.png?raw=true)</br>
</br>

In actuality this function was already redundant as although its purpose was to call a default image when the user was adding/updating a post image using the form, an If statement in the blog page html already handled an image not being included.
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/blog-models-pyerror-fix.png?raw=true)</br>
</br>


### 6.2 Bugs - Unfixed
</br>

#### Product Rating

As documented above in the User Testing Section, authenticated and logged in users are able to review products. Any site visitor, authenticated or not can browse products and filter by price and category. Earlier drafts contained sort by rating functionality. If a product had more than one rating, it would display normally on the main product page. When a user sorted products according to rating, the product would duplicate (with different ratings) according to the number of ratings it had. As per the screenshot below, two users left ratings and so two instances of the product were displayed when a user sorted by rating.
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/rating-error.png?raw=true)</br>
</br>

This appears to be due to an instance of each rating being called rather than the average rating. This bug is currently unresolved and in order to ensure that only one entry of each product is returned to the user, the sort by rating functionality has been removed.
</br>

#### Duplicate Attribute Error
</br>

The blog and product app both contain identical files titled "custom_clearable_file_input.html". This file activates the "widget.py" file which again is common to both apps (blog app displayed below). When a Superuser accesses the form to either add or edit a blog post or product, a thumbnail of the image that is being uploaded or is currently in place will be rendered.
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/edit-product-test-2.png?raw=true)</br>
</br>

However, to achieve this, the widget replaces the old image with the new. The old image is removed and the new image is assigned an id of "new-image". However, an error arises during HTML validation whereby when the form is rendered it appears that two id's appear on the same line of code which causes a "Duplicate Attribute" error.
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/form-error-1.png?raw=true)</br>
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/form-error-2.png?raw=true)</br>
</br>

In order to fix the HTML validation error the "custom_clearable_file_input.html" is no longer called as part of the form and the associated JavaScript has been removed from the add and edit blog/product html templates. The result is that there is now full error-free functionality. The Superuser no longer has a visual que, particularly for editing images but instead must rely on file names. It is due to this impact on user experience that this bug is considered unfixed.
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/form-error-3.png?raw=true)</br>
</br>

#### Duplicate ID Error
</br>

A HTML validation error of duplicate id's was returned on the bag page. This was due to the "quality-form.html" being called for both desktop and mobile views. When the page was rendered, the id that was in the "quality-form.html" and is used on the "Remove" link to remove an item from the cart was returned twice.
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/html-testing-bag.png?raw=true)</br>
</br>

To solve this, two html files were created and called instead of one:
* quantity_form_desktop.html
* quantity_form_mobile.html

Both of these used different id's for "Remove" item link. The class names utilised by the JavaScript in the bag.html files were left unchanged. Leaving these unchanged meant that when an item was removed, an error was raised in the terminal whereby the item id came back as undefined. The item was successfully deleted however.
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/html-testing-bag-console-error.png?raw=true)</br>
</br>

Making the class names different in each of the templates and the JavaScript fixed the server error. Items are successfully deleted without either HTML or Console errors.
</br>

![image](https://github.com/cmikedev/mystic-mindfulness/blob/main/readme_images/html-testing-bag-fix.png?raw=true)</br>
</br>

However, when the user hovers their cursor over the "Remove" link it changes to a "caret". This directly impacts user experience as a user would not expect the cursor to display in "caret" style unless it was placed over text. The "Remove" link works as it should but due to the impact on user experience this bug is considered unfixed.
</br>



# Other


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

