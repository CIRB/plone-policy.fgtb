from setuptools import setup, find_packages

version = '1.0'

setup(name='policy.fgtb',
        version=version,
        description="'Policy of FGTB site'",
        long_description=open("README.rst").read() + "\n" +
        open("CHANGES.txt").read(),
# Get more strings from
# http://pypi.python.org/pypi?%3Aaction=list_classifiers
        classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
        keywords='',
        author='',
        author_email='',
        url='https://github.com/collective/',
        license='gpl',
        packages=find_packages('src'),
        package_dir={'': 'src'},
        namespace_packages=['policy'],
        include_package_data=True,
        zip_safe=False,
        install_requires=[
        'setuptools',
        'Plone',
        'Products.LinguaPlone',
        'cirb.zopemonitoring',
# -*- Extra requirements: -*-
        'cirb.footersitemap',
        'collective.anysurfer',
        'collective.ckeditor',
        'collective.contentstats',
        'collective.easyslider', 
        'collective.js.fullcalendar',
        'collective.linguafaq',
        'collective.plonefinder',
        'collective.portlet.videoanysurfer',
        'collective.quickupload',
        'collective.recaptcha',
        'collective.videoanysurfer',
        'plonetheme.fgtb',
        'products.geoloc',
        'Products.Maps',
        'Products.PloneFormGen',
        'qi.portlet.TagClouds',
        'quintagroup.analytics',
        'Solgema.fullcalendar',
        'webcouturier.dropdownmenu',
        ],
        entry_points="""
# -*- Entry points: -*-
        [z3c.autoinclude.plugin]
        target = plone
        """,
        )
