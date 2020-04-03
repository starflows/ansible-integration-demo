import os
import yaml


def handler(system, this):
    inputs = this.get('input_value')
    headers = inputs.get('headers', {})
    event = headers.get('x-github-event', headers.get('X-GitHub-Event'))
    if event == 'ping':
        return this.success('Ping event OK')

    if event is None:
        ref = 'master'
    else:
        assert event == 'push', event
        ref = inputs['data_json']['after']
    this.task(
        'GIT',
        command='get',
        repository_url='https://github.com/starflows/ansible-integration-demo.git',
        files_path='ansible-integration-demo',
        ref=ref,
    )
    for file_ in system.files(filter={'field': 'name', 'op': 'like', 'value': 'ansible-integration-demo/%'}):
        filename, content = file_.get('name', 'content')
        name, ext = os.path.splitext(os.path.basename(filename))
        if ext == '.yaml':
            data = yaml.safe_load(content)
            system.setting(name).save(value=data)
        elif ext == '.py':
            system.flow(name).save(script=content)

    this.flow(
        'ansible-test',
        wait=False,
    )

    return this.success('all done')
