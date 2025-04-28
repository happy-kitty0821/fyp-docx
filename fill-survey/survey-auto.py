from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# -----------------------
# Configuration
# -----------------------

# Update with your chromedriver path
service = Service(executable_path=r'C:\Users\np05c\OneDrive\Documents\chromedriver-win64\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(service=service, options=options)

# URL of the form
form_url = 'https://forms.gle/NWQxig8cYuknWTDJ7'

# Nepali names (60 unique names)
names = [
    'Asmin', 'Trija', 'Suman', 'Bishal', 'Pratiksha', 'Binita', 'Manish', 'Anisha', 'Ravi', 'Apsara',
    'Shyam', 'Rajesh', 'Sita', 'Hari', 'Sanjay', 'Aarati', 'Maya', 'Ranjan', 'Sushil', 'Nisha',
    'Suman', 'Anil', 'Bina', 'Sushila', 'Poonam', 'Prakash', 'Sujan', 'Amit', 'Bishnu', 'Rita',
    'Jeevan', 'Dipesh', 'Nirajan', 'Srijan', 'Rohit', 'Shristi', 'Samir', 'Bikash', 'Kiran', 'Sunita',
    'Rohini', 'Nirupa', 'Rajani', 'Jeevika', 'Ujjwal', 'Arjun', 'Deepa', 'Rashmi', 'Madhav', 'Rohit',
    'Vikram', 'Sanjita', 'Madhuri', 'Chandra', 'Ganga', 'Pradeep', 'Suraj', 'Sabina', 'Krishna', 'Sushma'
]

# Nepali surnames (to choose randomly)
surnames = [
    'Bhandari', 'Sharma', 'Poudel', 'Gurung', 'Rai', 'Limbu', 'Magar', 'Thapa', 'Karki', 'Basnet',
    'Dahal', 'Khatri', 'Chhetri', 'Bista', 'Adhikari', 'Rana', 'Pandey', 'Joshi', 'Neupane', 'Koirala',
    'Acharya', 'Regmi', 'Gautam', 'Bhattarai', 'Dhakal', 'Lamichhane', 'Khanal', 'Panta', 'Rijal', 'Timalsina',
    'Sapkota', 'Subedi', 'Parajuli', 'Nepal', 'Khadka', 'Budhathoki', 'Giri', 'Puri', 'Bajracharya', 'Maharjan',
    'Shakya', 'Manandhar', 'Rajbhandari', 'Malla', 'Pradhan', 'Tandukar', 'Byanjankar', 'Dwadi', 'Silwal', 'Rimal'
]

# Rating options
rating_options = ['Excellent', 'Good', 'Fair', 'Poor']
binary_options = ['Yes, significantly', 'Yes, somewhat', 'No, not much', 'No, not at all']
importance_options = ['Extremely important', 'Important', 'Moderately important', 'Not important']

# Feature options
features = [
    'Real-time network traffic monitoring',
    'Customizable detection rules',
    'Deep packet inspection',
    'PCAP file analysis',
    'Visual network topology',
    'Web-based admin dashboard',
    'Scalability for high traffic',
    'Alerting and reporting system'
]

# Additional comments
comments = [
    'Great tool for network monitoring!',
    'Very useful for cybersecurity analysis.',
    'The dashboard could be more intuitive.',
    'Would love to see more detection rules.',
    'Excellent visualization features.',
    'The setup process was straightforward.',
    'Had some performance issues with large PCAP files.',
    'Very helpful for my network security class.',
    'The alerting system needs improvement.',
    'Overall a good NIDS solution.'
]

# -----------------------
# Helper Functions
# -----------------------

def wait_and_click(xpath, timeout=10):
    """Wait for element to be clickable and then click it"""
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()
    time.sleep(random.uniform(0.3, 0.7))

def wait_and_send_keys(xpath, text, timeout=10):
    """Wait for element to be visible and send keys"""
    element = WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.XPATH, xpath)))
    element.send_keys(text)
    time.sleep(random.uniform(0.3, 0.7))

def select_random_option(question_text, options):
    """Select a random option for a given question"""
    option = random.choice(options)
    xpath = f'//div[contains(text(), "{question_text}")]/ancestor::div[1]//div[contains(@data-value, "{option}")]/ancestor::div[@role="radio"]'
    wait_and_click(xpath)

def select_random_checkboxes(question_text, feature_list, min_select=3, max_select=6):
    """Select random checkboxes for features question"""
    num_to_select = random.randint(min_select, max_select)
    selected_features = random.sample(feature_list, num_to_select)
    
    xpath_base = f'//div[contains(text(), "{question_text}")]/ancestor::div[1]'
    
    for feature in selected_features:
        xpath = f'{xpath_base}//div[contains(text(), "{feature}")]/ancestor::div[@role="checkbox"]'
        wait_and_click(xpath)

# -----------------------
# Main Submission Function
# -----------------------

def submit_form():
    try:
        # Wait for form to load completely
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//div[@role="heading"]'))
        )
        
        # Fill Name
        full_name = f"{random.choice(names)} {random.choice(surnames)}"
        wait_and_send_keys('//input[@type="text"]', full_name)
        
        # Academic Year
        select_random_option("Academic Year", ['Year1', 'Year2', 'Year3', 'Other'])
        
        # Overall experience
        select_random_option("Overall, how would you rate your experience using VISTA?", rating_options)
        
        # Setup experience
        select_random_option("How easy was it to set up and start using VISTA?", rating_options)
        
        # Expectations met
        select_random_option("Did VISTA meet your expectations", ['Fully met', 'Mostly met', 'Somewhat met', 'Did not meet'])
        
        # Useful features
        select_random_checkboxes("Which VISTA features did you find most useful?", features)
        
        # Detection effectiveness
        select_random_option("How would you rate the effectiveness of VISTA's detection capabilities?", rating_options)
        
        # Customize detection rules
        select_random_option("How important was the ability to customize detection rules", importance_options)
        
        # PCAP analysis
        select_random_option("Did the PCAP file analysis help", ['Very helpful', 'Somewhat helpful', 'Not very helpful', 'Did not use this feature'])
        
        # Dashboard design
        select_random_option("How would you rate the design and usability of the web-based dashboard?", rating_options)
        
        # Visualization effectiveness
        select_random_option("Did the visualization of network topology", binary_options)
        
        # Dashboard intuitive
        select_random_option("Was the dashboard intuitive", ['Extremely intuitive', 'Somewhat intuitive', 'Neutral', 'Not very intuitive'])
        
        # Performance under load
        select_random_option("How would you rate VISTA's performance under different network loads?", rating_options)
        
        # Performance issues
        issues = random.choice(['None', 'Minor lag', 'Some crashes', 'Performance could be better'])
        wait_and_send_keys('//textarea', issues)
        
        # Additional features
        additional_features = random.choice([
            'More visualization options',
            'Better reporting tools',
            'Mobile app support',
            'Integration with other security tools'
        ])
        wait_and_send_keys('(//textarea)[2]', additional_features)
        
        # Comments
        wait_and_send_keys('(//textarea)[3]', random.choice(comments))
        
        # Submit the form
        wait_and_click('//span[text()="Submit"]')
        
        # Wait for confirmation
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(text(), "Your response has been recorded")]'))
        )
        
        print(f"Submission {i+1} completed successfully.")
        return True
        
    except Exception as e:
        print(f"Error in submission {i+1}: {str(e)}")
        return False

# -----------------------
# Start Submissions
# -----------------------

total_submissions = 60
successful_submissions = 0

for i in range(total_submissions):
    try:
        driver.get(form_url)
        if submit_form():
            successful_submissions += 1
        
        # Random delay between submissions (5-15 seconds)
        time.sleep(random.uniform(5, 15))
        
        # Clear cookies every 10 submissions
        if (i+1) % 10 == 0:
            driver.delete_all_cookies()
            time.sleep(2)
            
    except Exception as e:
        print(f"Fatal error in submission {i+1}: {str(e)}")
        # Try to recover by restarting the browser
        driver.quit()
        driver = webdriver.Chrome(service=service, options=options)
        time.sleep(5)

print(f"\nCompleted {successful_submissions} out of {total_submissions} submissions successfully.")

driver.quit()