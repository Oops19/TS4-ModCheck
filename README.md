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




---

# 📝 Addendum

## 🔄 Game compatibility
This mod has been tested with `The Sims 4` 1.121.342, S4CL 3.17, TS4Lib 0.3.42.
It is expected to remain compatible with future releases of TS4, S4CL, and TS4Lib.

## 📦 Dependencies
Download the ZIP file - not the source code.
Required components:
* [This Mod](../../releases/latest)
* [TS4-Library](https://github.com/Oops19/TS4-Library/releases/latest)
* [S4CL](https://github.com/ColonolNutty/Sims4CommunityLibrary/releases/latest)
* [The Sims 4](https://www.ea.com/games/the-sims/the-sims-4)

If not already installed, download and install TS4 and the listed mods. All are available for free.

## 📥 Installation
* Locate the localized `The Sims 4` folder (it contains the `Mods` folder).
* Extract the ZIP file directly into this folder.

This will create:
* `Mods/_o19_/$mod_name.ts4script`
* `Mods/_o19_/$mod_name.package`
* `mod_data/$mod_name/*`
* `mod_documentation/$mod_name/*` (optional)
* `mod_sources/$mod_name/*` (optional)

Additional notes:
* CAS and Build/Buy UGC without scripts will create `Mods/o19/$mod_name.package`.
* A log file `mod_logs/$mod_name.txt` will be created once data is logged.
* You may safely delete `mod_documentation/` and `mod_sources/` folders if not needed.

### 📂 Manual Installation
If you prefer not to extract directly into `The Sims 4`, you can extract to a temporary location and copy files manually:
* Copy `mod_data/` contents to `The Sims 4/mod_data/` (usually required).
* `mod_documentation/` is for reference only — not required.
* `mod_sources/` is not needed to run the mod.
* `.ts4script` files can be placed in a folder inside `Mods/`, but storing them in `_o19_` is recommended for clarity.
* `.package` files can be placed in a anywhere inside `Mods/`.

## 🛠️ Troubleshooting
If installed correctly, no troubleshooting should be necessary.
For manual installs, verify the following:
* Does your localized `The Sims 4` folder exist? (e.g. localized to Die Sims 4, Les Sims 4, Los Sims 4, The Sims 4, ...)
  * Does it contain a `Mods/` folder?
    * Does Mods/_o19_/ contain:
      * `ts4lib.ts4script` and `ts4lib.package`?
      * `{mod_name}.ts4script` and/or `{mod_name}.package`
* Does `mod_data/` contain `{mod_name}/` with files?
* Does `mod_logs/` contain:
  * `Sims4CommunityLib_*_Messages.txt`?
  * `TS4-Library_*_Messages.txt`?
  * `{mod_name}_*_Messages.txt`?
* Are there any `last_exception.txt` or `last_exception*.txt` files in `The Sims 4`?


* When installed properly this is not necessary at all.
For manual installations check these things and make sure each question can be answered with 'yes'.
* Does 'The Sims 4' (localized to Die Sims 4, Les Sims 4, Los Sims 4, The Sims 4, ...) exist?
  * Does `The Sims 4` contain the folder `Mods`?
    * Does `Mods` contain the folder `_o19_`? 
      * Does `_19_` contain `ts4lib.ts4script` and `ts4lib.package` files?
      * Does `_19_` contain `{mod_name}.ts4script` and/or `{mod_name}.package` files?
  * Does `The Sims 4` contain the folder `mod_data`?
    * Does `mod_data` contain the folder `{mod_name}`?
      * Does `{mod_name}` contain files or folders?
  * Does `The Sims 4` contain the `mod_logs` ?
    * Does `mod_logs` contain the file `Sims4CommunityLib_*_Messages.txt`?
    * Does `mod_logs` contain the file `TS4-Library_*_Messages.txt`?
      * Is this the most recent version or can it be updated?
    * Does `mod_logs` contain the file `{mod_name}_*_Messages.txt`?
      * Is this the most recent version or can it be updated?
  * Doesn't `The Sims 4` contain the file(s) `last_exception.txt`  and/or `last_exception*.txt` ?
* Share the `The Sims 4/mod_logs/Sims4CommunityLib_*_Messages.txt` and `The Sims 4/mod_logs/{mod_name}_*_Messages.txt`  file.

If issues persist, share:
`mod_logs/Sims4CommunityLib_*_Messages.txt`
`mod_logs/{mod_name}_*_Messages.txt`

## 🕵️ Usage Tracking / Privacy
This mod does not send any data to external servers.
The code is open source, unobfuscated, and fully reviewable.

Note: Some log entries (especially warnings or errors) may include your local username if file paths are involved.
Share such logs with care.

## 🔗 External Links
[Sources](https://github.com/Oops19/)
[Support](https://discord.gg/d8X9aQ3jbm)
[Donations](https://www.patreon.com/o19)

## ⚖️ Copyright and License
* © 2020-2025 [Oops19](https://github.com/Oops19)
* `.package` files: [Electronic Arts TOS for UGC](https://tos.ea.com/legalapp/WEBTERMS/US/en/PC/)  
* All other content (unless otherwise noted): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 

You may use and adapt this mod and its code — even without owning The Sims 4.
Have fun extending or integrating it into your own mods!

Oops19 / o19 is not affiliated with or endorsed by Electronic Arts or its licensors.
Game content and materials © Electronic Arts Inc. and its licensors.
All trademarks are the property of their respective owners.

## 🧾 Terms of Service
* Do not place this mod behind a paywall.
* Avoid creating mods that break with every TS4 update.
* For simple tuning mods, consider using:
  * [Patch-XML](https://github.com/Oops19/TS4-PatchXML) 
  * [LiveXML](https://github.com/Oops19/TS4-LiveXML).
* To verify custom tuning structures, use:
  * [VanillaLogs](https://github.com/Oops19/TS4-VanillaLogs).

## 🗑️ Removing the Mod
Installing this mod creates files in several directories. To fully remove it, delete:
* `The Sims 4/Mods/_o19_/$mod_name.*`
* `The Sims 4/mod_data/_o19_/$mod_name/`
* `The Sims 4/mod_documentation/_o19_/$mod_name/`
* `The Sims 4/mod_sources/_o19_/$mod_name/`

To remove all of my mods, delete the following folders:
* `The Sims 4/Mods/_o19_/`
* `The Sims 4/mod_data/_o19_/`
* `The Sims 4/mod_documentation/_o19_/`
* `The Sims 4/mod_sources/_o19_/`
