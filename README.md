Product Management System web app (Full Stack Frameworks with Django Project)

> > > This is a full stack web application (frontend and backend) that provides CRUD (Create, Read, Update, Delete) functionality to a database hosted in the cloud on Heroku platform as a service.

<img src="https://res.cloudinary.com/chuksmbanaso/image/upload/v1637340838/media/Product/Screenshot_16_bzgmp0.png" title="Product Management System Django" alt="Chuks Product Website">

<img src="https://res.cloudinary.com/chuksmbanaso/image/upload/v1637340937/media/Product/Screenshot_17_nbx6s6.png" title="Product Management System Django" alt="Chuks Product Website">

<img src="https://res.cloudinary.com/chuksmbanaso/image/upload/v1637341085/media/Product/Screenshot_15_s2xvji.png" title="Product Management System Django" alt="Chuks Product Website">

<img src="https://res.cloudinary.com/chuksmbanaso/image/upload/v1637341207/media/Product/Screenshot_18_ixwmad.png" title="Product Management System Django" alt="Chuks Product Website">


## Features

-View list of all the available products and make a pdf copy of the available products at the store.

-Add New Products to the website.

-cart system where users can choose items and get the total amount for the product

-Comment on existing products and choose whether to email the admin on the type of product he/she wants.

## Built With

- [Python 3](https://www.python.org/) - Programming language that lets you work quickly and integrate systems more effectively

- [Javascript](https://www.javascript.com) - It is a text-based programming language used both on the client-side and server-side that allows you to make web pages interactive.

- [Django](https://www.djangoproject.com/) - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design

- [Cloudinary](https://cloudinary.com/) - Cloudinary provides a secure and comprehensive API for easily uploading media files from server-side code, directly from the browser or from a mobile application.

- [PostgreSQL](https://www.postgresql.org/) - Object-relational database management system (ORDBMS) with an emphasis on extensibility and standards

- [Bootstrap](https://getbootstrap.com/) - Open source toolkit for developing with HTML, CSS, and JS

- [xhtml2pdf](https://pypi.org/project/xhtml2pdf/)- xhtml2pdf is a HTML to PDF converter using Python, the ReportLab Toolkit, html5lib and PyPDF2

- [Html and Css]

## Tools, libraries and resources used:

- [Pillow](https://pillow.readthedocs.io/en/5.3.x/) - Pillow is the friendly PIL fork. PIL is the Python Imaging Library

- [FontAwesome](https://fontawesome.com/)

- [PgAdmin](https://www.pgadmin.org/) - Open Source administration and development platform for PostgreSQL

## Getting started

-Clone the repo and cd into the project directory.

-Ensure you have Python 3 and Postgres installed and create a virtual environment and activate it.

-Install dependencies: pip3 install -r requirements.txt.

## Deployment

-Make sure requirements.txt and Procfile exist pip3 freeze --local requirements.txt echo web: python app.py > Procfile

-Create Heroku App, Select Postgres add-on, download Heroku CLI toolbelt, login to heroku (Heroku login), git init, connect git to heroku (heroku git remote -a ), git add ., git commit, git push heroku master.

-heroku run bash

-ls

-python manage.py migrate

-python manage.py create superuser

-heroku login
