import inspirobot
from urllib.request import Request
import urllib

quote = inspirobot.generate()  # Generate Image
request_site = Request(quote.url, headers={"User-Agent": "Mozilla/5.0"})
resource = urllib.request.urlopen(request_site)
output = open("inspire.jpg","wb")
output.write(resource.read())
output.close()
print("Generated an inspiring image.")