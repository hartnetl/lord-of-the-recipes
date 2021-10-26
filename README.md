![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

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

Overview the project

### Project Planning

Project conception, user stories, wireframes

## Data Model


Models tables and planning


## Technologies Used

***

- Python, javascript, html
- Libraries etc
    - django, bootstrap, taggit, summernote
    

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

