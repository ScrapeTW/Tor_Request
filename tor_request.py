from torrequest import TorRequest

with TorRequest() as tr:
    tr.reset_identity()
    response = tr.get('http://ipecho.net/plain')
    print(response.text)
