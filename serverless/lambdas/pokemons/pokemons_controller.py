import json
import boto3
import os
from datetime import datetime, timedelta
from boto3.dynamodb.conditions import Key
from tools.http_error import HTTPError
from tools.decimalencoder import DecimalEncoder
from aws_xray_sdk.core import patch

from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch

libraries = (['boto3'])
patch(libraries)


aws_region = os.environ.get('AWS_REGION')
pokemons_table = os.environ['POKEMONS_TABLE']

dynamodb = boto3.resource('dynamodb', region_name=aws_region)

dybamodb_pokemons_table = dynamodb.Table(pokemons_table)

def get_pokemon_by_id(data):
    try:
        response = dybamodb_pokemons_table.query(
            KeyConditionExpression=Key('id').eq(int(data["id"]))
        )
        return response["Items"]
    except Exception as e:
        raise HTTPError(500, 'Internal Error: %s' % e)

def get_pokemon_by_name(data):
    try:
        response = dybamodb_pokemons_table.query(
            IndexName='NameIndex',
            KeyConditionExpression=Key('name').eq(data["name"])
        )
        return response["Items"] 
    except Exception as e:
        raise HTTPError(500, 'Internal Error: %s' % e)

def post_pokemon(data):
    try:
        pokemon = {
            "id": int(data["id"]),
            "name": data["name"],
            "data":data["data"]
        }
        dybamodb_pokemons_table.put_item(Item=pokemon)

        response = {"Create": True}
        return response

    except Exception as e:
        raise HTTPError(500, "Internal Error: %s" % e)
