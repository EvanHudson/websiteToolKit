# Group 2 Website Tool Kit
#https://nmap.org/download.html#windows download nmap then switch the file location to the location of the nmap.exe
import requests
import subprocess

class WebsiteToolKit:
    def __init__(self, analyzer_tools=None, pentester_tools=None):
        """
        Initialize the WebsiteToolKit with attributes for analyzer and pentester tools.
        
        :param analyzer_tools: List of tools for analysis (default: empty list)
        :param pentester_tools: List of tools for penetration testing (default: empty list)
        """
        self.analyzer_tools = analyzer_tools if analyzer_tools is not None else []
        self.pentester_tools = pentester_tools if pentester_tools is not None else []

    def add_analyzer_tool(self, tool):
        """Add an analysis tool to the toolkit."""
        self.analyzer_tools.append(tool)

    def add_pentester_tool(self, tool):
        """Add a penetration testing tool to the toolkit."""
        self.pentester_tools.append(tool)

    def list_tools(self):
        """Return a dictionary listing both analyzer and pentester tools."""
        return {
            "Analyzer Tools": self.analyzer_tools,
            "Pentester Tools": self.pentester_tools
        }
    
    def sql_tester(self, website_url):
        """Run SQL test."""
        return f"Running SQL test on {website_url}"
    
    def port_mapper(self):
        """Map ports using nmap."""
        print("Running port_mapper")
        nmap_path = r"C:\Program Files (x86)\Nmap\nmap.exe"  # Updated path
        return subprocess.run([nmap_path, "-p-", "-T4", "-oN", "port_scan.txt"], capture_output=True, text=True).stdout
    
    def http_mapper(self):
        """Map all paths in website using dictionary file."""
        return "Mapping website paths..."
    
    def buffer_overflow_tester(self):
        """Inputs long string into text entry to test for buffer overflow vulnerabilities."""
        return "Testing for buffer overflow..."
    
    def page_speed_insights(self, website_url):
        """Analyze website performance using PageSpeed Insights API."""
        print("Running page_speed_insight")
        try:
            response = requests.get(f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={website_url}")
            return response.json()
        except requests.exceptions.RequestException as e:
            return f"Error fetching PageSpeed Insights: {e}"
    
    def burp_suite_scan(self, website_url):
        """Perform a security scan using Burp Suite."""
        return f"Initiating Burp Suite scan on {website_url}. (Implementation requires Burp Suite API or manual setup)"
# Example Usage:
toolkit = WebsiteToolKit()
toolkit.add_analyzer_tool("PageSpeed Insights")
toolkit.add_pentester_tool("Burp Suite")
print(toolkit.list_tools())
print(toolkit.port_mapper())
print(toolkit.page_speed_insights("https://the-internet.herokuapp.com/"))
