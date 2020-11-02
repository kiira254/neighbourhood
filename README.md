# neighbourhood
  https://hood-app.herokuapp.com/
# Description  
This project allows users to post their hood, posts, police stations and businesses around their neighbourhood

## User Story  
  
* A user can view different neighbourhoods  
* A user can post their neighbourhood   
* Search for businesses  
* A user can write a post for other users to see
* A user can view their profile page. 
* A user can add a business name that is near the neigbourhood 
  
  
## Setup and installations

#### Prerequisites

1. [Python3.6](https://www.python.org/downloads/)
2. [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
3. [Pip](https://pip.pypa.io/en/stable/installing/)
4. [Postgres](https://www.postgresql.org/download/)
5. Python3.6
6. Ubuntu Software

#### Technologies used

    - Python 3.6
    - HTML
    - Bootstrap 4
    - Heroku
    - Postgresql
    - Django

#### Clone the Repo and rename it to suit your needs.

```bash
git clone https://github.com/kiira254/neighbourhood.git
```

#### Initialize git and add the remote repository

```bash
git init
```

```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment

```bash
python3.6 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables

Create a `.env` file and paste paste the following filling where appropriate:

```
SECRET_KEY='342s(s(!hsjd998sde8$=o4$3m!(o+kce2^97kp6#ujhi'
DEBUG=True #set to false in production
DB_NAME='instagram'
DB_USER='user'
DB_PASSWORD='password'
DB_HOST='127.0.0.1'
MODE='dev' #set to 'prod' in production
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
DISABLE_COLLECTSTATIC=1
```

#### Install dependancies

Install dependancies that will create an environment for the app to run

```bash
pip install -r requirements.txt
```

#### Run initial Migration

```bash
python3.6 manage.py migrate
```

#### Run the app

```bash
python3.6 manage.py runserver
```

#### Access the application through localhost:8000

Open [localhost:8000](http://127.0.0.1:8000/)

## Contributing

Please read this [comprehensive guide](https://opensource.guide/how-to-contribute/) on how to contribute. Pull requests are welcome :-)

## Bugs

Create an issue mentioning the bug you have found

#### Known bugs

- N/A

## Support and contact details

Contact [Nelly Kamotho](nkamotho69@gmail.com) for further help/support

### License

[MIT](/license)

Copyright (c)2019 **Nelly kamotho**
