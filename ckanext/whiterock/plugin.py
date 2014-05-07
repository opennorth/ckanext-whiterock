import ckan.plugins as plugins
import ckan.plugins.toolkit as tk

def update_frequency():
    frequency_list = (u"Yearly", u"Monthly", u"Weekly", u"Daily", u"Realtime", u"Punctual", u"Variable", u"Never")
    return frequency_list

class WhiteRockCommonPlugin(plugins.SingletonPlugin, tk.DefaultDatasetForm):
    '''An example that shows how to use the ITemplateHelpers plugin interface.

    '''
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IDatasetForm, inherit=False)
    plugins.implements(plugins.ITemplateHelpers)

    num_times_new_template_called = 0
    num_times_read_template_called = 0
    num_times_edit_template_called = 0
    num_times_search_template_called = 0
    num_times_history_template_called = 0
    num_times_package_form_called = 0
    num_times_check_data_dict_called = 0
    num_times_setup_template_variables_called = 0


    # Update CKAN's config settings, see the IConfigurer plugin interface.
    def update_config(self, config):

        # Tell CKAN to use the template files in
        # ckanext/example_itemplatehelpers/templates.
        plugins.toolkit.add_template_directory(config, 'templates')
        plugins.toolkit.add_public_directory(config, 'public')
        plugins.toolkit.add_resource('fanstatic', 'ckanext-whiterock')


    # Tell CKAN what custom template helper functions this plugin provides,
    # see the ITemplateHelpers plugin interface.
    def get_helpers(self):
        return {'update_frequency': update_frequency}


    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []

    def _modify_package_schema(self, schema):
        schema.update({
                'update_frequency': [tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_extras')]
                })

        schema.update({
                'coordinate_system': [tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_extras')]
                })
        return schema


    def create_package_schema(self):
        schema = super(WhiteRockCommonPlugin, self).create_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def update_package_schema(self):
        schema = super(WhiteRockCommonPlugin, self).update_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def show_package_schema(self):
        schema = super(WhiteRockCommonPlugin, self).show_package_schema()

        # Add our custom_text field to the dataset schema.
        schema.update({
            'update_frequency': [tk.get_converter('convert_from_extras'),
                tk.get_validator('ignore_missing')]
            })

        schema.update({
            'coordinate_system': [tk.get_converter('convert_from_extras'),
                tk.get_validator('ignore_missing')]
            })

        schema.update({
            'more_information': [tk.get_converter('convert_from_extras'),
                tk.get_validator('ignore_missing')]
            })

        schema.update({
            'attribute_details': [tk.get_converter('convert_from_extras'),
                tk.get_validator('ignore_missing')]
            })


        schema.update({
            'is_geospatial': [tk.get_converter('convert_from_extras'),
                tk.get_validator('ignore_missing')]
            })




        return schema

    # These methods just record how many times they're called, for testing
    # purposes.
    # TODO: It might be better to test that custom templates returned by
    # these methods are actually used, not just that the methods get
    # called.

    def setup_template_variables(self, context, data_dict):
        WhiteRockCommonPlugin.num_times_setup_template_variables_called += 1
        return super(WhiteRockCommonPlugin, self).setup_template_variables(
                context, data_dict)

    def new_template(self):
        WhiteRockCommonPlugin.num_times_new_template_called += 1
        return super(WhiteRockCommonPlugin, self).new_template()

    def read_template(self):
        WhiteRockCommonPlugin.num_times_read_template_called += 1
        return super(WhiteRockCommonPlugin, self).read_template()

    def edit_template(self):
        WhiteRockCommonPlugin.num_times_edit_template_called += 1
        return super(WhiteRockCommonPlugin, self).edit_template()

    def search_template(self):
        WhiteRockCommonPlugin.num_times_search_template_called += 1
        return super(WhiteRockCommonPlugin, self).search_template()

    def history_template(self):
        WhiteRockCommonPlugin.num_times_history_template_called += 1
        return super(WhiteRockCommonPlugin, self).history_template()

    def package_form(self):
        WhiteRockCommonPlugin.num_times_package_form_called += 1
        return super(WhiteRockCommonPlugin, self).package_form()

    # check_data_dict() is deprecated, this method is only here to test that
    # legacy support for the deprecated method works.
    def check_data_dict(self, data_dict, schema=None):
        WhiteRockCommonPlugin.num_times_check_data_dict_called += 1
