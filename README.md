# Petra Tools

This repository is a collection of python scripts that were written to help a Petra user complete workflows easier. 

Petra is a geological interpretation sotfware by S&P Global:
[https://www.spglobal.com/commodityinsights/en/ci/products/petra-geological-analysis.html](https://www.spglobal.com/commodityinsights/en/ci/products/petra-geological-analysis.html)

# Table of Contents
- [Petra Batch Grid Import](#PetraBatchGridImport)

## Petra Batch Grid Import

### Workflow for Kingdom Grids

1. Export grids from Kingdom using the IsoMap Z-MAP Plus format.
   - Tip: Export each interpreter's grids into their own folder and use the `moveandaddinterpreter()` function. This will rename the grid files using the folder name as a prefix, making it easier to identify the grid's creator when using them in Petra.

2. Create a text file containing the file paths of the grid files you want to import into Petra using the `petrabatchgridtxtfile()` function.

3. Import the grids into Petra:
   - Go to Petra > Map > Contours > Grids > Import > Landmark Zmap Plus Grid.
   - Check the "Input File Is Really A List of Grid Files To Batch Import" option.
   - Select the file created in step 2 as the input file.

### Additional Functions

In addition to the Kingdom workflow, this repository provides functions to create text files for batch loading of shapefiles and .dat files into Petra:

- `petrabatchshapefiletxtfile(filepath)`: Create a text file for batch loading shapefiles into Petra.
- `petrabatchdatfiletxtfile(filepath)`: Create a text file for batch loading .dat files into Petra.

### Usage

You can use these functions to simplify your workflow when working with grid data in Petra and Kingdom. Simply follow the instructions above for each step of the process.

#### `moveandaddinterpreter(filepath)`

This function renames grid files using the folder name as a prefix. Files will be moved from the subfolders in `filepath` to `filepath`.

```python
moveandaddinterpreter('C:\Grids for Petra')
```

#### `petrabatchgridtxtfile(filepath)`

This function creates a text file that can be used to batch import grid files into Petra.

```python
petrabatchgridtxtfile('C:\Grids for Petra')
```

#### `petrabatchshapefiletxtfile(filepath)`

Create a text file to batch import shapefiles into Petra.

```python
petrabatchshapefiletxtfile('C:\Shapefiles for Petra')
```

#### `petrabatchdatfiletxtfile(filepath)`

Create a text file to batch import .dat files into Petra.

```python
petrabatchdatfiletxtfile('C:\DatFiles for Petra')
```

Feel free to contribute to this repository and improve the workflow tools. If you encounter any issues or have suggestions, please create an issue or a pull request.

Happy geoscience coding!
```

You can copy and paste this Markdown code into your GitHub repository's README.md file.
