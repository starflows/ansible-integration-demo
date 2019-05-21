def handler(system, this):
    inputs = this.get('input_value')
    ansible_host_setting = inputs.get('ansible-host', 'ansible-host')
    target_hosts = inputs.get('target')
    files = inputs.get('files', [])
    playbook = inputs['playbook']
    script = f'ansible-playbook {playbook}'
    become = inputs.get('become')
    if become:
        script += ' -b'
    if target_hosts:
        script += f' -i "{target_hosts},"'
    ansible_host = system.setting(ansible_host_setting).get('value')
    for file in files:
        this.task(
            'SCP',
            **ansible_host,
            src=f'cloudomation:ansible-integration-demo/{file}',
            dst=file,
            run=True,
        )
    this.task(
        'SCP',
        **ansible_host,
        src=f'cloudomation:ansible-integration-demo/{playbook}',
        dst=playbook,
        run=True,
    )
    this.task(
        'SSH',
        **ansible_host,
        script=script,
        run=True,
    )
    return this.success('all done')
