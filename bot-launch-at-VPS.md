
# The code run at VPS

### Cricial references
📁 app location: `/opt/ai-diet-planner/`  
⚙️ service manager: **systemd**  
📄 service file: `/etc/systemd/system/ai-diet-planner.service`  
▶️ control: `systemctl start/stop/enable ai-diet-planner`  
📜 logs:  `journalctl -u ai-diet-planner -f --since "5 min ago"`  


## Enable and start
```
$ sudo systemctl enable ai-diet-planner
$ sudo systemctl start ai-diet-planner
```

## Check if successful
```
$ sudo systemctl status ai-diet-planner.service
```

## Logs
```
journalctl -u ai-diet-planner -f --since "5 min ago"
```

## Pull updates
```
cd /opt/ai-diet-planner
git pull origin main
```

## Restart service to use new code
```
sudo systemctl restart ai-diet-planner
```


# Restart `systemctl`, the "init system" and system manager
```
$ sudo systemctl daemon-reexec
```
## Explanation (short)
The `systemctl daemon-reexec` command shuts down and restarts the systemd process itself.

Think of it as "restarting the manager" **without restarting the entire server**. It's a way to reload the systemd daemon's configuration and internal state without a full system reboot.

## The Detailed Explanation
To understand this, you first need to know what **systemd** is.

### What is "systemd"?
**systemd** is the "init system" and system manager on most modern Linux distributions (including those running on your VPS). It is the first process that runs when the server boots (it has Process ID 1, or PID 1). Its job is to manage all other services and processes—starting them, stopping them, logging their output, and managing dependencies.

### What is the "systemd daemon"?
The "daemon" is the core background process (/usr/lib/systemd/systemd) that does all the work mentioned above. It's the brain of the operation.

### What does daemon-reexec do?
When you run sudo systemctl daemon-reexec, you are telling the currently running systemd process to:

- Re-execute itself. It starts a new copy of the systemd binary (/usr/lib/systemd/systemd).

- Replace itself. The new systemd process takes over the same PID 1.

- Re-read its own configuration. During this re-execution, it parses its main configuration files (like those in /etc/systemd/system.conf and unit files) again.

Crucially, this does NOT restart the services that systemd is managing. Services like your web server (nginx/apache), database (MySQL/PostgreSQL), and SSH will continue running uninterrupted.

## Analogy
Imagine a restaurant:

*The Kitchen & Waitstaff*: your running services `(nginx, SSH, database)`.

*The Head Chef* `(systemd)`: the manager who coordinates everything, reads new recipes (configuration), and gives orders.

Running `daemon-reexec` is like the head chef stepping out for a moment, quickly reading a new, updated recipe book, and then immediately returning to their post. The kitchen and waitstaff continue their work without stopping. The chef is now working from the new instructions.
