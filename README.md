# python_flask_blueprint_based_restapi

## Author

**Kanak Sachan**

## Date 2024-05-18

## Requirements

- Python 3.x
- Flask 3.0.3
- Other dependencies as listed below

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/kanak152/python_flask_Blueprint.git
   cd python_flask_Blueprint
   ```

2. **Create a virtual environment:**

   ```sh
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:

     ```sh
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```sh
     source venv/bin/activate
     ```

4. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

## Dependencies

- **blinker 1.8.2**: Provides fast, simple object-to-object and broadcast signaling.
- **click 8.1.7**: A package for creating command line interfaces.
- **colorama 0.4.6**: Cross-platform colored terminal text.
- **Flask 3.0.3**: A microframework for Python based on Werkzeug and Jinja2.
- **importlib_metadata 7.1.0**: A library to access the metadata for a Python package.
- **itsdangerous 2.2.0**: A package for data signing.
- **Jinja2 3.1.4**: A template engine for Python.
- **MarkupSafe 2.1.5**: A library for safe string handling.
- **pip 24.0**: The package installer for Python.
- **setuptools 41.2.0**: A package development and distribution library.
- **Werkzeug 3.0.3**: A comprehensive WSGI web application library.
- **zipp 3.18.2**: A backport of pathlib-compatible object wrapper for zip files.

## Running the Application

1. **Start the Flask application:**

   ```sh
   python app.py
   ```

2. **Access the application:**

   Open your web browser and navigate to `http://127.0.0.1:5000` to see the home page.

## API Endpoints

- **GET /api/items**: Retrieve a list of items.
- **GET /api/items/<int:item_id>**: Retrieve a specific item by its ID.
- **POST /api/items**: Create a new item. Provide a JSON body with `name` and `description` fields.

## Sample Data

The application uses a sample dataset to simulate a database, which is defined in `app.py`.

```python
sample_data = [    {"id": 1, "name": "Item 1", "description": "This is item 1"},    {"id": 2, "name": "Item 2", "description": "This is item 2"},    {"id": 3, "name": "Item 3", "description": "This is item 3"},]

```

# Flask Blueprint structure Explanation

## Description

A basic definition of Flask Blueprint. In Flask, Blueprints are a way to organize your application into smaller and reusable modules. They help you structure your app by grouping related routes and functions together. This is especially useful for large applications.

## Why Use Blueprints?

- **Modularity**: Allows you to break your application into smaller, manageable pieces.
- **Reusability**: Blueprints can be reused across different projects.
- **Organization**: Helps keep your codebase organized and clean.

## Project Structure

my_flask_app/
├── app.py
├── application/
│ ├── init.py
│ ├── routes.py
└── templates/
└── index.html

## Explanation

### `application/__init__.py`

- Create a Blueprint named `application`.
- Import the routes from the `routes.py` file within the `application` package.

### `application/routes.py`

- Define a route for the home page using the `application` Blueprint.
- The route renders the `index.html` template.

### `templates/index.html`

- Simple HTML file that will be rendered when accessing the home page.

### `app.py`

- Create the Flask application instance.
- Register the `application` Blueprint with the Flask app.
- Run the app, making it accessible from any IP address on port 5000.
