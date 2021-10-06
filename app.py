from GoogleNews import GoogleNews

googlenews = GoogleNews()
googlenews = GoogleNews(period = '7')
googlenews.search('UG')
result = googlenews.result()
for x in result:
    print("_"*50)
    print("Title: ", x['title'])
    print("Date: ", x['date'])
    print("Description: ", x['desc'])
    print("Link: ", x['link'])