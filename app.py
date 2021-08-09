import requests
import json
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def proxy():
    city = request.args.get('city')
    state = request.args.get('state')
    postal_code = request.args.get('postal_code')
    number = request.args.get('number')
    enumeration_type = request.args.get('enumeration_type')
    taxonomy_description = request.args.get('taxonomy_description')
    first_name = request.args.get('first_name')
    use_first_name_alias = request.args.get('use_first_name_alias')
    last_name = request.args.get('last_name')
    organization_name = request.args.get('organization_name')
    address_purpose = request.args.get('address_purpose')
    country_code = request.args.get('country_code')
    limit = request.args.get('limit')
    skip = request.args.get('skip')

    # res = requests.get(f"https://npiregistry.cms.hhs.gov/api/?version=2.1&city={city}&taxonomy_description=${taxonomy}")
    res = requests.get(f'https://npiregistry.cms.hhs.gov/api/?number={number}&enumeration_type={enumeration_type}&taxonomy_description={taxonomy_description}&first_name={first_name}&use_first_name_alias={use_first_name_alias}&last_name={last_name}&organization_name={organization_name}&address_purpose={address_purpose}&city={city}&state={state}&postal_code={postal_code}&country_code={country_code}&limit={limit}&skip={skip}&version=2.1&pretty=true')

    resJson = res.json()
    return resJson

if __name__ == '__main__':
    app.run()
