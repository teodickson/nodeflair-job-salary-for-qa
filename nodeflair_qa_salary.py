import requests
from email import message
from datetime import datetime
from total_page_num import Page

the_page = Page()
pages = the_page.get_page_num()
base_art_location_url = "https://nodeflair.com/api/v2/salaries"
api_url_telegram = "https://api.telegram.org/bot2066670954:AAFo3w3TzPKg1y6rGrlhIOEkeuK55VAFGJE/sendMessage?chat_id=@__groupid__&text="
group_id = "demo_telegram_cowims"

def extract_data(page):
	query_params = "?page={}&user_submitted_only=false&positions%5B%5D=qa_engineer".format(page)
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
	final_url = base_art_location_url + query_params
	response = requests.get(final_url, headers=headers)
	extract_data_from_search_result(response)
	
def get_data_per_page():
    for page in range(pages):
        extract_data(page)

def extract_data_from_search_result(response):
    response_json = response.json()
    for salary_group in response_json["salaryGroups"]:
        avgSalary = salary_group["avgSalary"]
        if salary_group["avgSalary"] == "0":
            avgSalary = salary_group["salaryMin"] + " - " + salary_group["salaryMax"]

        message = "Company: {}, \nAverage Salary: {}, \nSeniority: {}, \nCount: {}".format(
            salary_group["company"]["companyname"], 
            avgSalary, 
            salary_group["seniority"],
            salary_group["verifiedCount"]
        )
        send_message_to_telegram(message)

def send_message_to_telegram(message):
	final_telegram_url = api_url_telegram.replace("__groupid__", group_id)
	final_telegram_url = final_telegram_url + message
	response = requests.get(final_telegram_url)
	print(response)

if __name__ == "__main__":
	get_data_per_page()