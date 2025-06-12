import json
import requests
import urllib3

# Class created to have a comprehensive list of API endpoints for the CML Instance
# If you are locally using your CML, you might not have SSL on you CML therefore set "ssl_verify = False"
class APIcml: 
    def __init__(self, base_url, username=None, password=None, ssl_verify=False):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.ssl_verify = ssl_verify
        self.token = None
        self.session = requests.Session()  # Using session for persistent connections

    def api_auth(self):
        """Authenticate to the CML API and store the token."""
        url = f"{self.base_url}/authenticate"
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        param = {
            "username": self.username,
            "password": self.password
        }
        try:
            # Make POST request to authenticate
            response = self.session.post(url, json=param, headers=headers, verify=self.ssl_verify)
            response.raise_for_status()  # Raise exception for 4xx or 5xx status codes
            
            # Directly extracting token from the response (assuming it's returned as a plain string)
            self.token = response.text.strip().strip('"')  # Remove quotes if present
            
            if self.token:
                print("Authentication was successful, Token acquired.")
                print(f"Token: {self.token}")
            else:
                print("Failed to retrieve token.")
        
        except requests.exceptions.RequestException as e:
            print(f"Authentication failed: {e}")
            return None

    def make_request(self, endpoint):
        """Make an authenticated GET request to a given endpoint."""
        if not self.token:
            print("No valid token found. Please authenticate first.")
            return
        
        url = f"{self.base_url}/{endpoint}"
        headers = {
            'Authorization': f'Bearer {self.token}',  # Pass token in the header for subsequent requests
            'Accept': 'application/json'
        }
        
        try:
            # Make GET request to the endpoint with token authorization
            response = self.session.get(url, headers=headers, verify=self.ssl_verify)
            response.raise_for_status()  # Check for HTTP errors
            
            # Assuming the response is JSON
            data = response.json()
            print("Response data:", json.dumps(data, indent=4))  # Pretty print the JSON response
            
        except requests.exceptions.RequestException as e:
            print(f"Request to {endpoint} failed: {e}")
            print(f"Raw response: {response.text}")  # Log the raw response for debugging
    
    def lab_inventory(self):
        lab_id = APIcml.make_request(self,endpoint='labs')
        labs = lab_id
        for lab in labs:
            url = f"{self.base_url}/labs/{lab}"
    

    def get_nodes(self):
        nodes = APIcml.make_request(self,endpoint='nodes')
                
            
        



url_in = "https://192.168.50.114/api/v0/"
user_in = input("|Username> ")
pass_in = input("|Password> ")
init_api = APIcml(username=user_in,password=pass_in,base_url=url_in,ssl_verify=False)
APIcml.api_auth(init_api)
APIcml.lab_inventory(init_api)






