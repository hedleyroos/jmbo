from setuptools import setup, find_packages


setup(
    name='jmbo',
    version='3.0.5',
    description='The Jmbo base product introduces a content type and various tools required to build Jmbo products.',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Praekelt Consulting',
    author_email='dev@praekelt.com',
    license='BSD',
    url='http://www.jmbo.org',
    packages = find_packages(),
    install_requires = [
        # The bare minimum requirements. The tests use explicit versions.
        "Pillow",
        "pytz",
        "django>=2",
        "django-category>=2.0.0",
        "django-contrib-comments>=1.8.0",
        "django-layers-hr>=1.11.1",
        "django-likes>=2.0.0",
        "django-preferences",
        "django-photologue>=3.11",
        "djangorestframework-jwt==1.8.0",
        "django-sites-groups>=1.9.1",
        "django-sortedm2m>=1.4.0",
        "django-ultracache>=1.11.10",
        "django-crum",
        "dj-pagination>=2.5.0",
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
