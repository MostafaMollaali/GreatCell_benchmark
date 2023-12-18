<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE OGS-GML-DOM>
<OpenGeoSysGLI xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ogs="http://www.opengeosys.org">
 <name>G3_geometry</name>
 <points>
  <point id="0" x="0."   y="0.0" z="0.06" />
  <point id="1" x="0.04" y="0.0" z="0.06"/>
  <point id="2" x="0.04" y="0.0" z="0.16"/>
  <point id="3" x="0.0"  y="0.0" z="0.16"/>
 </points>
 <polylines>
    <polyline name="fracture_left" id="0">
       <pnt>0</pnt>
       <pnt>3</pnt>
   </polyline>
    <polyline name="fracture_right" id="1">
       <pnt>1</pnt>
       <pnt>2</pnt>
   </polyline>
    <polyline name="fracture_bottom" id="2">
       <pnt>0</pnt>
       <pnt>1</pnt>
   </polyline>
    <polyline name="fracture_top" id="3">
       <pnt>2</pnt>
       <pnt>3</pnt>
   </polyline>      
 </polylines>
</OpenGeoSysGLI>
