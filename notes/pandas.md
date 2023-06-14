# Pandas

## To remember

* Set appropriate types with `astype` when loading the data set.
* Use `assign` to create new columns
* Use method chaining and `pipe`. It will:
  - make code readable
  - easy to debug
  - less bug-prone
* Don't use mutations (i.e. no `inplace` property)
* Don't use `apply` if you can, it's slow for numbers, it's ok with strings. It's better than loops though.
* Never use Python loops to manipulate data with Pandas

## Data Types

Setting appropriate types helps saving space in memory and enable appropriate operations on types (math for numbers, manipulation for strings, etc.)

| **Pandas** | **NumPy** | **Python** |
|:---:|:---:|:---:|
| object | string_, unicode_, mixed types | str, mixed |
| int64 | int_, int8, int16, int32, int64, uint8, uint16, uint32, uint64 | int |
| float64 | float_, float16, float32, float64 | float |
| bool | bool_ | bool |
| datetime64 | datetime64[ns] | NA |
| timedelta[ns] | NA | NA |
| category | NA | NA |

When loading data, Pandas casts the values of the dataset in generally three main data types (four if we explicitly cast dates).

### int64

The values are integer and there are no missing values.

### float64

In this case, the values can be
* integers with missing values
* actual floating point numbrs with or without missing values

### object

This is the type used when Pandas doesn't know how to interpret the values. Usually, text or mixed numeric and non-numeric values.

Objects are not fast because they point to a Python object type. In general, strings are cast as object, but it could be other data like JSON for example.

## How to set data types

It reduces memory usage.

```py
(
  dataset
    .astype({
      'col1': 'int8',
      'col2': 'float16',
      'col3': 'datetime64',
      'col4': 'bool',
      'col5': 'category'
    })
)
```

## How to create new columns

Use `assign` to create new columns.

```py
(
  dataset
    .assign(
      col1 = dataset.col2 + dataset.col3,
      col5 = dataset.col4.fillna('Other').astype('category')
    )
)
```

## Method chaining

Use method chaining to prepare the dataset.

Use `pipe` if something can't be chained (it doesn't return "self").

Easy to debug:
- comment out chained statements
- use pipe to print the intermediate dataframe with IPython.display (or plain `print` function)
- use pipe to assign the intermediate dataframe to a global variable to be printed later outside the chain

```py
(
  dataset
    .assign(
      col1 = dataset.col2 + dataset.col3,
      col5 = dataset.col4.fillna('Other').astype('category')
    )
)
```

## Mutations

Do not mutate.

Ref:
- https://github.com/pandas-dev/pandas/issues/16529
- https://github.com/pandas-dev/pandas/issues/16529#issuecomment-323890422

* No performance gain
* Stops chaining
* Prevents `SettingWithCopyWarning` to occur

### The `SettingWithCopyWarning` issue

The output of a `get` (indexing) operation in Pandas is not guaranteed. Either a view or a copy of the DataFrame could be returned. Whether you get a reference or not depends on the structure and data types in the original DataFrame.

This happens because Pandas uses NumPy under the hood. An indexing operation that slices a portion of the DataFrame with same data type will be referenced in the same NumPy array for efficiency. If we set a value of a different data type, a new array must be created to store that value. This is because NumPy arrays store a series of values of the same type.

To prevent unintended operations - i.e. assigning a value to a view thinking is a copy and viceversa - pandas raises a `SettingWithCopyWarning` warning because it cannot infer whether the returned value is a view or a copy and what your intention is.

## The `apply` method

As a general rule of thumb, try not to use the `apply` method if you can, unless you have to.

Because we are passing a Python function to the `apply` method, Pandas is going to get each individual entry from the DataFrame, convert it in a Python object, pass the entry as a parameter and manipulate it and finally convert the result back to the Pandas original data type. This overhead makes this method slow, compared to a more Pandas-oriented approach.

**Example: Celsius to Kelvin conversion**

Let's transform Celsius temperatures to Kelvin. The formula is the following:

$$Kelvin = Celsius + 273.15$$

The `apply` method will be something like the following

```py
def get_kelvin_from_celsius(temp):
  return temp + 273.15

dataframe.temperature.apply(get_kelvin_from_celsius)
```

whereas an approach that uses Pandas indexing will look like the following

```py
dataframe.temperature = dataframe.temperature + 273.15
```

The last approach is more performant than the `apply` method.

Strings are not optimised in Pandas. It uses Python objects under the hood. For this reason the performance may look similar with both methods.

With numbers you can also use the `where` method combined in an `assign`. With strings it will be a bit slower compared to the `apply` example.

```py
(
  dataframe
    .assign(col1='Default')
    .assign(col1=lambda df: df.col1.where(df.col2.isin(values)), 'Standard')
)
```

## Aggregation

if `groupby` is similar to the SQL counterpart, the `having` clause can be emulated with a `pipe` function.

```py
def greater_than(df, val):
  return df[df.gt(val)].dropna()

(
  dataframe
    .groupby(['col1'])
    .pipe(greater_than, '100') # having
)
```
