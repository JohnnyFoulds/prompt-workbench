# backend/services/database.py
import weaviate
import uuid
from typing import List, Optional

def get_client():
    client = weaviate.connect_to_embedded()
    client.connect()
    return client

