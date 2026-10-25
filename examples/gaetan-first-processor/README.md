# Gaetan's first Orca processor example

A small integration example contributed on top of [Orca Core](https://github.com/orca-telemetry/core). Orca supplies the orchestration framework and Python SDK.

```text
window.py -> Orca Core -> processor.py -> structured demo result
```

## What the code does

- Registers a Python processor named `ml`.
- Defines a `Every30Second` window type with an `asset_id` metadata field.
- Emits a 30-second window every 30 seconds using fictional `asset_id=1`.
- Triggers a function named `LinearRegression`.
- Returns a structured result with constant `m=10`, `c=-1`, the asset ID and a status field.

The algorithm is an orchestration demonstration. It does not fit a linear regression model or measure prediction accuracy.

## Prerequisites

1. Use a working Orca Core instance and its PostgreSQL data layer, following the [upstream documentation](https://orcatelemetry.io/docs).
2. Create a Python environment with an `orca_python` SDK version compatible with that Core instance.
3. Configure the SDK connection according to that version's documentation.

This example does not yet pin an SDK version or provide its own dependency file. Do not assume an SDK package name or version from the import alone.

## Run from the repository root

Start Core first. In one terminal, activate the prepared Python environment and run the processor:

```sh
python examples/gaetan-first-processor/processor.py
```

In a second terminal using the same SDK environment:

```sh
python examples/gaetan-first-processor/window.py
```

Stop either process with Ctrl+C. The emitter runs indefinitely.

The code prints emitted time windows and processor activity. A successful Core connection, scheduling and structured result should be verified against sanitized runtime output; this README does not claim that such a run was performed during the 2026-10-25 audit.

## Verification and limitations

- Both Python files passed static AST syntax parsing during the audit.
- The Python SDK, gRPC connection, database and full execution chain were not run during that audit.
- No real regression, benchmark or production-readiness claim is made.
- Metadata conversion is demonstration code; test it with the actual SDK/Protobuf value types before relying on nonnumeric values.
- Keep real asset identifiers, credentials and private telemetry out of public output.

## Attribution

The example files are the focused personal contribution. The Go framework, database orchestration and inherited tests belong to the upstream Orca project. Preserve [the MIT license](../../LICENSE.md).
