# Lord of the Recipes

[Live Site]( )

![Am I responsive screenshot]( )


1. [Introduction](#introduction)
2. [Data Model](#data-model)
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
* The main font used is x because x
* The main heading font is x because x
* The recipe create form has summernote fields which gives users the ability to quickly input their own fonts, styles etc. As this site aims to deliver a community feel I felt it best to enable users to be able to express some personality.

**Colour Scheme**

## Data Structure

    How the site operates and works
    Database used (postgres) and image source (cloudinary)


<details>
<summary>Data models used:</summary>

![datamodels used](static/readme/models.png)


## Technologies Used

***

Languages
    - Python, javascript, html, css
Libraries etc
    - django, bootstrap, taggit, summernote, googlefonts, fontawesome, postgresql, cloudinary
Other tools
    - gitpod, git, github, heroku, w3c markup for html and css, jshint validator, linkchecker, lighthouse, pep8, grammerly, githubprojects, balsamiq,
    

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


### Future features 



## Testing 

***

### Manual Testing

Dev tools devices, users
Table for user stores - associated features - works as expected


### Validation

html -
css - 
python/django - 


### Automated testing

unit test


## Bugs

***

### Fixed 


### Remaining


### Terminal problems


## Credits

***

- Media
    

- Code
    

## Deployment

***

This program is deployed using [Heroku](https://dashboard.heroku.com/login).  

Before deploying a project, ensure all dependencies (libraries etc that Heroku needs to build and run your project) are listed. The command "pip3 freeze > requirements.txt" in the python terminal will generate this list in a file called requirements.txt which will be read by Heroku.  
Ensure debug is set to false

### Set up the App


### Deployment


## Getting a copy of this project

### Forking Repository

To get a copy of this code you can manipulate without affecting the main code, it can be forked.

- Go to the repository page on GitHub. This project is 
- Find 'fork' along the top of the page
- A copy of this code will be sent to your own repository, where you can use that pretty green button to open it in GitPod

### Cloning Repository

If you need a local copy of the code to play with, cloning the code is a better option.

- Go to the repository page on GitHub. This project is 
- Find the button that says 'Code' beside the green Gitpod button. 
- Choose the cloning method you require (HTTPS/ SSH or CLI)
- Open Git Bash
- Enter the working directory as your desired location for the cloned directory
- Type "git clone" and paste the URL you copied from github
- Hit enter and the code should be cloned for local use

## Acknowledgements

