# rotating-proxies
<h4>Rotating Proxies Module for Scrappers written in python.</h4><br/>
An easy to use application to rotate proxies while scrapping using python, works very smooth like requests module.
Install the modules required for the Proxy-Rotator
<pre>pip install -r requirements.txt</pre>

To use the script, use as following in your python code:
<pre>
from proxy import *
url="https://www.google.com" #Enter the url you want to ping
response=get_response(url)
#returns a reponse objects as returned by requests.get(url), you can use it in your scrapper
</pre>
