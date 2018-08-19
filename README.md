# -Displacement--Chromatography
Dieses Werkzeug zur Simulation einer chromatographischen Säule war Teil meiner Masterarbeit. Mit diesem Projekt habe ich mich in die objektorientierte Programmierung eingearbeitet. Neben den standard Bibliotheken wie ```numpy, matplotlib``` fürs wissenschaftliche Arbeiten habe ich [PyQT](https://www.riverbankcomputing.com/software/pyqt/intro) und [Cython](http://cython.org/) benutzt.

# GUI
Die unten aufgeführte graphische Oberfläche habe ich mit ```PyQT5``` erstellt. Mit dem _QT designer_ lässt sich so eine graphische Oberfläche, auch für einen Neuling, innerhalb von einigen Tagen erstellen. 

In der oberen linken Ecke werden die thermodynamischen Eigenschaften über das Adsoption- und Desorptionsverhalten der Komponenten eingestellt. Mit dem **Show adsoption isotherm**-Button lassen sich diese Eigenschaften in einem Plot überprüfen.

In der linken unteren Ecke technischen Eigenschaften des Setups eingestellt. Sobald alle Eigenschaften eingestellt sind, muss diese akzeptiert werden, bevor die Simulation gestartet werden kann. Die Daten der Simulation können als eine ```numpy``` Datei (```.npy```) gespeichert oder geladen werden.

Auf der recheten Seite kann das Ergebniss eienr Simulation in den beiden Plots analysiert werden. Die Verteilung der Komponenten in der Säule wird oben dargestellt. Zum Vergleich zu realen Messungen wird ebenfalls ein Chromatogram zur Simulation erzeugt (unten).

Um die graphische Oberfläche zu starten, öffne eine _Comand-Line_ in dem Ordner mit __Chromatography_Simulator.py__ und führe ```python Chromatography_Simulator.py``` aus.

![Cromatography Simulator GUI](https://raw.githubusercontent.com/Tocha4/-Displacement--Chromatography/master/cs.png)

# Lösung der Gleichung
Um die unten dargestellt Gleichung effektiv lösen zu können, habe ich die Bibliothek ```Cython``` verwendent. Es hat sich gezeigt, dass einfache Simulationen mit ```numpy``` relativ schnell durchgeführt werden können. Sobald aber die Anzahl der Komponenten steigt und die Säulen größer werden, steigt die Berechungungszeit. Mit ```Cython``` habe ich die rechenintensiven Berechnungen in kompilierten Funktionen ausgelagert. Damit habe ich eine Erhöhung der Berechungsgeschwindigkeit um den Faktor _x6_ erreicht. 

![mass balance](https://raw.githubusercontent.com/Tocha4/-Displacement--Chromatography/master/mass_balance.png)
