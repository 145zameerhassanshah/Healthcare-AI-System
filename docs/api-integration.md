# Introduction to APIs

## Objective

Understand how REST APIs allow applications to retrieve data from external services using HTTP requests and process JSON responses in Python.

## Python Environment

The API integration was developed and tested inside the project's isolated Python virtual environment:

```text
.venv/
## API Used

JSONPlaceholder was used as a public REST API for testing and learning purposes.

## Python Library

The `requests` library was used to communicate with the external API.

## GET Request Workflow

1. Define the API endpoint.
2. Send an HTTP GET request using `requests`.
3. Check the HTTP response status.
4. Convert the response to JSON.
5. Extract selected information from the JSON data.
6. Display the required fields.

## Concepts Implemented

- REST API
- API endpoint
- HTTP GET request
- HTTP response
- Status codes
- JSON data
- JSON parsing
- Path parameters
- Query parameters
- Selected-field extraction
- Request timeout
- Error checking with `raise_for_status()`

## REST Methods Reviewed

The implementation also demonstrates the basic REST methods:

- GET - retrieve data
- POST - create data
- PUT - replace/update data
- PATCH - partially update data
- DELETE - delete data

These additional methods were implemented for REST API practice beyond the core GET requirement.

## Result

Successfully retrieved user data from an external REST API using Python, converted the JSON response into Python data structures, and extracted selected user information such as ID, name, email, and city.