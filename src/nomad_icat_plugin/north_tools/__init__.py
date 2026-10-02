from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NORTHToolEntryPoint

my_north_tool = NORTHTool(
    short_description='Jupyter Notebook server in NOMAD NORTH for NOMAD plugin nomad-icat-plugin.',
    image='ghcr.io/nomad-hzb/nomad-icat-plugin:main',
    description='Jupyter Notebook server in NOMAD NORTH for NOMAD plugin nomad-icat-plugin.',
    external_mounts=[],
    file_extensions=['ipynb'],
    icon='logo/jupyter.svg',
    image_pull_policy='Always',
    default_url='/lab',
    maintainer=[{'email': 'marcus.lewerenz@helmholtz-berlin.de', 'name': 'Marcus Lewerenz'}],
    mount_path='/home/jovyan',
    path_prefix='lab/tree',
    privileged=False,
    with_path=True,
    display_name='my_north_tool',
)

north_entry_point = NORTHToolEntryPoint(
    id_url_safe='nomad-icat-plugin-my-north-tool',
    north_tool=my_north_tool,
)
