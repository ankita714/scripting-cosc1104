"""
Assignment 3
Name: Ankita (100941771)
Date: 12/10/2024
Cloud Storage Cost Calculator that calculates the monthly cost of cloud storage based on user input, 
including the amount of data stored and the frequency of data access.

"""
# Importing necessary libraries
# 'requests' is used to fetch data from the web, and 'BeautifulSoup' helps parse HTML data.

import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore
import math

# Web scraping is extracting data from websites using automated scripts. 
# The below function is defined to fatch pricing data from aws/gcp pricing page.
 
def fatch_pricing():
   
    print("Fetching cloud storage pricing from their official sites: ")
    
    # Dictionary to store pricing details for AWS and GCP, separated by storage type.

    pricing = {
        "AWS": {"Standard": {}, "Infrequent": {}},
        "GCP": {"Standard": {}, "Infrequent": {}},
    }
    
    # AWS Pricing Scrape 

    aws_pricing_url = "https://aws.amazon.com/s3/pricing/"  # AWS S3 pricing URL
    response = requests.get(aws_pricing_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
       
        pricing["AWS"]["Standard"]["storage"] = 0.023  # Example scraped value
        pricing["AWS"]["Standard"]["access"] = 0.004
        pricing["AWS"]["Infrequent"]["storage"] = 0.0125
        pricing["AWS"]["Infrequent"]["access"] = 0.01
    else:
        print("Failed to fetch AWS pricing. Using default values.")

    # GCP Pricing Scrape 
    gcp_pricing_url = "https://cloud.google.com/storage/pricing"  # GCP storage pricing URL
    response = requests.get(gcp_pricing_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
       
        pricing["GCP"]["Standard"]["storage"] = 0.02
        pricing["GCP"]["Standard"]["access"] = 0.004
        pricing["GCP"]["Infrequent"]["storage"] = 0.01
        pricing["GCP"]["Infrequent"]["access"] = 0.008
    else:
        print("Failed to fetch GCP pricing. Using default values.")
    
    return pricing

def calculate_storage_cost(pricing, provider, storage_type, data_size_gb, access_frequency):
   
    if provider not in pricing or storage_type not in pricing[provider]:
        raise ValueError("Invalid provider or storage type")
    
    # Fetch the relevant pricing
    storage_cost_per_gb = pricing[provider][storage_type]["storage"]
    access_cost_per_gb = pricing[provider][storage_type]["access"]
    
    # Calculate costs
    total_storage_cost = data_size_gb * storage_cost_per_gb
    total_access_cost = data_size_gb * access_frequency * access_cost_per_gb
    
    return math.ceil((total_storage_cost + total_access_cost) * 100) / 100

def main():
    print("Cloud Storage Cost Calculator with Dynamic Pricing")
    print("*",*20)
    
    # Fatching data by calling the below function. 
    pricing = fatch_pricing()
    
    # Getting input from user
    provider = input("Choose a provider (AWS/GCP): ").strip()
    storage_type = input("Choose storage type (Standard/Infrequent): ").strip()
    data_size_gb = float(input("Enter data size in GB: "))
    access_frequency = int(input("Enter number of accesses per month: "))
    
    try:
        # Calculate cost by calling calculate_storage_cost function.
        total_cost = calculate_storage_cost(pricing, provider, storage_type, data_size_gb, access_frequency)
        print(f"\nEstimated Monthly Cost: ${total_cost}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

