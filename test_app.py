import pytest
import json
from app import app, create_items_table, delete_item_from_db

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        with app.app_context():
            create_items_table()  # Ensure the table exists
            yield client

def test_get_items_empty(client):
    # Test retrieving items when none exist
    response = client.get('/items')
    assert response.status_code == 200

def test_create_item(client):
    # Test creating a new item
    response = client.post('/items', 
                           data=json.dumps({'key': 'fruit', 'value': 'apple'}),
                           content_type='application/json')
    assert response.status_code == 201
    assert 'Item created successfully' in response.json['message']

def test_get_item(client):
    # Test retrieving an item that exists
    client.post('/items', 
                data=json.dumps({'key': 'fruit', 'value': 'apple'}),
                content_type='application/json')
    response = client.get('/items/fruit')
    assert response.status_code == 200
    assert response.json == ['fruit', 'apple']

def test_get_item_not_found(client):
    # Test retrieving an item that does not exist
    response = client.get('/items/vegetable')
    assert response.status_code == 404
    assert 'Item not found' in response.json['error']

def test_update_item(client):
    # Test updating an existing item
    client.post('/items', 
                data=json.dumps({'key': 'fruit', 'value': 'apple'}),
                content_type='application/json')
    response = client.put('/items/fruit', 
                          data=json.dumps({'value': 'banana'}),
                          content_type='application/json')
    assert response.status_code == 200
    assert 'Item updated successfully' in response.json['message']

def test_update_item_not_found(client):
    # Test updating an item that does not exist
    response = client.put('/items/vegetable', 
                          data=json.dumps({'value': 'carrot'}),
                          content_type='application/json')
    assert response.status_code == 404
    assert 'Item not found' in response.json['error']

def test_delete_item(client):
    # Test deleting an existing item
    client.post('/items', 
                data=json.dumps({'key': 'fruit', 'value': 'apple'}),
                content_type='application/json')
    response = client.delete('/items/fruit')
    assert response.status_code == 200
    assert 'Item deleted successfully' in response.json['message']

def test_delete_item_not_found(client):
    # Test deleting an item that does not exist
    response = client.delete('/items/vegetable')
    assert response.status_code == 404
    assert 'Item not found' in response.json['error']
