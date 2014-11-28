IDA6.1PluginforQIRA
===================

IDA 6.1 Plug-in(IDA Python) for QIRA


###Requirements
* QIRA
* IDA Python

###Installation
```
  mv i2q.py %IDA6.1%/Plugins/
  mv i2q.py %IDA6.1%/Plugins/
```

###Usage
1. connect qira server using Chrome Browser
```
ex) http://x.x.x.x:4000
```

2. run middle-server
```
python server.py
```

3. run IDA & IDA-Plugin
```
alt+x : send IDA instruction address to Qira
alt+c : send Qira instrunction address to IDA
```

