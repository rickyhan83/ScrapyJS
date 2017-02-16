# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 12:15:46 2017

@author: newton
"""

from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

import random
import base64
from settings import PROXIES
from settings import USER_AGENTS

class RandomUserAgent(UserAgentMiddleware):
    """Randomly rotate user agents based on a list of predefined ones"""

    def __init__(self, agents):
        self.user_agent = USER_AGENTS

    def process_request(self, request, spider):
        #这句话用于随机选择user-agent
        ua = random.choice(self.user_agent)
        if ua:
            request.headers.setdefault('User-Agent', ua)


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)
        if proxy['user_pass'] is not None:
            request.meta['proxy'] = "http://%s" % proxy['ip_port']
            encoded_user_pass = base64.encodestring(proxy['user_pass'])
            request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
            print "**************ProxyMiddleware have pass************" + proxy['ip_port']
        else:
            print "**************ProxyMiddleware no pass************" + proxy['ip_port']
            request.meta['proxy'] = "http://%s" % proxy['ip_port']       
         