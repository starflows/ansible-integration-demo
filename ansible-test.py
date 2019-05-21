def handler(system, this):
    this.flow(
        'ansible.play',
        playbook='verify-apache.yaml',
        become=True,
        run=True,
    )
    return this.success('all done')
