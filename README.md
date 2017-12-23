# RotBot

A bot which does various rot13 related stuff that's very useful for mobile users and stuff.

### Version 1.0.4
* Final version.

### Version 1.0.3
* Fixed the fact that the bot wouldn't work on DMs.
* .rl and .rl n now work on DMs.

### Version 1.0.2
* Bot's token is now stored in a variable before all methods are defined instead of directly inputted in the run() arguments.
* Changed the limit of messages .rl checks from 15 to 100.
* Direct Message behavior has been altered; now rots any text the user DMs the bot, except for .rhelp, which works normally.
* .rhelp command now uses rich embed and is declared before all methods are defined.
* Updated .rhelp command to reflect changes. Also hid information about the .rot command, since it's now superfluous.
