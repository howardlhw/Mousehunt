# Mousehunt

Python scripts for making our mouse hunting lives easier. A few selected hunting locations have been built due to the additional human-input requirement during hunting.

# Quick Overview
To use this application, make sure you have python 3 installed on your computer. Install virtual environment and the additional dependencies.

```
python app.py
```

Execute the application by running app.py. You will need to update the file with your cookies and unique hash. 

```
user_cookies = {
    "hg_session[sessionId]": [YOUR_SESSIONID_HERE],
    "HG_TOKEN": [YOUR_TOKEN_HERE]
}

user_body = {"uh": [YOUR_UNIQUE_HASH_HERE],}
```

The following hunting locations have been built
- Labyrinth
- Bristle Woods Rift
- Valor Rift

# Detailed Usage
## Step 1 - Creating Virtual Environmnet
If you have not installed virtual env, install by by executing `pip install virtualenv`

Create python virtual environment by executing the following codes
'''
virtualenv venv
cd venv/Scripts
activate
cd ..
cd ..
pip install -r requirements.txt

## Step 2 - Accessing Token and Unique Hash
After logging into mousehunt, press F12 to access development tab. Click on 'camp' to trigger a round of data retrieval from server. Retrieve the token and unique hash as shown below.


## Step 3 - Configuring app.py
Use a text editor to edit app.py. Update the token, session[id] (if applicable) and unique hash.
```
user_cookies = {
    "hg_session[sessionId]": [YOUR_SESSIONID_HERE],
    "HG_TOKEN": [YOUR_TOKEN_HERE]
}

user_body = {"uh": [YOUR_UNIQUE_HASH_HERE],}
```

## Step 4 - Executing script
Update the following section with the updated codes. The instance will run automatically when automateHunt is called. The parameters of automate hunt to pass into can be found in the respective sections.

```
def runHornContinuously():
    while True:
        mh_vrift = Vrift(howard_cookies, howard_body)
        mh_vrift.automateHunt()

        time.sleep(600)

if __name__ == "__main__":
    runHornContinuously()

```


