#CSC 440 Team02 project website analyzer tool kit

#external libraries used Wapiti3, beautifulsoup, nmap, sqlmap, selenium, XSStrike
#DVWA install https://www.geeksforgeeks.org/how-to-setup-dvwa-in-windows/
#https://www.geeksforgeeks.org/python-gui-tkinter/
#https://docs.python.org/3/library/tkinter.html



"""
if you want to run on your machine make sure to download nmap and move .exe here            
            C: Program Files (x86) Nmap nmap.exe
also make sure download firefox

also make sure download everything else in in same directory as websiteToolKit_gui.exe


# Install required Python libraries
pip install requests beautifulsoup4


# Install Nmap (Port Scanner)
Download from https://nmap.org/download.html and install manually
#https://nmap.org/download.html#windows download nmap then switch the file location to the location of the nmap.exe

# Install SQLMap
pip install sqlmap

# Install Wapiti3 (Web Vulnerability Scanner)
pip install wapiti3  
# Install Commix (XSS Testing)
git clone https://github.com/commixproject/commix.git
###################################TEAM 2 CSC440###########################
#pip install pyreadline
# pip install selenium
# pip install webdriver_manager
if get error that is missing anything else then do pip install something else name
#install firefox


git clone https://github.com/s0md3v/XSStrike.git
cd XSStrike
pip install -r requirements.txt



"""
##############################################################IMPORTS
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import simpledialog
import requests                 #for response time analysis and to see if goof website
import subprocess
import os                    #for system calls
import time               #for timming
from datetime import datetime   #for logging
from selenium import webdriver                  #for graphical display of current webpage in firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager  # Use GeckoDriverManager for Firefox

import socket
try:
    os.system("pip install sqlmap")
    os.system("pip install wapiti3")
    os.system("pip install pyreadline")
    os.system("pip install requests beautifulsoup4")
    os.system("pip install selenium")
    os.system("pip install webdriver_manager")
    os.system("cd XSStrike")
    os.system("pip install -r requirements.txt")
    os.system("cd ..")
except Exception as e:
    print(f"raised error {e}")
#################################################################MAIN CLASS##############
class WebsiteToolkitGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Website Analyzer Toolkit for EDUCATIONAL PURPOSES ONLY")
        self.root.geometry("500x500")
        self.dialogueBoxes = True   #so that can silence them during complete website test and dont have ti press ok every time
        ttk.Label(root, text="Website Analyzer Toolkit", font=("Arial", 16)).pack(pady=10)

        self.url_entry = ttk.Entry(root, width=50)
        self.url_entry.pack(pady=5)
        self.url_entry.insert(0, "Enter website URL")
        self.url_entry.bind("<FocusIn>", self.clear_placeholder)
        self.url_entry.bind("<FocusOut>", self.restore_placeholder)
        with open(f"WebsiteAnalysisToolKit.txt", "w") as f:
            f.write("                                                        Website Analysis Tool Kit by Team02\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        self.create_buttons()

        # Initialize Selenium WebDriver for Firefox
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))  # Use Firefox here

    def clear_placeholder(self, event):
        if self.url_entry.get() == "Enter website URL":
            self.url_entry.delete(0, tk.END)

    def restore_placeholder(self, event):
        if not self.url_entry.get():
            self.url_entry.insert(0, "Enter website URL")

    def create_buttons(self):
        ttk.Button(self.root, text="Less Intrusive Tests", command=self.analyze_website).pack(pady=5)
        ttk.Button(self.root, text="More Intrusive Tests", command=self.pen_test_website).pack(pady=5)
#        ttk.Button(self.root, text="Port Scan", command=self.port_scan).pack(pady=5)
        ttk.Button(self.root, text="Complete Website Test", command=self.complete_website_test).pack(pady=5)

    def analyze_website(self):
        self.show_options("Less Intrusive Tests", [ "Performance Test","SEO Analysis","CSRF Test"])

    def pen_test_website(self):
        self.show_options("More Intrusive Tests", ["Brute Force Login", "SQLmap Analysis", "XSStrike", "Nmap Port Scan", "Wapiti3 Security Scan"])

    def show_options(self, title, options):
        option_window = tk.Toplevel(self.root)
        option_window.title(title)
        option_window.geometry("300x250")

        ttk.Label(option_window, text=title, font=("Arial", 14)).pack(pady=10)

        for option in options:
            ttk.Button(option_window, text=option, command=lambda opt=option: self.run_tool(opt)).pack(pady=5)

    def run_tool(self, tool_name):
        url = self.url_entry.get()

        if tool_name == "SEO Analysis":
            self.seo_analysis(url)
        elif tool_name == "Wapiti3 Security Scan":
            self.security_scan(url)
        elif tool_name == "Performance Test":
            self.performance_test(url)
        elif tool_name == "Total Analysis":
            self.total_analysis(url)
        elif tool_name == "SQLmap Analysis":
            self.sql_injection_test(url)
        elif tool_name == "XSStrike":
            self.xss_test(url)
        elif tool_name == "Nmap Port Scan":
            self.port_scan(url)
        elif tool_name == "CSRF Test":    #move to less intrusive
            self.csrf_test(url)
        elif tool_name == "Total Pen Test":
            self.total_pen_test(url)
        elif tool_name == "Brute Force Login":
            self.bruteForceLogin(url)

    def seo_analysis(self, url):
        #Uses Selenium to extract SEO-related metadata dynamically
        self.driver.get(url)
        time.sleep(2)

        title = self.driver.title
        try:
            meta_desc = self.driver.find_element(By.NAME, "description").get_attribute("content")
        except:
            meta_desc = "No Meta Description Found"

        with open(f"WebsiteAnalysisToolKit.txt", "a") as f:
            f.write("\n\n\n                                                        SEO Analysis\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            f.write(f"Ran @ {datetime.now().strftime("%H:%M:%S")}\n")
            f.write(f"Website: {url}\nTitle: {title}")
            f.write(meta_desc)
            print("\nprinted selenium results to file\n")
        if self.dialogueBoxes:
            messagebox.showinfo("SEO Analysis", f"Website: {url}\nTitle: {title}\nMeta Description: {meta_desc}")
    def bruteForceLogin(self, url):
        #cutoms written tool that uses dictioary file for bruteforce login
        with open(f"WebsiteAnalysisToolKit.txt", "a") as f:
            f.write("\n\n\n                                                        Brute Force Login\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            f.write(f"Ran @ {datetime.now().strftime("%H:%M:%S")}\n")        
        userField = simpledialog.askstring("Input", "Enter the name of the username field:")
        passField = simpledialog.askstring("Input", "Enter the name of the password field:")
        logButtonField = simpledialog.askstring("Input", "Enter the name of the Login button:")

        wordlistOption = simpledialog.askstring("Input", "Would you like a comprehensive dictionary file (1) or a common list (2)? Enter 1 or 2:")
        # Load dictionary
        if(wordlistOption == "1"):
            dictionaryFile="dictionary.txt"
        else:
            dictionaryFile="test.txt"
        #with open("test.txt", 'r') as file:
        with open(dictionaryFile, 'r') as file:
            wordlist = [line.strip() for line in file]

        driver = webdriver.Firefox()

        try:
            for username in wordlist:
                for password in wordlist:
                    driver.get(url)  # Reload page for every attempt

                    wait = WebDriverWait(driver, 10)
                    username_field = wait.until(EC.presence_of_element_located((By.NAME, userField)))
                    password_field = driver.find_element(By.NAME, passField)

                    username_field.clear()
                    password_field.clear()

                    username_field.send_keys(username)
                    password_field.send_keys(password)

                    login_button = driver.find_element(By.NAME, logButtonField)
                    login_button.click()

                    time.sleep(1)  # Give time for loading

                    # If login successful URL will change
                    if "login" not in driver.current_url:
                        with open(f"WebsiteAnalysisToolKit.txt", "a") as f:
                            #f.write("\n\n\n                                                        SEO Analysis\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
                            #f.write(f"Ran @ {datetime.now().strftime("%H:%M:%S")}\n")
                            f.write(f"SUCCESS you hit the JACKPOT blue 42! Username: {username}, Password: {password}\n")
                            print("\nprinted bruteforce result to file\n")
                        print(f"SUCCESS you hit the JACKPOT blue 42! Username: {username}, Password: {password}")
                        break
                    else:
                        print(f"Failed: {username}:{password}")

        except Exception as e:
            print(f"Error: {e}")
    def security_scan(self, url):
        # Runs Wapiti3 for web vulnerability scanning
        #command = f"wapiti -u {url} -m all"
        #os.system(command)
        try:
            command = ["wapiti", "-u", url, "-m", "all"]
            #referenced https://stackoverflow.com/questions/10406532/python-subprocess-output-on-windows
            #refernced https://stackoverflow.com/questions/12605498/how-to-use-subprocess-popen-python
            with open("WebsiteAnalysisToolKit.txt", "a", encoding="utf-8") as f: #had issue with encoding utf-8 fixes
                process = subprocess.Popen(
                    command,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    bufsize=1
                )
                f.write("\n\n\n                                                        Wapiti3\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
                f.write(f"Ran @ {datetime.now().strftime("%H:%M:%S")}\n")
                for line in process.stdout:
                    print(line, end="")       # Print to console
                    f.write(line)       

                process.stdout.close()
                process.wait()
                f.write("finished Wapiti3 Scan")
        except KeyboardInterrupt:
            print("keyboard interupt so going to simpler scan")
            try:
                command = ["wapiti", "-u", url]
                #referenced https://stackoverflow.com/questions/10406532/python-subprocess-output-on-windows
                #refernced https://stackoverflow.com/questions/12605498/how-to-use-subprocess-popen-python
                with open("WebsiteAnalysisToolKit.txt", "a", encoding="utf-8") as f: #had issue with encoding utf-8 fixes
                    process = subprocess.Popen(
                        command,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True,
                        bufsize=1
                    )
                    f.write("\n\n\n                                                        Wapiti3\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
                    f.write(f"Ran @ {datetime.now().strftime("%H:%M:%S")}\n")
                    for line in process.stdout:
                        print(line, end="")       # Print to console
                        f.write(line)       

                    process.stdout.close()
                    process.wait()
                    f.write("finished Wapiti3 Scan")
            except Exception as e:
                  print("wapiti3 FAILED raised the error {e}")
        except Exception as e:
            print("wapiti3 FAILED raised the error {e}")
        """
        try:
          
            command = ["wapiti", "-u", url, "-m", "cookie_flags,blindsql,brute_login,csrf, xss"]  #all
            # put tripple start
            command = [
                "wapiti",
                "-u", url,
                "-m", "backup,blindsql,brute_login,command_exec,cookie_flags,crlf,csrf,exec,file_handling,fingerprints,htaccess,http_headers,methods,permanent_xss,redirect,shellshock,sql,xss",
                "--max-depth", "0",            # Don't crawl deeper
                "--max-links-per-page", "1",   # Don't follow links
                "--max-scan-time", "300"       # Max 5 min)
            ]

            #put tripple end
            #os.system(command[0]+command[1]+command[2]+command[3]+command[4]+command[5])
            print("Running wapiti3")
            result = subprocess.run(command, capture_output=True, text=True)
            
            messagebox.showinfo("Wapiti3 scan completed", f"Security Scan test completed on {url}")
            
            # Print to console
            print(result.stdout)
            
            # Save the results to FIXME switch name to have url in it
            with open(f"WebsiteAnalysisToolKit.txt", "a") as f:
                f.write("                                                        Wapiti3\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
                f.write(f"Ran @ {datetime.now().strftime("%H:%M:%S")}\n")
                f.write(result.stdout)
                print("\nprinted Wapiti3 results to file\n")
        except Exception as e:
            messagebox.showerror("Error", f"Wapiti3 Scan failed: {str(e)}")
        messagebox.showinfo("Security Scan", f"Completed security scan on {url}")
        """
    def performance_test(self, url):
        start_time = time.time()
        response = requests.get(url, verify=False) #weak so disable SSL Damn VUlnerable sucks
        
        end_time = time.time()
        print(f"Response time: {end_time - start_time} seconds")
        with open(f"WebsiteAnalysisToolKit.txt", "a") as f:
            f.write("\n\n\n                                                        Performance Test\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            f.write(f"Ran @ {datetime.now().strftime("%H:%M:%S")}\n")
            f.write(f"Website: {url}\nStatus Code: {response.status_code}\nLoad Time: {end_time - start_time:.2f} seconds")
            print("\nprinted performance test results to file\n")
        if self.dialogueBoxes:
            messagebox.showinfo("Performance Test", f"Website: {url}\nStatus Code: {response.status_code}\nLoad Time: {end_time - start_time:.2f} seconds")

#referenced https://stackoverflow.com/questions/10406532/python-subprocess-output-on-windows
#refernced https://stackoverflow.com/questions/12605498/how-to-use-subprocess-popen-python
    def sql_injection_test(self, url):
        #Uses SQLmap to perform SQL Injection testing on the given URL
        command = ["sqlmap", "-u", url, "--crawl=2"]

        
        automated_responses = [
            "Y\n",  
            "Y\n",  
            "5\n"   
        ]

        try:
            
            with open("WebsiteAnalysisToolKit.txt", "a", encoding="utf-8") as f:
                f.write("\n\n\n                                                        SQLmap\n")
                f.write("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
                f.write(f"Ran @ {datetime.now().strftime('%H:%M:%S')}\n")

                print("Starting SQLmap")

                # Start SQLmap
                process = subprocess.Popen(
                    command,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    stdin=subprocess.PIPE,
                    text=True,
                    bufsize=1
                )

                if not process:
                    print("Error: subprocess.Popen failed to start the process.")
                    return

                response_index = 0

                while True:
                    # check for a prompt
                    output = process.stdout.readline()
                    if output == '' and process.poll() is not None:
                        break

                    if output:
                        print(output.strip())  # Print to console
                        f.write(output)  

                        # looking for questions in out
                        if "Do you want to check for the existence of site's sitemap?" in output:
                            process.stdin.write(automated_responses[0])
                            process.stdin.flush()
                            print(f"Sent: {automated_responses[0].strip()}")

                        elif "Do you want to follow the redirect?" in output:
                            process.stdin.write(automated_responses[1])
                            process.stdin.flush()
                            print(f"Sent: {automated_responses[1].strip()}")

                        elif "Please enter number of threads?" in output:
                            process.stdin.write(automated_responses[2])
                            process.stdin.flush()
                            print(f"Sent: {automated_responses[2].strip()}")
                        time.sleep(.1)

                # Clean up subprocess streams
                process.stdout.close()
                process.stderr.close()
                process.stdin.close()
                process.wait()  # Wait for the process to finish

                f.write("finished SQL Injection test\n")

        except Exception as e:
            print(f"Error encountered: {str(e)}")
            if self.dialogueBoxes:
                messagebox.showerror("Error", f"SQL Injection test failed: {str(e)}")

        print("SQL map finished printed to file\n")

    
    def xss_test(self, url):
        #refrenced https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.youtube.com/watch%3Fv%3DyoGbw9bT-Zg&ved=2ahUKEwit77qTxPaMAxVHv4kEHQ7tM0MQtwJ6BAgKEAI&usg=AOvVaw02chEdaijYhGUoI5qdvcai
        #refrenced https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.youtube.com/watch%3Fv%3DoEFPFc36weY&ved=2ahUKEwit77qTxPaMAxVHv4kEHQ7tM0MQtwJ6BAgNEAI&usg=AOvVaw1w5F04Kk44F5q0noVaTHIv
        #refrenced https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.youtube.com/watch%3Fv%3DA9ZS5rtb_I0&ved=2ahUKEwit77qTxPaMAxVHv4kEHQ7tM0MQtwJ6BAgREAI&usg=AOvVaw2gOgu4uAyg1pdL8VMOVUP7
        #XSStrike system call
        #command = f"python XSStrike/xsstrike.py -u {url} --crawl --blind --log xss-log"
        #os.system(command)
        try:
          
            command = ["python", "XSStrike/xsstrike.py", "-u", url, "--crawl", "--blind", "--log", "xss-log"]
            #os.system(command[0]+command[1]+command[2]+command[3]+command[4]+command[5])
            print("Running XSStrike")
            result = subprocess.run(command, capture_output=True, text=True)
            if self.dialogueBoxes:
                messagebox.showinfo("XSStrike completed", f"XSStrike test completed on {url}")
            
            # Print to console
            print(result.stdout)
            
            # Save the results to FIXME switch name to have url in it
            with open(f"WebsiteAnalysisToolKit.txt", "a") as f:
                f.write("                                                        Xsstrike\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
                f.write(f"Ran @ {datetime.now().strftime("%H:%M:%S")}\n")
                f.write(result.stdout)
                print("\nprinted xss results to file\n")
        except Exception as e:
            if self.dialogueBoxes:
                messagebox.showerror("Error", f"xss test failed: {str(e)}")
        if self.dialogueBoxes:
            messagebox.showinfo("XSS Test", f"XSS Test completed on {url}")
    def csrf_test(self, url):
        self.driver.get(url)
        time.sleep(2)

        result=""

        try:
            form = self.driver.find_element(By.TAG_NAME, "form")
            submit_button = form.find_element(By.TAG_NAME, "input[type='submit']")
            submit_button.click()
            time.sleep(2)
            result="Form submitted. Check for CSRF vulnerabilities manually."
            if self.dialogueBoxes:
                messagebox.showinfo("CSRF Test", "Form submitted. Check for CSRF vulnerabilities manually.")
        except:
            result= "Error, No form detected for CSRF testing."
            if self.dialogueBoxes:
                messagebox.showerror("Error", "No form detected for CSRF testing.")
        with open(f"WebsiteAnalysisToolKit.txt", "a") as f:
            f.write("\n\n\n                                                        CSRF Test\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            f.write(f"Ran @ {datetime.now().strftime("%H:%M:%S")}\n")
            f.write(f"{result}")
            print("\nprinted csrf results to file\n")

    def port_scan(self,url):            #NO ONE TOUCH THIS I DONT EVEN KNOW HOW I GOT IT WORKING
        # using nmap
        #url = self.url_entry.get()
        
        # Extract first part
        domain = url.split("//")[-1].split("/")[0]
        if domain.startswith("www."):
            domain = domain[4:]

        try:
            # make ip address to feed into nmap
            ip_address = socket.gethostbyname(domain)

            #if you want to run on your machine make sure to download nmap and move it here            
            nmap_path = r"Nmap\nmap.exe"  

            
            command = [nmap_path, "-p-", "-T4", "-oN", "port_scan.txt", ip_address]
            #os.system(command[0]+command[1]+command[2]+command[3]+command[4]+command[5])
            
            result = subprocess.run(command, capture_output=True, text=True)
            if self.dialogueBoxes:
                messagebox.showinfo("Port Scan", f"Port scan completed on {ip_address}")
            
            # Print to console
            print(result.stdout)
            
            # Save the results to FIXME switch name to have url in it
            with open(f"WebsiteAnalysisToolKit.txt", "a") as f:
                f.write("\n\n\n                                                        Nmap Port Mapper\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
                f.write(f"Ran @ {datetime.now().strftime("%H:%M:%S")}\n")
                f.write(result.stdout)
                print("\nprinted nmap results to file\n")

        except socket.gaierror as e:
            if self.dialogueBoxes:
                messagebox.showerror("Error", f"Unable to resolve IP address for {domain}: {e}")
        except Exception as e:
            if self.dialogueBoxes:
                messagebox.showerror("Error", f"Port scan failed: {e}")

    def total_pen_test(self, url):
        self.sql_injection_test(url)
        self.xss_test(url)
        self.csrf_test(url)
        self.port_scan()
        messagebox.showinfo("Total Pen Test", "Full penetration test completed!")

    def close(self):
        self.driver.quit()

    def complete_website_test(self):
        url = self.url_entry.get()
        
        if url == "Enter website URL" or not url.strip():
            messagebox.showerror("Error", "Please enter a valid website URL.")
            return

        messagebox.showinfo("Complete Website Test", "Running full website analysis and penetration testing...")
        
        self.dialogueBoxes=False #turn off confirmation dialogue boxes
        
        # Run all tests
        self.seo_analysis(url)
        self.performance_test(url)
        self.csrf_test(url)
        self.port_scan(url)
        self.xss_test(url)
        self.security_scan(url)
        self.sql_injection_test(url)
        self.dialogueBoxes=True
        messagebox.showinfo("Complete Website Test", "All tests completed successfully!")

#########################################MAIN LOOP RUNNING GUI###########################
if __name__ == "__main__":
    root = tk.Tk()
    app = WebsiteToolkitGUI(root)
    root.mainloop()
