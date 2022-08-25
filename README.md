# EM7 Framework

This is a framework that connects to the API of an EM7 monitoring appliance.

## Authentication

Credentials are stored in JSON format, in the same directory as the `em7.py` file. The name of the file should be `credentials.json`.

Other authentication methods, such as KDBX, have been tested, but this way it keeps the hard-coded passwords out of the source code.

```
{
	"credentials": {
		"em7_hostname": {
			"username": "",
			"password": ""
		}
	}
}
```

The name of the credential is the DNS name or IP of the EM7 and references username and password.

API calls will be made to `https://` + host and will automatically authenticate on instantiation.

## Getting Started

To instantiate a `EM7` object, pass a string of the EM7 server name created in the "Authentication" section :

```
>>> server_name = 'em7.domain.com'
>>> e = EM7(server_name)
```

## EM7 Features

To list EM7's available features :

```
>>> features = e.feature_list()
```

Most additional features of the API to retrieve data are written :
- Get access locks
- Get account info
- Get account policy info
- Get alert info
- Get asset info
- Get cleared events
- Get contacts
- Get stored credentials
- Get dashboards
- Get data performance info (raw and non)
- Get device info
- Get device group info
- Get disovery session info
- Get active discovery session info
- Get dynamic application info
- Get Event info
- Get filestores
- Get interface metrics
- Get monitor info
- Get organization info
- Get relationship info
- Get relationship hierarchy info
- Get scheduling info
- Get system thresholds
- Get tasks
- Get threshold value override values
- Get ticket info
- Get ticket category info
- Get ticket chargebacks
- Get ticket logs
- Get ticket notes
- Get vendor info
