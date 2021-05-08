from selenium import webdriver as wd
import time
import json


class WyzantWebTester:
    def __init__(self):
        self.driver = wd.Firefox(executable_path="/path/to/geckodriver")

    def grab_tutoring_data(self):
        self.driver.get("https://www.wyzant.com/tutor/lessons")

        #populate username
        self.driver.find_element_by_css_selector('.sso-login-form > div:nth-child(2) > input:nth-child(2)').send_keys('your-username')

        #populate password
        self.driver.find_element_by_css_selector('.sso-login-form > div:nth-child(3) > input:nth-child(2)').send_keys('your-password')

        #click login
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div/div/div[8]/form/button').click()

        #wait for page to load (this is a hack, change later??)
        time.sleep(5)

        #click show all button
        self.driver.find_element_by_css_selector('#ctl00_ctl00_PageCPH_CenterColumnCPH_LessonDisplay1_btnShowAll').click()

        time.sleep(5)

        #select 100 per page
        self.driver.find_element_by_xpath('//*[@id="ctl00_ctl00_PageCPH_CenterColumnCPH_LessonDisplay1_ListViewSession_Pager_DDPageSize"]/option[text()=\'100\']').click()

        time.sleep(5)

        # We also want to account for if there are over 100 entries on the first page, then we want to click through
        # to the next page

        lesson_dates = []
        lesson_lengths = []
        lesson_earned = []
        students = []

        while True:

            for date in self.driver.find_elements_by_xpath('//*[@id="LessonsList"]/tbody/tr[*]/td[1]/span[1]/span[1]'):
                lesson_dates.append(date.text)

            for length in self.driver.find_elements_by_xpath('//*[@id="LessonsList"]/tbody/tr[*]/td[2]'):
                lesson_lengths.append(length.text)

            for earned in self.driver.find_elements_by_xpath('//*[@id="LessonsList"]/tbody/tr[*]/td[10]'):
                lesson_earned.append(earned.text)

            # Check if new student or returning student
            # May have to go to earliest page first, then start populating students into student dictionary from there ...
            for student in self.driver.find_elements_by_xpath('//*[@id="LessonsList"]/tbody/tr[*]/td[5]/span/a'):
                students.append(student.text)

            next_page_button_class = self.driver.find_element_by_xpath(
                '//*[@id="ctl00_ctl00_PageCPH_CenterColumnCPH_LessonDisplay1_ListViewSession_Pager_NextPageBTN"]').get_attribute(
                'class')

            if next_page_button_class == 'aspNetDisabled':
                break
            else:
                self.driver.find_element_by_xpath('//*[@id="ctl00_ctl00_PageCPH_CenterColumnCPH_LessonDisplay1_ListViewSession_Pager_NextPageBTN"]').click()
                time.sleep(5)

        self.driver.close()

        lesson_data = []

        for i in range(0, len(lesson_dates)):
            lesson_data.append({'date': lesson_dates[i],
                                'length': lesson_lengths[i],
                                'earned': lesson_earned[i],
                                'student': students[i]})

        print(lesson_data)

        with open("../notebooks/tutoring_data.txt", 'w') as outfile:
            json.dump(lesson_data, outfile)
