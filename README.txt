IR LED ring (ILR) illuminator
Designed to be used with Mitutoyo M Plan IR objectives


Design summary:
-ilr-ext: externally powered LED array, all in series
    ie use lab bunch supply
    r1
        scrapped due to error in inner diameter
    r2
        Shrunk ID
        Add IR warning
        Clean up mounting holes
    TODO: add fuse
    TODO: possibly increase LED hole to help set angle
-solder_jig
    Places LEDs at 45 degree angle for above assembly
-ilr-lm317: LM317 design with 12V in regulating to fixed 100 mA
    Does not work / don't use
-ilr-r: 12V in resistor limiting to around 100 mA
    Does not work / don't use


Max LED power
150 mW dissipation
100 mW current => 8 mW optical
1.4 Vdrop max => 1.4 * 0.1 = 140 - 8 mW = 132 mW
1.25 Vdrop typ => 1.25 * 0.1 = 125 - 8 mW = 117 mW
Safe to run at 100 mW continuously, assuming reasonable 25C air flow


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

