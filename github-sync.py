import yaml
import os


def handler(system, this):
    inputs = this.get('input_value')
    headers = inputs.get('headers', {})
    event = headers.get('x-github-event', headers.get('X-GitHub-Event'))
    if event == 'ping':
        return this.success('Ping event OK')

    if event is None:
        commit_sha = 'origin/master'
    else:
        assert event == 'push', event
        commit_sha = inputs['data_json']['after']
    this.task(
        'GIT',
        command='get',
        repository_url='https://github.com/starflows/ansible-integration-demo.git',
        repository_path='ansible-integration-demo',
        ref=commit_sha,
        run=True,
    )
    for file in system.files(dir='ansible-integration-demo'):
        type, path, content = file.get('type', 'path', 'content')
        if type != 'file':
            continue
        name, ext = os.path.splitext(os.path.basename(path))
        if ext == '.yaml':
            data = yaml.safe_load(content)
            system.setting(name, value=data)
        elif ext == '.py':
            system.flow(name, script=content)

    this.flow(
        'ansible-test',
        run=True,
        wait=False,
    )

    return this.success('all done')
