# What is this?

## A toolkit of chatgpt related tools

this toolkit shows how to send a request to the davinci-003 GPT framework
which is like GPT3 (whereas chatgpt is basically gpt3.5).

##  Requirements

### Setup

I'm running this in python3.11, but you could probably get away
with far lower - I'm just using the requests library, everything
else is the standard library.  For AWS stuff, you'll need Boto3.

### API Key
an api key (you can get that from the OpenAI website), and 
to register a credit card with them - I set a maximum account
usage limit to $10 a month personally, but you do you.

### Operation

Make sure you have an API key, store it as the environment
variable API_KEY.  Then run the following command

`python3 linux_helper.py -p "print hello world to the console and then also put it in a file called test.txt" -v`
and see what you get!