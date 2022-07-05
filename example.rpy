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
    # Trigger CI (again)
    m 1eua "Hello, World!"
    return