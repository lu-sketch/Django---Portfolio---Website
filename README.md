
# Django Portfolio Project 

## Overview

This project showcases a portfolio of website created using the popular 
Django framework.
The website consits of several different applications.
These apps includes various features such as;
- A project app - Showcasing latest projects with links to GitHub repositories.
- A blog app - documenting my coding journey.
- A personal app - providing background, educational and contact information.
- A polls app - where users can vote on exciting polls. project showcases.

## Features

- **Blog Application**: Create, edit, and delete blog posts.
- **Personal Profile**: Display personal information and achievements.
- **Polls Application**: Vote on different questions.
- **Projects Section**: Showcase various projects with descriptions and links.
- **Sphinx Documentation**: Comprehensive project documentation available [here](https://wiidlucille247.github.io/django-portfolio).

## Quick Start
### Setting Up the Project

#### Using a Python Virtual Environment
1. **Create a virtual environment**:  
   python -m venv env

2. **Activate a virtual environment**:  
On MacOS and Linux:  
source env/bin/activate  
On Windows:  
env\Scripts\activate


3. **Install project dependencies**:  
pip install -r requirements.txt


### Running the Project with Docker

####  Running the Project using Docker Playground
1. **Visit Docker Playground:**
Go to [Docker Playground](https://labs.play-with-docker.com/)

2. **Start a New Instance:**
Click on the "Start" button to initiate a new instance.

3. **Create a New Session:**
Click on the "Add New Instance" button.

4. **Pull the Docker image:**
Run the following command in the Docker Playground terminal:
docker pull wiidlucille247/django_portfolio

5. **Run Docker Container:**
Start the following command in the Docker Playground terminal
docker run -p 8000:8000 wiidlucille247/django_portfolio

6. **Run Docker Container:**
Access the application.
Click on the "8000" link that appears in the terminal to access your running application in a new browser tab.


### Credits & Acknowledgements

Hyperiondev documentation used as part of the Software Engineernig Bootcamp.

Special thanks to my fellow mentor and colleague, Chris Smit, for providing guidance and mentorship especially getting me through 
Django, thank you, Chris! 

