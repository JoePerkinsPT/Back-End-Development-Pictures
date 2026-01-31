import os
from pymongo import MongoClient

# Store client at module level so routes can import without circular dependency
mongodb_client = None

def init_db():
    global mongodb_client
    # Use IBM Cloud lab env vars if set, otherwise localhost for local dev
    mongodb_service = os.environ.get('MONGODB_SERVICE', '127.0.0.1')
    mongodb_port = os.environ.get('MONGODB_PORT', '27017')
    mongodb_username = os.environ.get('MONGODB_USERNAME')
    mongodb_password = os.environ.get('MONGODB_PASSWORD')

    if mongodb_username and mongodb_password:
        url = f"mongodb://{mongodb_username}:{mongodb_password}@{mongodb_service}:{mongodb_port}"
    else:
        url = f"mongodb://{mongodb_service}:{mongodb_port}"

    client = MongoClient(url)
    db = client.picturesdb
    db.pictures.drop()
    db.pictures.insert_many(
        [
            {
                "id": 1,
                "pic_url": "http://dummyimage.com/136x100.png/5fa2dd/ffffff",
                "event_country": "United States",
                "event_state": "District of Columbia",
                "event_city": "Washington",
                "event_date": "11/16/2022"
            },
            {
                "id": 2,
                "pic_url": "http://dummyimage.com/230x100.png/dddddd/000000",
                "event_country": "United States",
                "event_state": "Florida",
                "event_city": "Naples",
                "event_date": "11/2/2022"
            },
            {
                "id": 3,
                "pic_url": "http://dummyimage.com/123x100.png/5fa2dd/ffffff",
                "event_country": "United States",
                "event_state": "Ohio",
                "event_city": "Youngstown",
                "event_date": "7/11/2022"
            },
            {
                "id": 4,
                "pic_url": "http://dummyimage.com/175x100.png/dddddd/000000",
                "event_country": "United States",
                "event_state": "California",
                "event_city": "Anaheim",
                "event_date": "3/10/2022"
            },
            {
                "id": 5,
                "pic_url": "http://dummyimage.com/167x100.png/ff4444/ffffff",
                "event_country": "United States",
                "event_state": "New Jersey",
                "event_city": "Newark",
                "event_date": "12/25/2022"
            },
            {
                "id": 6,
                "pic_url": "http://dummyimage.com/232x100.png/5fa2dd/ffffff",
                "event_country": "United States",
                "event_state": "North Carolina",
                "event_city": "Charlotte",
                "event_date": "8/2/2022"
            },
            {
                "id": 7,
                "pic_url": "http://dummyimage.com/237x100.png/ff4444/ffffff",
                "event_country": "United States",
                "event_state": "Texas",
                "event_city": "San Antonio",
                "event_date": "4/1/2022"
            },
            {
                "id": 8,
                "pic_url": "http://dummyimage.com/152x100.png/cc0000/ffffff",
                "event_country": "United States",
                "event_state": "Florida",
                "event_city": "Orlando",
                "event_date": "7/12/2022"
            },
            {
                "id": 9,
                "pic_url": "http://dummyimage.com/188x100.png/ff4444/ffffff",
                "event_country": "United States",
                "event_state": "California",
                "event_city": "Los Angeles",
                "event_date": "8/6/2022"
            },
            {
                "id": 10,
                "pic_url": "http://dummyimage.com/187x100.png/5fa2dd/ffffff",
                "event_country": "United States",
                "event_state": "Florida",
                "event_city": "Miami Beach",
                "event_date": "11/19/2022"
            }
        ]
    )
    mongodb_client = client
    return client
