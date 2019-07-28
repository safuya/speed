# Speed

A utility to run speed tests and upload the results to a public Google
Spreadsheet.

## Installation

This application was developed on a Mac and deployed on a Raspberry Pi 3 Model
B. For installation on a Raspberry Pi follow the instructions below:


### On the Raspberry Pi

Install [Raspbian Stretch 10](https://www.raspberrypi.org/downloads/raspbian/).

Install dependencies.

```
sudo apt install libatlas-base-dev
```

Create a new user for the program.

```
sudo useradd speed
```

Make a new directory for your speed programs output.

```
sudo mkdir /var/speed
```

Change the owner for this folder.

```
sudo chown speed:speed /var/speed
```

Change the permissions for this folder to allow read and write access for
speed, but read access for everyone else.

```
sudo chmod 644 /var/speed
```

Clone this repository.

```
git clone something
```

### On your local machine

[Create a service account](https://gspread.readthedocs.io/en/latest/oauth2.html).
These instructions need updating due to a new interface on the Google console,
but I would recommend contributing to an update in the upstream gspread project
instead of making the changes here.

You then need to rename the credentials json file you have downloaded to
`client_secret.json` and put it in the same folder as the rest of the cloned
repository. Copy the contents of this folder to your Raspberry Pi.

```
scp client_secret.json raspberrypi.local:~/speed/
```

### On your Raspberry Pi

Log on to your Raspberry Pi again and move the files to the home directory of
speed.

```
sudo mv speed/* ~/speed/
```

Change the owner of all these files to speed.

```
sudo chown speed:speed /home/speed/*
```

Change to the speed user.

```
sudo su speed
```

Run `crontab -e`, choose your preferred editor and add the following line to
your cron jobs.

```
0 */3 * * * /home/speed/speed.sh
```
