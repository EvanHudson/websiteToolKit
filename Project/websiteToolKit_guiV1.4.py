#external libraries used Wapiti3, beautifulsoup, nmap, sqlmap, commix, selenium, XSStrike
#DVWA install https://www.geeksforgeeks.org/how-to-setup-dvwa-in-windows/
#https://www.geeksforgeeks.org/python-gui-tkinter/
#https://docs.python.org/3/library/tkinter.html
"""


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
import requests
import subprocess
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager  # Use GeckoDriverManager for Firefox

import socket


#################################################################MAIN CLASS##############
class WebsiteToolkitGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Website Security & Analysis Toolkit")
        self.root.geometry("500x500")

        ttk.Label(root, text="Website Toolkit", font=("Arial", 16)).pack(pady=10)

        self.url_entry = ttk.Entry(root, width=50)
        self.url_entry.pack(pady=5)
        self.url_entry.insert(0, "Enter website URL")
        self.url_entry.bind("<FocusIn>", self.clear_placeholder)
        self.url_entry.bind("<FocusOut>", self.restore_placeholder)

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
        ttk.Button(self.root, text="Analyze Website", command=self.analyze_website).pack(pady=5)
        ttk.Button(self.root, text="Pen Test Website", command=self.pen_test_website).pack(pady=5)
        ttk.Button(self.root, text="Port Scan", command=self.port_scan).pack(pady=5)
        ttk.Button(self.root, text="Complete Website Test", command=self.complete_website_test).pack(pady=5)

    def analyze_website(self):
        self.show_options("Analyze Website", ["SEO Analysis", "Security Scan", "Performance Test", "Total Analysis"])

    def pen_test_website(self):
        self.show_options("Pen Test Website", ["SQL Injection Test", "XSS Test", "CSRF Test", "Total Pen Test"])

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
        elif tool_name == "Security Scan":
            self.security_scan(url)
        elif tool_name == "Performance Test":
            self.performance_test(url)
        elif tool_name == "Total Analysis":
            self.total_analysis(url)
        elif tool_name == "SQL Injection Test":
            self.sql_injection_test(url)
        elif tool_name == "XSS Test":
            self.xss_test(url)
        elif tool_name == "CSRF Test":
            self.csrf_test(url)
        elif tool_name == "Total Pen Test":
            self.total_pen_test(url)

    def seo_analysis(self, url):
        """ Uses Selenium to extract SEO-related metadata dynamically. """
        self.driver.get(url)
        time.sleep(2)

        title = self.driver.title
        try:
            meta_desc = self.driver.find_element(By.NAME, "description").get_attribute("content")
        except:
            meta_desc = "No Meta Description Found"

        messagebox.showinfo("SEO Analysis", f"Website: {url}\nTitle: {title}\nMeta Description: {meta_desc}")

    def security_scan(self, url):
        """ Runs Wapiti3 for web vulnerability scanning. """
        command = f"wapiti -u {url} -m all"
        os.system(command)
        messagebox.showinfo("Security Scan", f"Completed security scan on {url}")

    def performance_test(self, url):
        start_time = time.time()
        response = requests.get(url, verify=False) #weak so disable SSL Damn VUlnerable sucks
        
        end_time = time.time()
        print(f"Response time: {end_time - start_time} seconds")

        messagebox.showinfo("Performance Test", f"Website: {url}\nStatus Code: {response.status_code}\nLoad Time: {end_time - start_time:.2f} seconds")

    def sql_injection_test(self, url):
        #uses SQL MAP
        command = ["sqlmap", "-u", url, "--crawl=2"]

        # Automated responses for terminal questions
        inputs = "N\nY\n5\n"

        try:
            process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output, error = process.communicate(inputs)

            
            print(output)

            messagebox.showinfo("SQL Injection Test", f"SQL Injection test completed on {url}")

        except Exception as e:
            messagebox.showerror("Error", f"SQL Injection test failed: {str(e)}")
    def xss_test(self, url):
        #XSStrike system call
        command = f"python XSStrike/xsstrike.py -u {url} --crawl --blind --log xss-log"
        os.system(command)
        messagebox.showinfo("XSS Test", f"XSS Test completed on {url}")
    def csrf_test(self, url):
        self.driver.get(url)
        time.sleep(2)

        try:
            form = self.driver.find_element(By.TAG_NAME, "form")
            submit_button = form.find_element(By.TAG_NAME, "input[type='submit']")
            submit_button.click()
            time.sleep(2)

            messagebox.showinfo("CSRF Test", "Form submitted. Check for CSRF vulnerabilities manually.")
        except:
            messagebox.showerror("Error", "No form detected for CSRF testing.")

    def port_scan(self):            #NO ONE TOUCH THIS I DONT EVEN KNOW HOW I GOT IT WORKING
        # using nmap
        url = self.url_entry.get()
        
        # Extract first part
        domain = url.split("//")[-1].split("/")[0]
        if domain.startswith("www."):
            domain = domain[4:]

        try:
            # make ip address to feed into nmap
            ip_address = socket.gethostbyname(domain)

            
            nmap_path = r"C:\Program Files (x86)\Nmap\nmap.exe"  

            
            command = [nmap_path, "-p-", "-T4", "-oN", "port_scan.txt", ip_address]
            
            
            result = subprocess.run(command, capture_output=True, text=True)
            
            messagebox.showinfo("Port Scan", f"Port scan completed on {ip_address}")
            
            # Print to console
            print(result.stdout)
            
            # Save the results to FIXME switch name to have url in it
            with open("port_scan_results.txt", "w") as f:
                f.write(result.stdout)

        except socket.gaierror as e:
            messagebox.showerror("Error", f"Unable to resolve IP address for {domain}: {e}")
        except Exception as e:
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

        # Run all tests
        self.seo_analysis(url)
        self.security_scan(url)
        self.performance_test(url)
        self.sql_injection_test(url)
        self.xss_test(url)
        self.csrf_test(url)
        self.port_scan()

        messagebox.showinfo("Complete Website Test", "All tests completed successfully!")

#########################################MAIN LOOP RUNNING GUI###########################
if __name__ == "__main__":
    root = tk.Tk()
    app = WebsiteToolkitGUI(root)
    root.mainloop()
