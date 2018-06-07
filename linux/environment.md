[Home Index](/README.md)  
[Linux Home Index](/linux/index.md)  

## Linux Environment

### So what is *environment* in general?  
Let us get out of the computer world and first talk about *weather*.  

#### What is **weather** ?
> Weather is basically the way the atmosphere is behaving, mainly with respect to its effects upon life and human activities. Most people think of weather in terms of:
> 1. temperature
> 1. humidity
> 1. precipitation
> 1. cloudiness
> 1. brightness
> 1. visibility
> 1. wind
> 1. atmospheric pressure, as in high and low pressure  
> Source : https://www.nasa.gov/mission_pages/noaa-n/climate/climate_weather.html

So it means there are a number of factors on which we decide - "how the weather is". 

So if we find the below configuration one day, what can you comment about the weather?

| Variable           | State         |
|:------------------:|:-------------:|
|temperature         | 30 deg.celsius|
|humidity            | high          |
|precipitation       | rain / hail   |
|cloudiness          | black clouds  |
|brightness          | average       |
|visibility          | low           |
|wind                | high / cool   |
|atmospheric pressure| low           |

Answer => It is a `thunder-storm`.


And if we find the below configuration one day, what can you comment about the weather?

| Variable           | State         |
|:------------------:|:-------------:|
|temperature         | 39 deg.celsius|
|humidity            | low           |
|precipitation       | none          |
|cloudiness          | clear sky     |
|brightness          | high          |
|visibility          | really good   |
|wind                | hot           |
|atmospheric pressure| low           |

Answer => It is a `sunny-day`.

If your friend from some other city asks you: *"How is the weather in your city today?"*  
It would too much tedious to say -  
`It is that kind of day when, the temperature is 30 deg.celsius, the humidity is high, the precipitation is rain and hail, the cloudiness is black clouds, the brightness is average, the visibility is low, the wind is high/cool and the atmospheric pressure is low.`

We need one **short and globally understood** terminology.  
It is a `thunder-storm` day.

So as you can see, we have to give **a collective name to the state of weather variables**, for our ease of use.  
This **collective name** is called as an `environment` in linux.


So this draws us to our next question.  
### What are the various linux environments? What all variables do they depend upon?
There is no direct answer to this.  
There is no hard-coded global definition of environment.  
Every organization, have their own set of environments, that are created for internal use.  
All of the organization's members are well aware of the `state` of `variables` under different environments.  

Let us assume an organization which has 3 environments.  
 - `development` : where development happen
 - `testing`     : for testing of the developed applications and catching bugs
 - `production`  : finally where the code is installed to be used by organisation


And they have defined their own variables for various purposes -
1. *DB_DIR* : directory name containing database files and libraries
1. *DB_ADDR* : server-address alias for the actual database hosted
1. *LOG_DIR* : directory name where application logs are to be written 
1. *EXE_DIR* : directory name where the applications are deployed
1. *DATA_DIR* : directory name from where data is to be read/written
1. *TMP_DIR* : a directory for creating intermediate temporary files
1. *MAIL_ID* : email-id on which reports are to be sent
1. *LIMIT*   : number of parallel database connections allowed
1. *CURR_ENV* : current environment, for diagnostic purposes

Here is the `state` of `environment variables` under various `environment`:

|variable|development        |testing             |production          |
|:------:|:-----------------:|:------------------:|:------------------:|
|DB_DIR  |/usr/lib/db/dev    |/usr/lib/db/test    |/usr/lib/db/prod    |
|DB_ADDR |192.208.34.34:7098 |192.208.35.34:1998  |192.200.34.34:1993  |
|LOG_DIR |/usr/log/dev       |/usr/log/test       |/usr/log/prod       |
|EXE_DIR |/usr/bin/dev       |/usr/bin/test       |/usr/bin/prod       |
|DATA_DIR|/usr/share/data/dev|/usr/share/data/test|/usr/share/data/prod|
|TMP_DIR |/tmp/dev           |/tmp/test           |/tmp/prod           |
|MAIL_ID |gtock.dev@gmail.com|gtock.test@gmail.com|gtock.prod@gmail.com|
|LIMIT   |200                |200                 |200                 |
|CURR_ENV|dev                |test                |prod                |

Any variable that is a potential candidate in affecting the `environment` is known as an `environment variable`.  
By convention, the environment variables are stored in upper-case charactors.  
For our sample organization, `LOG_DIR` is an environment variable. Since on changing the variable, the logs would be written in some different place.

> Note :  
> In linux, you can list all the currently set *environment variables* using the command `env`



### What is the use of environment variables? Why one should use them?
For writing scripts that will adapt dynamically on changing the environment.  
In script one has to use `$db_addr` and the script will automatically connect to production database on production environment, development database on development environment, and so on.  

### How to set environment variables?
### How to switch between environments  

### Some common env variables 
(PATH, LD_LIBRARY_PATH, PWD, USER, SHELL, etc)  


