# CompanyDashboard

A simple admin dashboard web application using the Django Framework with authentication. On the site a user can make customer accounts that can receive orders from a list products. These orders can be in multiple states of delivery (ex. pending, out for delivery, Delivered). You can view user information and update this information at any time. This dashboard uses the Django Framework to combine the tools used in python with html for the front end. The styling for the webpage used Bootstrap/CSS. The dashboard is supported by various APIs witten using Django standards of REST. Storage is handled on AWS RDS instance for the Postgres. For image storage I used an Amazon S3 instance.

## Overview
- The frontend used Django
- Each service is supported by multiple Django standard API's.
- Data for each service is stored in a instance of Postgres (AWS-RDS instance).
- The entire application is deployed and run on a AWS-EC2 instance and static storage with an Amazon S3 bucket instance.
- Most styling was bootstrap with some custom CSS.

## Main Objectives
- Implement a Web Application using Django web design.
- Solved some complexities with form design using python with HTML
- Deploy using AWS hosting (AWS-RDS, AWS-EC2, AWS-S3 bucket)
- Develop reusuable code in for other large project.

## Some of what I learned
- Patterns for creating scalable Django web applications for a variety of app domains.
- Implementing python models into HTML design.
- Create a consistent structured responses from the different API's.
- Configure and scale a service with AWS-RDS instances.
- Document and enforce structural constraints.
- Limit access to my API's with proper authentication and CSRF tokens.
## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/KyleJGlover/CompanyDashboard.git
   ```
2. Install Django packages
   ```sh
   pip install -r requirements.txt
   ```
You will need django to be installed in you computer to run this app. Head over to https://www.djangoproject.com/download/ for the download guide

Download django usig pip

3. Install Django
   ```sh
   pip install django
   ```
 - Once you have downloaded django, go to the cloned repo directory and run the following command

3. Make model migrations
   ```sh
   python manage.py makemigrations
   ```
 - This will create all the migrations file (database migrations) required to run this App.
Now, to apply this migrations run the following command
4. Migrate model
   ```sh
   python manage.py migrate
   ```
 - One last step and then our todo App will be live. We need to create an admin user to run this App. On the terminal, type the following command and provide username, password and email for the admin user

5. Create Super User (Admin)
   ```sh
   python manage.py createsuperuser
   ```

6. Run Server
   ```sh
   python manage.py runserver
   ``` 

Couple of preperations for a developer:
- This project still needs some improvements such as updating the model structure to contain a more coherent Admin and Customer differences.
- Make sure to implement you own .env file for settings.py environment variables.

## Tech Stack
1. Front-End 
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com)
2. Back-End
- [Django](https://www.djangoproject.com/)

- [Postgres](https://www.mongodb.com/)
4. Hosting 
- [AWS-RDS](https://aws.amazon.com/rds/)
- [AWS-EC2](https://aws.amazon.com/ec2/)
  
## Screenshot