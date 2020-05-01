## Things to correct

- 12factor guidelines
```
A.2. Some commits have an unclear name.
B.1. Not all dependencies in the requirements.txt file have been defined using: dep-name>=ma.mi.pa,<ma.mi.pa.
B.2. Not all config variables have been defined as a environment variable.
~~ C.1. There is no a proper development branch in the repository. ~~
```

- TravisCI
```
B.1. Deploy specification is not declared.
```

- Docker container
```
A.2. Not added a runner user as a security countermeasure.
A.3. Some great (but not mandatory) specifications are missing in the docker-compose.yml file like container_name, restart behavior, etc.
B.1. Some configuration in the docker-compose.yml file has not been setted using environment variables when was possible.
```

- Heroku
```
B.1. Not used gunicorn as a web server for production.
```

- Observations
```
You should separte models definitions from API queries.
```

# Spotifly

The topic of this project is about music. We will use the Spotify API to get information about the artists, to make a TOP 10 tracks and to create customized playlists.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

- Install python3
```
sudo apt-get update
sudo apt-get install python3
```

### Installing

A step by step series of examples that tell you how to get a development env running

Clone the repository and change to web-project directory
```
git clone https://github.com/Javigoo/web-project.git
cd web-project/
```

Activate the virtual environment using:
```
python3 -m venv venv
source venv/bin/activate
```

“requirements.txt” is a file containing a list of items to be installed using pip
install like so:
```
pip3 install -r requirements.txt
```

Apply a migration to tell Django what changes need to be made to the database
```
python3 manage.py migrate
```

Check if the install worked successfully running it
```
python3 manage.py runserver
```

We can deactivate the virtual environment typing:
```
deactivate
```

## Running the tests

To run the automated tests for this system use:
```
python3 manage.py test apps
```
The tests are also performed automatically with each commit.

## Deployment

Spotifly is deployed automatically on the master branch. It is available on Heroku, you can check it [here](https://spotiflyyy.herokuapp.com/).

To review the deployment settings in Heroku and Spotify for Developers contact us via [email](mailto:spotiflywebproject@gmail.com).

## Built With

* [Django](https://www.djangoproject.com/) - Web framework
* [Heroku](https://dashboard.heroku.com/) - Deploy platform

## Contributing

Make sure you have the latest version to avoid possible overwrites
```
git pull
```

Make sure everything works perfectly, for this you can run the server and see that everything is still in place
```
python3 manage.py runserver
```

Finally make the pull request

## Authors

* **Javier Roig Gregorio** - [Javigoo](https://github.com/Javigoo)
* **Jorge Nueno Abril** - [Jorgics](https://github.com/jorgics)
* **Gabriel Garcia Scoles** - [Gabygarcia98](https://github.com/gabygarcia98)
* **Jose Miguel Avellana Lopez** - [Jal04](https://github.com/jal04)
* **Víctor Alcobé Sorolla** - [Valcobe](https://github.com/valcobe)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
