<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis styleCategories="Symbology|Labeling" labelsEnabled="1" version="3.34.0-Prizren">
  <renderer-v2 enableorderby="0" forceraster="0" referencescale="-1" type="singleSymbol" symbollevels="0">
    <symbols>
      <symbol force_rhr="0" clip_to_extent="1" alpha="1" type="marker" is_animated="0" name="0" frame_rate="10">
        <data_defined_properties>
          <Option type="Map">
            <Option type="QString" name="name" value=""/>
            <Option name="properties"/>
            <Option type="QString" name="type" value="collection"/>
          </Option>
        </data_defined_properties>
        <layer enabled="1" pass="0" locked="0" id="{cd6e1e4a-b248-42bb-831f-9beb1ae7f247}" class="GeometryGenerator">
          <Option type="Map">
            <Option type="QString" name="SymbolType" value="Marker"/>
            <Option type="QString" name="geometryModifier" value="with_variable('val', &quot;form&quot;,&#xa;&#x9;collect_geometries(&#xa;&#x9;&#x9;array_foreach(&#xa;&#x9;&#x9;&#x9;lfb_landmarken(@val),&#xa;&#x9;&#x9;&#x9;project(&#xa;&#x9;&#x9;&#x9;&#x9;@geometry,&#xa;&#x9;&#x9;&#x9;&#x9;@element['distance'],&#xa;&#x9;&#x9;&#x9;&#x9;@element['azimuth']&#xa;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;)&#xa;&#x9;)&#xa;)"/>
            <Option type="QString" name="units" value="MapUnit"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" clip_to_extent="1" alpha="1" type="marker" is_animated="0" name="@0@0" frame_rate="10">
            <data_defined_properties>
              <Option type="Map">
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
            </data_defined_properties>
            <layer enabled="1" pass="0" locked="0" id="{d1709de4-6325-4512-a01a-b87eb78314b8}" class="FontMarker">
              <Option type="Map">
                <Option type="QString" name="angle" value="0"/>
                <Option type="QString" name="chr" value="A"/>
                <Option type="QString" name="color" value="0,0,0,255"/>
                <Option type="QString" name="font" value="Ubuntu"/>
                <Option type="QString" name="font_style" value="Light Italic"/>
                <Option type="QString" name="horizontal_anchor_point" value="0"/>
                <Option type="QString" name="joinstyle" value="bevel"/>
                <Option type="QString" name="offset" value="0,0.80000000000000004"/>
                <Option type="QString" name="offset_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="offset_unit" value="MM"/>
                <Option type="QString" name="outline_color" value="255,255,255,255"/>
                <Option type="QString" name="outline_width" value="0"/>
                <Option type="QString" name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="outline_width_unit" value="MM"/>
                <Option type="QString" name="size" value="2.8"/>
                <Option type="QString" name="size_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="size_unit" value="RenderMetersInMapUnits"/>
                <Option type="QString" name="vertical_anchor_point" value="0"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" name="name" value=""/>
                  <Option type="Map" name="properties">
                    <Option type="Map" name="char">
                      <Option type="bool" name="active" value="true"/>
                      <Option type="QString" name="expression" value="with_variable('val', &quot;form&quot;,&#xa;&#x9;lfb_label_landmarke(@val, @geometry_part_num)&#xa;)"/>
                      <Option type="int" name="type" value="3"/>
                    </Option>
                  </Option>
                  <Option type="QString" name="type" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer enabled="1" pass="0" locked="0" id="{036a6528-f805-4d37-a230-b79f83e37df8}" class="GeometryGenerator">
          <Option type="Map">
            <Option type="QString" name="SymbolType" value="Marker"/>
            <Option type="QString" name="geometryModifier" value="with_variable('val', &quot;form&quot;,&#xa;&#x9;collect_geometries(&#xa;&#x9;&#x9;array_foreach(&#xa;&#x9;&#x9;&#x9;lfb_landmarken(@val),&#xa;&#x9;&#x9;&#x9;project(&#xa;&#x9;&#x9;&#x9;&#x9;@geometry,&#xa;&#x9;&#x9;&#x9;&#x9;@element['distance'],&#xa;&#x9;&#x9;&#x9;&#x9;@element['azimuth']&#xa;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;)&#xa;&#x9;)&#xa;)"/>
            <Option type="QString" name="units" value="MapUnit"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" clip_to_extent="1" alpha="1" type="marker" is_animated="0" name="@0@1" frame_rate="10">
            <data_defined_properties>
              <Option type="Map">
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
            </data_defined_properties>
            <layer enabled="1" pass="0" locked="0" id="{f4879583-0e22-4557-87b6-fed1f8c5493d}" class="SimpleMarker">
              <Option type="Map">
                <Option type="QString" name="angle" value="0"/>
                <Option type="QString" name="cap_style" value="square"/>
                <Option type="QString" name="color" value="35,35,35,255"/>
                <Option type="QString" name="horizontal_anchor_point" value="1"/>
                <Option type="QString" name="joinstyle" value="bevel"/>
                <Option type="QString" name="name" value="square"/>
                <Option type="QString" name="offset" value="0,0"/>
                <Option type="QString" name="offset_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="offset_unit" value="MM"/>
                <Option type="QString" name="outline_color" value="255,255,255,255"/>
                <Option type="QString" name="outline_style" value="solid"/>
                <Option type="QString" name="outline_width" value="0.4"/>
                <Option type="QString" name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="outline_width_unit" value="MM"/>
                <Option type="QString" name="scale_method" value="area"/>
                <Option type="QString" name="size" value="1.6"/>
                <Option type="QString" name="size_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="size_unit" value="MM"/>
                <Option type="QString" name="vertical_anchor_point" value="1"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" name="name" value=""/>
                  <Option name="properties"/>
                  <Option type="QString" name="type" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer enabled="1" pass="0" locked="0" id="{b1902374-991f-4d42-8592-15e0d5799a4c}" class="GeometryGenerator">
          <Option type="Map">
            <Option type="QString" name="SymbolType" value="Line"/>
            <Option type="QString" name="geometryModifier" value="with_variable('val', &quot;form&quot;,&#xa;&#x9;make_line(&#xa;&#x9;&#x9;$geometry,&#xa;&#x9;&#x9;project( &#xa;&#x9;&#x9;&#x9;@geometry,&#xa;&#x9;&#x9;&#x9;meters_to_map_units(22), &#xa;&#x9;&#x9;&#x9;radians(&#xa;&#x9;&#x9;&#x9;&#x9;azimuttransektploteins_to_degree(@val)&#xa;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;)&#xa;&#x9;)&#xa;)"/>
            <Option type="QString" name="units" value="MapUnit"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" clip_to_extent="1" alpha="0.396" type="line" is_animated="0" name="@0@2" frame_rate="10">
            <data_defined_properties>
              <Option type="Map">
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
            </data_defined_properties>
            <layer enabled="1" pass="0" locked="0" id="{d37516a8-f293-416e-8aa6-788ef9c47bbd}" class="SimpleLine">
              <Option type="Map">
                <Option type="QString" name="align_dash_pattern" value="0"/>
                <Option type="QString" name="capstyle" value="square"/>
                <Option type="QString" name="customdash" value="5;2"/>
                <Option type="QString" name="customdash_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="customdash_unit" value="MM"/>
                <Option type="QString" name="dash_pattern_offset" value="0"/>
                <Option type="QString" name="dash_pattern_offset_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="dash_pattern_offset_unit" value="MM"/>
                <Option type="QString" name="draw_inside_polygon" value="0"/>
                <Option type="QString" name="joinstyle" value="bevel"/>
                <Option type="QString" name="line_color" value="35,35,35,255"/>
                <Option type="QString" name="line_style" value="solid"/>
                <Option type="QString" name="line_width" value="0.26"/>
                <Option type="QString" name="line_width_unit" value="MM"/>
                <Option type="QString" name="offset" value="0"/>
                <Option type="QString" name="offset_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="offset_unit" value="MM"/>
                <Option type="QString" name="ring_filter" value="0"/>
                <Option type="QString" name="trim_distance_end" value="0"/>
                <Option type="QString" name="trim_distance_end_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="trim_distance_end_unit" value="MM"/>
                <Option type="QString" name="trim_distance_start" value="0"/>
                <Option type="QString" name="trim_distance_start_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="trim_distance_start_unit" value="MM"/>
                <Option type="QString" name="tweak_dash_pattern_on_corners" value="0"/>
                <Option type="QString" name="use_custom_dash" value="0"/>
                <Option type="QString" name="width_map_unit_scale" value="3x:0,0,0,0,0,0"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" name="name" value=""/>
                  <Option name="properties"/>
                  <Option type="QString" name="type" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer enabled="1" pass="0" locked="0" id="{b58a09a4-97b8-4d70-83f5-cc3f997c4a1c}" class="GeometryGenerator">
          <Option type="Map">
            <Option type="QString" name="SymbolType" value="Marker"/>
            <Option type="QString" name="geometryModifier" value="with_variable('val', &quot;form&quot;,&#xa;&#x9;make_point(&#xa;&#x9;&#x9;x(&#xa;&#x9;&#x9;&#x9;project( &#xa;&#x9;&#x9;&#x9;&#x9;@geometry,&#xa;&#x9;&#x9;&#x9;&#x9;meters_to_map_units(11), &#xa;&#x9;&#x9;&#x9;&#x9;radians(&#xa;&#x9;&#x9;&#x9;&#x9;&#x9;azimuttransektploteins_to_degree(@val)&#xa;&#x9;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;),&#xa;&#x9;&#x9;y(&#xa;&#x9;&#x9;&#x9;project( &#xa;&#x9;&#x9;&#x9;&#x9;@geometry,&#xa;&#x9;&#x9;&#x9;&#x9;meters_to_map_units(11), &#xa;&#x9;&#x9;&#x9;&#x9;radians(&#xa;&#x9;&#x9;&#x9;&#x9;&#x9;azimuttransektploteins_to_degree(@val)&#xa;&#x9;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;)&#xa;&#x9;)&#xa;)"/>
            <Option type="QString" name="units" value="MapUnit"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" clip_to_extent="1" alpha="1" type="marker" is_animated="0" name="@0@3" frame_rate="10">
            <data_defined_properties>
              <Option type="Map">
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
            </data_defined_properties>
            <layer enabled="1" pass="0" locked="0" id="{f54aded5-4f5e-4d8f-85de-f560f4c10c8f}" class="FontMarker">
              <Option type="Map">
                <Option type="QString" name="angle" value="0"/>
                <Option type="QString" name="chr" value="A"/>
                <Option type="QString" name="color" value="35,35,35,255"/>
                <Option type="QString" name="font" value="Ubuntu"/>
                <Option type="QString" name="font_style" value="Light Italic"/>
                <Option type="QString" name="horizontal_anchor_point" value="1"/>
                <Option type="QString" name="joinstyle" value="bevel"/>
                <Option type="QString" name="offset" value="0,-2"/>
                <Option type="QString" name="offset_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="offset_unit" value="RenderMetersInMapUnits"/>
                <Option type="QString" name="outline_color" value="35,35,35,255"/>
                <Option type="QString" name="outline_width" value="0"/>
                <Option type="QString" name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="outline_width_unit" value="MM"/>
                <Option type="QString" name="size" value="2"/>
                <Option type="QString" name="size_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="size_unit" value="RenderMetersInMapUnits"/>
                <Option type="QString" name="vertical_anchor_point" value="1"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" name="name" value=""/>
                  <Option type="Map" name="properties">
                    <Option type="Map" name="angle">
                      <Option type="bool" name="active" value="true"/>
                      <Option type="QString" name="expression" value="with_variable('val', &quot;form&quot;,&#xa;&#x9;azimuttransektploteins_to_degree(@val) - 90&#xa;)"/>
                      <Option type="int" name="type" value="3"/>
                    </Option>
                    <Option type="Map" name="char">
                      <Option type="bool" name="active" value="true"/>
                      <Option type="QString" name="expression" value="with_variable('val', &quot;form&quot;,&#xa;&#x9;azimuttransektploteins(@val)&#xa;)"/>
                      <Option type="int" name="type" value="3"/>
                    </Option>
                  </Option>
                  <Option type="QString" name="type" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer enabled="1" pass="0" locked="0" id="{c72874b1-3170-434f-bc32-49a138b62db1}" class="GeometryGenerator">
          <Option type="Map">
            <Option type="QString" name="SymbolType" value="Marker"/>
            <Option type="QString" name="geometryModifier" value="with_variable('val', &quot;form&quot;,&#xa;&#x9;collect_geometries(&#xa;&#x9;&#x9;array_foreach(&#xa;&#x9;&#x9;&#x9;lfb_baumplot(@val),&#xa;&#x9;&#x9;&#x9;project(&#xa;&#x9;&#x9;&#x9;&#x9;@geometry,&#xa;&#x9;&#x9;&#x9;&#x9;@element['distance'],&#xa;&#x9;&#x9;&#x9;&#x9;@element['azimuth']&#xa;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;)&#xa;&#x9;)&#xa;)"/>
            <Option type="QString" name="units" value="MapUnit"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" clip_to_extent="1" alpha="1" type="marker" is_animated="0" name="@0@4" frame_rate="10">
            <data_defined_properties>
              <Option type="Map">
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
            </data_defined_properties>
            <layer enabled="1" pass="0" locked="0" id="{43f852b4-ce69-451d-9b55-b51c766b72b8}" class="SimpleMarker">
              <Option type="Map">
                <Option type="QString" name="angle" value="0"/>
                <Option type="QString" name="cap_style" value="square"/>
                <Option type="QString" name="color" value="30,108,18,255"/>
                <Option type="QString" name="horizontal_anchor_point" value="1"/>
                <Option type="QString" name="joinstyle" value="bevel"/>
                <Option type="QString" name="name" value="circle"/>
                <Option type="QString" name="offset" value="0,0"/>
                <Option type="QString" name="offset_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="offset_unit" value="RenderMetersInMapUnits"/>
                <Option type="QString" name="outline_color" value="255,255,255,255"/>
                <Option type="QString" name="outline_style" value="solid"/>
                <Option type="QString" name="outline_width" value="0"/>
                <Option type="QString" name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="outline_width_unit" value="RenderMetersInMapUnits"/>
                <Option type="QString" name="scale_method" value="diameter"/>
                <Option type="QString" name="size" value="5"/>
                <Option type="QString" name="size_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="size_unit" value="RenderMetersInMapUnits"/>
                <Option type="QString" name="vertical_anchor_point" value="1"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" name="name" value=""/>
                  <Option type="Map" name="properties">
                    <Option type="Map" name="fillColor">
                      <Option type="bool" name="active" value="true"/>
                      <Option type="QString" name="expression" value="with_variable('val', &quot;form&quot;,&#xa;&#x9;lfb_tree_generated_color(@val, @geometry_part_num)&#xa;)"/>
                      <Option type="int" name="type" value="3"/>
                    </Option>
                    <Option type="Map" name="size">
                      <Option type="bool" name="active" value="true"/>
                      <Option type="QString" name="expression" value="with_variable('val', &quot;form&quot;,&#xa;&#x9;lfb_tree_size(@val, @geometry_part_num)&#xa;)"/>
                      <Option type="int" name="type" value="3"/>
                    </Option>
                  </Option>
                  <Option type="QString" name="type" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer enabled="1" pass="0" locked="0" id="{95b167d9-5c3d-42e9-aaec-aeae11d7d347}" class="GeometryGenerator">
          <Option type="Map">
            <Option type="QString" name="SymbolType" value="Marker"/>
            <Option type="QString" name="geometryModifier" value="with_variable('val', &quot;form&quot;,&#xa;&#x9;collect_geometries(&#xa;&#x9;&#x9;array_foreach(&#xa;&#x9;&#x9;&#x9;lfb_baumplot(@val),&#xa;&#x9;&#x9;&#x9;project(&#xa;&#x9;&#x9;&#x9;&#x9;@geometry,&#xa;&#x9;&#x9;&#x9;&#x9;@element['distance'],&#xa;&#x9;&#x9;&#x9;&#x9;@element['azimuth']&#xa;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;)&#xa;&#x9;)&#xa;)"/>
            <Option type="QString" name="units" value="MapUnit"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" clip_to_extent="1" alpha="1" type="marker" is_animated="0" name="@0@5" frame_rate="10">
            <data_defined_properties>
              <Option type="Map">
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
            </data_defined_properties>
            <layer enabled="1" pass="0" locked="0" id="{55dbda7b-5df1-4855-9125-c30c25751de8}" class="FontMarker">
              <Option type="Map">
                <Option type="QString" name="angle" value="0"/>
                <Option type="QString" name="chr" value="A"/>
                <Option type="QString" name="color" value="35,35,35,255"/>
                <Option type="QString" name="font" value="Ubuntu"/>
                <Option type="QString" name="font_style" value="Light Italic"/>
                <Option type="QString" name="horizontal_anchor_point" value="0"/>
                <Option type="QString" name="joinstyle" value="bevel"/>
                <Option type="QString" name="offset" value="1,1.59999999999999987"/>
                <Option type="QString" name="offset_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="offset_unit" value="RenderMetersInMapUnits"/>
                <Option type="QString" name="outline_color" value="35,35,35,255"/>
                <Option type="QString" name="outline_width" value="0.2"/>
                <Option type="QString" name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="outline_width_unit" value="RenderMetersInMapUnits"/>
                <Option type="QString" name="size" value="2.2"/>
                <Option type="QString" name="size_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="size_unit" value="RenderMetersInMapUnits"/>
                <Option type="QString" name="vertical_anchor_point" value="1"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" name="name" value=""/>
                  <Option type="Map" name="properties">
                    <Option type="Map" name="char">
                      <Option type="bool" name="active" value="true"/>
                      <Option type="QString" name="expression" value="with_variable('val', &quot;form&quot;,&#xa;&#x9;lfb_label_baumart(@val, @geometry_part_num)&#xa;)"/>
                      <Option type="int" name="type" value="3"/>
                    </Option>
                  </Option>
                  <Option type="QString" name="type" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer enabled="1" pass="0" locked="0" id="{c9f23fb5-410c-4f9b-8a30-a58b56e76efb}" class="SimpleMarker">
          <Option type="Map">
            <Option type="QString" name="angle" value="0"/>
            <Option type="QString" name="cap_style" value="square"/>
            <Option type="QString" name="color" value="222,204,68,255"/>
            <Option type="QString" name="horizontal_anchor_point" value="1"/>
            <Option type="QString" name="joinstyle" value="bevel"/>
            <Option type="QString" name="name" value="asterisk_fill"/>
            <Option type="QString" name="offset" value="0,0"/>
            <Option type="QString" name="offset_map_unit_scale" value="3x:0,0,0,0,0,0"/>
            <Option type="QString" name="offset_unit" value="MM"/>
            <Option type="QString" name="outline_color" value="35,35,35,255"/>
            <Option type="QString" name="outline_style" value="solid"/>
            <Option type="QString" name="outline_width" value="0"/>
            <Option type="QString" name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0"/>
            <Option type="QString" name="outline_width_unit" value="MM"/>
            <Option type="QString" name="scale_method" value="diameter"/>
            <Option type="QString" name="size" value="3"/>
            <Option type="QString" name="size_map_unit_scale" value="3x:0,0,0,0,0,0"/>
            <Option type="QString" name="size_unit" value="MM"/>
            <Option type="QString" name="vertical_anchor_point" value="1"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option type="Map" name="properties">
                <Option type="Map" name="fillColor">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="expression" value="color_by_workflow('s')"/>
                  <Option type="int" name="type" value="3"/>
                </Option>
              </Option>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer enabled="1" pass="0" locked="1" id="{d157f02f-5e00-4b72-85ef-b4ef282ad333}" class="GeometryGenerator">
          <Option type="Map">
            <Option type="QString" name="SymbolType" value="Marker"/>
            <Option type="QString" name="geometryModifier" value="with_variable('val', &quot;form&quot;,&#xa;&#x9;make_point(&#xa;&#x9;&#x9;x(&#xa;&#x9;&#x9;&#x9;project( &#xa;&#x9;&#x9;&#x9;&#x9;@geometry,&#xa;&#x9;&#x9;&#x9;&#x9;meters_to_map_units(22), &#xa;&#x9;&#x9;&#x9;&#x9;radians(&#xa;&#x9;&#x9;&#x9;&#x9;&#x9;azimuttransektploteins_to_degree(@val)&#xa;&#x9;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;),&#xa;&#x9;&#x9;y(&#xa;&#x9;&#x9;&#x9;project( &#xa;&#x9;&#x9;&#x9;&#x9;@geometry,&#xa;&#x9;&#x9;&#x9;&#x9;meters_to_map_units(22), &#xa;&#x9;&#x9;&#x9;&#x9;radians(&#xa;&#x9;&#x9;&#x9;&#x9;&#x9;azimuttransektploteins_to_degree(@val)&#xa;&#x9;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;)&#xa;&#x9;)&#xa;)"/>
            <Option type="QString" name="units" value="MapUnit"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" clip_to_extent="1" alpha="1" type="marker" is_animated="0" name="@0@7" frame_rate="10">
            <data_defined_properties>
              <Option type="Map">
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
            </data_defined_properties>
            <layer enabled="1" pass="0" locked="0" id="{eaabff36-dfb8-439f-b90b-2d30a61d272c}" class="SimpleMarker">
              <Option type="Map">
                <Option type="QString" name="angle" value="0"/>
                <Option type="QString" name="cap_style" value="square"/>
                <Option type="QString" name="color" value="222,204,68,255"/>
                <Option type="QString" name="horizontal_anchor_point" value="1"/>
                <Option type="QString" name="joinstyle" value="bevel"/>
                <Option type="QString" name="name" value="star"/>
                <Option type="QString" name="offset" value="0,0"/>
                <Option type="QString" name="offset_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="offset_unit" value="MM"/>
                <Option type="QString" name="outline_color" value="35,35,35,255"/>
                <Option type="QString" name="outline_style" value="solid"/>
                <Option type="QString" name="outline_width" value="0"/>
                <Option type="QString" name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="outline_width_unit" value="MM"/>
                <Option type="QString" name="scale_method" value="area"/>
                <Option type="QString" name="size" value="1.4"/>
                <Option type="QString" name="size_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="size_unit" value="MM"/>
                <Option type="QString" name="vertical_anchor_point" value="1"/>
              </Option>
              <effect type="effectStack" enabled="0">
                <effect type="drawSource">
                  <Option type="Map">
                    <Option type="QString" name="blend_mode" value="0"/>
                    <Option type="QString" name="draw_mode" value="2"/>
                    <Option type="QString" name="enabled" value="1"/>
                    <Option type="QString" name="opacity" value="1"/>
                  </Option>
                </effect>
              </effect>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" name="name" value=""/>
                  <Option type="Map" name="properties">
                    <Option type="Map" name="fillColor">
                      <Option type="bool" name="active" value="true"/>
                      <Option type="QString" name="expression" value="CASE&#xa;&#x9;WHEN attribute('workflow') = 4 THEN '#decc44'&#xa;&#x9;WHEN attribute('workflow') > 1 AND attribute('workflow') &lt;= 5 THEN '#e62323'&#xa;&#x9;WHEN attribute('workflow') > 5 AND attribute('workflow') &lt;= 6 THEN '#729b6f'&#xa;&#x9;WHEN attribute('workflow') > 7 AND attribute('workflow') &lt;= 8 THEN '#f3a6b2'&#xa;&#x9;WHEN attribute('workflow') > 11 AND attribute('workflow') &lt;= 12 THEN '#1228d1'&#xa;&#x9;ELSE '#1228d1'&#xa;&#x9;&#xa;END"/>
                      <Option type="int" name="type" value="3"/>
                    </Option>
                  </Option>
                  <Option type="QString" name="type" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <selection mode="Default">
    <selectionColor invalid="1"/>
    <selectionSymbol>
      <symbol force_rhr="0" clip_to_extent="1" alpha="1" type="marker" is_animated="0" name="" frame_rate="10">
        <data_defined_properties>
          <Option type="Map">
            <Option type="QString" name="name" value=""/>
            <Option name="properties"/>
            <Option type="QString" name="type" value="collection"/>
          </Option>
        </data_defined_properties>
        <layer enabled="1" pass="0" locked="0" id="{b074ea98-79da-4b10-a0c3-5a19890e155c}" class="SimpleMarker">
          <Option type="Map">
            <Option type="QString" name="angle" value="0"/>
            <Option type="QString" name="cap_style" value="square"/>
            <Option type="QString" name="color" value="255,0,0,255"/>
            <Option type="QString" name="horizontal_anchor_point" value="1"/>
            <Option type="QString" name="joinstyle" value="bevel"/>
            <Option type="QString" name="name" value="circle"/>
            <Option type="QString" name="offset" value="0,0"/>
            <Option type="QString" name="offset_map_unit_scale" value="3x:0,0,0,0,0,0"/>
            <Option type="QString" name="offset_unit" value="MM"/>
            <Option type="QString" name="outline_color" value="35,35,35,255"/>
            <Option type="QString" name="outline_style" value="solid"/>
            <Option type="QString" name="outline_width" value="0"/>
            <Option type="QString" name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0"/>
            <Option type="QString" name="outline_width_unit" value="MM"/>
            <Option type="QString" name="scale_method" value="diameter"/>
            <Option type="QString" name="size" value="2"/>
            <Option type="QString" name="size_map_unit_scale" value="3x:0,0,0,0,0,0"/>
            <Option type="QString" name="size_unit" value="MM"/>
            <Option type="QString" name="vertical_anchor_point" value="1"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </selectionSymbol>
  </selection>
  <labeling type="simple">
    <settings calloutType="simple">
      <text-style fontItalic="0" previewBkgrdColor="255,255,255,255" textOrientation="horizontal" fontKerning="1" fontFamily="Ubuntu" fontWordSpacing="0" forcedBold="0" textColor="0,0,0,255" multilineHeight="1" namedStyle="Regular" isExpression="0" legendString="Aa" textOpacity="1" capitalization="0" fontUnderline="0" useSubstitutions="0" fontSize="12" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontLetterSpacing="0" fontWeight="50" fontStrikeout="0" fieldName="los_id" forcedItalic="0" allowHtml="0" fontSizeUnit="Point" blendMode="0" multilineHeightUnit="Percentage">
        <families/>
        <text-buffer bufferBlendMode="0" bufferDraw="1" bufferColor="0,0,0,255" bufferJoinStyle="128" bufferNoFill="1" bufferSize="0.10000000000000001" bufferSizeUnits="MM" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferOpacity="1"/>
        <text-mask maskType="0" maskSizeMapUnitScale="3x:0,0,0,0,0,0" maskSize="1.5" maskedSymbolLayers="" maskEnabled="0" maskSizeUnits="MM" maskJoinStyle="128" maskOpacity="1"/>
        <background shapeType="0" shapeOpacity="1" shapeOffsetY="0" shapeBorderWidth="0" shapeBlendMode="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeDraw="0" shapeSizeX="0" shapeJoinStyle="64" shapeRotationType="0" shapeFillColor="255,255,255,255" shapeBorderColor="128,128,128,255" shapeRadiiUnit="MM" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiX="0" shapeSVGFile="" shapeSizeY="0" shapeRadiiY="0" shapeOffsetUnit="MM" shapeSizeType="0" shapeRotation="0" shapeOffsetX="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthUnit="MM" shapeSizeUnit="MM">
          <symbol force_rhr="0" clip_to_extent="1" alpha="1" type="marker" is_animated="0" name="markerSymbol" frame_rate="10">
            <data_defined_properties>
              <Option type="Map">
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
            </data_defined_properties>
            <layer enabled="1" pass="0" locked="0" id="" class="SimpleMarker">
              <Option type="Map">
                <Option type="QString" name="angle" value="0"/>
                <Option type="QString" name="cap_style" value="square"/>
                <Option type="QString" name="color" value="183,72,75,255"/>
                <Option type="QString" name="horizontal_anchor_point" value="1"/>
                <Option type="QString" name="joinstyle" value="bevel"/>
                <Option type="QString" name="name" value="circle"/>
                <Option type="QString" name="offset" value="0,0"/>
                <Option type="QString" name="offset_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="offset_unit" value="MM"/>
                <Option type="QString" name="outline_color" value="35,35,35,255"/>
                <Option type="QString" name="outline_style" value="solid"/>
                <Option type="QString" name="outline_width" value="0"/>
                <Option type="QString" name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="outline_width_unit" value="MM"/>
                <Option type="QString" name="scale_method" value="diameter"/>
                <Option type="QString" name="size" value="2"/>
                <Option type="QString" name="size_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="size_unit" value="MM"/>
                <Option type="QString" name="vertical_anchor_point" value="1"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" name="name" value=""/>
                  <Option name="properties"/>
                  <Option type="QString" name="type" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
          <symbol force_rhr="0" clip_to_extent="1" alpha="1" type="fill" is_animated="0" name="fillSymbol" frame_rate="10">
            <data_defined_properties>
              <Option type="Map">
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
            </data_defined_properties>
            <layer enabled="1" pass="0" locked="0" id="" class="SimpleFill">
              <Option type="Map">
                <Option type="QString" name="border_width_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="color" value="255,255,255,255"/>
                <Option type="QString" name="joinstyle" value="bevel"/>
                <Option type="QString" name="offset" value="0,0"/>
                <Option type="QString" name="offset_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="offset_unit" value="MM"/>
                <Option type="QString" name="outline_color" value="128,128,128,255"/>
                <Option type="QString" name="outline_style" value="no"/>
                <Option type="QString" name="outline_width" value="0"/>
                <Option type="QString" name="outline_width_unit" value="MM"/>
                <Option type="QString" name="style" value="solid"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" name="name" value=""/>
                  <Option name="properties"/>
                  <Option type="QString" name="type" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </background>
        <shadow shadowOffsetDist="1" shadowOffsetUnit="MM" shadowUnder="0" shadowRadiusAlphaOnly="0" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusUnit="MM" shadowOpacity="0.69999999999999996" shadowDraw="0" shadowOffsetGlobal="1" shadowColor="0,0,0,255" shadowBlendMode="6" shadowRadius="1.5" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowScale="100" shadowOffsetAngle="135"/>
        <dd_properties>
          <Option type="Map">
            <Option type="QString" name="name" value=""/>
            <Option name="properties"/>
            <Option type="QString" name="type" value="collection"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format wrapChar="" leftDirectionSymbol="&lt;" autoWrapLength="0" addDirectionSymbol="0" placeDirectionSymbol="0" formatNumbers="0" multilineAlign="3" reverseDirectionSymbol="0" useMaxLineLengthForAutoWrap="1" plussign="0" decimals="3" rightDirectionSymbol=">"/>
      <placement yOffset="0" maxCurvedCharAngleIn="25" overrunDistanceUnit="MM" distMapUnitScale="3x:0,0,0,0,0,0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" overlapHandling="PreventOverlap" centroidWhole="0" repeatDistance="0" lineAnchorClipping="0" priority="5" placementFlags="10" preserveRotation="1" quadOffset="4" centroidInside="0" xOffset="0" geometryGeneratorEnabled="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" placement="0" lineAnchorPercent="0.5" layerType="PointGeometry" fitInPolygonOnly="0" geometryGeneratorType="PointGeometry" rotationUnit="AngleDegrees" geometryGenerator="" offsetType="0" lineAnchorType="0" distUnits="MM" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" repeatDistanceUnits="MM" rotationAngle="0" offsetUnits="MM" allowDegraded="0" polygonPlacementFlags="2" maxCurvedCharAngleOut="-25" overrunDistance="0" lineAnchorTextPoint="FollowPlacement" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" dist="0"/>
      <rendering obstacleFactor="1" fontMaxPixelSize="10000" minFeatureSize="0" zIndex="0" scaleMax="0" limitNumLabels="0" unplacedVisibility="0" maxNumLabels="2000" obstacleType="1" scaleMin="0" labelPerPart="0" mergeLines="0" obstacle="1" upsidedownLabels="0" drawLabels="1" fontLimitPixelSize="0" fontMinPixelSize="3" scaleVisibility="0"/>
      <dd_properties>
        <Option type="Map">
          <Option type="QString" name="name" value=""/>
          <Option name="properties"/>
          <Option type="QString" name="type" value="collection"/>
        </Option>
      </dd_properties>
      <callout type="simple">
        <Option type="Map">
          <Option type="QString" name="anchorPoint" value="pole_of_inaccessibility"/>
          <Option type="int" name="blendMode" value="0"/>
          <Option type="Map" name="ddProperties">
            <Option type="QString" name="name" value=""/>
            <Option name="properties"/>
            <Option type="QString" name="type" value="collection"/>
          </Option>
          <Option type="bool" name="drawToAllParts" value="false"/>
          <Option type="QString" name="enabled" value="0"/>
          <Option type="QString" name="labelAnchorPoint" value="point_on_exterior"/>
          <Option type="QString" name="lineSymbol" value="&lt;symbol force_rhr=&quot;0&quot; clip_to_extent=&quot;1&quot; alpha=&quot;1&quot; type=&quot;line&quot; is_animated=&quot;0&quot; name=&quot;symbol&quot; frame_rate=&quot;10&quot;>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option type=&quot;QString&quot; name=&quot;name&quot; value=&quot;&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;type&quot; value=&quot;collection&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;layer enabled=&quot;1&quot; pass=&quot;0&quot; locked=&quot;0&quot; id=&quot;{a6a2b52d-6ec8-418c-a77a-863433452952}&quot; class=&quot;SimpleLine&quot;>&lt;Option type=&quot;Map&quot;>&lt;Option type=&quot;QString&quot; name=&quot;align_dash_pattern&quot; value=&quot;0&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;capstyle&quot; value=&quot;square&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;customdash&quot; value=&quot;5;2&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;customdash_map_unit_scale&quot; value=&quot;3x:0,0,0,0,0,0&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;customdash_unit&quot; value=&quot;MM&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;dash_pattern_offset&quot; value=&quot;0&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;dash_pattern_offset_map_unit_scale&quot; value=&quot;3x:0,0,0,0,0,0&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;dash_pattern_offset_unit&quot; value=&quot;MM&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;draw_inside_polygon&quot; value=&quot;0&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;joinstyle&quot; value=&quot;bevel&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;line_color&quot; value=&quot;60,60,60,255&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;line_style&quot; value=&quot;solid&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;line_width&quot; value=&quot;0.3&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;line_width_unit&quot; value=&quot;MM&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;offset&quot; value=&quot;0&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;offset_map_unit_scale&quot; value=&quot;3x:0,0,0,0,0,0&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;offset_unit&quot; value=&quot;MM&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;ring_filter&quot; value=&quot;0&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;trim_distance_end&quot; value=&quot;0&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;trim_distance_end_map_unit_scale&quot; value=&quot;3x:0,0,0,0,0,0&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;trim_distance_end_unit&quot; value=&quot;MM&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;trim_distance_start&quot; value=&quot;0&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;trim_distance_start_map_unit_scale&quot; value=&quot;3x:0,0,0,0,0,0&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;trim_distance_start_unit&quot; value=&quot;MM&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;tweak_dash_pattern_on_corners&quot; value=&quot;0&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;use_custom_dash&quot; value=&quot;0&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;width_map_unit_scale&quot; value=&quot;3x:0,0,0,0,0,0&quot;/>&lt;/Option>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option type=&quot;QString&quot; name=&quot;name&quot; value=&quot;&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;type&quot; value=&quot;collection&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>"/>
          <Option type="double" name="minLength" value="0"/>
          <Option type="QString" name="minLengthMapUnitScale" value="3x:0,0,0,0,0,0"/>
          <Option type="QString" name="minLengthUnit" value="MM"/>
          <Option type="double" name="offsetFromAnchor" value="0"/>
          <Option type="QString" name="offsetFromAnchorMapUnitScale" value="3x:0,0,0,0,0,0"/>
          <Option type="QString" name="offsetFromAnchorUnit" value="MM"/>
          <Option type="double" name="offsetFromLabel" value="0"/>
          <Option type="QString" name="offsetFromLabelMapUnitScale" value="3x:0,0,0,0,0,0"/>
          <Option type="QString" name="offsetFromLabelUnit" value="MM"/>
        </Option>
      </callout>
    </settings>
  </labeling>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerGeometryType>0</layerGeometryType>
</qgis>
