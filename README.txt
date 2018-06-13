IR LED ring (ILR) illuminator
Designed to be used with Mitutoyo M Plan IR objectives


Mityotyo M Plan APo objective measurements
Note: https://www.edmundoptics.com/microscopy/infinity-corrected-objectives/Mitutoyo-NIR-NUV-and-UV-Infinity-Corrected-Objectives/
Note: https://www.edmundoptics.com/microscopy/infinity-corrected-objectives/Mitutoyo-Infinity-Corrected-Long-Working-Distance-Objectives/
Main diameter: 32.25 mm
Objective to objective clearance on main area up to knurled area: ~30 mm
    Total clearance diameter: 32.25 + 30/2 = 47.25 mm
    Try to keep below 45
Knurled diameter: 34.00 mm
Flat area to knurled (10x objective): ~20.5 mm
Mityotyo sample working distances (note: multiple versions)
    Mag     WD
    5x      37.5
    10x     30.5
    20x     20,25.5
    50x     10,17
    100x    10,12

Dimension proposals
LEDs at 50 mm diameter
LEDs are 8.6 mm high => 10 mm approximately with standoff
Middle of PCB cut to 33 mm (touch up with file if necessary)

45 degree angle seems good starting point
What would focal point be at?
distance = 25 * sin(45) = 17.7 mm
limits use to the 20x objective


Designs 
-ilr-ext: externally powered using benchtop supply in current mode, 100 mA max
    Production design, use this
-ilr-lm317: LM317 current regulated, 12V in, always max brightness
-ilr-r: resistance regulated, 12V in for max brightness

