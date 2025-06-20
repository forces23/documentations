# Home Server

##### Things ill need to do

* [ ] install windows 11
* [ ] install CasaOS
  * [ ] install Prowlarr
  * [ ] install Radarr
  * [ ] install Sonarr
  * [ ] install Flaresolverr
  * [ ] install Qbittorrent
  * [ ] install Plex Server
  * [ ] install Cloudflare
  * [ ] install Overseerr

##### Things That Should Be Behind A VPN :

* prowlarr
* Qbittorrent


##### In Depth Guide

* [TRaSH Guides](https://trash-guides.info/)
* [Servarr Wiki](https://wiki.servarr.com/)


# Setting Up FlareSolverr

create the docker container in CasaOS by:

1. navigating to the **+** icon in the top right corner of the apps section
2. click on **install a customized app**
3. Docker image: `ghc.io/flaresovlerr`
4. Tag: `latest`
5. Title: `FlareSolverr`
6. Icon URL: `<should auto poputlate>`
7. Web UI:
   * URL: `<should stay empty>`
   * PORT: `8191`
8. Host: `8191`
9. Contianer: `8191`
10. Protocol: `TCP`
11. Container Name: `Flaresolverr`
12. Click **Save**

##### Adding As Indexer Proxy in Prowlarr

After the actuall docker container is set up then you want to go into Prowlarr and add it as a **Indexer Proxy**

1. go to prowlarr
2. navigate to settings
3. click on indexers
4. click on the + (add) button/box
5. Name: Flaresolverr
6. Tags: flaresolverr
7. Host: `http://<host ip>:8191/`
   * host url should be the ip of the server
8. click test to make sure it connects
9. then click save

# Setting Up Prowlarr

will need to set up a few areas in the casaos app and within prowlarr in here:

in casaos: the settings should be pre configured theres nothing you should need to do here

within Prowlarr:

* indexers, indexers in settings, apps, downlaod clients, proxy

to install Prowlarr just go to the app store and search prowlarr and click install

### Indexers

indexers are basically the torrent sites you need to add them so that you are able to search for movies and tv shows and download them

if indexers are not showing up you can add custom indexers:

https://github.com/Prowlarr/Indexers/tree/master/definitions/v11

https://www.reddit.com/r/prowlarr/comments/y23ut2/custom_indexers_defintions/

Inside Prowlarr:

##### Configure Indexer Proxy

1. navigate to settings
2. go to indexers
3. and follow the steps for **Adding As Indexer Proxy** in **setting up flaresolverr**


##### Adding a Indexer

1. go to Indexers (should be the first option in the navigation pane in the left)
2. click the `+ Add `Indexer to add indexer
3. find the indexer you want to add
4. it'll open a window. theres nothing you need to do here most of the time but there are some indexers that need flaresolverr to work. to use attach flaresolverr to the indexer scroll down in this window and in Tags put the tag you gave flaresolverr so for my case i would put `flaresolverr`.
5. after adding the tag click test
6. then click save

##### Trusted Indexers

* EZTV
* Torrentz2nz
* YTS
* 1337x

### Adding Applications

here is where you add radarr and sonarr to prowlarr

1. navigate to settings
2. go to Apps
3. click the + block/box
4. find the one you want to add - Radarr
5. here you need to fill out all the information that connects it to radarr and prowlarr
   * Name: `Radarr`
   * Prowlarr Server: `http://host ip:9696`
   * Radarr: `http://host ip:7878`
   * API Key: `found in radarr >> settings >> General >> API Key`
   * click test to make sure it connects
   * then click save
6. repeat steps 4 and 5 to add Sonarr

### Adding a Download Client

1. go to **Settings**
2. go to **Download Clients**
3. click the **+** block/box
4. a window will pop up select the download client you would like to use/set up. In my case I am using qBittorrent
5. another window will pop up where you'll need to enter in all the details to connect to qBittorrent. some info is already populated.
   * Name: `qBittorrent`
   * Enabled: `make sure that it is enabled`
   * Host: `<host ip>`
   * Port: `8181`
   * UserName: `<username used to login into qbittorrent>`
   * Password: `<passwoerd used to login into qbittorent>`
   * Default Category: `prowlarr`
6. click test to make sure connection is successful
7. click save

# Setting Up Radarr

Settings in CasaOS:

1. navigate to the application conatiner settings by hovering over the app and clicking on the 3 dots in the top right corner
2. once in here scroll down to Volumes
3. here you need to add the locations of the movies and downloads folders that are in the mounted hdd

   * Example :
   * Host: `/mnt/Storage1/media/movies`      |   Contaier:`/Storage1/media/movies`
   * Host: `/mnt/Storage1/media/downlaods`  |   Contaier: `/Storage1/media/downloads`

### Configure Media Managment

add the path to the movies folder in here and set the formats

### Configure Profiles

### Configure Quality

### Create Custom Formats

### Indexers should get pulled automatically from prowlarr

### set up the download client

### Configure Import List: Plex Watchlist

### Configure Connections : Plex Media Server


# Setting Up Sonarr

SAME AS RADARR ESSENTIALLY

Settings in CasaOS:

1. navigate to the application conatiner settings by hovering over the app and clicking on the 3 dots in the top right corner
2. once in here scroll down to Volumes
3. here you need to add the locations of the tv shows and downloads folders that are in the mounted hdd

   * Example :
   * Host: `/mnt/Storage1/media/tvshows`      |   Contaier:`/Storage1/media/tvshows`
   * Host: `/mnt/Storage1/media/downlaods`  |   Contaier: `/Storage1/media/downloads`

### Configure Media Managment

add the path to the tvshows folder in here and set the formats

### Configure Profiles

### Configure Quality

### Create Custom Formats

### Indexers should get pulled automatically from prowlarr

### set up the download client

### Configure Import List: Plex Watchlist

### Configure Connections : Plex Media Server


# Setting Up qBittorrent

Settings in CasaOS:

1. navigate to the application conatiner settings by hovering over the app and clicking on the 3 dots in the top right corner
2. once in here scroll down to Volumes
3. here you need to add the locations of the media folder that is in the mounted hdd

   * Example :
   * Host: `/mnt/Storage1/media`      |   Contaier:`/Storage1/media`


# Setting Up Plex Media Server

Settings in CasaOS:

1. navigate to the application conatiner settings by hovering over the app and clicking on the 3 dots in the top right corner
2. once in here scroll down to Volumes
3. here you need to add the locations of the media folder that is in the mounted hdd

   * Example :
   * Host: `/mnt/Storage1/media`      |   Contaier:`/Storage1/media`



# Setting Up Overseerr

Settings in CasaOS:

1. navigate to the application conatiner settings by hovering over the app and clicking on the 3 dots in the top right corner
2. once in here scroll down to Volumes
3. here you need to add the locations of the media folder that is in the mounted hdd
   * Example :
   * Host: `/mnt/Storage1/media`      |   Contaier:`/Storage1/media`




# Setting Up Cloudflared (optional)

Settings in CasaOS:

1. navigate to the application conatiner settings by hovering over the app and clicking on the 3 dots in the top right corner
2. once in here scroll down to Volumes
3. here you need to add the locations of the media folder that is in the mounted hdd
   * Example :
   * Host: `/mnt/Storage1/media`      |   Contaier:`/Storage1/media`
