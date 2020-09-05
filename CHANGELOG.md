# Changelog

## Version 2.1 9/4/2020

### Added Support for Shiny Pokemon

### Updates
 - Shiny Pokemon will now be recognized by the bot.
 - When a shiny Pokemon spawns (whether you catch it or not) it will be logged in the console.
 - If you do manage to capture the shiny Pokemon, a special image will be printed to the console!

## Version 2.0 7/2/2020

### Autocatcher is now FIXED.

### Updates
 - Added ``eval`` command so that you can use any mania command. It appends the string after the command to the configured prefix for the server.
 - sb!eval trade @user -> < guild prefix >trade @user
 - Added prompts for changing varibales without having to restart the bot. These will be fully implemented in the next update.
 - Added prompts for configuration of unknown/unconfigured guilds with the bot. 
 - Added more security around who is able to type commands and control the bot.
 - Removed catch chance temporarily, it will be reintroduced in a later update.
 - Started to set up a better system for hardcoding exceptions to the pokemon name finding method
 - Exception catching is now used in a signifncant portion of the code
 - Improved the response time/limit of fake responses when catching



## Version 1.3.1 6/30/2020

### Updates
 - Created changelog, documentedchanges over time

## Version 1.3 6/29/2020

### Updates
 - Added chance mechanic to autocatching
 - Added checks for autocatching value

## Version 1.2 6/28/2020

### Updates
 - Added a series of checks on the config file to prevent errors.
 - Added checks to prevent EmptyEmbed errors.
 - The bot will now suggest you change certain values/let you know if values are not configured at all.

## Version 1.1 6/27/2020

### Updates
 - Support for Alolan and Galarian Pokemon autocatching added.
 - You can set a Pokeball type to catch with in ``setup.py``. 
 - Changed the logic/added more checks to prevent common errors
 - When out of Pokeballs, the bot will buy a configurabela amount of balls. The default value is 5 and can be changed in ``setup.py``.
 - Added support for catching and logging in multiple servers.
 - Added check to make sure you can only autocatch in a configured server. 
 - Added check to make sure only the selfbot owner can use any commands.
 
### Bugs
- Improve the amount and quality of search results
- Write documentation in ``README.md``


## Version 1.0 6/26/2020

### Initial Release!

- Initial Release!
- Autocatching for PokeMania
- Webpage Report detailing the bot's progress in the current session
- Randomly triggered dialogue upon catching/escaping/incorrect name events 
- ``nh!viewer <code>`` is used to view doujins. Two emojis are used to naviagte through the pages. 

### BUGS
 - Alolan/Galar forms do not work
 - Several pokemon need to be hardcoded, only one (flabebe) has been done so far
 - Incorrect name code is very error prone
