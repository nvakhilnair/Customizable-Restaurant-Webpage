
# Customizable Restaurant Webpage

This is fully customizable webpage for resturants. All fields can be easily customized from the admin panel.
This is achieved by connecting the front-end fields directly to the database.

Template: https://www.free-css.com/free-css-templates/page252/live-dinner


## Installation

Installation of required python libraries

```bash
  pip install -r requirement.txt
```

## Run Locally

1. Make the changes for your database in **./django_mysql/settings.py**

2. Manually create a scheme in your database using SQL command below 
```bash
  CREATE SCHEMA `Restaurant` ;
```
3. Make migrations
```bash
  python manage.py makemigrations
```
4. Migrate
```bash
  python manage.py migrate
```
5. Create Superuser to access the admin panel
```bash
  python manage.py createsuperuser
```
6. To run this project run the following command in downloaded directory
```bash
  python manage.py runserver 127.0.0.1:9000
```


## Features

- Simple and easily  customizable
- Responsive and Fast
- Cross platform
- Easy maintenance


## Tech Stack

**Client:** HTML, CSS, Javascript

**Server:** Python, Django, Mysql , Ajax




## License

[MIT](https://choosealicense.com/licenses/mit/)


## Feedback

If you have any feedback, please reach out to us at madewithpy009@gmail.com

For support, email madewithpy009@gmail.com.## 🚀 About Me
- 👋 Hi, I’m @nvakhilnair
- 👀 I’m interested in Data Science,Machine learning, Data Mining, Data Visualization and Programing
- 🌱 I’m currently open to work
- 📫 How to reach me https://www.linkedin.com/in/akhilnvnair
## Authors

- [@nvakhilnair](https://github.com/nvakhilnair)
