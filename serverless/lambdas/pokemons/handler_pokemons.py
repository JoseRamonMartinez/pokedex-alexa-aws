import json
import logging
import os
import time
import uuid
from tools.decimalencoder import DecimalEncoder
import boto3

from lambdas.pokemons.pokemons_controller import (
    get_pokemon_by_name,
    get_pokemon_by_id,
    post_pokemon
)

def h_get_pokemon_by_id(event, context):

    response = {
        "headers": {"Access-Control-Allow-Origin": "*"},
        "statusCode": 200,
        "body": None,
    }

    try:
        headers = event["headers"] if "headers" in event else None
        data = event["pathParameters"] if "pathParameters" in event else None

        result = get_pokemon_by_id(data)

        response.update({"body": json.dumps(result, cls=DecimalEncoder)})

    except Exception as e:
        print("> Error: %s" % e)
        response.update({"statusCode": 500, "body": "Internal Error: %s" % e})

    return response

def h_get_pokemon_by_name(event, context):

    response = {
        "headers": {"Access-Control-Allow-Origin": "*"},
        "statusCode": 200,
        "body": None,
    }

    try:
        headers = event["headers"] if "headers" in event else None
        data = event["pathParameters"] if "pathParameters" in event else None
            
        result = get_pokemon_by_name(data)

        response.update({"body": json.dumps(result, cls=DecimalEncoder)})

    except Exception as e:
        print("> Error: %s" % e)
        response.update({"statusCode": 500, "body": "Internal Error: %s" % e})

    return response

def h_post_pokemon(event, context):

    response = {
        "headers": {"Access-Control-Allow-Origin": "*"},
        "statusCode": 200,
        "body": None,
    }

    try:
        headers = event["headers"] if "headers" in event else None
        data = event["body"] if "body" in event else None
        
        data = json.loads(data) if data else None

        result = post_pokemon(data)

        response.update({"body": json.dumps(result)})

    except Exception as e:
        print("> Error: %s" % e)
        response.update({"statusCode": 500, "body": "Internal Error: %s" % e})

    return response