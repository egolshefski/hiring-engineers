from datadog import initialize, api

options = {
    'api_key': 'd6ddf50c17ee7a58a70e2f35761694d9',
    'app_key': 'ea0a4b78f41f7ab180deebeb37f09c4eac64b4c2'
}

initialize(**options)

title = 'Visualizing Data v2'

widgets = [{
# create graph for my_metric scoped over my host
    'definition': {
        'type': 'timeseries',
        'requests': [
            {'q': 'avg:my_metric{host:docker-desktop}'}
        ],
        'title': 'Avg of my_metric over host:docker-desktop'
    }
},
{
# creates graph of a MongoDB metric w/ the anomaly function applied
    'definition': {
        'type': 'timeseries',
        'requests': [
            {'q': "anomalies(avg:mongodb.stats.objects{*}, 'basic', 2)"}
        ],
        'title': 'Avg of mongodb.stats.objects over * with basic anomaly function'
    }
}
]

layout_type = 'ordered'
description = 'Visualizing Data portion of Datadog take home assignment.'
is_read_only = False

# API call to create dashboard
api.Dashboard.create(title=title,
                     widgets=widgets,
                     layout_type=layout_type,
                     description=description,
                     is_read_only=is_read_only)