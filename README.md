# tor-node-inspector
Parse and monitor Tor nodes for statistics and patterns.

## Description

We need to read and store data for the first 100 nodes that we find in the local Tor compendium.
Once we get data for a week or so, we will be able to infer statistics and to identify patterns.

### Objectives

Be able to identify the best nodes to connect at the Tor network.

## Instructions

To read the contents of the configuration file:
    ```python inspect_nodes.py >> output_file```

### Configuration

We can configure this task to be executed on a crontab every third hour:
    ```0 */3 * * * /bin/python inspect_nodes.py```

## TODO - Read gathered data
