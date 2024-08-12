
# Flask Key-Value Store API

## Overview

This project is a simple Flask web application that provides a RESTful API for managing key-value pairs. The application allows you to create, read, update, and delete items stored in a SQLite database.

## Features

- **Create an item**: Add a new key-value pair to the database.
- **Retrieve all items**: Get a list of all key-value pairs stored in the database.
- **Retrieve a specific item**: Get the value associated with a specific key.
- **Update an item**: Modify the value associated with a specific key.
- **Delete an item**: Remove a key-value pair from the database.

## Setup

### Prerequisites

- Python 3.x
- Flask
- SQLite3

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install Flask
    ```

4. **Run the application:**

    ```bash
    python app.py
    ```

5. **Access the API:**

    Open your web browser or API client (like Postman) and go to `http://127.0.0.1:5001`.

## API Endpoints

### 1. Get All Items

- **Endpoint**: `/items`
- **Method**: `GET`
- **Description**: Retrieve all key-value pairs stored in the database.
- **Response**:
  - `200 OK`: Returns a JSON array of all items.
  
  **Example Response**:
  ```json
  [
      ["example_key", "value 1"],
      ["another_key", "value 2"]
  ]
  ```

### 2. Get Item by Key

- **Endpoint**: `/items/<key>`
- **Method**: `GET`
- **Description**: Retrieve the value associated with a specific key.
- **Path Parameter**: 
  - `key` (string): The key of the item to retrieve.
- **Response**:
  - `200 OK`: Returns the key-value pair as a JSON array.
  - `404 Not Found`: If the key does not exist.
  
  **Example Response**:
  ```json
  ["example_key", "value 1"]
  ```

### 3. Create a New Item

- **Endpoint**: `/items`
- **Method**: `POST`
- **Description**: Create a new key-value pair in the database.
- **Request Body**:
  - JSON object with `key` and `value`.
  
  **Example Request Body**:
  ```json
  {
      "key": "example_key",
      "value": "value 1"
  }
  ```
- **Response**:
  - `201 Created`: Returns a success message.
  - `400 Bad Request`: If the key or value is missing.

### 4. Update an Item

- **Endpoint**: `/items/<key>`
- **Method**: `PUT`
- **Description**: Update the value of an existing key in the database.
- **Path Parameter**:
  - `key` (string): The key of the item to update.
- **Request Body**:
  - JSON object with the new `value`.
  
  **Example Request Body**:
  ```json
  {
      "value": "new value"
  }
  ```
- **Response**:
  - `200 OK`: Returns a success message.
  - `400 Bad Request`: If the value is missing.
  - `404 Not Found`: If the key does not exist.

### 5. Delete an Item

- **Endpoint**: `/items/<key>`
- **Method**: `DELETE`
- **Description**: Delete a specific key-value pair from the database.
- **Path Parameter**:
  - `key` (string): The key of the item to delete.
- **Response**:
  - `200 OK`: Returns a success message.
  - `404 Not Found`: If the key does not exist.

## Functions

### `create_items_table()`
- **Description**: Creates the `items` table in the database if it doesn't already exist. This table stores key-value pairs.

### `get_all_items_from_db()`
- **Description**: Fetches all key-value pairs from the `items` table in the database.

### `get_item_from_db(key)`
- **Description**: Fetches a specific key-value pair from the `items` table based on the provided key.

### `create_item_in_db(key, value)`
- **Description**: Inserts a new key-value pair into the `items` table.

### `update_item_in_db(key, value)`
- **Description**: Updates the value of an existing key in the `items` table.

### `delete_item_from_db(key)`
- **Description**: Deletes a key-value pair from the `items` table based on the provided key.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
