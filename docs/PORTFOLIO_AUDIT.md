# Fork attribution and portfolio technical audit

Audit date: 2026-10-25. Default-branch source reviewed: `5c2a0dbb0878043deb06a867c96b9e8922f998aa`. Personal example reviewed: `50a5afde14727263f62654f83dc9be7efd29caab` on `feature/advanced-modules`.

## Upstream attribution

This repository is a fork of [orca-telemetry/core](https://github.com/orca-telemetry/core). Orca's Go framework provides telemetry-analytics orchestration using time windows, gRPC, a PostgreSQL data layer and dependency scheduling. Those components and their inherited tests are upstream work.

The upstream module path remains `github.com/orca-telemetry/core`. `LICENSE.md` credits Orca under the MIT license; preserve that license and attribution.

## Personal contribution

[Commit 50a5afde](https://github.com/thestratege/core/commit/50a5afde14727263f62654f83dc9be7efd29caab), authored by `thestratege`, adds three files on the personal feature branch:

- `examples/gaetan-first-processor/README.md`
- `examples/gaetan-first-processor/processor.py`
- `examples/gaetan-first-processor/window.py`

At the reviewed revision, this branch was one commit ahead of the default branch. The example is not present in the reviewed default-branch tree.

`processor.py` registers a processor named `ml` with a `Every30Second` window type and a function named `LinearRegression`. `window.py` emits 30-second windows carrying fictional `asset_id=1` metadata.

The demonstration result returns constants `m=10` and `c=-1`. It does not fit a regression model, measure prediction accuracy or demonstrate model training. The portfolio should attribute the integration example to Gaetan, with Orca credited for the framework.

## Verification and limits

Python AST syntax parsing of both example files passed. The SDK, processor, window emission, Core/PostgreSQL/gRPC chain, Docker environment and Go test suite were not executed during this audit.

The inherited repository contains Go tests and CI declaring `go test ./... -v`. Test presence does not establish that tests ran successfully here and does not change attribution. No performance, production-readiness or ML-quality metric is claimed.

The example README at the reviewed commit was truncated and contained accidental heredoc text plus a machine-specific path. A repair on the personal branch should supply repository-relative commands, runtime prerequisites and these limitations.

## Useful next steps

1. Pin the Python SDK version and document its Core/contract compatibility.
2. Run Core with a disposable PostgreSQL instance using upstream documentation.
3. Run processor and emitter in separate terminals; capture sanitized output.
4. Add focused tests for metadata conversion and structured results.
5. If adding real regression, distinguish training/evaluation from the current constant-result example.

## Résumé français

Contribution Python ciblée sur un fork MIT d'Orca: déclaration d'un processeur, émission de fenêtres de 30 secondes et résultat structuré de démonstration. Le framework Go est attribué à Orca. L'exemple ne réalise pas encore d'apprentissage et son exécution complète n'est pas vérifiée par cet audit.
