import argparse
import random
import requests
import json
import os
from importlib.resources import read_text
from .CheggScraper import CheggScraper
import main

def sd(URL,name,update,context,a,fechaCad, cred, fila):
    """
    User Friendly Downloader for chegg homework help pages

    :return: Nothing
    :rtype: None
    """
    x = random.randint(1, 1)
    print(x)
    if x == 1:
        conf = json.loads(read_text('cheggscraper', 'conf1.json'))
    if x == 2:
        conf = json.loads(read_text('cheggscraper', 'conf2.json'))
    if x == 3:
        conf = json.loads(read_text('cheggscraper', 'conf3.json'))
    if x == 4:
        conf = json.loads(read_text('cheggscraper', 'conf4.json'))
    if x == 5:
        conf = json.loads(read_text('cheggscraper', 'conf5.json'))
    if x == 6:
        conf = json.loads(read_text('cheggscraper', 'conf6.json'))
    if x == 7:
        conf = json.loads(read_text('cheggscraper', 'conf7.json'))
    if x == 8:
        conf = json.loads(read_text('cheggscraper', 'conf8.json'))
    if x == 9:
        conf = json.loads(read_text('cheggscraper', 'conf9.json'))
    if x == 10:
        conf = json.loads(read_text('cheggscraper', 'conf10.json'))

    # conf = json.loads(read_text('cheggscraper', 'conf.json'))

    default_save_file_format = conf.get('default_save_file_format')
    default_cookie_file_path = conf.get('default_cookie_file_path')

    ap = argparse.ArgumentParser()
    ap.add_argument('-c', '--cookie', default=default_cookie_file_path,
                    help='path of cookie life', dest='cookie_file')
    ap.add_argument('-u', '--url', help='url of chegg homework-help, put inside " "',
                    type=str, dest='url')
    # FIXME: DIFF TAGS FOR FILE FORMAT AND BASE PATH
    ap.add_argument('-s', '--save',
                    help='file path, where you want to save, put inside " " eg: test.html or'
                         ' D:\\myFolder\\test.html or /home/test.html',
                    type=str, default=default_save_file_format, dest='file_format')
    args = vars(ap.parse_args())
    print(args['cookie_file'])

    if not os.path.exists(path=args['cookie_file']):
        raise Exception(f'{args["cookie_file"]} does not exists')

    if not args.get('url'):
        args.update({'url': URL})

    Chegg = CheggScraper(cookie_path=args['cookie_file'])
    print(Chegg.url_to_html(args['url'], file_name_format=args['file_format']))
    f = open(args['cookie_file'], 'r')
    User_Agent = f.read()
    f.close()
    f = open("chegg_scraper.txt", "w")
    f.write(f"{User_Agent}")
    f.close()
    print(f'{default_cookie_file_path}')

    if a == 1:
        print(f"{name} - Response Sent to the Group - {default_cookie_file_path}")
        main.echo(URL, name, update, context, fechaCad, cred, fila, default_cookie_file_path)
