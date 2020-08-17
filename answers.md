# Take Home Assignment Answers

## Collecting Metrics

Below is a screenshot of a hostmap of my host, **docker-desktop**, and the tag **environment:dev**:

![hostmap with tag](media/collecting-metrics/hostname-with-tag.png)

**Bonus Question**: Can you change the collection interval without modifying the Python check file you created?

See the following files for code I used in this section:

- [datadog.yaml](datadog.yaml): Added tag **environment:dev**
- [custom_mymetric.py](custom_mymetric.py): Code used to create **my_metric**

## Visualizing Data

## Visualize my_metric and MongoDB metric

Below is a screenshot of my dashboard:

![visualizing data dashboard](media/visualizing-data/visualizing-data-dashboard.png)

See [**create_dashboard.py**](create_dashboard.py) for the code used to create this dashboard. 

### Send a snapshot using @

Below is a screenshot confirming I sent a snapshot to myself using the @ notation:

![confirm snapshot email](media/visualizing-data/confirm-snapshot-email.png)