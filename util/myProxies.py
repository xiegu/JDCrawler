import random, requests

def get_proxies(proxiesUrl, free = False):
	html = requests.get(proxiesUrl)
	content = html.json()
	if not free:
		http = str('http://%s:%d' %(content[0][0], content[0][1]))
		https = str('http://%s:%d' %(content[1][0], content[1][1]))
		proxies = {'http': http, 'https': https}
	else:
		p1 = random.randint(1,10)-1
		p2 = random.randint(1,10)-1
		http = str('http://%s:%d' %(content[p1][0], content[p1][1]))
		https = str('http://%s:%d' %(content[p2][0], content[p2][1]))
		proxies = {'http': http, 'https': https}
	return proxies