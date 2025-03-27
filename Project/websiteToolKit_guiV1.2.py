#external libraries used Wapiti3, beautifulsoup, nmap, sqlmap, commix
#DVWA install https://www.geeksforgeeks.org/how-to-setup-dvwa-in-windows/
"""


# Install required Python libraries
pip install requests beautifulsoup4

# Install Nmap (Port Scanner)
Download from https://nmap.org/download.html and install manually

# Install SQLMap
pip install sqlmap

# Install Wapiti3 (Web Vulnerability Scanner)
pip install wapiti3  
# Install Commix (XSS Testing)
git clone https://github.com/commixproject/commix.git

if get error that is missing anything else then do pip install something else name







"""
import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import requests
from bs4 import BeautifulSoup
import os

class WebsiteToolkitGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Website Toolkit")
        self.root.geometry("450x450")
        
        ttk.Label(root, text="Website Toolkit", font=("Arial", 16)).pack(pady=10)
        
        self.url_entry = ttk.Entry(root, width=50)
        self.url_entry.pack(pady=5)
        self.url_entry.insert(0, "Enter website URL or IP")
        self.url_entry.bind("<FocusIn>", self.clear_placeholder)
        self.url_entry.bind("<FocusOut>", self.restore_placeholder)
        
        self.create_buttons()
    
    def clear_placeholder(self, event):
        if self.url_entry.get() == "Enter website URL or IP":
            self.url_entry.delete(0, tk.END)
    
    def restore_placeholder(self, event):
        if not self.url_entry.get():
            self.url_entry.insert(0, "Enter website URL or IP")
    
    def create_buttons(self):
        ttk.Button(self.root, text="Analyze Website", command=self.analyze_website).pack(pady=5)
        ttk.Button(self.root, text="Pen Test Website", command=self.pen_test_website).pack(pady=5)
        ttk.Button(self.root, text="Complete Website Test", command=self.complete_website_test).pack(pady=5)
    
    def analyze_website(self):
        """ Show analysis options including 'Port Map'. """
        self.show_options("Analyze Website", ["SEO Analysis", "Security Scan", "Performance Test", "Port Map", "Total Analysis"])
    
    def pen_test_website(self):
        """ Show penetration testing options. """
        self.show_options("Pen Test Website", ["SQL Injection Test", "XSS Test", "CSRF Test", "Total Pen Test"])
    
    def complete_website_test(self):
        """ Run all available tests. """
        messagebox.showinfo("Complete Website Test", "Running full website analysis and penetration testing...")
        url = self.url_entry.get()
        self.total_analysis(url)
        self.total_pen_test(url)
    
    def show_options(self, title, options):
        """ Display available options in a popup window. """
        option_window = tk.Toplevel(self.root)
        option_window.title(title)
        option_window.geometry("300x250")
        
        ttk.Label(option_window, text=title, font=("Arial", 14)).pack(pady=10)
        
        for option in options:
            ttk.Button(option_window, text=option, command=lambda opt=option: self.run_tool(opt)).pack(pady=5)
    
    def run_tool(self, tool_name):
        url = self.url_entry.get()
        if url in ["", "Enter website URL or IP"]:
            messagebox.showerror("Error", "Please enter a valid website URL or IP address.")
            return

        if tool_name == "SEO Analysis":
            self.seo_analysis(url)
        elif tool_name == "Security Scan":
            self.security_scan(url)
        elif tool_name == "Performance Test":
            self.performance_test(url)
        elif tool_name == "Port Map":
            self.port_map(url)
        elif tool_name == "SQL Injection Test":
            self.sql_injection_test(url)
        elif tool_name == "XSS Test":
            self.xss_test(url)
        elif tool_name == "CSRF Test":
            self.csrf_test(url)
        elif tool_name == "Total Analysis":
            self.total_analysis(url)
        elif tool_name == "Total Pen Test":
            self.total_pen_test(url)
    
    def seo_analysis(self, url):
        """ Analyzes the SEO structure of the website. """
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            title = soup.title.string if soup.title else "No Title"
            meta_desc = soup.find("meta", attrs={"name": "description"})
            description = meta_desc["content"] if meta_desc else "No Meta Description"

            messagebox.showinfo("SEO Analysis", f"Website: {url}\nTitle: {title}\nMeta Description: {description}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to analyze {url}: {e}")

    def security_scan(self, url):
        """ Runs a security scan using Wapiti3. """
        try:
            messagebox.showinfo("Security Scan", f"Running security scan on {url}...")
            subprocess.run(["wapiti", "-u", url], capture_output=True, text=True)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to scan {url}: {e}")

    def performance_test(self, url):
        """ Measures response time using requests. """
        try:
            response = requests.get(url)
            time_taken = response.elapsed.total_seconds()
            messagebox.showinfo("Performance Test", f"Website: {url}\nResponse Time: {time_taken:.2f} seconds")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to test performance: {e}")

    def port_map(self, url):
        """ Runs Nmap to scan and map open ports. """
        try:
            messagebox.showinfo("Port Map", f"Scanning ports on {url}...")
            result = subprocess.run(["nmap", "-p-", url], capture_output=True, text=True)
            self.display_scan_results(result.stdout, "Port Map Results")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to map ports on {url}: {e}")

    def sql_injection_test(self, url):
        """ Runs SQLMap for SQL Injection testing. """
        try:
            messagebox.showinfo("SQL Injection Test", f"Testing SQL Injection on {url}...")
            subprocess.run(["sqlmap", "-u", url, "--batch", "--level=5"], capture_output=True, text=True)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to test SQL Injection: {e}")

    def xss_test(self, url):
        """ Runs Commix for XSS Testing. """
        try:
            messagebox.showinfo("XSS Test", f"Testing XSS vulnerabilities on {url}...")
            subprocess.run(["commix", "--url", url], capture_output=True, text=True)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to test XSS: {e}")

    def csrf_test(self, url):
        """ Uses Wapiti3 to check for CSRF vulnerabilities. """
        self.security_scan(url)  # CSRF is checked as part of Wapiti's scan.

    def total_analysis(self, url):
        """ Runs all analysis tools. """
        self.seo_analysis(url)
        self.security_scan(url)
        self.performance_test(url)
        self.port_map(url)

    def total_pen_test(self, url):
        """ Runs all penetration tests. """
        self.sql_injection_test(url)
        self.xss_test(url)
        self.csrf_test(url)

    def display_scan_results(self, results, title):
        """ Displays scan results in a popup window. """
        result_window = tk.Toplevel(self.root)
        result_window.title(title)
        result_window.geometry("500x400")

        text_area = tk.Text(result_window, wrap="word")
        text_area.insert(tk.END, results)
        text_area.pack(expand=True, fill="both")

if __name__ == "__main__":
    root = tk.Tk()
    app = WebsiteToolkitGUI(root)
    root.mainloop()
