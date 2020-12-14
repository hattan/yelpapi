#!/usr/bin/env python3

from yelpapi import YelpAPI
from pprint import pprint
import csv
import click
import os
from dotenv import load_dotenv
load_dotenv()

@click.command()
@click.option('--search', prompt='Search Term', help='what to search for')
@click.option('--location', prompt='Location', help='where to search')

def main(search, location):
    yelp_api = YelpAPI(os.getenv("YELP_API_KEY"))    
    outputFile=search + ".csv"    
    print("Searching Yelp for " + search + " in " + location) 
    response = yelp_api.search_query(term=search, location=location, sort_by='rating', limit=50)

    with open(outputFile, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for business in response["businesses"]:
            address = ' '.join(business['location']['display_address'])
            writer.writerow([business['name'],business['display_phone'],address, business['rating'],business['url'],business['review_count']])

    print("Complete! File " + outputFile + " created!")    

if __name__ == '__main__':
    main()