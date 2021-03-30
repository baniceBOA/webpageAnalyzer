#writing a page to a file 
import requests
url = 'https://www.google.com/search?q=windows+sdk.&sxsrf=ALeKk00ki9HGFQ6jEioOirQMYikvw08T8g%3A1617109120072&source=hp&ei=gCBjYPOgAoGkgweb6r6QDA&oq=w&gs_lcp=ChFtb2JpbGUtZ3dzLXdpei1ocBABGAIyBAgjECcyBAgjECcyBAgjECcyCggAELEDEIMBEEMyBAgAEEMyBAgAEEMyBAgAEEMyBQgAELEDOgcIIxDqAhAnUOQNWOQNYP0raABwAHgAgAHgBYgB-QiSAQc0LTEuMC4xmAEAoAEBsAEP&sclient=mobile-gws-wiz-hp'
content = requests.get(url).content
content = str(content)
f = open('index.html', 'w')
f.write(content)
f.close()