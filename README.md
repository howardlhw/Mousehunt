# Mousehunt

Python scripts for making our mouse hunting lives easier. A few selected hunting locations have been built due to the additional human-input requirement during hunting.

# Disclaimer

Note that using the bot to automate any processes is against the Mousehunt's gameplay rules and may result in the termination of the account. We do not take any responsibilities if your account has been impacted by using the following scripts.

This project is intended for hobby and coding practices only.

# Quick Overview

To use this application, make sure you have python 3 installed on your computer. Install virtual environment and the additional dependencies.

```
python app.py
```

Execute the application by running app.py. You will need to update the file with your cookies and unique hash.

```
user = {
    'HG_TOKEN': [YOUR_TOKEN_HERE],
    'uh': [YOUR_UNIQUE_HASH_HERE]
}
```

The following hunting locations have been built

-   Labyrinth
-   Bristle Woods Rift
-   Valor Rift

Execute the code with:

```
mh_bwrift = BWrift(user)
mh_bwrift.automateHunt()
```

# Detailed Usage

## Step 1 - Creating Virtual Environmnet

If you have not installed virtualenv, install by by executing `pip install virtualenv`

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

This is the location of token, it is stored as a cookie.
![Image of token](https://raw.githubusercontent.com/howardlhw/Mousehunt/master/images/token.png)

This is how you get the unique hash (uh). It is stored as as a response from http requsest.
![Image of hash](https://raw.githubusercontent.com/howardlhw/Mousehunt/master/images/unique_hash.png)

## Step 3 - Configuring app.py

Use a text editor to edit app.py. Update the token, and unique hash.

```
user = {
    'HG_TOKEN': [YOUR_TOKEN_HERE],
    'uh': [YOUR_UNIQUE_HASH_HERE]
}
```

## Step 4 - Executing script

Update the following section with the updated codes. The instance will run automatically when automateHunt is called. The parameters of automate hunt to pass into can be found in the respective sections.

```
def runHornContinuously():
    while True:
        mh_vrift = Vrift(user)
        mh_vrift.automateHunt()

        time.sleep(600)

if __name__ == "__main__":
    runHornContinuously()
```

# Quest Files

This section will elaborate in detail the configurations required to use the quest files.

## Labyrinth

In Labyrinth, user is required to have 5-10 shuffler's cube to enable shuffling of the doors. User will need to define the doors to enter in order of preference. The doors are:

-   Fealty - Epic Fealty (y3), Superior Fealty (y2), Plain Fealty (y)
-   Scholar - Epic Scholar (s3), Superior Scholar (s2), Plain Scholar (s)
-   Tech - Epic Tech (h3), Superior Tech (h2), Plain Tech (h)

Each door comes with 3 lenght variations, they are:

-   short (s)
-   medium (m)
-   long (l)

The name of the choice of door will be [doorname][length]. For example

-   Long Epic Fealty - y3l
-   Short Epic Fealty - y3s
-   Medium Superior Tech - h3m
-   Short Superiod Tech - h2s

List the preferred doors in order of descending preference, and pass it as an array to the automateHunt method. For example, if the preferred door is `['y3l','y3m','y3s','y2l', 'y2m', 'y2s', 'yl', 'ym', 'ys']`, the corresponding method to execute is as below. The algorithm shuffles the door when the preferred door is not found.

```
mh_labyrinth = Labyrinth(user)
mh_labyrinth.automateHunt(['y3l','y3m','y3s','y2l', 'y2m', 'y2s', 'yl', 'ym', 'ys'])
```

## Bristle Woods Rift

In Bristle Woods Rift, user input is required for the following actions.

1. Toggling of Quantum Quarts
2. Chance of Traps
3. Change of Cheese
4. Portal selection
5. Scramble portals

The algorithm is designed to optimize cost and maximize yield. It is recommended to have at least 40 Quantum Quarts and 10 Portal Scramblers (option) to use the script.

**Configure Trap Setup in each chamber**

User can configure whether to use Quantum Quarts, type of cheese and type of charm to use in each chamber by configuring the bwrift_config.py. Configuration is required. You can also use the default configuration.

```
'security_chamber': {
    'quantumQuarts': True,
    'bait': 'magical_string_cheese',
    'trinket': 'rift_vacuum_trinket'
}
```

The following choices of bait and charma are available:
Cheese Options (bait)

-   brie_string_cheese
-   runic_string_cheese
-   ancient_string_cheese

Charm Options (trinket)

-   rift_vacuum_trinket
-   super_rift_vacuum_trinket
-   rift_trinket

The chambers are selected automatically based on the user's stats. **This is still work in progress**.

Execute the code by:

```
mh_bwrift = BWrift(user)
mh_bwrift.automateHunt()
```

## Valour Rift

In Valour Rift, the user input comes in during the toggling of Champion's Fire. Champion's fire is activated on Floor 8 and deactivated on every other floor.

Execute the code by:

```
mh_vrift = Vrift(user)
mh_vrift.automateHunt()
```
