# pythonWebsiteBlocker

It blocks given websites' url for a set duration of time.

### Clone the project
```
git clone https://github.com/rajeshtezu90/pythonWebsiteBlocker.git
```

### Usage for Windows user
* Edit the code and set the "startTime" and "endTime" variable's value according to your need. Also set websites url which
you want to be blocked to website_list variable.
* Change the file name with .pyw extension, so this code could run in the background.
* Create a Task Schedular with highest privilege for this program for at the startup of computer.

### usage for Mac/Linux user
* Edit the code and set the "startTime" and "endTime" variable's value according to your need. Also set websites url which
you want to be blocked to website_list variable.
```
$sudo crontab -e
```
Now insert the following at the bottom of opened file
```
@reboot python3 <path to websiteBlocker.py>
Eg: @reboot python3 /home/rajesh/Python3Env/pythonWebsiteBlocker/websiteBlocker.py
```

