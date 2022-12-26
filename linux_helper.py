"""
This script is a command line tool for getting chatgpt to craft you linux commands that "do what I mean"
flags   -p
            - required, this is the prompt
        -e
            -not required, default to false, this the command that executes the code
        -v
            - not required, this is the flag that tags it as verbose or not (so it prints the response from OpenAI)

"""

import os
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", type=str)
parser.add_argument("-e", default=False, action='store_true')
parser.add_argument("-v", default=True, action='store_true')

API_KEY = os.environ['API_KEY']

if __name__ == "__main__":
    URL = "https://api.openai.com/v1/completions"

    args = parser.parse_args()
    verbose = args.v
    prompt = args.p
    execute = args.e

    data = {
        "model": "text-davinci-003",
        "prompt": f"respond with the command or code only to do the following:  {prompt}",
        "max_tokens": 2048,
        "temperature": 0
    }

    result = requests.post(URL,
                           headers={'Content-Type': 'application/json',
                                    'Authorization': 'Bearer {}'.format(API_KEY)},
                           json=data)

    return_text = result.json()['choices'][0]['text']

    if verbose:
        print(f'you said: {prompt}')
        print('OpenAI Davinci-003 says...')
        print(return_text)

    if execute:

        if verbose:
            print('executing the following command')
            print(return_text)

        os.system(return_text)
