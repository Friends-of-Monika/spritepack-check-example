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

label example:
    m 1eua "Hello, World!"
    return