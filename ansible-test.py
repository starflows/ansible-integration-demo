def handler(system, this):
    report = this.flow(
        'ansible-play',
        playbook='verify-apache.yaml',
        target='ansible-host-1',
        become=True,
        files=['test-site.conf.j2', 'index.html.j2'],
        run=True,
    ).get('output_value')['report']
    this.save(output_value={'report': report})
    return this.success('all done')
