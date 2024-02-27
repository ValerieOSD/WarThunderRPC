# WarThunder Discord Rich Presence (RPC)

## About

**This is a external application which adds War Thunder as a Discord Rich Presence application. \[1].**

\[1] This application **pulls in-game information from War Thunder through Port 8111**.
War Thunder outputs some in-game data to 127.0.0.1:8111 and it's subfolders automatically on all machines. There really isn't much to go off and it's pretty awfully structured, but it makes do for now.
This application modifies in no way whatsoever any data from the game, it is completely safe and will not get you banned.

### Requirements (The runtime comes pre-embedded into the .EXE, you do *not* need to download this. It's only for debugging.)

 - [Python 3.11+](https://www.microsoft.com/store/productId/9NRWMJP3717K?ocid=pdpshare)

### Features

  - Shows if you are in the hangar, in a match, or in a test drive.
  - Shows what map you are in.
  - Detects what vehicle you are using.
  - Displays simple match statistics (Air or Ground, Domination or Conquest, etc).

Unfortunately some modes or vehicles aren't supported due to how the data is structured from the game itself,
Naval vehicles show no data and will not work, it will show up as "Unknown vehicle".

Your status might show up as "test drive" or that you are flying a "DUMMY_PLANE" during the first few seconds of a match, this is as far as I know unavoidable for now, but it should fix itself once you load in. :)

## Development

I'm working on this myself, as an amateur in Python, please feel free to contribute and reach out to me if you have any suggestions, feedback or ideas!
