# smartercoffee

Python script for controlling Smarter Coffee machine http://smarter.am/

As there is no open api for this wifi enabled machine i have made a small script for contolling it from a computer.

## Send command to machine

```
python sendcommand.py
```

You must specify an function via command line parameter `-f`.

* 1 = startbrew whit options -c -g -m -s
* 2 = startbrew whit settings already on brewer
* 3 = start hotplate whit option -m
* 4 = set cups whit option -c
* 5 = set strength whit option -s
* 6 = define beans or filter whit option -g

Where `s` means strength (1-3), `c` means cups (1-12), `m` means minutes for hotplate, and `g` means filter or brew.

This IP Address of the machine can be set via option `-i` whith a default of `192.168.1.2`.

## Polling of Machine Status

```
python pollingStatusMessage.py
```

This command uses an optional parameter `--notify GNOME`.

This IP Address of the machine can be set via option `-i` whith a default of `192.168.1.2`.

## Output Machine Status

This command is similar to the polling except that it does output the current status of the machine only once. It it intended as an integration call with a smart home system which does the permanent monitoring my other means.

```
python outputStatusMessage.py
```

This IP Address of the machine can be set via option `-i` whith a default of `192.168.1.2`.
