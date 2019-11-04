from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

#while True:

class baidu_login():


	def __init__(self,usern,passw):
		self.username = usern
		self.password = passw

	def action(self):
		browser = webdriver.Chrome()
		browser.get('https://www.baidu.com')

		# define all the locater
		Login_but_locater = "a[name='tj_login']"
		Username_Login_but_locater = "p#TANGRAM__PSP_10__footerULoginBtn"
		Username_Input_locater = "input[name='userName']"
		Password_Input_locater = "input[name='password']"
		Login_but2_locater = "input[id='TANGRAM__PSP_10__submit']"




		Login_but = browser.find_elements_by_css_selector(Login_but_locater)[1]
		#Login_but = browser.find_elements_by_css_selector('div[id=u1] a[class=lb]')[0]

		Login_but.click()

		WebDriverWait(browser,20).until(lambda x:x.find_elements_by_css_selector(Username_Login_but_locater))

		Username_Login_but = browser.find_elements_by_css_selector(Username_Login_but_locater)[0]
		Username_Login_but.click()

		WebDriverWait(browser,20).until(lambda x:x.find_elements_by_css_selector(Username_Input_locater))

		Username_Input = browser.find_elements_by_css_selector(Username_Input_locater)[0]

		Username_Input.send_keys(self.username)

		Password_Input = browser.find_elements_by_css_selector(Password_Input_locater)[0]

		Password_Input.send_keys(self.password)

		Login_but2 = browser.find_elements_by_css_selector(Login_but2_locater)[0]
		Login_but2.submit()







def endof():
	while True:
		exit_input=input('please enter "exit" to exit the program,or "restart" to restart')

		if exit_input == "exit" or exit_input == "restart":
			global endpara
			endpara = exit_input
			break
		else:
			continue


#	endof()

#	if endpara == "exit":
#		break
#	elif endpara == "restart":
#		continue