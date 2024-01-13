#This module provides a reusable byline for the author's services

import math
import statistics

company_name: str = "Toba Analytics Ltd."
company_address: str = "1 Ust Lane, Stonah, caldwell, Cal"
company_phone: str = "1-800-123-4567"
company_email: str = "tobd@adeyemi.com"
employee_count: int = 201
count_active_projects: int = 50
count_total_projects: int = 105
has_international_presence: bool = True
list_countries_we_work: int = ["USA", "Canada", "Germany", "Japan", "Australia"]
average_client_satisfaction: float = 4.5

services_offered: list = ["Machine Learning", "Business Intelligence", "Data Analysis", "Data Warehousing"]
satisfaction_scores: list = [4.3, 4.1, 3.9, 3.7, 4.6]

print(company_name)
print(company_address)
print(company_phone)
print(company_email)
print(employee_count)
print ('Services offered')
print(services_offered)

active_projects_string: str = f"Active Projects: {count_active_projects}"
international_presence_string: str = f"International Presence: {has_international_presence}"
countries_we_work: str = f"Countries We Work: {list_countries_we_work}"
client_satisfaction_string: str = f"Average Client Satisfaction: {average_client_satisfaction}"
services_offered: str = f"services_offered: {services_offered}"

smallest= min(satisfaction_scores)
largest= max(satisfaction_scores)
total= sum(satisfaction_scores)
count= len(satisfaction_scores)
mean= statistics.mean(satisfaction_scores)
mode= statistics.mode(satisfaction_scores)
median= statistics.median(satisfaction_scores)
standard_deviation=statistics.stdev(satisfaction_scores)

#calculate the average satisfaction score
average_satisfaction_score = statistics.mean(satisfaction_scores)

stats_string: str = f"""
Statistics for Client Satisfaction Scores:
  Smallest: {smallest}
  Largest: {largest}
  Total: {total}
  Count: {count}
  Mean: {mean}
  Mode: {mode}
  Median: {median}
  Standard Deviation: {standard_deviation}
"""

byline: str = f"""
{company_name}
{active_projects_string}
{international_presence_string}
{countries_we_work}
{client_satisfaction_string}
{stats_string}
"""

print(stats_string)
print("this is the smallest satisfaction scored by a client")
print(smallest)

print("this is the largest satisfaction scored by a client")
print(largest)

print(byline)

def main():
  ''' Display all output'''
  print(company_name)
  print(active_projects_string)
  print(international_presence_string)
  print(client_satisfaction_string)
  print(stats_string)
  print(byline)
