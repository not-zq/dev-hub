
# Home server

## Overview

This is a work in progress project turning a Microsoft Surface Go into a light-weight, low power always-on personal home server running Linux to host personal applications and data. 

## Quickstart

### Connect to the server from personal computer

In the personal computer
1. Activate Tailscale
2. Open a command terminal
3. Connect using `zk@homeserver`

### Start the Hermes agent

1. In the personal computer, start Ollama.
2. In the server, run `hermes`.

### Access a personal web application remotely

1. Activate Tailscale on remote device
2. In a browser, access `192.168.0.3/biometrics/`

### Miscellaneous commands

- Shutdown the server | `sudo shutdown now`
- Check battery status | `upower -i /org/freedesktop/UPower/devices/battery_BAT1`

## Configuration

### Server

The server is a *Microsoft Surface Go* with the following specifications
```
Model: 1824
CPU: Intel Pentium Gold 4415Y
RAM: 4 GB
Storage: 64 GB
```
with a 64 GB microSD for backup files.

###  OS

The server is running *Ubuntu Server 26.04 LTS*.

### Network

The server has the reserved local LAN address `192.168.0.3`.

### Directory structure

The server is organized around the following directory structure
```
/home/zk/server/
├── apps            # Personal applications
├── data
│   └── postgres    # Personal data (PostgreSQL database)
└── services        # Third-party services
    ├── nginx
    └── postgres
/mnt/backups        # Backups
```

## Components

### Tailscale

Tailscale was installed on the server to:
- Access personal applications hosted on the server from personal phone remotely.
- Connect Hermes (on server) to an Ollama model running in personal computer.

### Docker

Docker is used to define and manage services like nginx, postgres and personal projects.

### PostgreSQL

PostgreSQL is running in a Docker container from an existing image, `postgres:16`, with the purpose to hold in a database, `homeserver`, personal data for analysis.

### nginx

nginx is running in a Docker container, as a reverse proxy and entry point for web applications.

### Personal web applications

Currently, only a single application (which is still a work in progress) is being hosted on the server. However, the intention is to develop several applications for various personal use-cases. All these will be developed using Django, will connect to a specific schema in the postgres database, and will be accessible remotely from my personal phone through nginx and aided by tailscale.

Then, the web architecture is as follows
```
           Client
              │
    Local LAN / Tailscale
              │
           Server
              │
            nginx
              │
         /biometrics/
              │
            Django
              │
          PostgreSQL
    (homeserver.biometrics)
```

The three main uses cases will be body measurements, food tracking and finance transactions.

#### Biometrics

This application runs in Docker, listening on `8000`, can be accessed from [`http://192.168.0.3/biometrics/`](http://192.168.0.3/biometrics/).

Currently, the application provides a way to
- enter body measurements (like weight),
- store them in the postgres database,
- and retrieve this measurements.

### Hermes

Currently, the purpose of Hermes is to have an agent which understands the server, and is capable of look into its content to help with its development, and potentially perform administrative/development tasks.

The preferred architecture was a local Ollama model running in the personal computer to handle the computationally expensive inference.

#### Architecture
```
       ┌──────────┐
       │  Server  │
       │          │
       │  Hermes  │
       └─────┬────┘
             │
         Tailscale
             │
    ┌──────────────────┐
    │     Personal     |
    |     computer     │
    │                  │
    │      Ollama      │
    │        │         │
    │  qwen3.5-hermes  │
    │        │         │
    │     RX 6600      │
    └──────────────────┘
```

#### Modelfile | qwen3.5-hermes
```
FROM qwen3.5:latest
PARAMETER num_ctx 65536
```

#### Personal computer
```
CPU: Ryzen 5 5600G
GPU: Radeon RX6600
RAM: 16 GB
OS: Windows 11
```

## Pending

- Setup backups on microSD (`/mnt/backups`).
- Grafana monitoring
- CI/CD
- Web applications
