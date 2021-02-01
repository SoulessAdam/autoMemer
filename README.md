# autoMemer
Automated script/program for sending basic dank memer commands, made in 5 minutes with minimal effort and no concern for efficiency or a tidy code base. Written in python, uses basic libraries included in the default installation, built for windows however can be easily reproduced or edited to work on other platforms.

## Instructions for use: 
### Intercepting a good post request:
* Using a tool like Fiddler, Burp or general network debugging tools your browser may have included, intercept a successful POST request method spawned from sending a message.
* Extract the necessary info and add it to the python script (config file and setup on first run coming soon). The main info you will need is:
  * Your authentication token for sending messages e.g. authorization: {Token here} in your POST headers.
  * The request url, used to specify which channel messages are sent to e.g. https://discord.com/api/v8/channels/####################/messages
* Fill in the necessary information in the script and run

### General use:
* Use this tool whenever necessairy, you may run multiple instances all with different auth tokens allowing you to bot on many accounts at once, however, the spamming of the Discord API will not only cause flags but will result in a pretty quick rate limit. 
* It is advised you obtain the following items before use:
  * Hunting Rifle
  * Laptop
  * Fishing Pole
  * Lifesavers (Random Events may kill you, be wary, this is a precautionary item)

* To stop the script use the Keyboard Interrupt shortcut, ``Control``+``C`` to stop, or close the Python window.


###### By using this tool you aknowledge that you are at risk of punishment from Dank Memer and/or Discord. I am not responisble for any losses or punishment you recieve, it is your choice to use this tool and your responsibility to keep use of said tool covert, unsuspicious and unknown to those you do not trust, in order to avoid bans. 
