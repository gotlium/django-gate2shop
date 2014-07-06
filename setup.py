from setuptools import setup, find_packages
from g2s import get_version

setup(
    name='django-gate2shop',
    version=get_version(),
    keywords="payment django g2s gate2shop",
    author='GoTLiuM InSPiRiT',
    author_email='gotlium@gmail.com',
    maintainer="GoTLiuM InSPiRiT",
    maintainer_email="gotlium@gmail.com",
    description='Gate2Shop gateway for accept payments on your website.',
    url='https://github.com/gotlium/django-gate2shop',
    packages=find_packages(exclude=['demo']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django>=1.4',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python',
    ],
)
