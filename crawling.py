from bs4 import BeautifulSoup

soup = BeautifulSoup(open('sina.html'))
for ele in soup.find_all("a"):
	if len(ele.contents) > 0:
		print ele.contents[0].encode("utf-8")
	if "href" in ele.attrs:
		print ele["href"].encode("utf-8")
