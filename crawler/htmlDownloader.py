from config import get_header, TIMEOUT
import requests, socket

class HtmlDownloader(object):
	@staticmethod
	def download(url):
		try:
			html = requests.get(url, headers = get_header(), timeout = TIMEOUT)
			content = html.text
			return content
		except (requests.exceptions.Timeout, socket.timeout) as e:
			errorUrl = url
			return errorUrl
		except requests.exceptions.ConnectionError:
			errorUrl = url
			return errorUrl

	@staticmethod
	def download_proxy(url, proxies):
		try:
			html = requests.get(url, headers = get_header(), proxies = proxies, timeout = TIMEOUT)
			content = html.text
			return content
		except (requests.exceptions.Timeout, socket.timeout) as e:
			errorUrl = url
			return errorUrl
		except requests.exceptions.ConnectionError:
			errorUrl = url
			return errorUrl
		except request.exceptions.ProxyError:
			errorUrl = url
			return errorUrl
