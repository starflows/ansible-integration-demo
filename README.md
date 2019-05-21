# Ansible & Cloudomation

In this repository you find some boilerplate scripts to demonstrate a
possibility of integrating Ansible and Cloudomation.

The demonstration aims for Cloudomation users who already have Ansible
playbooks and

* are looking for a way to embed them in a bigger automation landscape.

* want to orchestrate Ansible runs.

## Setup

This example assumes you

* have an Ansible master host set up

* have a host available where apache2 will be set up and configured

To get started, copy the content of [github-sync.py](github-sync.py) to a
new flow script and execute it. The flow script will then sync all needed files
into your Cloudomation client.

## Content

### `ansible-host-template.yaml`

will be synced as a setting record to your
Cloudomation client. You should duplicate that setting and provide credentials
for your ansible master host.

### `ansible-play.py`

will be synced as a flow script to your Cloudomation client.
This flow script enables you to conveniently start Ansible playbooks from
Cloudomation.

### `ansible-test.py`

will be synced as a flow script to your Cloudomation client.
This flow script will call the `ansible-play` flow script to setup apache2
on a host.

### `client.webhook.ansible-test.yaml`

will be synced as a setting record to your
Cloudomation client. This setting activates a Cloudomation webhook which can
be used to execute the `ansible-test` flow script using a HTTP request.

The webhook endpoint will be available via the url
```
https://cloudomation.com/api/webhook/<your client name>/ansible-test
```

### `client.webhook.github-push.yaml`

will be synced as a setting record to your
Cloudomation client. This setting activates a Cloudomation webhook which can
be used by GitHub to execute the `github-sync` flow script every time a
repository receives a push event.

The webhook endpoint will be available via the url
```
https://cloudomation.com/api/webhook/<your client name>/github-push
```

Please check out [Creating Webhooks](https://developer.github.com/webhooks/creating/)
for instructions on how to register the webhook in GitHub.

### `github-sync.py`

will be synced as a flow script to your Cloudomation client.
This flow script will sync the content of this repository into your
Cloudomation client.

### `index.html.j2`

a minimal template for the demonstration page which apache2
will display.


### `README.md`

this file.

### `test-site.conf.j2`

the template for the apache2 configuration.

### `verify-apache.yaml`

an Ansible playbook which ensures apache2 is installed,
up-to-date, running, and configured.
