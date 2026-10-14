# Reporte de Análisis de Datos - Pandas

`Jesus Arriaga Machine Learning pandas, NC 0019`

## 1. DataFrame Convertido
```text
                 Titulo           Autor  Paginas
0           Don Quijote       Cervantes      863
1  Cien años de soledad  García Márquez      471
2                  1984          Orwell      328
3         El Principito   Saint-Exupéry       96
4                Hamlet     Shakespeare      180
5                Odisea          Homero      541
```

## 2.1 Primeras Filas (head)
```text
                 Titulo           Autor  Paginas
0           Don Quijote       Cervantes      863
1  Cien años de soledad  García Márquez      471
```

## 2.2 Últimas Filas (tail)
```text
   Titulo        Autor  Paginas
4  Hamlet  Shakespeare      180
5  Odisea       Homero      541
```

## 2.3 Dimensiones (Filas, Columnas)
```text
(6, 3)
```

## 2.4 Tipos de Datos por Columna
```text
Titulo       str
Autor        str
Paginas    int64
dtype: object
```

## 2.5 Información General (info)
```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   Titulo   6 non-null      str  
 1   Autor    6 non-null      str  
 2   Paginas  6 non-null      int64
dtypes: int64(1), str(2)
memory usage: 276.0 bytes

```

## 3. Estadísticas Generales de la Columna 'Paginas'
```text
count      6.000000
mean     413.166667
std      277.218626
min       96.000000
25%      217.000000
50%      399.500000
75%      523.500000
max      863.000000
Name: Paginas, dtype: float64
```

## 4. Ordenar Ascendente por Paginas
```text
                 Titulo           Autor  Paginas
3         El Principito   Saint-Exupéry       96
4                Hamlet     Shakespeare      180
2                  1984          Orwell      328
1  Cien años de soledad  García Márquez      471
5                Odisea          Homero      541
0           Don Quijote       Cervantes      863
```

## 5. Ordenar Descendente por Paginas
```text
                 Titulo           Autor  Paginas
0           Don Quijote       Cervantes      863
5                Odisea          Homero      541
1  Cien años de soledad  García Márquez      471
2                  1984          Orwell      328
4                Hamlet     Shakespeare      180
3         El Principito   Saint-Exupéry       96
```

`Jesus Arriaga Machine Learning pandas, NC 0019`