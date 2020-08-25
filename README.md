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
```
virtualenv venv
cd venv/Scripts
activate
cd ..
cd ..
pip install -r requirements.txt
```

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

# Quest Files
This section will elaborate in detail the configurations required to use the quest files.

## Labyrinth
In Labyrinth, user is required to have 5-10 shuffler's cube to enable shuffling of the doors. User will need to define the doors to enter in order of preference. The doors are:

Fealty - Epic Fealty (y3), Superior Fealty (y2), Plain Fealty (y)
Scholar - Epic Scholar (s3), Superior Scholar (s2), Plain Scholar (s)
Tech - Epic Tech (h3), Superior Tech (h2), Plain Tech (h)

Each door comes with 3 lenght variations, they are short (s), medium (m), or long (l).  The choice of door in order of preference will be [doorname][length]. For example

1. Long Epic Fealty - y3l
2. Short Epic Fealty - y3s
3. Medium Superior Tech - h3m
4. Short Superiod Tech - h2s

List the preferred doors in order of descending preference, and pass it as an array to the automateHunt method. For example, if the preferred door is `['y3l','y3m','y3s','y2l', 'y2m', 'y2s', 'yl', 'ym', 'ys']`, the corresponding method to activate is as below. The algorithm shuffles the door when the preferred door is not found.


```
mh_labyrinth = Labyrinth(acc2_cookies, acc2_body, debug=True)
mh_labyrinth.automateHunt(['y3l','y3m','y3s','y2l', 'y2m', 'y2s', 'yl', 'ym', 'ys'])
```
