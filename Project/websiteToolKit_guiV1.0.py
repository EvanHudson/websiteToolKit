import tkinter as tk
from tkinter import ttk, messagebox
import requests

class WebsiteToolkitGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Website Toolkit")
        self.root.geometry("400x350")
        
        ttk.Label(root, text="Website Toolkit", font=("Arial", 16)).pack(pady=10)
        
        self.url_entry = ttk.Entry(root, width=50)
        self.url_entry.pack(pady=5)
        self.url_entry.insert(0, "Enter website URL")
        self.url_entry.bind("<FocusIn>", self.clear_placeholder)
        self.url_entry.bind("<FocusOut>", self.restore_placeholder)
        
        self.create_buttons()
    
    def clear_placeholder(self, event):
        if self.url_entry.get() == "Enter website URL":
            self.url_entry.delete(0, tk.END)
    
    def restore_placeholder(self, event):
        if not self.url_entry.get():
            self.url_entry.insert(0, "Enter website URL")
    
    def create_buttons(self):
        ttk.Button(self.root, text="Analyze Website", command=self.analyze_website).pack(pady=5)
        ttk.Button(self.root, text="Pen Test Website", command=self.pen_test_website).pack(pady=5)
        ttk.Button(self.root, text="Complete Website Test", command=self.complete_website_test).pack(pady=5)
    
    def analyze_website(self):
        self.show_options("Analyze Website", ["SEO Analysis", "Security Scan", "Performance Test", "Total Analysis"])
    
    def pen_test_website(self):
        self.show_options("Pen Test Website", ["SQL Injection Test", "XSS Test", "CSRF Test", "Total Pen Test"])
    
    def complete_website_test(self):
        messagebox.showinfo("Complete Website Test", "Running full website analysis and penetration testing...")
        # Call actual testing functions here
    
    def show_options(self, title, options):
        option_window = tk.Toplevel(self.root)
        option_window.title(title)
        option_window.geometry("300x200")
        
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
        else:
            messagebox.showinfo("Tool Running", f"Running {tool_name} on {url}...")
    
    def seo_analysis(self, url):
        try:
            response = requests.get(url)
            status_code = response.status_code
            content_length = len(response.text)
            messagebox.showinfo("SEO Analysis", f"Website: {url}\nStatus Code: {status_code}\nContent Length: {content_length} characters")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to analyze {url}: {e}")
    
    def security_scan(self, url):
        messagebox.showinfo("Security Scan", f"Running security scan on {url}...")
    
    def performance_test(self, url):
        messagebox.showinfo("Performance Test", f"Running performance test on {url}...")
    
    def total_analysis(self, url):
        messagebox.showinfo("Total Analysis", f"Running total analysis on {url}...")
    
    def sql_injection_test(self, url):
        messagebox.showinfo("SQL Injection Test", f"Running SQL Injection Test on {url}...")
    
    def xss_test(self, url):
        messagebox.showinfo("XSS Test", f"Running XSS Test on {url}...")
    
    def csrf_test(self, url):
        messagebox.showinfo("CSRF Test", f"Running CSRF Test on {url}...")
    
    def total_pen_test(self, url):
        messagebox.showinfo("Total Pen Test", f"Running total penetration test on {url}...")

if __name__ == "__main__":
    root = tk.Tk()
    app = WebsiteToolkitGUI(root)
    root.mainloop()
