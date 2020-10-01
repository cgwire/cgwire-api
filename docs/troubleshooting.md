# Troubleshooting

To solve issues related to your installation, you can do several actions to
get information about what is going wrong.

## Error logs

Main error logs are stored in the `/opt/zou/gunicorn_error.log` file. Errors 
can be explicit. They can tell what is going wrong.


## Status route


To know if all the required services are up, you can connect to the following
route: `http://kitsu.mystudio.com/api/status`.

You should see something like this:

```
{
    "version": "0.11.3",
    "event-stream-up": true,
    "database-up": true,
    "key-value-store-up": true,
    "name": "Zou"
}
```

If one of the service is set to false, it means that it is down or that
Zou cannot connect to it. Zou cannot run properly in that case.

NB: Database refers to Posgres, Key Value Store refers to Redis and Event
Stream refers to `zou-events`.

## Installing on Ubuntu server or minimal desktop

will require libjpeg-dev so along with 3rd party software install like this:
sudo apt-get install libjpeg-dev

## To enable zou/kitsu to start on reboot

sudo systemctl enable zou
sudo systemctl enable zou-events
