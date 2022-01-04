# frontend

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

# Initialize the project with docker
To initialize the project without having vue installed localy, can create everything in a container using `Dockerfile_init_vue` image.

Run:
```
docker build frontend/Dockerfile_init_vue -t npm_vue_init:latest .
docker run -it -v /home/neil/product_review/frontend:/app npm_vue_init:latest vue create frontend
chown -R $USER:$USER frontend
```

# Running in development mode with docker
```
docker build -t product_review_frontend:0.1 -f frontend/Dockerfile .
docker run -it -v /home/neil/product_review/frontend:/app -p 8080:8080 product_review_frontend:0.1 
```



# Errors:
* If there is an error like `Error from chokidar (/frontend/src/views): Error: ENOSPC: System limit for number of file watchers reached` you need to increase the number of file watchers allowed with something like `sudo sysctl -n -w fs.inotify.max_user_watches=16384`. To see the number of active watches run `sudo lsof | grep inotify | wc -l`