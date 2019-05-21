def handler(system, this):
    this.flow(
        'ansible-play',
        playbook='verify-apache.yaml',
        target='ansible-host-1',
        become=True,
        files=['test-site.conf.j2', 'index.html.j2'],
        run=True,
    )
    return this.success('all done')
