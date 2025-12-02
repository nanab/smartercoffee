# smartercoffee

Python script to control the Smarter Coffee machine http://smarter.am/.

As there is no open API for this WIFI-enabled device, I have created a small script for controlling it from a computer.

## Send command to machine

```
python sendcommand.py
```

You must specify a function via command line parameter `-f`.

* 1 = Start the brewing process with options -c -g -m -s
* 2 = Start the brewing process with the settings already present in the brewer.
* 3 = Start hotplate with option -m
* 4 = Set cups with option -c
* 5 = Set strength with option -s
* 6 = Define beans or filter with option -g

Where `s` means strength (1-3), `c` means cups (1-12), `m` means minutes for hotplate, and `g` means filter or brew.

The IP address of the machine can be set via option `-i` with a default of `192.168.1.2`.

## Polling of Machine Status

```
python pollingStatusMessage.py
```

This command uses an optional parameter `--notify GNOME`.

This IP address of the machine can be set via option `-i` with a default of `192.168.1.2`.

## Output Machine Status

This command is similar to the polling, except that it does output the current status of the machine only once. It is intended as an integration call with a smart home system that does the permanent monitoring of my other devices and facilities.

```
python outputStatusMessage.py
```

The IP address of the machine can be set via option `-i` with a default of `192.168.1.2`.
