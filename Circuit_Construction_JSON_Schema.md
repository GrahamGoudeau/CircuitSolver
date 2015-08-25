# Circuit Construction JSON Schema
### Schema
Requests to the service must take the form of JSON objects which conform to the following schema:

- `components` - top-level array of component objects
- `component objects` - must contain the following properties
    - `name` - must be unique across the list of components, error if not unique
    - `type` - must be one of the members of the list below, all lowercase letters
    - `junctions` - a list of strings which are the names of junctions this component is connected to.
        - The list of junctions must have as many entries as the component has prongs.  For example, a resistor must have two entries in its `junctions` list, while an open must have only one.  It is an error if this requirement is not satisfied.
    - `value` - this field is required if the component has some value like resistance or capacitance associated with it.  It is an error if this field is expected but is missing.

An example JSON object which conforms to the schema:
```
{
    "components": [
        {
            "name": "resistor1",
            "type": "resistor",
            "value": 5,
            "junctions": [
                "j1",
                "j2"
            ]
        },
        {
            "name": "resistor2",
            "type": "resistor",
            "value": 10,
            "junctions": [
                "j1",
                "j2"
            ]
        }
    ]
}
```

### Accepted component types
The accepted component types must be drawn from the lists below:


` Single prong: ['open']`

` Two prongs: ['resistor', 'capacitor'] `
