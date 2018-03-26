import sqlite3
import json

import click 
import requests

REST_END_POINT = 'https://country.register.gov.uk/records.json'

def british_data_for_country(c):
	pass

def save_data_to_sql_db(d):
	pass

def pretty_print_all_data_from_db():
	pass


@click.command()
@click.argument('country_name')
def our_program(country_name):
	country_data = british_data_for_country(country_name)
	was_persist_successful = save_data_to_sql_db(country_data)
	pretty_print_all_data_from_db()

if __name__ == '__main__':
	our_program()