# -*- coding: utf-8 -*-
"""
@author: jjcharzynski
linkedin.com/in/jjcharzynski
github.com/jjcharzynski

Workflow for grids:
    1. Export grids from Kingdom using the IsoMap Z-MAP Plus format
        Tip: Export each interpreter's grids into their own folder and use the moveandaddinterpreter() function.
            This will rename the grid files using the folder name as a prefix so that you know who made the grid when using in Petra
    2. Create a text file of the grid files file paths to import into Petra using petrabatchgridtxtfile() function.
    3. Import the grids using Petra>Map>Contours>Grids>Import>Landmark Zmap Plus Grid
        using the Input File Is Really A List of Grid Files To Batch Import Checkbox and selecting the file created in step 2.

Additional functions to create text file for batch .shp and .dat file loading into Petra.
    petrabatchshapefiletxtfile(filepath)
    petrabatchdatfiletxtfile(filepath)
    
"""

def moveandaddinterpreter(filepath):
    '''
    Renames grid files using the folder name as a prefix so that users know who made the grid when using in Petra.
    Files will be moved from the subfolders in filepath to filepath.

    Parameters
    ----------
    filepath : STRING
        String to the folder containing the grids to import. (e.g. 'C:\Grids for Petra') 
        Subfolders for each interpreter's grids will be subfolders in this folder.

    Returns
    -------
    None.

    '''
    import os
    import shutil
    from pathlib import Path
    
    listoffiles = list()
    for (dirpath, dirnames, filenames) in os.walk(filepath):
        listoffiles += [os.path.join(dirpath, file) for file in filenames]
      
    for file in listoffiles:
        folder = os.path.dirname(file)
        filename = Path(file).name
        newname = folder + '_' + filename
        shutil.move(file, newname)


def petrabatchgridtxtfile(filepath):
    '''
    Creates a text file to be used in the Map Module>Contours>Grids>Import>Landmark Zmap Plus Grid
        using the Input File Is Really A List of Grid Files To Batch Import Checkbox
    
    Parameters
    ----------
    filepath : STRING
        String to the folder containing the grids to import. (e.g. 'C:\Grids for Petra')
    Assumes that grids used are in the IsoMap Z-MAP Plus format and .dat files
        
    Returns
    -------
    None.

    '''
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(filepath) if isfile(join(filepath, f))]
    batchfile = filepath + '\\' + 'BatchGridsToImport.txt'
    with open(batchfile, "w") as file:
        for x in onlyfiles:
            if '.dat' in x:
                string = filepath + '\\' + x
                file.write(string + '\n')


def petrabatchshapefiletxtfile(filepath):
    '''
    Creates a text file to be used in the Map Module>Contours>Grids>Import>Landmark Zmap Plus Grid
        using the Input File Is Really A List of Grid Files To Batch Import Checkbox
    
    Parameters
    ----------
    filepath : STRING
        String to the folder containing the grids to import. (e.g. 'C:\Grids for Petra')
    Assumes that grids used are in the IsoMap Z-MAP Plus format and .dat files
        
    Returns
    -------
    None.

    '''
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(filepath) if isfile(join(filepath, f))]
    batchfile = filepath + '\\' + 'BatchShapefilesToImport.txt'
    with open(batchfile, "w") as file:
        for x in onlyfiles:
            if '.shp' in x:
                string = filepath + '\\' + x
                file.write(string + '\n')
                
def petrabatchdatfiletxtfile(filepath):
    '''
    Creates a text file to be used in the Map Module>Contours>Grids>Import>Landmark Zmap Plus Grid
        using the Input File Is Really A List of Grid Files To Batch Import Checkbox
    
    Parameters
    ----------
    filepath : STRING
        String to the folder containing the grids to import. (e.g. 'C:\Grids for Petra')
    Assumes that grids used are in the IsoMap Z-MAP Plus format and .dat files
        
    Returns
    -------
    None.

    '''
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(filepath) if isfile(join(filepath, f))]
    batchfile = filepath + '\\' + 'BatchShapefilesToImport.txt'
    with open(batchfile, "w") as file:
        for x in onlyfiles:
            if '.dat' in x:
                string = filepath + '\\' + x
                file.write(string + '\n')