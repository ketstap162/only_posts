# OnlyPost Service

![Logo of the project](https://i.ibb.co/zhnXVvJ/icon.png)


### About
The OnlyPosts Service is a simple project, "mini-Twitter", 
which has the following features:
- Postgres DB;
- Docker Compose for Deployment;
- registration, email authentication and authorization systems;
- possibility to create posts with attachments (image and text file);
- the ability to reply to posts;
- replies are rendered recursively;
- post sorting and filtering;
- minimalistic user interface.

### How to setup project?
1) Create and open the `.env` file. 
Enter there all the necessary variables given in the example `.env.sample`.
2) Configure `posts_app/posts_setting.py` for your needs.
3) Run Docker Engine in your device or server.
4) Run commands in Terminal:
```commandline
docker-compose build
docker-compose up
```
or 
```commandline
docker-compose up --build
```

Now you can access to project site via localhost:DJANGO_PORT (127.0.0.1:DJANGO_PORT}.
