import tls_client

session = tls_client.Session(client_identifier="Chrome116")

def getja3():
    return session.get("https://tls.peet.ws/api/tls").json().get("tls").get("ja3")
