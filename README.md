<!--- Heading --->
<div align="center">
  <h1>NBCC Loadings</h1>
  <p>
    Library to obtain NBCC Loadings
  </p>
<h4>
    <a href="https://github.com/rpakishore/nbcc-loadings/">View Demo</a>
  <span> · </span>
    <a href="https://github.com/rpakishore/nbcc-loadings">Documentation</a>
  <span> · </span>
    <a href="https://github.com/rpakishore/nbcc-loadings/issues/">Report Bug</a>
  <span> · </span>
    <a href="https://github.com/rpakishore/nbcc-loadings/issues/">Request Feature</a>
  </h4>
</div>
<br />

[![tests](https://github.com/rpakishore/nbcc-loadings/actions/workflows/test.yml/badge.svg)](https://github.com/rpakishore/nbcc-loadings/actions/workflows/test.yml)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/rpakishore/nbcc-loadings)
![GitHub last commit](https://img.shields.io/github/last-commit/rpakishore/nbcc-loadings)

![PyPI - Format](https://img.shields.io/pypi/format/nbcc_loading) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/nbcc_loading)

<!-- Table of Contents -->
<h2>Table of Contents</h2>

- [1. About the Project](#1-about-the-project)
- [2. Getting Started](#2-getting-started)
  - [2.1. Installation](#21-installation)
- [3. Usage](#3-usage)
- [4. Roadmap](#4-roadmap)
- [5. License](#5-license)
- [6. Contact](#6-contact)
- [7. Acknowledgements](#7-acknowledgements)

<!-- About the Project -->
## 1. About the Project

A library to supply NBCC loadings, to be incorporated into other calculations

<!-- Getting Started -->
## 2. Getting Started

<!-- Installation -->
### 2.1. Installation

Install from pypi

```bash
pip install nbcc_loading
```
<!-- Usage -->
## 3. Usage

```python
# Load required modules
from nbcc_loading import Snow, Wind

# Set the year
snow = Snow.set_year(year=2015) 
## Can also directly call instance, such as
wind = Wind(2015)

# Get the 3 closest stations to specified coordinates
s_loads = snow.by_gps(latitude=49.2508744, longitude=-122.9032094, data_points=3)
w_load = wind.by_location(city='Agassiz')

# Extract Station Information
s_load = s_loads[0]
s_load.Ss # Snow Load
s_load.Sr # Rain Load
w_load.yr10 # 10-year return wind
w_load.yr50 # 50-year return wind
```

<!-- Roadmap -->
## 4. Roadmap

- [ ] Snow Loadings
  - [x] NBCC 2020
  - [x] NBCC 2015
  - [ ] NBCC 2010
- [ ] Wind Loadings
  - [x] NBCC 2020
  - [x] NBCC 2015
  - [ ] NBCC 2010
- [ ] Seismic Loadings
  - [ ] NBCC 2020
  - [ ] NBCC 2015
  - [ ] NBCC 2010

<!-- License -->
## 5. License

See `LICENSE` for more information.

<!-- Contact -->
## 6. Contact

Arun Kishore - [@rpakishore](mailto:pypi@rpakishore.co.in)

Project Link: [https://github.com/rpakishore/nbcc-loadings](https://github.com/rpakishore/nbcc-loadings)

<!-- Acknowledgments -->
## 7. Acknowledgements

- [Awesome README Template](https://github.com/Louis3797/awesome-readme-template/blob/main/README-WITHOUT-EMOJI.md)
- [Shields.io](https://shields.io/)
