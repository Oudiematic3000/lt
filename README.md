# GetBest.py Lab Test
Authored by **nixkj** and **morisscofield**
Modified by **Oudiematic3000**
 **Ariel Oudmayer - 2695316**
## Description
getbest.py is a program that returns the student with the highest mark given a data file containing (at least) students' student numbers and marks in correlating columns.

The data file must be in a text format. The first line should be the column heads as such:

*Course,Student Number,Mark,Comment*

Each next line should be the data for one student as such:

*ELEN3020,160001,72,OK*

Any order of columns is permitted so long as the headings always match the column data.

## How to Use

Within the `lt/getbest` directory, run the script directly from the command line:

```
python getbest.py bestdat0.csv
```
Note that `bestdat0.csv` is the sample data in the repository and can be replaced with any csv file of correct format.

## Tests

Four tests exist to check the `getCols(f)` method (Which returns the columns containing student number and marks) and the `FindTop(f)` method (which returns the student number with the highest mark and said mark)

Run the tests from `lt` using
```
python -m unittest discover
```
or directly from `lt` using
```
python -m unittest test.test_getbest
```

Note that the tests run on a different set of sample data to show that the functions work independent of column order and data.