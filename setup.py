#!/usr/bin/env python3
from setuptools import setup

# skill_id=package_name:SkillClass
PLUGIN_ENTRY_POINT = 'skill-raventv.jarbasai=skill_raventv:RavenTVSkill'

setup(
    # this is the package name that goes on pip
    name='ovos-skill-raventv',
    version='0.0.1',
    description='ovos RavenTV movies skill plugin',
    url='https://github.com/JarbasSkills/skill-raventv',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    package_dir={"skill_raventv": ""},
    package_data={'skill_raventv': ['locale/*', 'ui/*']},
    packages=['skill_raventv'],
    include_package_data=True,
    install_requires=["ovos_workshop~=0.0.5a1"],
    keywords='ovos skill plugin',
    entry_points={'ovos.plugin.skill': PLUGIN_ENTRY_POINT}
)
