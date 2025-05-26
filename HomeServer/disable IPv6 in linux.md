To disable IPv6 on Linux Mint, it's generally recommended to do it through the `sysctl.conf` file for a more straightforward and permanent solution. Here's the step-by-step process:

### 1. **Edit the `sysctl.conf` File**

Open the `sysctl.conf` file using a text editor with root privileges.

```
sudo nano /etc/sysctl.conf
```

2. **Add the Following Lines**

At the end of the file, add the following lines to disable IPv6 globally:

```
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
```

These lines will disable IPv6 on all network interfaces (`all`), the default settings (`default`), and the loopback interface (`lo`).

### 3. **Apply the Changes**

After saving the file, apply the changes by running the following command:

```
sudo sysctl -p
```

### 4. **Verify IPv6 is Disabled**

You can check if IPv6 is disabled by running:

```
ip a | grep inet6
```

If IPv6 is successfully disabled, you should not see any `inet6` addresses listed.
