#White Rock CKAN extension

*CKAN extension for the implementation of the [White Rock City](http://www.whiterockcity.ca/)*

The extension contains the following features:

- Add a custom CSS file
- Add custom pages (contact & suggest dataset forms + follow page) with implementation of iRoutes
- Add public file (images)
- Add custom licence
- Add predefined extra fields at the dataset level
- Support custom templates

More documentation available in  [ckanext/whiterock/docs/customization.md](ckanext/whiterock/docs/customization.md)

## Prerequisite

This extension needs the stats extension to be activated with the tracking options. Some links (in the footer), also need the [ckanext-page](https://github.com/ckan/ckanext-pages) extension. In order to install and enable stats and ckanext-pages: 

```
pip install -e git+https://github.com/ckan/ckanext-pages.git#egg=ckanext-pages
```

Then configure the plugins in the .ini file: 

```
ckan.plugins =  ... stats pages...
ckan.tracking_enabled = true 
```

The template need the follow page to be created:

- faq


In order to refresh the most popular dataset values on the landing page, make sure to set up the cron jobs (see below).

The extension has been developed and tested to run with CKAN 2.2.

## Installation

Activate your pyenv and go to the CKAN root, for example:
```
 cd /usr/lib/ckan/default/
 source bin/activate
 cd src/ckan
```

Install the extension from GitHub:

```
pip install -e git+https://github.com/opennorth/ckanext-whiterock.git#egg=ckanext-whiterock
```


Add the extension in the configuration file. `wrcommon` does most of the work, `wrpage` add some custom pages.
```
ckan.plugins =  ... wrcommon wrpages wrfacet 
``` 

Add the custom licence file in the configuration file. 

```
licenses_group_url = file:///path/to/extension/ckanext-whiterock/ckanext/whiterock/licences.json
```


## Set up jobs

Some cron jobs have to be set up in order to have the extension working as expected.

In order to update the recent visits, the tracker and the index has to be rebuilt. The following command will do this using `crontab -e` (make sure that the path to `paster` and the .ini file correspond to your installation):
```
@hourly /usr/lib/ckan/default/bin/paster --plugin=ckan tracking update -c /etc/ckan/default/production.ini > /dev/null
@hourly /usr/lib/ckan/default/bin/paster --plugin=ckan search-index rebuild -r -c /etc/ckan/default/production.ini > /dev/null
```

where `/etc/ckan/default/production.ini` is the path to your configuration file (might be different)

In order to receive mail notification (either for the admin and for the users who are registering) add the following comming in the cron jobs:
```
@daily echo '{}' | /usr/lib/ckan/default/bin/paster --plugin=ckan post -c /etc/ckan/default/production.ini /api/action_notifications > /dev/null
```
