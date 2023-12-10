# PyFortran

### Executand

Para executar:

```bash
python -m src.pyfortran
```

## Compilação da lib Fortran

A compilação será feita de forma manual usando o `f2py` e `meson`.

Primeiro entrar na pasta `src/pyfortran/lib`. Para compilar a lib `.so` basta:

```bash
python -m numpy.f2py -c fblas.f90 fblas.pyf
```

Para gerar o arquivo de interface `fblas.pyf` basta:

```bash
python -m numpy.f2py fblas.f90 -h fblas.pyf -m fblas
```

## Scripts de apoio

Os scripts de apio são:

- build_lib.sh: Gera a lib `.so`
- build_pyf_files.sh: Gera o arquivo `.pyf`
- clean_lib.sh: Deleta o arquivo lib `.so`
- clean_pyf_files.sh: Deleta o arquivo `.pyf`
- clean.sh: Deleta os arquivos `.pyf` e `.so`
- build.sh: Gera os arquivos `.pyf` e `.so`

Para usaros scripts basta:

```bash
./scripts/build.sh
```
