# How to use binarycat/cx_oracle

```
cd ~
git clone git@github.com:catbinary/cx_oracle_example.git
cd cx_oracle_example
docker build -t "cx_oracle_example:latest" .
docker run -e DB_USER='some-user' -e DB_PASSWORD='some-password' -e DB_HOST='some-db-host' -e DB_PORT=1521 -e DB_SID='some-sid' -d -p 8080:80 "cx_oracle_example:latest"
```

```
curl localhost:8080
```