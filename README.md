# Data Collection Tool- Backend

This is a Django project that includes [list some main features of the project here].

## Installation

1. Fork and clone the repository to your local machine using the following command:
   ```bash:
   https://github.com/psalmuelle/Mboalab-Task_Django.git
   ```
2. Navigate to the project directory:
   ```bash:
   cd Mboalab-Task_Django
   ```
3. Create a virtual environment for the project:
   ```bash:
   pyton -m venv env
   ```
4. Activate the virtual environment:
   ```bash:
   source env/bin/activate
   ```
5. Install the required dependencies:
   ```bash:
   pip install -r requirements.txt
   ```
6. Change directory to `/hospitalist` and create the database and apply migrations:
   ```bash:
   python manage.py migrate
   ```
7. Create a superuser account:
   ```bash:
   python manage.py createsuperuser
   ```
8. Start the development server:
   ```bash:
   python manage.py runserver
   ```
9.

The application should now be running on [http://localhost:8000](http://localhost:8000). Open this URL in your web browser to view the app.

## API Usage

This Django project uses Django Rest Framework to provide an API. Here's an example of how to make an API request to one of the endpoints:

#### Endpoint 1

**GET Request**

To make a GET request to Endpoint 1, send a GET request to the following URL:

```bash:
http://localhost:8000/api/endpoint1/
```

**This will return a list of all the items in Endpoint 1.**

#### Endpoint 1

**POST Request**

To make a POST request to Endpoint 1, send a GET request to the following URL:

```bash:
http://localhost:8000/api/endpoint1/
```

The request should include a JSON payload in the following format:

```json:
{
    "field1": "value1",
    "field2": "value2",
    "field3": "value3"
}
```

Replace "field1": "value1", "field2": "value2", and "field3": "value3" with the actual values you want to send.

**This will create a new item in Endpoint 1.**
