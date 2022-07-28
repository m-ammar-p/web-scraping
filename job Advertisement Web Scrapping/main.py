import time

from bs4 import BeautifulSoup
import requests

print("put some skill that you are not familier with")
unfamiliar_skill = input('>')

print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    soup = BeautifulSoup(html_text, 'html.parser')

    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    # allows index in list
    for index, job in enumerate(jobs):
        # accessing span inside span
        published_date = job.find('span', class_='sim-posted').span.text

        if 'few' in published_date:

            # replace white spaces to no spaces
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')

            skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')

            # to get only link from 'a' tag of href element
            more_info = job.header.h2.a['href']

            # filter out unfamiliar skills should not be in skilss
            if unfamiliar_skill not in skills:
                # f variable to write into file
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More Info: {more_info}")
                print(f'File Saved: {index}')
                # print("========================")


if __name__ == '__main__':
    while True:
        find_jobs()
        # for 10 minutes
        tim_wait = 10
        print(f'Wating {tim_wait} Minutes...')
        # in milliseconds
        time.sleep(tim_wait * 60)