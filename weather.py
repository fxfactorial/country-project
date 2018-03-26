import sqlite3
import json

import click 
import requests

@click.command()
@click.argument('city_name')
def our_program(city_name):
	print(city_name)

if __name__ == '__main__':
	our_program()