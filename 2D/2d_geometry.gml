<?xml version="1.0" encoding="ISO-8859-1"?>
<?xml-stylesheet type="text/xsl" href="OpenGeoSysGLI.xsl"?>

<OpenGeoSysGLI xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.opengeosys.org/images/xsd/OpenGeoSysGLI.xsd" xmlns:ogs="http://www.opengeosys.org">
    <name>2D</name>
    <points>
        <point id="0" x="0." y="0.09894" z="0" name="p_top"/>
        <point id="1" x="0.0" y="-0.09894" z="0" name="p_bottom"/>
        <point id="2" x="0.09894" y=".0" z="0" name="p_right"/>
        <point id="3" x="-0.09894" y=".0" z="0" name="p_left"/>

	<point name="Bag1_cedge_z_0" x="0.09894" id="4" z="0" y="-0.0145213"/>
	<point name="Bag1_aedge_z_0" x="0.09894" id="5" z="0" y="0.0145213"/>
	
	<point name="Bag2_cedge_z_0" x="0.0858516110225958" id="6" z="0" y="-0.05127865915588"/>
	<point name="Bag2_aedge_z_0" x="0.0969657439491436" id="7" z="0" y="-0.0244467687105909"/>
	
	<point name="Bag3_cedge_z_0" x="0.0596930529640449" id="8" z="0" y="-0.0802292928289395"/>
	<point name="Bag3_aedge_z_0" x="0.0802292928289395" id="9" z="0" y="-0.0596930529640449"/>
	
	<point name="Bag4_cedge_z_0" x="0.0244467687105909" id="10" z="0" y="-0.0969657439491436"/>
	<point name="Bag4_aedge_z_0" x="0.05127865915588" id="11" z="0" y="-0.0858516110225958"/>
	
	<point name="Bag5_cedge_z_0" x="-0.0145213144685405" id="12" z="0" y="-0.0989400395497483"/>
	<point name="Bag5_aedge_z_0" x="0.0145213144685405" id="13" z="0" y="-0.0989400395497483"/>
	
	<point name="Bag6_cedge_z_0" x="-0.05127865915588" id="14" z="0" y="-0.0858516110225958"/>
	<point name="Bag6_aedge_z_0" x="-0.0244467687105909" id="15" z="0" y="-0.0969657439491436"/>
	
	<point name="Bag7_cedge_z_0" x="-0.0802292928289395" id="16" z="0" y="-0.0596930529640449"/>
	<point name="Bag7_aedge_z_0" x="-0.0596930529640449" id="17" z="0" y="-0.0802292928289395"/>
	
	<point name="Bag8_cedge_z_0" x="-0.0969657439491436" id="18" z="0" y="-0.0244467687105909"/>
	<point name="Bag8_aedge_z_0" x="-0.0858516110225958" id="19" z="0" y="-0.05127865915588"/>
	
	<point name="Bag9_cedge_z_0" x="-0.0989400395497483" id="20" z="0" y="0.0145213144685405"/>
	<point name="Bag9_aedge_z_0" x="-0.0989400395497483" id="21" z="0" y="-0.0145213144685405"/>
	
	<point name="Bag10_cedge_z_0" x="-0.0858516110225958" id="22" z="0" y="0.05127865915588"/>
	<point name="Bag10_aedge_z_0" x="-0.0969657439491436" id="23" z="0" y="0.0244467687105909"/>
	
	<point name="Bag11_cedge_z_0" x="-0.0596930529640449" id="24" z="0" y="0.0802292928289395"/>
	<point name="Bag11_aedge_z_0" x="-0.0802292928289395" id="25" z="0" y="0.0596930529640449"/>
	
	<point name="Bag12_cedge_z_0" x="-0.0244467687105909" id="26" z="0" y="0.0969657439491436"/>
	<point name="Bag12_aedge_z_0" x="-0.05127865915588" id="27" z="0" y="0.0858516110225958"/>
	
	<point name="Bag13_cedge_z_0" x="0.0145213144685405" id="28" z="0" y="0.0989400395497483"/>
	<point name="Bag13_aedge_z_0" x="-0.0145213144685405" id="29" z="0" y="0.0989400395497483"/>
	
	<point name="Bag14_cedge_z_0" x="0.05127865915588" id="30" z="0" y="0.0858516110225958"/>
	<point name="Bag14_aedge_z_0" x="0.0244467687105909" id="31" z="0" y="0.0969657439491436"/>
	
	<point name="Bag15_cedge_z_0" x="0.0802292928289395" id="32" z="0" y="0.0596930529640449"/>
	<point name="Bag15_aedge_z_0" x="0.0596930529640449" id="33" z="0" y="0.0802292928289395"/>

	<point name="Bag16_cedge_z_0" x="0.0969657439491436" id="34" z="0" y="0.0244467687105909"/>
	<point name="Bag16_aedge_z_0" x="0.0858516110225958" id="35" z="0" y="0.05127865915588"/>

    </points>

    <polylines>
	<polyline id="100" name="BAG1">
		<pnt>4</pnt>
		<pnt>5</pnt>
	</polyline>
	<polyline id="101" name="BAG2">
		<pnt>6</pnt>
		<pnt>7</pnt>
	</polyline>
	<polyline id="102" name="BAG3">
		<pnt>8</pnt>
		<pnt>9</pnt>
	</polyline>
	<polyline id="103" name="BAG4">
		<pnt>10</pnt>
		<pnt>11</pnt>
	</polyline>
	<polyline id="104" name="BAG5">
		<pnt>12</pnt>
		<pnt>13</pnt>
	</polyline>
	<polyline id="105" name="BAG6">
		<pnt>14</pnt>
		<pnt>15</pnt>
	</polyline>
	<polyline id="106" name="BAG7">
		<pnt>16</pnt>
		<pnt>17</pnt>
	</polyline>
	<polyline id="107" name="BAG8">
		<pnt>18</pnt>
		<pnt>19</pnt>
	</polyline>
	<polyline id="108" name="BAG9">
		<pnt>20</pnt>
		<pnt>21</pnt>
	</polyline>
	<polyline id="109" name="BAG10">
		<pnt>22</pnt>
		<pnt>23</pnt>
	</polyline>
	<polyline id="110" name="BAG11">
		<pnt>24</pnt>
		<pnt>25</pnt>
	</polyline>
	<polyline id="111" name="BAG12">
		<pnt>26</pnt>
		<pnt>27</pnt>
	</polyline>
	<polyline id="112" name="BAG13">
		<pnt>28</pnt>
		<pnt>29</pnt>
	</polyline>
	<polyline id="113" name="BAG14">
		<pnt>30</pnt>
		<pnt>31</pnt>
	</polyline>
	<polyline id="114" name="BAG15">
		<pnt>32</pnt>
		<pnt>33</pnt>
	</polyline>
	<polyline id="115" name="BAG16">
		<pnt>34</pnt>
		<pnt>35</pnt>
	</polyline>

	<polyline id="116" name="STRIP1">
		<pnt>4</pnt>
		<pnt>7</pnt>
	</polyline>
	<polyline id="117" name="STRIP2">
		<pnt>6</pnt>
		<pnt>9</pnt>
	</polyline>
	<polyline id="118" name="STRIP3">
		<pnt>8</pnt>
		<pnt>11</pnt>
	</polyline>
	<polyline id="119" name="STRIP4">
		<pnt>10</pnt>
		<pnt>13</pnt>
	</polyline>
	<polyline id="120" name="STRIP5">
		<pnt>12</pnt>
		<pnt>15</pnt>
	</polyline>
	<polyline id="121" name="STRIP6">
		<pnt>14</pnt>
		<pnt>17</pnt>
	</polyline>
	<polyline id="122" name="STRIP7">
		<pnt>16</pnt>
		<pnt>19</pnt>
	</polyline>
	<polyline id="123" name="STRIP8">
		<pnt>18</pnt>
		<pnt>21</pnt>
	</polyline>
	<polyline id="124" name="STRIP9">
		<pnt>20</pnt>
		<pnt>23</pnt>
	</polyline>
	<polyline id="125" name="STRIP10">
		<pnt>22</pnt>
		<pnt>25</pnt>
	</polyline>
	<polyline id="126" name="STRIP11">
		<pnt>24</pnt>
		<pnt>27</pnt>
	</polyline>
	<polyline id="127" name="STRIP12">
		<pnt>26</pnt>
		<pnt>29</pnt>
	</polyline>
	<polyline id="128" name="STRIP13">
		<pnt>28</pnt>
		<pnt>31</pnt>
	</polyline>
	<polyline id="129" name="STRIP14">
		<pnt>30</pnt>
		<pnt>33</pnt>
	</polyline>
	<polyline id="130" name="STRIP15">
		<pnt>32</pnt>
		<pnt>35</pnt>
	</polyline>
	<polyline id="131" name="STRIP16">
		<pnt>34</pnt>
		<pnt>5</pnt>
	</polyline>

    </polylines>

</OpenGeoSysGLI>
