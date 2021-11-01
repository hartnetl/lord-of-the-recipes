# MANUAL TESTING OF LORD OF THE RECIPES

This website was tested using devtools on a 11.5" Lenovo ideapad s130-11IGM and a OnePlus Nord smartphone.
The dev tools devices used were iPhone 5, iPhone6, iPhone 6 plus, iPhone X, iPad, iPad mini, iPad Pro, surface duo and motoG4.

## Testing user stories for all users

* As a general user I can click on the navbar links to easily and intuitively go from one page to another

 Feature  | Expectation  | Works as expected |
|:-------------:| :-----: | :-------------: |
| Clickable navbar links | Clicking on a links in the navbar redirects to the appropriate page | :heavy_check_mark: |
| Navbar on every page | The navbar is at the top of everypage and all links work | :heavy_check_mark: |
| Navbar links are intuitively named | The headings are named so that information is displayed where expected | :heavy_check_mark: |

* As a general user I can use the contact page form to communicate with admin  
 Feature  | Expectation  | Works as expected |
|:-------------:| :-----: | :-------------: |
| A working form | Form filled out by users is submitted to admin with their message and contact info | :heavy_check_mark: |
| Form validation | Form will only be submitted if filled out correctly by user | :heavy_check_mark: |
| Form feedback | An alert message pops up when form is submitted, a spinner is displayed while the submission processes and the user receives a confirmation e-mail with copy of their message | :heavy_check_mark: |
| Form response | Users can get a response from admin if a valid e-mail is supplied | :heavy_check_mark: |

* As a general user I can click on recipes to view them in full detail 
 Feature  | Expectation  | Works as expected |
|:-------------:| :-----: | :-------------: |
| Link button | Each recipe card has a button which directs user to full view page of that recipe | :heavy_check_mark: |
|  | The link button is displayed on the back of each card on large screens, and the front for smaller screens | :heavy_check_mark: |
| Full view | The recipe is displayed in full view | :heavy_check_mark: |

* As a general user I can search recipes by the existing tags 
 Feature  | Expectation  | Works as expected |
|:-------------:| :-----: | :-------------: |
| Clickable taglist | Clicking on a tag will display all recipes which have that tag | :heavy_check_mark: |
| Clickable categories | Clicking on a category button will display all recipes assigned that category | :heavy_check_mark: |

* As a general user I can create an account
 Feature  | Expectation  | Works as expected |
|:-------------:| :-----: | :-------------: |
|  Registration form | Filling out the form registers user to database | :heavy_check_mark: |
| Profile | Users have a profile from the moment they sign up | :heavy_check_mark: |
| Recipes displayed in profile | Each time a user creates a published or draft recipe, or saves a recipe, it is added to their profile | :heavy_check_mark: |

Registered have all the capabilities of general users plus:

* As a registered user I can create recipes
 Feature  | Expectation  | Works as expected |
|:-------------:| :-----: | :-------------: |
| Create recipe button | Button displayed on recipe list and profile pages only shows to registered users, and redirects to create recipe form | :heavy_check_mark: |
| Create recipe form | Forms filled out correctly are submitted to database | :heavy_check_mark: |
| Public display | Submitted recipes are displayed in the public recipe list once approved by admin | :heavy_check_mark: |
| Draft recipes | Recipes can be saved as drafts so users can save progress without making it visable to everyone | :heavy_check_mark: |
| Summernote fields | Summernote fields are included in some of the recipe form fields to allow users to input their own styling | :heavy_check_mark: |

* As a registered user I can edit and delete my recipes
 Feature  | Expectation  | Works as expected |
|:-------------:| :-----: | :-------------: |
| Private edit and delete buttons | Edit and delete buttons appear on a recipe view only if the user created the recipe | :heavy_check_mark: |
| Edit button | The edit button links to the edit recipe form | :heavy_check_mark: |
| Edit form | Current info is displayed on the edit form to make editing easier. Any saved edits are updated on recipe  page. | :heavy_check_mark: |
| Edit form feedback | A recipe can be edited without approval, but admin will be notified to review this. A message appears to inform users. | :heavy_check_mark: |
| Edit redirect | When edits are saved user is redirected to full view of recipe | :heavy_check_mark: |
| Delete button | The delete button redirects user to the confirm delete page | :heavy_check_mark: |
| Delete page | User is asked to confirm deletion. If selected, recipe is removed from database.  | :heavy_check_mark: |
| Delete redirect | User is redirected to recipe list page if delete is confirmed. Redirects to recipe if not. | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
|  |  | :heavy_check_mark: |
