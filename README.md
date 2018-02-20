# How to use binarycat/cx_oracle

## Required:

- docker >= 1.13
    - [Mac OS](https://docs.docker.com/docker-for-mac/install/)
    - [Windows](https://docs.docker.com/docker-for-windows/install/)
    - [Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce)
    - [Centos](https://docs.docker.com/install/linux/docker-ce/centos/#install-docker-ce)
- docker-compose
    - [Install Docker Compose](https://docs.docker.com/compose/install/)

## Environments

### use .env files
- DB_USER=user
- DB_PASSWORD=password
- DB_HOST=localhost
- DB_PORT=1521
- DB_SID=sid

## Example 

```
git clone git@github.com:catbinary/cx_oracle_example.git ~/cx_oracle_example
cd ~/cx_oracle_example
docker-compose up -d
```

```
~> curl -v 127.0.0.1:8080
< ORA-12541: TNS:no listener
```