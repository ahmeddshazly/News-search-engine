# Description

A News search engine using Vue.js and Flask:

1. User can search for any news topic
2. User can search News Topics in all languages
3. User can search English topics or German topics only
4. Articles are sorted by Date by default
5. Get your ApiKey from [https://newsapi.org/]

## The project uses the following technologies:

1. Vue.js for the frontend

- The frontend contain 2 components:
  - App
  - NewsArticles

2. Flask for the backend

- Routes:
  - \Search (Get request)

# Getting Started

## Available Scripts

## In the Frontend directory, you can run:

### to install the dependencies

```
npm install
```

### Run app in development mode

```
npm run serve
```

Runs the app in the development mode.\
Open [http://localhost:8080](http://localhost:8080) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### Compiles and minifies for production

```
npm run build
```

### Lints and fixes files

```
npm run lint
```

### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).

## In the Backend directory, you can run:

### Activate virtual environment

To use the environment the following command is neccessary

```
# Linux/Mac
$ source venv/bin/activate

# Windows
> ./venv/Scripts/activate
```

### Exiting the virtual environment

To exit the environment and make use of the globally installed python version again, use

```
# Linux/Mac
$ deactivate

# Windows
> venv/Scripts/deactivate
```

### Installing dependencies

To install the neccessary dependencies in the environment use this command:

```
pip install -r requirements.txt
```

## Configuration

For execution, the backend needs the following environment:

```
SET FLASK_DEBUG=development
```

SET FLASK_APP=app.py

## Running

for running the app, use this command:

```
py -m flask run
```
