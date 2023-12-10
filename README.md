# PyFortran

### Executand


Para executar:

```bash
python -m src.pyfortran
```

## Compilação da lib Fortran

A compilaçãp será feita de forma manual usando o `f2py` e `meson`.

Primeiro entrar na pasta `src/pyfortran/lib`. Para compilar a lib `.so` basta:

```bash
python -m numpy.f2py -c --backend meson fblas.f90 fblas.pyf
```

Para gerar o arquivo de interface `fblas.pyf` basta:

```bash
python -m numpy.f2py fblas.f90 -h fblas.pyf -m fblas
```
