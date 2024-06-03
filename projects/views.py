from django.shortcuts import render

# Create your views here.
"""Here the views are created for each project that is linked to the 'projects'
page. In a list of dictionaries, with links to the code"""

def project_list(request):
    projects = [
        {
            'name': 'Flask App to manage a Book store Inventory',
            'description':  '''Welcome to the Read-A-While Books Manager! 
            This project was originally created with Python and Sqlite. Now
            I have used the code to create an app with Flask.''',
            'github_url': 'https://github.com/lu-sketch/Flask-Book-store-app/blob/main/README.md',
            'live_demo_url': 'https://flask-book-store-app-i0t7.onrender.com/'
        },
        {
            'name': "A Toy Website - Maggie's Toybox",
            'description': '''This project is a static toy website.
            Designed using Bootstrap, CSS and HTML. The website consists of 
            one page, i.e. index.html. Styling is done, using an external main.css file.''',
            'github_url': 'https://github.com/lu-sketch/Project-Static_website',
            'live_demo_url':'https://lu-sketch.github.io/Project-Static_website/'
            
        },
         {
            'name': "Machine Learning Projects",
            'description': '''This repository contains various machine 
            learning models that I completed during my Data Science bootcamp
            with Hyperiondev. 
            These models cover a range of topics and techniques to enhance 
            my understanding and proficiency in machine learning.''',
            'github_url': 'https://github.com/lu-sketch/Machine-Learning-models',
            'live_demo_url':None
        },
        {
            'name': "EDA - Project Analyzing the Titanic Data Set",
            'description': '''This project I conducted to improve my EDA analysis
            using Pandas, Seaborn and Matplolib libraries.
            The main objective of this project is to perform EDA to 
            understand the characteristics of the Titanic dataset, 
            uncover correlations between variables, and identify factors 
            influencing survival rates.
            Had alot of fun with this project :)''',
            'github_url': 'https://github.com/lu-sketch/EDA---Titanic-data-set/tree/main',
            'live_demo_url':None
        },

            
    ]
    return render(request, 'projects/project_list.html', {'projects': projects})

