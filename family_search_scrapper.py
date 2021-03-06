import time

import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

import re
import requests

from fs_parser.pr_parser import PRParser

class FamilySearchScrapper(PRParser):
    def __init__(self, **kwargs):
        self.match = kwargs.get('match', 'exact')
        self.firstname = kwargs.get('firstname', '').replace(' ', '%20')
        self.surname = kwargs.get('surname', '').replace(' ', '%20')

        self.req = requests.Session()
        print("Logging in...")
        login_url = 'https://www.familysearch.org/auth/familysearch/login?fhf=true&returnUrl=%2F'
        html = self.req.get(login_url)
        params = re.findall(r'<input type=\"hidden\" name=\"params\" value=\"([\w\-\=]+)\"\/>', html.text)[0]

        # print(params)

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'keep-alive',
            'Origin': 'https://ident.familysearch.org',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': html.url,
        }

        body = {
            'userName': 'ww1_project',
            'password': 'maledizione222',
            'params': params
        }

        self.req.post('https://ident.familysearch.org/cis-web/oauth2/v3/authorization', data=body, headers=headers)
        # print(post.text)

    
    def search(self):
        if (self.firstname == '' and self.surname == ''):
            raise Exception("Must have firstname or surname")

        if self.match == 'approximate':
            self.search_url = f"https://www.familysearch.org/search/record/results?q.givenName=f{self.firstname}&q.surname={self.surname}&f.collectionId=2125045&count=20&offset=0&m.defaultFacets=on&m.queryRequireDefault=on&m.facetNestCollectionInCategory=on"
        elif self.match == "exact":
            self.search_url = f"https://www.familysearch.org/service/search/hr/v2/personas?q.givenName={self.firstname}&q.givenName.exact=on&q.surname={self.surname}&q.surname.exact=on&f.collectionId=2125045&count=20&offset=0&m.defaultFacets=on&m.queryRequireDefault=on&m.facetNestCollectionInCategory=on"
        else:
            raise Exception("Unknown match criteria")

        start = time.time()

        test = self.req.get(self.search_url)
        source = test.text

        links = re.findall(r'https://www.familysearch.org/ark:/[0-9]+/[0-9]+:[0-9]+:[\w-]+', source)

        # print(links)
        try:
            print(links[0])
        except:
            print(f"Not found for {self.firstname}")
            return

        fssessionid = self.req.cookies.get_dict()['fssessionid']

        data_header = {
            'Accept' : 'application/x-gedcomx-v1+json, application/json',
            'Accept-Encoding' : 'gzip, deflate, br',
            'Accept-Language' : 'en',
            'Authorization': 'Bearer ' + fssessionid,
            'Referer' : self.search_url,
            'from' : 'fsSearch.record.getGedcomX@familysearch.org',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin'
        }

        data = self.req.get(links[0], headers = data_header)
        # print(data.text)

        super().__init__(data.text)
        end = time.time()

        print(end - start)

    def get_data(self):
        return super().get_data()
    
    def clear_data(self):
        super().clear_data()

if __name__ == '__main__':
    obj = FamilySearchScrapper()
    obj.firstname = 'A'
    obj.surname = 'Thomas'
    obj.search()
    print(obj.get_data())