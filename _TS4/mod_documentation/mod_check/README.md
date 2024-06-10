# TS4 Mod Check

This is a very simple mod to list all files in `The Sims 4⁽¹⁾/Mods` and to search for issues like duplicate file names, wrong file locations, ...
The mod does nothing until it's invoked by the user.

It's purpose is to help identifying issues caused by installations placed in wrong folders.

In case you don't want to reveal the DLCs and/or mods you are using don't share the output with anyone or make sure to wipe it before sharing.


`The Sims 4`⁽¹⁾ is a localized folder name which depends on the install language.


## User Cheat Commands

For a user to check things on their own these commands are helpful.

* `o19.mc.lazy` runs most of the commands below in one go.
This will take a while, depending on the number of installed UGC.
Run `o19.mc.reset` afterwards to free the allocated memory. 

* `o19.mc.duplicate_dates` logs all duplicate file names.
Duplicate package files usually do no harm.
Duplicate script files with different versions lead to odd results.
The size and date are logged so one can compare the files without opening the explorer.

* `o19.mc.checksums` compares also the content and will match regardless of the file name.
Obviously tow different script mod versions can't be detected this way.
While `HQ.package`and `-HQ-.package` with the same content will be displayed.
There may be checksum collisions as two completely different files may return the same checksum.

* `o19.mc.inactive` logs script mods which can't work.

* `o19.mc.dlcs` - Log installed DLCs.

* `o19.mc.reset` - Clear all cached data. The commands above cache data and allocate some memory.


## Other cheat commands

* `o19.mc.filenames` - Log all file names to one log line.

* `o19.mc.filetypes` - Log all found file types and file names. One would expect only 'ts4script' and 'package'.

* `o19.mc.filetype_details` - Log the file types and the folders containing them. 
* 
* `o19.mc.duplicate_dates` Logs all duplicate files to one log line.

* `o19.mc.checksums fast_checksums=True|False return_only_duplicates=True|False` - Create checksums for all files and log them.
Default is `o19.mc.checksums (True True)` to read 4 MB to create a checksum instead of the whole file and to return only duplicates.
`o19.mc.checksums False False` reads also 2 GB files completely to create the checksum and logs all files/checksums. This takes quite long.
There may be checksum collisions as two completely different files may return the same checksum.

* `o19.mc.mod_data` - Log mod_data folders and their sub folders but no details about the files.
I store all config information for mods in `The Sims 4⁽¹⁾/mod_data`.
Replacing the `Mods`folder has - as long as my mods are still loaded - no effect on my mods.
Other mod authors store their working data in `The Sims 4⁽¹⁾/Mods/mod_data`. 

* `o19.mc.instance_managers` - Logs all instance managers.

* `o19.mc.reset` - Clear all cached data. The commands above cache data and allocate some memory.





# Addendum

## Game compatibility
This mod has been tested with `The Sims 4` 1.107.151, S4CL 3.4, TS4Lib 0.3.20 (2024-05).
It is expected to be compatible with many upcoming releases of TS4, S4CL and TS4Lib.

## Dependencies
Download the ZIP file, not the sources.
* [This Mod](../../releases/latest)
* [TS4-Library](https://github.com/Oops19/TS4-Library/releases/latest)
* [S4CL](https://github.com/ColonolNutty/Sims4CommunityLibrary/releases/latest)
* [The Sims 4](https://www.ea.com/games/the-sims/the-sims-4)

If not installed download and install TS4 and these mods.
All are available for free.

## Installation
* Locate the localized `The Sims 4` folder which contains the `Mods` folder.
* Extract the ZIP file into this `The Sims 4` folder.
* It will create the directories/files `Mods/_o19_/$mod_name.ts4script`, `Mods/_o19_/$mod_name.package`, `mod_data/$mod_name/*` and/or `mod_documentation/$mod_name/*`
* `mod_logs/$mod_name.txt` will be created as soon as data is logged.

### Manual Installation
If you don't want to extract the ZIP file into `The Sims 4` folder you might want to read this. 
* The files in `ZIP-File/mod_data` are usually required and should be extracted to `The Sims 4/mod_data`.
* The files in `ZIP-File/mod_documentation` are for you to read it. They are not needed to use this mod.
* The `Mods/_o19_/*.ts4script` files can be stored in a random folder within `Mods` or directly in `Mods`. I highly recommend to store it in `_o19_` so you know who created it.

## Usage Tracking / Privacy
This mod does not send any data to tracking servers. The code is open source, not obfuscated, and can be reviewed.

Some log entries in the log file ('mod_logs' folder) may contain the local username, especially if files are not found (WARN, ERROR).

## External Links
[Sources](https://github.com/Oops19/)
[Support](https://discord.gg/d8X9aQ3jbm)
[Donations](https://www.patreon.com/o19)

## Copyright and License
* © 2024 [Oops19](https://github.com/Oops19)
* License for '.package' files: [Electronic Arts TOS for UGC](https://tos.ea.com/legalapp/WEBTERMS/US/en/PC/)  
* License for other media unless specified differently: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) unless the Electronic Arts TOS for UGC overrides it.
This allows you to use this mod and re-use the code even if you don't own The Sims 4.
Have fun extending this mod and/or integrating it with your mods.

Oops19 / o19 is not endorsed by or affiliated with Electronic Arts or its licensors.
Game content and materials copyright Electronic Arts Inc. and its licensors. 
Trademarks are the property of their respective owners.

### TOS
* Please don't put it behind a paywall.
* Please don't create mods which break with every TS4 update.
* For simple tuning modifications use [Patch-XML](https://github.com/Oops19/TS4-PatchXML) 
* or [LiveXML](https://github.com/Oops19/TS4-LiveXML).
* To check the XML structure of custom tunings use [VanillaLogs](https://github.com/Oops19/TS4-VanillaLogs).
