import yaml
import os


def handler(system, this):
    inputs = this.get('input_value')
    event = inputs['headers']['X-GitHub-Event']
    if event == 'ping':
        return this.success('Ping event OK')

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
        path, content = file.get('path', 'content')
        name, ext = os.path.splitext(os.path.basename(path))
        if ext == '.yaml':
            data = yaml.safe_load(content)
            system.setting(name, value=data)
        elif ext == '.py':
            system.flow(name, script=content)
    return this.success('all done')
