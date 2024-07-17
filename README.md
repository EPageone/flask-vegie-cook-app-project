# Code Institute Milestone Project 3 Backend Project - Vegie Cookapp

## Description

The purpose of this project was to create a web application that allws users to add and store their own data ans be able to edit and delete. This used the CRUD (Create, Read, Update and Delete) functionality. As I like to cook I decided to create a cookapp that was for vegetarians and that the user could register, log in, use a profile, add recipes, edit recipes and manage what type of vegetables they could use and add more vegetables to the database. I used MongoDB for my database as a non-relational database. I found this easier to use and to add to rather than relational databases such as mysql. I used dictionaries in the database and languages such as python, html, css and jquery. It was deployed using Heroku and I constantly checked to make sure that it worked and was continuing to load and be able to use. 
 
Throughout this particular project I did struggle with the making sure I kept the MongoDB database clear and simple and I seemed to receive many errors that I had to overcome using python. I found that I am more confident in html and css languages and that jquery was easier to use than javascript, but still had to overcome a lot of earning curves. I was able to do this with support from Stack Overflow with quesions that had been asked before and realised that some of the code in python had changed their methods from remove to delete and using the correct methods, otherwise the devlopment could not be built. It was a difficult project, but feel quite proud that I managed to produce something that users can add, update, edit and delete and I created two users one for a regular user that add recipes but cannot see the rest of the databases that an admin user can see. 

Username: User3
Password: Password

Admin username: Admin
Password:       password1


## UX Design

### User Design

1. Any user can register, login and add to the reipe database and logout
2. Any user can use the dropdown to choose their veg type and then add to an ingredients list and then give a recipe description.
3. Any user can edit their own recipes and also have access to the homepage which has five recipes their which they can try out. These cannot be edited by the user. 
4. The admin user has access to the manage vegies database and can add more vegetabels to the database, but the registered user does not have access. 
5. All users including admin user can search on the home page any keywords and that the database will update itself accordingly. For example if the user searches for mushrooms, then the recipes that include mushrooms will stay on the home page and the others that do not, remove themselves from the homepage. If the user resets the page then all the recipes appear. 
6. All users including admin can logout of the system and then login again. 


## Wireframes

![alt text](<wireframes/Vegie Cookapp Home Page.png>)
![alt text](<wireframes/Vegie Cookapp Register Page.png>)
![alt text](<wireframes/Vegie Cookapp Log In Page.png>)
![alt text](<wireframes/Vegie Cookapp Profile Page.png>)
![alt text](<wireframes/Vegie Cookapp Log Out Page.png>)
![alt text](<wireframes/Vegie Cookapp Add Recipe Page.png>)
![alt text](<wireframes/Vegie Cookapp Manage Vegies Page.png>)
![alt text](<wireframes/Vegie Cookapp Mobile Home Page.png>)
![alt text](<wireframes/Vegie Cookapp Mobile Register Page.png>)
![alt text](<wireframes/Vegie Cookapp Mobile Profile Page.png>)
![alt text](<wireframes/Vegie Cookapp Mobile Log In Page.png>)
![alt text](<wireframes/Vegie Cookapp Mobile Add Recipe Page.png>)
![alt text](<wireframes/Vegie Cookapp Mobile Manage Vegies.png>)
![alt text](<wireframes/Vegie Cookapp Mobile Log Out Page .png>)
![alt text](<wireframes/Vegie Cookapp Tablet Home Page.png>)
![alt text](<wireframes/Vegie Cookapp Tablet Register Page .png>)
![alt text](<wireframes/Vegie Cookapp Tablet Log In Page copy.png>)
![alt text](<wireframes/Vegie Cookapp Tablet Log Out Page .png>)


## Database Collections

My MongoDB database consists of three collections, one for each of the following:

1. Recipes
2. Vegies
3. Users

The recipes collections contain all the information including recipe name, ingredients list, recipe name and who it is created by. 
The vegies collections contain all the information for vegie names. 
The users collection saves the users information if they have logged in. 


## Technologies Used

1. HTML- a standardized system for tagging text files to achieve font, colour, graphic, and hyperlink effects on World Wide Web pages.
2. CSS - cascading style sheets to style the content and layout of the site.
3. JQuery - Javascript library which makes it easier to use Javascript.
4. Python - Programming Language to create the backend that decides upon the responses to the user's input.
5. Gitpod - IDE (Integrated Development Environment) to create and write code. 
6. GitHub - for version control and backup of code
7. Materalize -  A framework for developing responsive websites.
8. Flask - python web framework to hold all the code and templates together as one site.
9. MongoDB - Non-relational database to store all information about the recipes, vegies etc.
10. Heroku - is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

### Libraries I had to install

1. Flask
2. PyMongo
3. BSON
4. JQeury
5. DNSPython


### Testing

I tested my HTML and CSS code using the W3Schools Validation tools. 
I also completed manual testing and tested out all functions to make sure they worked. 

![alt text](<CSS Validated code checked and passed.jpg>)
![alt text](<html validate 1.jpg>)
![alt text](<html validate 2.jpg>)

### Manual Testing


| Feature                 |  Action                  | Expected Result                                |  Tested             | Passed        |
| -----------------------:|:------------------------:| ----------------------------------------------:|--------------------:|--------------:|
|  Home Page              | 5 recipes & search       | User can search and login                      | Yes                 | Yes           |
|  Login                  | User directed to LogIn   | User can login to account or register          | Yes                 | Yes           |
|  Add Recipes            | Add recipe, ingredients  | User can add and edit recipe                   | Yes                 | Yes           |
| Manage Vegies           | Vegies cards appear      | Admin can edit, not seen by the user           | Yes                 | Yes           |
| Log Out                 | Users can log out        | User can logout, returns to Log In Page        | Yes                 | Yes           |


### Problems in Development

I had some problems with certain python code such as update. I had to use the update_many method with python as the update method does not work. 
There were many issues with the devlopment and I had to look through each line of code to check that it was correct and also that my databases in MogoDB were communicating with the python language. 


### Deployment

Project was deployed to heroku with some ease.
Created Procfile and requirements.txt for dependencies.
Created new heroku app and set environment variables.
Linked my Github and environment with Heroku
Pushed to heroku.
Linked pre-existing mongodb to new site, no installation necessary.

My link for Heroku is: https://flask-vegie-cook-app-project-6ed612cf44b6.herokuapp.com/

My link for GitHub is: https://github.com/EPageone/flask-vegie-cook-app-project


### Acknowledgments

I used https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.1/css/all.min.css.
I used https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.
I used https://code.jquery.com/jquery-3.5.1.min.js.
I used W3 Schools to validate my CSS and HTML Code.
I used some recipes from my Mum, so thankyou. 



### 


