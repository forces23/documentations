# NextCloud CasaOS Setup/Information

---

## Volume Setup:

make sure to change the source paths to the preferred memory locations

currently i have the user data (not user profile) saving to a mnt drive (HDD) and everything else storred on the os drive (NVMe) since its faster

### CRON

```yaml
volumes:
      - type: bind
        source: /DATA/AppData/nextcloud/nextcloud/html  # drive A for Nextcloud app files
        target: /var/www/html
        bind:
          create_host_path: true
```

### DB-NEXTCLOUD

```yaml
volumes:
      - type: bind
        source: /DATA/AppData/nextcloud/nextcloud/pgdata  # drive A for PostgreSQL
        target: /var/lib/postgresql/data
        bind:
          create_host_path: true
```

### NEXTCLOUD

```yaml
volumes:
      - type: bind
        source: /DATA/AppData/nextcloud/nextcloud/html  # drive A for Nextcloud app files
        target: /var/www/html
        bind:
          create_host_path: true
      - type: bind
        source: /mnt/driveB/data/nextcloud/data  # drive B for user data, i.e. photos, docs, anything the user uploads
        target: /var/www/html/data
        bind:
          create_host_path: true
```

### REDIS-NEXTCLOUD

```yaml
volumes:
      - type: bind
        source: /DATA/AppData/nextcloud/nextcloud/redis  # drive A for Nextcloud app files
        target: /data
        bind:
          create_host_path: true
```

running the compose file you should consider changing the admin profile password by default it is

username: casaos

password: casaos


## TroubleShooting

---



### Not Possible to Execute The Cron Job

#### error:

```
	It was not possible to execute the cron job via CLI. The following technical errors have appeared: - Your data directory is not writable. Permissions can usually be fixed by giving the web server write access to the root directory. See https://docs.nextcloud.com/server/30/go.php?to=admin-dir_permissions.
```

#### How to Fix the Not Possible to Execute The Cron Job Issue:

Not Possible to Execute The Cron Job

##### **Verify Ownership and Permissions (Inside the Container)**

###### **Step 1: Enter the Container** :

```shell
   docker exec -it nextcloud /bin/bash
```

###### Step 2: **Check Ownership** :

```shell
   ls -ld /var/www/html/data
```

    **Expected Output** :

```shell
   drwxr-x--- 2 www-data www-data 4096 Mar  1 18:13 /var/www/html/data
```

   If the owner is not `www-data:www-data`, fix it:
   bash

```shell
   chown -R www-data:www-data /var/www/html/data
```

###### Step 3: **Check Permissions** :

```shell
   ls -ld /var/www/html/data
```

    **Expected Output** :

```shell
   drwxr-x--- 2 www-data www-data 4096 Mar  1 18:13 /var/www/html/data
```

   If the permissions are not `750`, fix them:
   bash

```shell
   chmod -R 750 /var/www/html/data
```


##### **Verify the `.ncdata` File (Inside the Container)**

###### Step 1: **Check the File** :

```shell
   ls -l /var/www/html/data/.ncdata
   cat /var/www/html/data/.ncdata
```

    **Expected Output** :

```shell
   -rw-r----- 1 www-data www-data 52 Mar  1 18:13 /var/www/html/data/.ncdata
   # Nextcloud data directory
```

   If the file is missing or incorrect, recreate it:

```shell
   echo "# Nextcloud data directory" > /var/www/html/data/.ncdata
   chown www-data:www-data /var/www/html/data/.ncdata
   chmod 640 /var/www/html/data/.ncdata
```


### Trusted Domains WebUI Error

you need to go to the config.php file and add the trusted domain to the trusted_domains array

#### Error:

(viewable as soon as you launch the nextcloud webui)

```
Please contact your administrator. If you are an administrator, edit the "trusted_domains" setting in config/config.php like the example in config.sample.php.
```

#### How to Fix the Trusted Domain Issue

##### Step 1: Locate the `config.php` File

The `config.php` file is located in the **Nextcloud app files directory** (`/DATA/AppData/nextcloud/html/config`). Open it for editing:

```shell
sudo nano /DATA/AppData/nextcloud/html/config/config.php
```

##### Step 2: Add Your Domain or IP to `trusted_domains`

In the `config.php` file, look for the `trusted_domains` array. It will look something like this:

```php
'trusted_domains' => 
  array (
    0 => 'localhost',
  ),
```

Add your **domain name** or **IP address** to the array. For example:

* If you’re accessing Nextcloud via an IP address (e.g., `192.168.1.100`):

  ```php
  'trusted_domains' => 
    array (
      0 => 'localhost',
      1 => '192.168.1.100',
    ),
  ```
* If you’re using a domain name (e.g., `nextcloud.example.com`):

  ```php
  'trusted_domains' => 
    array (
      0 => 'localhost',
      1 => 'nextcloud.example.com',
    ),
  ```

##### Step 3: Save and Exit

* Save the file (`Ctrl+O`) and exit the editor (`Ctrl+X`).

##### Step 4: Restart the Nextcloud Container

Restart the Nextcloud container to apply the changes:

click on the 3 dots on the upper right corner of the nextcloud conatainer in casaos and click the restart conatiner button
OR

```shell
docker-compose restart nextcloud
```

##### Step 5: Verify Access

Try accessing Nextcloud again using the IP or domain you added. The error should be resolved.

##### Example `config.php` After Modification

Here’s what the `trusted_domains` section might look like after adding your IP or domain:

```php
'trusted_domains' => 
  array (
    0 => 'localhost',
    1 => '192.168.1.100',  // Replace with your IP or domain
    2 => 'nextcloud.example.com',  // Optional: Add a domain if you have one
  ),
```


### **PHP Memory Limit** Issue

#### Warning:

while attempting to run a php command inside the NextCloud container terminal i was getting an error like this :

```shell
The current PHP memory limit is below the recommended value of 512MB.
```

This did not make since because i was setting the php limit in the compose.yaml file,

To test what was actually being stored in the NextCloud container i ran this command:

```shell
php -i | grep memory_limit
```

which gave me this:

```shell
memory_limit => 512M => 512M
```

that didnt make sense since i was setting 1024M in the compose.yaml file.

so i ran this command to check the nextcloud.ini file which contains the limit values:

```shell
cat /usr/local/etc/php/conf.d/nextcloud.ini
```

which gave me this output:

```shell
memory_limit=${PHP_MEMORY_LIMIT}
upload_max_filesize=${PHP_UPLOAD_LIMIT}
post_max_size=${PHP_UPLOAD_LIMIT}
```

this told me that the ini file was indeed supposed to be getting the values from the compose file stored in those environment variables.

I could have tried to figure out why they were not getting set but since i did not plan on changing these values i went ahead and hardcoded them by ruinning these commands:

```shell
echo "memory_limit=1024M" >> /usr/local/etc/php/conf.d/nextcloud.ini
echo "upload_max_filesize= 1024M" >> /usr/local/etc/php/conf.d/nextcloud.ini
echo "post_max_size= 1024M" >> /usr/local/etc/php/conf.d/nextcloud.ini
```

after running those i did a check just to see if they were set:

```shell
cat /usr/local/etc/php/conf.d/nextcloud.ini
```

which resulted in this showing that they were set correctly:

```shell
memory_limit=1024M
upload_max_filesize=1024M
post_max_size=1024M
```


### Accessing Site Insecurely via HTTP

Error:

```
Accessing site insecurely via HTTP. You are strongly advised to set up your server to require HTTPS instead. Without it some important web functionality like "copy to clipboard" or "service workers" will not work! For more details see the documentation ↗.
```

#### How to Fix Accessing Site Insecurely via HTTP

The way i fixed this issue was setting up CloudFlare tunneling and using a custom domain to access my NextCloud service. If youd like to set it up the same way reference the CloudFlare setup


## References

1. [Streamline Nextcloud Installation on CasaOS with BigBearCasaOS](https://www.youtube.com/watch?v=O0fzG16COYc)
