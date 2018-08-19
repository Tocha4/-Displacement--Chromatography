# -Displacement--Chromatography
Dieses Werkzeug zur Simulation einer chromatographischen Säule war Teil meiner Masterarbeit. Mit diesem Projekt habe ich mich in die objektorientierte Programmierung eingearbeitet. Neben den standard Bibliotheken wie ```numpy, matplotlib``` fürs wissenschaftliche Arbeiten habe ich [PyQT](https://www.riverbankcomputing.com/software/pyqt/intro) und [Cython](http://cython.org/) benutzt.



## Used versions:

* Linux 16.04 LTS 
* Python 3.6.1 | Anaconda 4.4.0 
* numpy 1.12.1 
* matplotlib 2.0.2 
* distutils 3.6.1 
* PyQT5 5.6.2 
* Cython 0.25.2 

Befor running the _Chromatography_Simulator.py_ file, open a **cmd** in _...Calculation/cython_functions_ and execute:

>.../cython_functions$  ```python setup.py build_ext --inplace```


# GUI
![Cromatography Simulator GUI](https://raw.githubusercontent.com/Tocha4/-Displacement--Chromatography/master/cs.png)

### The following equation is solved
![mass balance](https://raw.githubusercontent.com/Tocha4/-Displacement--Chromatography/master/mass_balance.png)
