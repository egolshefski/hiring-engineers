# Take Home Assignment Answers

## Collecting Metrics

Below is a screenshot of a hostmap of my host, **docker-desktop**, and the tag **environment:dev**:

![hostmap with tag](media/collecting-metrics/hostname-with-tag.png)

I used the following config and code files in this section:

- [**datadog.yaml**](snippets/datadog.yaml): Added tag **environment:dev**
- [**custom_mymetric.py**](snippets/custom_mymetric.py): Code used to create **my_metric**
- [**conf.yaml**](snippets/conf.yaml): Added values to configure metric collection from MongoDB integration

## Visualizing Data

## Visualize my_metric and MongoDB metric

Here is a public link to my timeboard: [**Visualizing Data**](https://p.datadoghq.com/sb/8vc0q0kczjqs7dzr-9028af4d446812c5aa928eb088f3b9be)

Below is a screenshot of my timeboard:

![visualizing data dashboard](media/visualizing-data/visualizing-data-dashboard.png)

See [**create_timeboard.py**](snippets/create_timeboard.py) for the code used to create this dashboard.

**Bonus Questions**: What is the Anomaly graph displaying?

- The anomaly graph is diplaying a grey band overlay that shows the expected series of behavior based on the past. This particular algorithm is showing the number of expected objects in the MongoDB database. Data within the bounds of the gray overaly can be interepreted as standard deviations (2-3 usually) for the algorithm.

### Send a snapshot using @

Below is a screenshot confirming I sent a snapshot to myself using the @ notation:

![confirm snapshot email](media/visualizing-data/confirm-snapshot-email.png)

## Final Question

I chose the [`dog-watcher`](https://github.com/brightcove/dog-watcher) community library.

Here's a link to my blog post: [Store dashboard and monitor configurations on GitHub with `dog-watcher`](dog-watcher-blog-post.md)