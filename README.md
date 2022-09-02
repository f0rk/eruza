eruza
=====

"Azure is so backwards we needed this tool."

`eruza` is a tool to simplify using multiple sets of credentials with Azure. If
you have multiple profiles, `eruza` eliminates the need to constantly re-export
values.

Requires python.

Install
=======

```!sh
$ curl https://raw.githubusercontent.com/f0rk/eruza/master/tools/eruza-standalone > ~/bin/eruza
$ chmod +x ~/bin/eruza
```

Configuration
=============

To setup profiles for eruza, make sure the folder `~/.azure/` exists and create
a file `~/.azure/credentials` with mode 600.

Add sections for each profile you'd like to use, for example:
```
[dev]
ARM_TENANT_ID=00000000-0000-0000-0000-000000000000
ARM_SUBSCRIPTION_ID=00000000-0000-0000-0000-000000000000
ARM_CLIENT_ID=00000000-0000-0000-0000-000000000000
ARM_CLIENT_SECRET=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
```

Usage
=====

```
$ eruza --profile dev exec func azure functionapp publish yourfunc
```

```
$ eruza --profile dev env
...
ARM_TENANT_ID=...
ARM_SUBSCRIPTION_ID=...
ARM_CLIENT_ID=...
ARM_CLIENT_SECRET=...
...
```

For convenience, you can use the `eval` subcommand to simplify:

```
$ eval $(eruza --profile dev eval)
$ env | grep ARM
... 
ARM_TENANT_ID=...
ARM_SUBSCRIPTION_ID=...
ARM_CLIENT_ID=...
ARM_CLIENT_SECRET=...
...
```
