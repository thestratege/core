from orca_python import (
    Processor,
    WindowType,
    StructResult,
    MetadataField,
    ExecutionParams,
)

proc = Processor("ml")

asset_id_field = MetadataField(
    name="asset_id",
    description="The unique ID of the asset."
)

Every30Second = WindowType(
    name="Every30Second",
    version="1.0.0",
    description="Triggers every 30 seconds",
    metadataFields=[asset_id_field],
)

def extract_metadata_value(value):
    """
    Convert Orca/Protobuf metadata values into normal Python values.
    """
    if value is None:
        return None

    if hasattr(value, "number_value"):
        return int(value.number_value)

    if hasattr(value, "string_value"):
        return value.string_value

    if hasattr(value, "bool_value"):
        return value.bool_value

    return str(value)

@proc.algorithm(
    name="LinearRegression",
    version="1.0.0",
    description="Simple linear regression example triggered every 30 seconds.",
    window_type=Every30Second
)
def linear_regression(params: ExecutionParams) -> StructResult:
    raw_asset_id = params.window.metadata.get("asset_id", None)
    asset_id = extract_metadata_value(raw_asset_id)

    print(f"Processing asset_id={asset_id}")
    print(f"Window from {params.window.time_from} to {params.window.time_to}")

    return StructResult({
        "m": 10,
        "c": -1,
        "asset_id": asset_id,
        "status": "success"
    })

if __name__ == "__main__":
    proc.Register()
    proc.Start()
