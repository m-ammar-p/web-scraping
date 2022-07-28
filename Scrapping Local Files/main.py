from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'html.parser')

    # find by html tags
    # courses_html_tags = soup.find_all('h1')
    # for course in courses_html_tags:
    #     print(course.text)

    course_cards = soup.find_all('div', class_='card')

    for course in course_cards:
        course_name = course.h1.text
        # splitting price sentence to only price to show from last (Accessing last word)
        course_price = course.a.text.split()[-1]
        print(f'{course_name} cost {course_price}')




