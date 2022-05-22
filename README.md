
This application implements the following functionality
- CRUD API to manage news posts. The post  has the next fields: title, link, creation date, amount of upvotes, author-name
- CRUD API to manage comments on news. The comment has the next fields: author-name, content, creation date
- The results of voting for the news are reset to zero at 11:59 p.m.


After run the application, enter in the address bar:
 'https://developsapiapp2.herokuapp.com/comments/'


Url scheme:
https://developsapiapp.herokuapp.com/comments/
    path('') - index page show all news
    path('news/') - Newslist API
    path('news/<int:pk>') - New API
    path('comment/') - Commentslist API
    path('commemt/<int:pk>') - Comment API

Docker image link:
docker pull andriimih/api_web_app:latest
Run command:
docker run -p 8000:8000 api_web_app