import time
import datetime as dt

from orca_python import Window, EmitWindow

def emit_window() -> None:
    now = dt.datetime.now()

    window = Window(
        time_from=now - dt.timedelta(seconds=30),
        time_to=now,
        name="Every30Second",
        version="1.0.0",
        origin="Example",
        metadata={"asset_id": 1},
    )

    print(f"Emitting window from {window.time_from} to {window.time_to}")
    response = EmitWindow(window)
    print(f"Emit response: {response}")

if __name__ == "__main__":
    while True:
        emit_window()
        time.sleep(30)
