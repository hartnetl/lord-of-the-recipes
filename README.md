# Lord of the Recipes

[Live Site]( https://lord-of-the-recipes.herokuapp.com/)


1. [Introduction](#introduction)
2. [Data Structure](#data-structure)
3. [Technologies used](#technologies-used)
4. [Features](#features)
5. [Testing](#testing)
6. [Bugs](#bugs)
7. [Credits](#credits)
8. [Deployment](#deployment)
9. [Acknowledgements](#acknowledgements)

## Introduction

***

Welcome to **Lord of the Recipes**. This website has been built for my fourth portfolio project with the Code Institute to create a django based application. This site is a hosting platform for recipes with a pop culture theme. So the target audience is anyone with a passion for cooking or baking (or y'know, just food in general) and a love for pop culture of any flavour. The recipes are open to be viewed by anyone who stumbles across the site. To add their own recipes, save their favourites or leave comments on other recipes, users must register an account.  
Unfortunately the internet can be a dangerous place these days, so to protect users from trolls and other creatures which lurk in the dark recesses of the web any content uploaded will be submitted to admin for approval before being published. 

### Project Planning

#### Agile Development

Agile development helps to create an organised and efficient development plan to create a project which fulfills it's purpose. I have attempted to use this approach to build this project.  
This system requires a thorough project planning phase - deciding what the app is, and what the main goals of the project are. These are then developed into user stories, and features are built to address these user stories. To keep track of my development I created a user stories kanban board in github projects ([here](https://github.com/hartnetl/lord-of-the-recipes/projects/1)). I created an issue for each user story which was set to automatically display in my user story project. As I tackled each user story, it was moved to the in progress column. When I felt it had been completed it was moved to complete. Agile development also allows for the project to change. If the requirements have been met it is possible to revisit an issue to make changes or improvements to deliver the project in the best form possible.  
A second kanban board was created on github projects - a [todo list](https://github.com/hartnetl/lord-of-the-recipes/projects/2). This list contained small detail or general things that were needed but weren't attributable to a user story.


#### User Goals

As a user I want to be able to   

* Browse recipes
* Add my own recipes
* Save recipes for quick access
* Easily find required information through intuitive layout and filter options
* Explore a well laid out, easy to use site on any device 

As a site owner I want to be able to  

* Add recipes
* Moderate the content being uploaded by users to create a safe and welcoming space
* Create a website that can be easily used by all to increase number of users
* Create a community of like minded people
* Encourage users to register on the site as that makes them more likely to reuse the site
* Offer a usable, convenient website which people actually wish to use day after day


#### User stories 

| As a:       | I can:         | So that:  |
| ------------- |:-------------:| -----:|
| general user  | click on the navbar links | I can easily and intuitively go from one page to another |
| general user  | use the contact page form |  I can communicate with the admin of the page with questions, comments, user feedback etc |
| general user  | click recipes | I can view them fully on a new page |
| general user  | search recipes by tags | I can easily find what I'm looking for |
| general user  | view a list of recipes | I can choose which one to make |
| general user  | create an account | I can join the community and get access to registered user features like creating recipes and adding comments |
|  |     |  |
| Registered User |  upload recipes  |  recipes can be viewed by myself and others when complete, or saved as a draft for myself until ready to be published |
| Registered User |  create, edit and delete my recipes | I can control my own contributions to the site |
| Registered User | add comments on recipes  | I can be a part of the conversation with the community |
|  |       |   |
| Superuser | approve content (recipes and comments) | I can manage the content and filter out those with unsuitable language etc |  
| |     |  |

#### Wireframes

<details>
<summary>Show wireframes</summary>
<details>
<summary>Home Page - logged in view</summary>

A logged in registered user sees a logout and profile button in the navbar and footer instead of login and register. Clicking the burger button causes the navbar to expand/collapse. This is common across all pages. The signup box on the home page is removed.  
![logged in home page](static/readme/Home-page-logged-in.png)
</details> 
<details>
<summary>Home Page - logged out view</summary>

![logged out home page](static/readme/Home-page-logged-out.png)
</details> 
<details>
<summary>About Page</summary>

![about page](static/readme/About-page.png)
</details> 

<details>
<summary>Contact Page </summary>

![contact page](static/readme/Contact-page-logged-in.png)
</details>
<details>
<summary>Logout Page </summary>

![logged page](static/readme/logout.png)
</details>
<details>
<summary>Sign-In Page </summary>

![sign in page](static/readme/sign-in.png)
</details>
<details>
<summary>Sign up Page </summary>

![sign up page](static/readme/sign-up.png)
</details>
<details>
<summary>Profile Page </summary>

Users will see the recpies they have uploaded, as well as any they have favourited.  
![profile page](static/readme/profile.png)
</details>
<details>
<summary>Recipe list</summary>

When logged in users will have the option to create a recipe. Logged out users can't see this button.  
![recipe list page](static/readme/Recipe-list-page-logged-in.png)
</details>
<details>
<summary>Recipe view</summary>

Logged in users will be able to see edit and delete buttons on this page if viewing their own recipes.  
![Recipe view page](static/readme/Recipe-view-page-logged-in.png)
</details>
</details>  
<br>

#### UI design

**Fonts**
* The logo font used is [bubblegum sans](https://fonts.google.com/specimen/Bubblegum+Sans). It's a very fun and quirky font suited to the vibe of the page.
* The main text font used is [Noto Sans](https://fonts.google.com/noto/specimen/Noto+Sans?category=Sans+Serif). It is a sans-serif font which is more a more accessible font type, and I think it compliments my header font nicely.
* The main heading font is [Architects Daughter](https://fonts.google.com/specimen/Architects+Daughter). Is is a relaxed, easy to read font which adds a bit of playfulness to the headings.
* The recipe create form has summernote fields which gives users the ability to quickly input their own fonts, styles etc. As this site aims to deliver a community feel, I felt it best to enable users to be able to express some personality and creativity.

**Colour Scheme**

## Data Structure

The database used locally and by heroku is postgres.  
Cloudinary is used to house user images uploaded to the website.  

The database contains two custom models - recipes and comments. Both link to the user model which is built into django.
Each registered user is assigned a user id. They can create recipes which will be linked to their id, and each recipe has an auto generated slug field (this is derived from the recipe's title). The recipe can be edited and deleted by the person who created it only (or admin, if guidelines are breached). Registered users can leave comments on any recipe and the comment will display their username. A registered user can choose to publish recipes so they are displayed on the public recipe page, or leave them as drafts so they will only be visible on their own profile page. 

<details>
<summary>Custom data models used:</summary>

![datamodels used](static/readme/models.png)
</details>

<br>

## Technologies Used

***

Languages  
* [Python3](https://www.python.org/about/) 
* [Javascript](https://www.tutorialspoint.com/javascript/javascript_overview.htm#:~:text=JavaScript%20is%20a%20dynamic%20computer,language%20with%20object%2Doriented%20capabilities.) 
* [html5](https://developer.mozilla.org/en-US/docs/Web/HTML) 
* [css](https://developer.mozilla.org/en-US/docs/Web/CSS)

<br>

Libraries and other technologies used
* [Django 3](https://www.djangoproject.com/start/overview/)
* [Bootstrap 5](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
* [Taggit](https://github.com/jazzband/django-taggit)
* [Summernote](https://summernote.org/)
* [Google fonts](https://fonts.google.com/)
* [Fontawesome](https://fontawesome.com/)
* [Postgresql](https://www.postgresql.org/)
* [cloudinary](https://cloudinary.com/about)

Other tools
* [Gitpod](https://www.gitpod.io/docs/) as the IDE for development 
* [Git](https://git-scm.com/about) for version control 
* [Github](https://github.com/about) to host the project code 
* [Heroku](https://www.heroku.com/about) to deploy the project
* W3C for validating [html](https://validator.w3.org/), [css](https://jigsaw.w3.org/css-validator/) and [links](https://validator.w3.org/checklink) 
* [jshint](https://jshint.com/about/) to validate javascript
* [pep8 online](http://pep8online.com/about) to validate python code
* [lighthouse](https://developers.google.com/web/tools/lighthouse) to test accessibilility and performance 
* [github projects](https://docs.github.com/en/issues/organizing-your-work-with-project-boards/managing-project-boards/about-project-boards) to create kanban boards 
* [balsamiq](https://balsamiq.com/) for wireframes
* [tinypng](https://tinypng.com/) to compress image file sizes
* [logomaker](https://www.logomaker.com/ ) to create the logo
    

## Features

- all pages
    - header
        - Website title which returns to home page if clicked
        - navbar with links for all users: home, recipes, about, contact 
        - navbar with links for logged out users: login, register 
        - navbar with links for logged in users: profile, logout
        - welcome message to logged in user
    - footer
        - social links (github and linkedin)
        - same links as navbar 
        
- home page
    - General intro to site so users know what the page is about upon landing
    - Explore box to encourage users to explore recipe page
    - Logged out users see a box which encourages them to sign up

- about page
    - a static page which tells users about the site, displays rules etc

- contact page
    - a form which visitors can use to contact site admin with queries, feedback etc.  
    Automated response to user is given with emailjs

- recipe page
    - List of recipes which have been published by users and approved by admin
    - Pagination of recipes so list isn't too long
    - Filter by category
    - Filter by tags
    - logged in users can create recipes
    - each recipe can be clicked to display the full version

- detailed recipe page
    - Full view of recipe
    - Option to save recipe
    - Comments can be viewed by all users, and left by registered users
    - If the user created the recipe they have the option to edit or delete the recipe

- profiles
    - Registered users have a profile which displayed the recipes they have created as drafts and published.
    - Also shows a list of recipes they have favourited

#### SCREENSHOTS

<details>
<summary>home page logged out </summary>

![home page logged out](static/readme/screenshots/home-out.png)
</details>
<details>
<summary>home page logged in  </summary>

![home page logged in](static/readme/screenshots/homepage-in.png)
</details>
<details>
<summary>navbar logged in  </summary>

![navbar logged in](static/readme/screenshots/navbar-in.png)  
</details>
<details>
<summary>profile page   </summary>

![profile page](static/readme/screenshots/profile.png) 
</details>
<details>
<summary>footer </summary>
 
![footer](static/readme/screenshots/footer.png) 

</details>
<details>
<summary>contact page   </summary>

![contact page](static/readme/screenshots/contact.png) 

</details>
<details>
<summary>recipe view logged in    </summary>

![recipe view logged in ](static/readme/screenshots/recipe-in.png) 

</details>
<details>

<summary>signout  </summary>

![sign out page](static/readme/screenshots/sign-out.png)  

</details>


### Future features 

* Socials sign in
* Forgot password functionality
* System to allow users to rate recipes and the average is displayed
* Alter ingredients field to input one by one instead of large text field
* Light mode / Dark mode

## Testing 

***

### Manual Testing

The manual testing file is [here](TESTING.md)


### Validation

html: [W3C markup validator](https://validator.w3.org/)   
Each page url was ran through the validator and any errors or warnings that appeared were corrected, and the url was ran through the validator again.  
<details>
<summary>This is the error and warning free validation seen for most pages</summary>

![w3c html validator results for home page](static/readme/html-validated.png)
</details>
<details>
<summary>Extra closing p tag error</summary>

In some pages such as the profile page, recipe view page and recipe list page an error was showing that there was a closing p tag but no opening tag for it. In my hardcoded html there was no extra closing p tag. I believe this to have come from the use of summernote injecting it's own html. Feedback from previous projects were very specific about not leaving in **any** errors so I made the decision to follow the validator and remove the hardcoded closing p tag. This removes the error upon validation, and none arise for not having a closing tag hard coded.

![p tag error](static/readme/p-close-error.png)
</details>  
<br>

CSS: [W3C validator](https://jigsaw.w3.org/css-validator/)  
CSS file was copied into the validator and all errors and warnings returned were addressed.  
<details>
<summary>View clear validator</summary>

![css validator with no warnings](static/readme/css-validate.png)
</details>   

<br>

Python: [pep8](http://pep8online.com/)  
Code was copied directly into the validator.
<details>
<summary>Pep8 all clear message</summary>

Most python files were vallidated and corrected to have no errors or warnings. 
![pep8 no warnings or errors visible on most python files](static/readme/pep8.png)
</details>

<details>
<summary>Some files had long lines which couldn't be broken</summary>

settings.py and views.py have lines which throw errors if broken using ' \ '.  
Instead #noqa was used to allow the validator to pass that line length error.  
While the limit should be kept below 79 characters, it is permissable to go up to 99 [[link](https://www.python.org/dev/peps/pep-0008/#:~:text=Some%20teams%20strongly%20prefer%20a%20longer%20line%20length.%20For%20code%20maintained%20exclusively%20or%20primarily%20by%20a%20team%20that%20can%20reach%20agreement%20on%20this%20issue%2C%20it%20is%20okay%20to%20increase%20the%20line%20length%20limit%20up%20to%2099%20characters%2C%20provided%20that%20comments%20and%20docstrings%20are%20still%20wrapped%20at%2072%20characters.)]
![e501 error - line too long](static/readme/pep8-e501.png)

Code over 79 characters
![example of code not to be broken](static/readme/longline.png)
<details>
<summary>Example line of code</summary>
</details>
<details>
<summary>Error code e501</summary>

![This is the pep8 error](static/readme/pep8-e501.png)
</details>
</details>

JS: [JSHint](https://jshint.com/)  
JS script was ran through jshint and returns no errors or warnings
<details><summary>View jshint result</summary>

![screenshot of jshint results](static/readme/jshint.png)
</details>


Links: [w3c link validator](https://validator.w3.org/checklink)
On the home page there was a warning for the LinkedIn link. It was tested manually as suggested and it works as expected.
<details>
<summary>View report here</summary>

![links report](static/readme/links.png)
</details>


## Bugs

***

### Fixed 

* BUG: When registering for a profile, users who enter an email address get a 500 server request.
    * FIX: Turn off email verification
* BUG: When users first sign up they get a server 500 error when viewing profile
    * FIX: Placement of {% empty %} was wrong
* BUG: Data in edit form shows html code
    * FIX: Add summernote widget to form fields
* BUG: Uploaded user photos don't show in full recipe view
    * FIX: Typo in html code
* BUG: Slug doesn't auto generate as in the admin panel
    * FIX: Add slugify to model for front end generation.  
    https://kodnito.com/posts/slugify-urls-django/
* BUG: Heroku error h10 
    * FIX: This appeared numerous times, and was usually a syntax / punctuation error in settings.py


### Remaining

* BUG: Server 500 error when approving comments/recipes in admin panel. Can be approved within recipe in panel.
    * No fix found as this is a recent bug - will be addressed in future
* BUG: Contact form and admin notifications potentially not working
    * At  10am or so on the morning of submission outlook suspended the email account using emailjs for suspicious looking activity. I'm hoping a few security measures can be fixed to get them working again - the code was working before this block and hopefully will again after.


## Credits

***

Code

* custom 404 page
https://www.youtube.com/watch?v=3SKjPppM_DU

* flip cards  
https://www.w3schools.com/howto/howto_css_flip_card.asp

* Many tutorials were followed using [geeksforgeeks](https://www.geeksforgeeks.org/), django documentation and youtube for learning about building the django app (views - urls - template). Especially the generic views (CreateView, DeleteView, UpdateView)

* Cancel function to load previous page  
https://stackoverflow.com/questions/524992/django-templates-create-a-back-link

* taggit tutorial  
https://www.youtube.com/watch?v=Y70bvbW8zso


MEDIA

    * 404 page map  
    https://pngtree.com/freepng/treasure-map-treasure-map-clip-art_5903304.html

    * icons are all fontawesome

    

## Deployment

***

This program is deployed using [Heroku](https://dashboard.heroku.com/login).  

Before deploying a project, ensure all dependencies (libraries etc that Heroku needs to build and run your project) are listed. The command "pip3 freeze > requirements.txt" in the python terminal will generate this list in a file called requirements.txt which will be read by Heroku.  
Ensure debug is set to false

### Set up the App


### Deployment

Note: These steps will walk through some of the steps to set up the environment settings just to ensure they are the same

This project was originally deployed following this Code Institute [cheat sheet](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf)
## Getting a copy of this project


### Forking Repository

To get a copy of this code it can be forked to your own repository.

- Go to the repository page on GitHub. This project's repo can be found [here](https://github.com/hartnetl/lord-of-the-recipes) 
- Find 'fork' along the top of the page on the right hand side
- A copy of this code will be sent to your own repository, where you can use that pretty green 'Gitpod' button to open it in GitPod
- You will need to set up your environment as described below for it to work

### Cloning Repository

If you need a local copy of the code to play with, cloning the code is a better option.

- Go to the repository page on GitHub. This project is [here](https://github.com/hartnetl/lord-of-the-recipes) 
- Find the button that says 'Code' to the left of the green Gitpod button. 
- Choose the cloning method you require (HTTPS/ SSH or CLI)
- Open Git Bash
- Enter the working directory as your desired location for the cloned directory
- Type "git clone" and paste the URL you copied from github
- Hit enter and the code should be cloned for local use

### Set up your local environment

Install requirements

* In your editor's terminal enter the following command:  

        pip3 install -r requirements.txt

    This will install all the dependancies needed to run the project


### Connect to heroku

Set up app on heroku 

* Go to Heroku, and register/login
* Click 'create new app'
* Setup your app name and region
* Navigate to the Resources tab. Set your database to Postgres with the hobby dev option.
* Go to the Deploy tab and connect your Github repository by searching for it (this one is lord-of-the-recipes)

Connect postgres database to local environment

* Go to or create env.py and import os
* set up your database and secret key

        os.environ["DATABASE_URL"] = "Paste in Heroku DATABASE_URL Link"  
        os.environ["SECRET_KEY"] = "Make up a randomSecretKey"

* Make sure env.py is in your gitignore file
* Go to heroku and add your secret key value to the config vars under SECRET_KEY

Set up environment 
    
* In settings.py add:
    
        from pathlib import Path
        import os
        import dj_database_ur

        if os.path.exists("env.py"):
            import env

* Set your secret key to

        SECRET_KEY = os.environ.get('SECRET_KEY')

* Set database to postgres

        DATABASES = {
        'default':
        dj_database_url.parse(os.environ.get("DATABASE_URL"))}

Run migrations using

    python3 manage.py makemigrations
    python3 manage.py migrate

Connect static files with cloudinary (this may be substituted for another platform such as aws)

* Create/login to cloudinary account and create project for this app
* Copy the cloudinary_url from the dashboard
* Set this in your env.py file

        os.environ["CLOUDINARY_URL"] ="cloudinary://1234:SHDUtZi@dbhyi45mc"


* Add this link to the heroku config vars
* Create DISABLE_COLLECTSTATIC config var and set to 1


* In settings.py add cloudinary to installed apps under staticfiles
* Set cloudinary as the location for static files

    STATIC_URL = '/static/'
    STATICFILES_STORAGE ='cloudinary_storage.storage.StaticHashedCloudinaryStorage'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    MEDIA_URL = '/media/'
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage

* Link templates directory in heroku to app (still in settings.py)

    Place under the BASE_DIR line  

        TEMPLATES_DIR = os.path.join(BASE_DIR,'templates')  

    Place in templates array  

        'DIRS': [TEMPLATES_DIR]  

* Add heroku and local environment as allowed hosts

    ALLOWED_HOSTS =["PROJECT_NAME.herokuapp.com", "localhost"]

Create Procfile in root directory **Note the capital P** 

    web: gunicorn PROJECT_NAME.wsgi

Commit and push your changes and your app should run in heroku  
To return to local development just switch debug to true and collectstatic (in heroku config vars) to 0  
Remember to swap the settings back before pushing and returning to deployed version  


## Acknowledgements

I would like to send an amazing thank you to my entire cohort, without your advice and support I wouldn't have made it through this project.  
To Kasia, my cohort tutor, words can't express how much your help, guidance and encouragement has motivated me day after day to keep going through this project and the course in general. Thank you for all that you do for us.  
To my mentor Maria, thank you for being so supportive and encouraging throughout this project, even though you have less availability. It is hugely appreciated.  
Finally to my friends and family subjected to my complaints, raves about mini problems solved, and then forced to test my site at every stage along the way, thank you. For everything. And I'm sorry for boring you with incessant coding rants and raves... At least that's another project out of the way so you get a break for a little while!  