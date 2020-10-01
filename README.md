# Dejamobile Take Home - Backend API SDK

Implements a SDK to use the [backend API](https://github.com/antbht/djm-back). This SDK could be embed into Python clients. [See here an example](https://github.com/antbht/djm-client).

##  Use in your app

### Add a dependency to the package

```lang=bash
cd /path/to/your/client/project
pip install /path/to/djm_sdk
```

### Initialize the API client

```lang=python
from djm_sdk import api

api_client = api.API("127.0.0.1", "8000")
```

### Use the API methods

```lang=python

api_client.get_cards("user_id")
>>> [<Object djm_sdk.model.Card>, ...]

api_client.add_card("user_id", "pan")
>>> [<Object djm_sdk.model.Card>, <Object djm_sdk.model.Card>]

api_client.delete_card("user_id", "card_id")
>>> "card_id"

for card in api_client.get_cards("user_id"):
    print(f"{card.id} : {card.hidden_pan}")
>>> e290b6aa-03a9-11eb-8b48-3c15c2c07228 : XXXXXXXXXXXX1234
e290b6aa-03a9-11eb-8b48-3c15c2c07289 : XXXXXXXXXXXX6789
```

## How to use as SDK developer ?

### Prerequisite 

- Have python 3.8 installed
- Have `virtualenv` python package installed
- Clone this project into your workspace

### Initialize the project

This is a Python project. For good practices and environments isolation purpose, we advise you to run it into a virtual envrionment.

```lang=bash
cd /path/to/workspace
git clone https://github.com/antbht/djm-sdk
cd djm-sdk
virtualenv .
source bin/activate
pip install -r requirements.txt
```

### Run the unit tests

Functions of this project are covered by unit tests. To execute them, please run this script :

```lang=bash
cd /path/to/djm-sdk
source bin/activate
python -m unittest unit_tests/*.py
```

### Build the wheel

```lang=bash
cd /path/to/djm-sdk
source bin/activate
python setup.py bdist_wheel
```

### Use the sample of ci script

This script simulates a CI script which could be implements for GitlabCI, jenkins, ... CI/CD platforms. It :
- Initializes the virtualenv
- Runs unit tests
- Builds the wheel

```lang=bash
cd /path/to/djm-djk
bash ci_script.sh
```
