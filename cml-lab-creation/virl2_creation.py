from virl2_client import ClientLibrary 

client = ClientLibrary("https://192.168.50.114",username="lcrismas",password="Cybersecure21!",ssl_verify=False)

lab = client.create_lab(title="TestAutomation")

router1 = lab.create_node("ISR_1","csr1000v",50,100)