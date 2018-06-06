## Linux and Environment

#### So what is *environment* in general?  
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
#### What are the various linux environments? What all variables do they depend upon?
There is no direct answer to this.  
There is no hard-coded global definition of environment.  
Every organisation, have their own set of environments, that are created for internal use.  
All of the organisation's members are well aware of the `state` of `variables` under different environments.  

Let us assume an organization which has 3 environments.  
 - `development` : where development happen
 - `testing`     : for testing of the developed applications and catching bugs
 - `production`  : finally where the code is installed to be used by organisation
 
And they have defined their own variables for various purposes -
1. *db_dir* : directory name containing database files and libraries
1. *log_dir* : directory name where application logs are to be written 
1. *exe_dir* : directory name where the applications are deployed
1. *data_dir* : directory name from where data is to be read/written
1. *tmp_dir* : a directory for creating intermediate temporary files
1. *mail_id* : email-id on which reports are to be sent
 
|variable|development        |testing             |production          |
|:------:|:-----------------:|:------------------:|:------------------:|
|db_dir  |/usr/lib/db/dev    |/usr/lib/db/test    |/usr/lib/db/prod    |
|log_dir |/usr/log/dev       |/usr/log/test       |/usr/log/prod       |
|exe_dir |/usr/bin/dev       |/usr/bin/test       |/usr/bin/prod       |
|data_dir|/usr/share/data/dev|/usr/share/data/test|/usr/share/data/prod|
|tmp_dir |/tmp/dev           |/tmp/test           |/tmp/prod           |
|mail_id |gtock.dev@gmail.com|gtock.test@gmail.com|gtock.prod@gmail.com|

So now what is the next step?


Environment  
What is an environment variable  
use some common env variables (PATH, LD_LIBRARY_PATH, PWD, USER, SHELL, etc)  
What is an environment? Why do we use them?  
How to switch between environments  

