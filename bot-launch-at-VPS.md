
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