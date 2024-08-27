[![DOI](https://zenodo.org/badge/699045305.svg)](https://zenodo.org/doi/10.5281/zenodo.13379848)
# Supplementary code for the paper Automatic motion estimation with applications to hiPSC-CMs

This repository contains supplementary code for reproducing results in the paper
>

Output of rendered notebooks are found at <https://computationalphysiology.github.io/automatic-motion-estimation/README.html>.

The code is heavily based on the library [`mps-motion`](https://github.com/ComputationalPhysiology/mps_motion). Please check out the [documentation](https://computationalphysiology.github.io/mps_motion/) in that library for more details.

## Running with binder
If you want to run the examples without installing anything you can launch an interactive environment with Binder, by clicking the following button [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ComputationalPhysiology/automatic-motion-estimation/HEAD)

## Running locally

### Python virtual environment
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

### Docker

We also provide two different docker images for you. In order to start a container you can use the docker run command. For example the command
```
docker run --rm -v $(pwd):/home/shared -w /home/shared -ti ghcr.io/computationalphysiology/automatic-motion-estimation:latest
```
will run the latest version and share your current working directory with the container. The source code of the repository is located at `/repo` in the docker container.

To run the notebooks, one can use `ghcr.io/computationalphysiology/automatic-motion-estimation-lab:latest`, i.e
```
docker run -ti -p 8888:8888 --rm ghcr.io/computationalphysiology/automatic-motion-estimation-lab:latest
```
to run interactively with Jupyter lab in browser.

## Citing
If you use this code in your research, please cite the following paper
```
@article{10.1088/2057-1976/ad7268,
	author={Finsberg, Henrik Nicolay Topnes and Charwat, Verena and Healy, Kevin E and Wall, Samuel},
	title={Automatic motion estimation with applications to hiPSC-CMs},
	journal={Biomedical Physics & Engineering Express},
	url={http://iopscience.iop.org/article/10.1088/2057-1976/ad7268},
	year={2024},
}
```
