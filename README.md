# PyFortran

Projeto simples para explorar `interoperabilidade` entre o `Fortran` e o `Python`. Para essa comunicação foi utilização o `f2py`. O `f2py` gera automaticamente um wrapper em `C` para depois compilar uma lib `cpython`. O `f2py` usa `meson` para configurar o build.

Para manter tudo o mais simples possivel a compilação foi feita de forma manual com auxilio de scripts,

## Executando

Para executar:

```bash
python -m src.pyfortran
```

## Compilação da lib Fortran

Primeiro entrar na pasta `src/pyfortran/lib`. Para compilar a lib `.so` basta:

```bash
python -m numpy.f2py -c fblas.f90 fblas.pyf
```

Para gerar o arquivo de interface `fblas.pyf` basta:

```bash
python -m numpy.f2py fblas.f90 -h fblas.pyf -m fblas
```

Após compilar deverá ser criado a lib `fblas.cpython-312-x86_64-linux-gnu.so`.

```bash
└── src
    └── pyfortran
        ├── blas.py
        ├── __init__.py
        ├── lib
        │   ├── fblas.cpython-312-x86_64-linux-gnu.so
        │   ├── fblas.f90
        │   └── fblas.pyf
        └── __main__.py
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

## Rodandos os teste

```bash
pytest
```
