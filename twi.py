#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Прототип этой либы написан Лерой @for15pounds Гаркавой году эдак в 2015 - 2016


import json
import requests
import base64
import sys
import re

class twitter:
    api_token = None
    auth_url = 'https://api.twitter.com/oauth2/token'

    # Конструктор класса. Тут мы проверяем, что твиттер нам выдал токен. И если нет, то авторизуемся методом get_token
    def __init__(self, **kwargs):
       if self.api_token == None:
          if 'api_key' in kwargs and 'api_secret' in kwargs:
             self.api_token = self.get_token(kwargs['api_key'], kwargs['api_secret'])
          else :
             return -1

    # Авторизация
    def get_token(self, api_key, api_secret):
       ultimate_secret = 'Basic ' + base64.standard_b64encode(api_key + ':' + api_secret)
       content_type = 'application/x-www-form-urlencoded;charset=UTF-8'
       headers = {'Authorization': ultimate_secret,'Content-type': content_type}
       payload = 'grant_type=client_credentials'
       result = requests.post(self.auth_url, headers=headers, data=payload)
       if 'access_token' in json.loads(result.text):
           return json.loads(result.text)['access_token']
       else:
           return -1
 
    # Запрос к URL с подстановкой авторизации по токену. 
    # Можно делать тупо: authget('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=for15pounds&count=2')
    # https://dev.twitter.com/rest/reference/get/statuses/user_timeline подробности тут
    # Хорошо тем, что можно получить полную огромную промокашку, в которой и то, на что ты отвечаешь и всё такое прочее.

    def authget(self, url):
        if self.api_token == None:
            return -1
        else:
            ultimate_token = 'Bearer ' + self.api_token
            headers = {'Authorization': ultimate_token}
        payload = 'grant_type=client_credentials'
        result = requests.get(url, headers=headers)
        return json.loads(result.content)

    # А это уже интерфейс к authget. Тупо передаёшь сюда юзера и параметры которые хочешь применить. Например количество постов
    # posts('for15pounds', count=150).
    # Список параметров снова тут: https://dev.twitter.com/rest/reference/get/statuses/user_timeline
    # В ответ получаем словарь вида {'id_поста':'текст поста'}

    def posts(self, user, **kwargs):
        original_count = 1
        posts = []
        if 'count' in kwargs:
            original_count = kwargs['count']
            if kwargs['count'] > 200: 
                kwargs['count'] = 200

        while original_count > 0:
            lposts = self.getposts(user, **kwargs)
            posts.extend(lposts)
            kwargs['max_id'] = posts[-1]['id'] - 1
            if len(lposts) < kwargs['count']-2:
                break
            if 'count' in kwargs:
                original_count -= kwargs['count']
            else:
                original_count = 0
        return posts

    def getposts(self, user, **kwargs):
        url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?' + 'screen_name=' + user
        for param in list(kwargs.keys()):
            url += '&' + str(param) + '=' + str(kwargs[param])
        posts = self.authget(url)
        return posts


class vk:

    def __init__(self, api_secret):
        self.api_secret = api_secret
        return None


    def search(self, **kwargs):
        search_url = 'https://api.vk.com/method/newsfeed.search'
        search_url += '?'
        search_url += 'v=5.103&access_token='+ self.api_secret +'&'
        query = []
        for key in list(kwargs.keys()):
            query.append(key + '=' + kwargs[key])
        search_url += '&'.join(query)
        result = self.authget(search_url)
        return result


    def authget(self, url):
        headers = ''
        result = requests.get(url, headers=headers)
        return json.loads(result.content)

