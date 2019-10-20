from selenium import webdriver




while True:
	# Open Chrome and get to the page
	web_browser = webdriver.Chrome()
	web_browser.get("https://techstepacademy.com/trial-of-the-stones")

	# All the variables here
	ROS_locater = 'input[id="r1Input"]'
	ROS_input="rock"
	ROSB_locater = 'button[id="r1Btn"]'

	ROS2_input = "div#passwordBanner > h4"
	ROS2_locater = "input[id='r2Input']"
	ROS2B_locater = 'button[id="r2Butn"]'

	Jessica_locater = '//b[text()="Jessica"]/../../p'
	Bernard_locater = '//b[text()="Bernard"]/../../p'
	#define the assignt_TTM_input function and global TTM_input variable here, and it will be used after we define the RichestMec function
	def assign_TTM_input():
		global TTM_input
		TTM_input = RichestMec(Value_Dic)

	TTM_locater = '//input[@id="r3Input"]'
	TTMB_locater = '//button[@id="r3Butn"]'


	CheckAnswers_locater = '//button[@id="checkButn"]'
	Answer_locater = '//div[@id="trialCompleteBanner"]/h4'





	


	# First part, Riidle of Stone
	RiddleOfStone = web_browser.find_element_by_css_selector(ROS_locater)
	RiddleOfStone.send_keys(ROS_input)

	RiddleOfStoneButton = web_browser.find_element_by_css_selector(ROSB_locater)	
	RiddleOfStoneButton.click()

	RiddeofStoneAnswer = web_browser.find_element_by_css_selector(ROS2_input)




	# Second Part Riddle of Secret
	RiddleofSecret = web_browser.find_element_by_css_selector(ROS2_locater)
	RiddleofSecretButton = web_browser.find_element_by_css_selector(ROS2B_locater)

	Secret = web_browser.find_element_by_css_selector(ROS2_input).text

	RiddleofSecret.send_keys(Secret)
	RiddleofSecretButton.click()





	#Third part, The Two Merchants

	Value_Dic = {}
	
	Jessica_Value = web_browser.find_element_by_xpath(Jessica_locater).text
	Value_Dic["Jessica"] = int(Jessica_Value)

	Bernard_Value = web_browser.find_element_by_xpath(Bernard_locater).text
	Value_Dic["Bernard"] = int(Bernard_Value)

	def RichestMec(lname):
		initial_value = 0
		for i in Value_Dic:
			if initial_value < lname[i]:
				initial_value = lname[i]
				Richest = str(i)
			else:
				continue


		return (Richest)

	#TTM_input = RichestMec(Value_Dic)

	assign_TTM_input()
	TTM = web_browser.find_element_by_xpath(TTM_locater)
	TTM.send_keys(TTM_input)
	TTMB = web_browser.find_element_by_xpath(TTMB_locater)
	TTMB.click()



	#Last part, assertion
	Check_Answer = web_browser.find_element_by_xpath(CheckAnswers_locater)
	Check_Answer.click()

	Answers_Result = web_browser.find_element_by_xpath(Answer_locater)
	Result = Answers_Result.text

	assert Result == "Trial Complete", "Error: Result Failed"




	




	end_input=input("Press exit to exit")
	if end_input == "exit":
		break
	else:
		web_browser.close()
		continue
