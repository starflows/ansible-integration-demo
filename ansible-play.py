def handler(system, this):
    inputs = this.get('input_value')
    ansible_host_setting = inputs.get('ansible-host', 'ansible-host')
    playbook = inputs['playbook']
    script = f'ansible-playbook {playbook}'
    become = inputs.get('become')
    if become:
        script += ' -b'
    ansible_host = system.setting(ansible_host_setting).get('value')
    this.task(
        'SSH',
        **ansible_host,
        script=script,
        run=True,
    )
    return this.success('all done')
