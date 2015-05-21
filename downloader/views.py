from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt  
import traceback
import json
import datetime as dt
import requests
import os
import subprocess

def current_time():
    return dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

indentation = " "*12
import platform
if platform.system() == 'Windows':
    bold=''
    underline=''

    red=''
    green=''
    blue=''
    reset=''
else:
    bold='\033[01m'
    underline='\033[04m'

    red='\033[31m'
    green='\033[32m'
    blue='\033[34m'
    reset='\033[0m'

@csrf_exempt   
def download(request):
    if request.method == 'POST':
        html_text = ""
        try:
            url = json.loads(request.body)['url']
            html_text = requests.get(url).text
            print bold+blue+"{0}[{1}] POST URL: {2}".format(indentation,current_time(),url)
            return HttpResponse(html_text)
        except:
            print bold+red+"{0}[{1}] POST URL: {2}".format(indentation+underline,current_time(),url)+reset
            html_text = "ERROR [{0}] {1}".format(current_time(),traceback.format_exc())
            print bold+red+html_text
            return HttpResponse(html_text)
            #test

def pull(request):
    try:
        pwd = os.getcwd()
        print bold+blue+"{0}[{1}] {2}$ git pull".format(indentation,current_time(),pwd)
        output = subprocess.Popen("git pull", shell=True, stdout=subprocess.PIPE).stdout.read()
        print bold+green+"{0}[{1}] {2}".format(indentation,current_time(),output)+reset
        return HttpResponse(output)
    except:
        print bold+red+traceback.format_exc()+reset
        return HttpResponse("ERROR "+traceback.format_exc())