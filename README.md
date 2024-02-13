# Supplementary code for the paper Automatic motion estimation with applications to hiPSC-CMs

This repository contains supplementary code for reproducing results in the paper
>


The code is heavily based on the library [`mps-motion`](https://github.com/ComputationalPhysiology/mps_motion). Please check out the [documentation](https://computationalphysiology.github.io/mps_motion/) in that library for more details.

## Running with binder
If you want to run the examples without installing anything you can launch an interactive environment with Binder, by clicking the following button: TODO: Add button

## Running locally
To run the notebooks locally, you first need to install the necessary requirements. There are two options. Either, you can create a virtual environment with python
```
python3 -m venv venv
```
and activate it. On Unix (MacOSX and Linux) you do
```
. \venv/bin/activate
```
and on Windows you do
```
.\venv\Scripts\activate
```
Next you install the dependencies
```
python3 -m pip install -r requirements.txt
```
