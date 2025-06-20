# CloudFlare Setup

## Get a Registered Domain Name

i used [namecheap](www.namecheap.com) but there are many places you can get a domain name

Places to Get domain Names:

* [namecheap](www.namecheap.com)
* [SquareSpace Domains](https://domains.squarespace.com/)
* [BlueHost](https://www.bluehost.com/domains)

## Create a CloudFlare Account and Setup

follow this video created by NetworkChuck

[EXPOSE your home network to the INTERNET!! (it&#39;s safe)](https://www.youtube.com/watch?v=ey4u7OUAF3c)

the only difference is that when you go to tie it to your casaOS container for cloudflare these are the steps:

in the Zero Trust >> Networks >> Tunnels >> `<your tunnel>` >> overview slect either debian or linux and grab the code where it says "If you already have cloudflared installed on your machine". this is what you will paste into the casaos cloudflare conatiner webui

Note: you'll paste the entire thing including the "sudo cloudflare service install"

## Create Subdomains in Cloudflare

## Connect CloudFlare Tunnel to the casaos container

go to casaos appstore and install the cloudflare container app after done installing as mentioned above in Create a CloudFlare Account and Setup section, paste the connector script into the input bar



## Navigating CloudFlare site

##### To get to tunnels

this is where you create your tunnel and add subdomains to your tunnel 

From Dashboard >> Zero Trust >> Networks >> Tunnels


## Navigating NameCheap

pretty easy to navigate its straight forward.

my domains are in dDomain List 


references

1. [EXPOSE your home network to the INTERNET!! (it&#39;s safe)](https://www.youtube.com/watch?v=ey4u7OUAF3c)
