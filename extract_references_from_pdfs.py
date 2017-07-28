import argparse
import json
import os
import requests
import urllib.parse

API_URL = os.getenv("CARA_API_URL", default='http://casetext-cara-staging.herokuapp.com')
API_USER = "casetext-staff"
API_PASSWORD = "helloCARA!"

def process_file(filename):
    params = urllib.parse.urlencode({ 'fileId': filename })
    files = {'file': open(filename, 'rb')}
    headers = {'content-type': 'application/pdf'}
    r = requests.post(API_URL + "/briefs?" + params, auth=(API_USER, API_PASSWORD), headers=headers, files=files)
 #   print("pdf brief request returned with %d" % r.status_code)
    response = json.loads(r.content.decode('utf-8'))
 #   print("results are: %s" % response)
    return r

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('pdf', help='PDF to get references from')
    args = parser.parse_args()

    process_file(args.pdf)
