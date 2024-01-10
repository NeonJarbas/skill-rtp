#!/usr/bin/env python3
from setuptools import setup

# skill_id=package_name:SkillClass
PLUGIN_ENTRY_POINT = 'skill-rtp.jarbasai=skill_rtp:RTPSkill'

setup(
    # this is the package name that goes on pip
    name='ovos-skill-rtp',
    version='0.0.1',
    description='ovos RTP skill plugin',
    url='https://github.com/JarbasSkills/skill-rtp',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    package_dir={"skill_rtp": ""},
    package_data={'skill_rtp': ['locale/*', 'res/*']},
    packages=['skill_rtp'],
    include_package_data=True,
    install_requires=["ovos_workshop~=0.0.5a1"],
    keywords='ovos skill plugin',
    entry_points={'ovos.plugin.skill': PLUGIN_ENTRY_POINT}
)
