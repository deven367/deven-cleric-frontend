---
title: deven-cleric-frontend
emoji: 🌍
colorFrom: red
colorTo: blue
sdk: streamlit
sdk_version: 1.33.0
app_file: app.py
pinned: false
---

## Description

I've built the web app with Streamlit. The app is deployed on huggingface spaces. The app as expected takes comma seperated URLs and a question/questions as input and returns facts.

The facts received from the API are in `list` format, however, a single element of the `list` can contain multiple sentences, so I tokenize them into multiple sentences using `nltk`.

The app is deployed on huggingface spaces and can be accessed &rarr; [here](https://huggingface.co/spaces/deven367/frontend).

## Install

Install the dependencies using,

```sh
pip install -r requirements.txt
```

Once installed, start the app using

```sh
streamlit run app.py
```
