init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="example",
            prompt="Example",
            category=["example"],
            pool=True
        )
    )

label example_break:
    m 1eua "Hello, World!"
    return