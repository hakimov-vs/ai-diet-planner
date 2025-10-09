
# The code run at VPS

📁 app location: `/opt/ai-diet-planner/`  
⚙️ service manager: **systemd**  
📄 service file: `/etc/systemd/system/ai-diet-planner.service`  
▶️ control: `systemctl start/stop/enable ai-diet-planner`  
📜 logs:  `journalctl -u ai-diet-planner -f --since "5 min ago"`  


## Restart
```
$ sudo systemctl daemon-reexec
```

## Enable and start
```
$ sudo systemctl enable ai-diet-planner
$ sudo systemctl start ai-diet-planner
```

## Check if successful
```
$ sudo systemctl status ai-diet-planner.service
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
