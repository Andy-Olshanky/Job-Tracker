import time
from bs4 import BeautifulSoup
import requests
from contact import send_email


def jobs():
    # send_email('Server', 'Server started', 'aolshans@temple.edu')
    URLS = [
        'https://www.lyft.com/careers/early-talent',
        'https://www.snap.com/en-US/jobs?types=Intern',
        'https://careers.google.com/jobs/results/?category=DATA_CENTER_OPERATIONS&category=DEVELOPER_RELATIONS&category=HARDWARE_ENGINEERING&category=INFORMATION_TECHNOLOGY&category=MANUFACTURING_SUPPLY_CHAIN&category=NETWORK_ENGINEERING&category=SOFTWARE_ENGINEERING&category=TECHNICAL_INFRASTRUCTURE_ENGINEERING&category=TECHNICAL_SOLUTIONS&category=TECHNICAL_WRITING&company=Fitbit&company=Google&company=Google%20Fiber&company=Loon&company=Verily%20Life%20Sciences&company=Waymo&company=Wing&company=X&company=YouTube&distance=50&employment_type=INTERN&has_remote=true&jlo=en_US&location=',
        'https://www.uber.com/us/en/careers/list/?department=University&team=Engineering&location=USA--Remote',
        'https://www.metacareers.com/careerprograms/students/?p[teams][0]=Internship%20-%20Engineering%2C%20Tech%20%26%20Design&p[teams][1]=Internship%20-%20Business&p[teams][2]=Internship%20-%20PhD&p[teams][3]=University%20Grad%20-%20PhD%20%26%20Postdoc&p[teams][4]=University%20Grad%20-%20Engineering%2C%20Tech%20%26%20Design&p[teams][5]=University%20Grad%20-%20Business&teams[0]=Internship%20-%20Engineering%2C%20Tech%20%26%20Design&teams[1]=Internship%20-%20Business&teams[2]=Internship%20-%20PhD&teams[3]=University%20Grad%20-%20PhD%20%26%20Postdoc&teams[4]=University%20Grad%20-%20Engineering%2C%20Tech%20%26%20Design&teams[5]=University%20Grad%20-%20Business&roles[0]=intern&offices[0]=Remote%2C%20US&offices[1]=Remote%2C%20Canada#openpositions'
    ]
    finds = [
        ['span', 'sc-cx1xxi-0 fAFtUC'],
        ['section', 'EmptyContainer-sc-6dwi2l hunthY'],
        ['div', 'wrapper__maincol'],
        ['div', 'bn bo mw mx fa my mz n0'],
        ['div', '_6b80']
    ]
    searches = [
        'Sorry, no jobs were found for that criteria.',
        'No results found for the selected filters.',
        'No results.',
        'No available jobs for that query.',
        'There are currently no open opportunities, please check back soon!'
    ]
    available = [False for _ in range(len(URLS))]
    done = False
    while not done:
        for i in range(len(URLS) - 1):
            if not available[i]:
                # print(i)
                found = False
                html_text = requests.get(URLS[i]).text
                soup = BeautifulSoup(html_text, 'lxml')
                # print(html_text)
                if finds[i][1] == '':
                    repos = soup.find_all(finds[i][0])
                else:
                    repos = soup.find_all(finds[i][0], class_=finds[i][1])
                # print(repos)
                for repo in repos:
                    if searches[i] in repo:
                        found = True
                        break

                if not found:
                    available[i] = True
                    # print('didnt find', i)
                    send_email('GO APPLY TO JOBS!', 'Job opening at ' + URLS[i], 'aolshans@temple.edu')

                time.sleep(1)

        done = is_done(available)
        # print('cycle')
        if not done:
            time.sleep(30)



def is_done(arr):
    for b in arr:
        if not b:
            return False
    return True


