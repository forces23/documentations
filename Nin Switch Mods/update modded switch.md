things needed is hekate, atmosphere, fusee.bin, sigpatches, appstore, switch firmware.

# Fresh Install / Updating Modded Switch

## Hekate

Go to [Hekates Github](https://github.com/ctcaer/hekate/releases) and grab the latest releases

* download hekate it should look something like this : `hekate_ctcaer_x.x.x_Nyx_x.x.x.zip`

once downloaded

1. extract the hekate zip somewhere on your desktop for easy access
2. drag the `bootloader` and `hekate_ctcaer_x.x.x.bin` folders over to the root of the sd card
3. drag the fusee.bin file over to the root of the sd card

## Atmosphere

Go to [Atmosphere Github](https://github.com/Atmosphere-NX/Atmosphere/releases) and grab the latest releases

* download atmosphere it should look something like this : `atmosphere-x.x.x-master-xxxxxxxx+hbl-x.x.x+hbmenu-x.x.x.zip`
* download `fusee.bin` file

Once downloaded

1. extract the atmosphere zip somewhere on your desktop for easy access
2. drag the `/atmosphere `and /`switch `folders over to the root of the sd card
3. drag the `fusee.bin` file over to the root of the sd card
4. navigate to `/bootloader/payloads` and dump the `fusee.bin` in here

## SigPatches

Go to the [SigmaPatches](https://sigmapatches.su/) site and grab the latest sigpatches

* once in the site find DOWNLAOD SIGPATCHES and click on it the zip should start downloading

Once downloaded

1. extract sigpatches zip somewhere on the desktop for easy access
2. drag the `/atmosphere`, /`bootloader` and `/switch` folders over to the root of the sd card

after that you should have the latest sigpatches

## HomeBrew Appstore

Go to the [HB Appstore GitHub](https://github.com/fortheusers/hb-appstore/releases) and download the lates HB Appstore nro file

once download

1. in the sd card navigate to the `/switch` folder and create a folder called `appstore`
2. after creating the `appstore` folder drag and drop the `appstore.nro` file into the `appstore` folder

# Creating emuMMC

1. In Hekate go to emuMMC
2. tap on Create emuMMC
3. tap on SD Partition
4. tap Continue
5. tap Continue
6. in Partition Manager for OLED go to as far as you can which is 58 GiB
7. tap Start
8. press POWER to continue
9. tap OK
10. tap Close(top left)
11. click on Create emuMMC again
12. tap part 1
13. wait for it to finish
14. once done tap on close(top  left)
15. if done correctly you should see under "emuMMC Info & Selection", Enabled!

# Create NAND Backup

1. Go to "Tools" (top middle)
2. tap on Backup eMMC
3. tap "eMMC BOOT0 & Boot1"
4. once it is complete tap on close(top left)
5. then tap on "eMMC RAW GPP"
6. this will take a while let it work and then once finish tap on close(top left)
7. once this is all complete you will want to store this back up in secure location on your computer

# Grab the Prod key file

Go to the [SigmaPatches](https://sigmapatches.su/) site and grab the latest lockpick_RCM

1. once downloaded extract to desktop for easy access
2. add the `Lockpick_RCM_vx.x.x` to the `/bootloader/payloads` folder
3. eject the switch/SD card from the computer
4. on the home screen tap on payloads and tap on the LockPick file
5. make sure you are on the option that say "DUMP from SysNAND"
6. this will dump the Prod.keys file to your switch folder
7. go back to lockpick menu home
8. navigate to reboot option
9. after that connect switch or insert sd card into the computer
10. dump the keys in the same area as the backup you created above.

# Switch FirmWare

whether you need to downgrade or want to upgrade the switch firmware these are the steps

1. navigate to the [darthsternie ](https://darthsternie.net/switch-firmwares/)site to grab the firmware you want
2. extract to the desktop for easy access
3. drap and drop the folder to the root of the sd card
4. disconnect from the computer or eject sd card and place back into switch
5. launch the CFW symmc
6. navigate to homebrew
7. launch the daybreak app
8. click on the folder and let it validate
9. after validation go ahead and continue
10. click preserve settings
11. click install (FAT32 + exFAT)
12. lastly click continue and let it install
13. after install make sure you reboot

# Specail Links for the switch

1. [HomeBrew Appstore](https://hb-app.store/)

# Apps to download for the switch

[What is on my Modded Nintendo Switch 2024 (Atmosphere 18.0.0)](https://www.youtube.com/watch?v=YdUhCVJ5Z6s&list=WL&index=77)

1. JKSV: Save manager for backing up saves. At least one game messed up their save system at some point and can corrupt your save through no fault of your own. Also has other creative uses for trading with an emu when playing pokemon or certain other games.
2. Daybreak: For upgrading your emunand firmware without burning fuses for newer models. Or just being able to upgrade at all for v1 erista without having to worry about turning off 90dns.
3. FTPDb: For managing sd card files over the network. Far slower than usb, but if you only need to manage smaller files, the speed loss is negligible.
4. Edizon: Cheating tool. I mainly use it for skipping grind-heavy game sections. Look into the edizon overlay, which goes with the tesla overlay.
5. Tesla overlay. Needed to make edizon overlay work. Also used by some other tools not listed here with their overlays.
6. RetroArch, to turn your switch to a one-stop retro arcade and emulation station.
7. Ldn_mitm, to play online games with other modders and emu players because you can't go online on a modded switch on cfw without getting it banned.
