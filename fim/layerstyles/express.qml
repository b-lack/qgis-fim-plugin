<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="3.34.0-Prizren" labelsEnabled="1" styleCategories="Symbology|Labeling">
  <renderer-v2 symbollevels="0" referencescale="-1" enableorderby="0" type="singleSymbol" forceraster="0">
    <symbols>
      <symbol is_animated="0" name="0" frame_rate="10" alpha="1" clip_to_extent="1" type="marker" force_rhr="0">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" value="" type="QString"/>
            <Option name="properties"/>
            <Option name="type" value="collection" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer locked="0" class="GeometryGenerator" id="{cd6e1e4a-b248-42bb-831f-9beb1ae7f247}" pass="0" enabled="1">
          <Option type="Map">
            <Option name="SymbolType" value="Marker" type="QString"/>
            <Option name="geometryModifier" value="with_variable('val', &quot;form&quot;,&#xa;&#x9;collect_geometries(&#xa;&#x9;&#x9;array_foreach(&#xa;&#x9;&#x9;&#x9;lfb_landmarken(@val),&#xa;&#x9;&#x9;&#x9;project(&#xa;&#x9;&#x9;&#x9;&#x9;@geometry,&#xa;&#x9;&#x9;&#x9;&#x9;@element['distance'],&#xa;&#x9;&#x9;&#x9;&#x9;@element['azimuth']&#xa;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;)&#xa;&#x9;)&#xa;)" type="QString"/>
            <Option name="units" value="MapUnit" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol is_animated="0" name="@0@0" frame_rate="10" alpha="1" clip_to_extent="1" type="marker" force_rhr="0">
            <data_defined_properties>
              <Option type="Map">
                <Option name="name" value="" type="QString"/>
                <Option name="properties"/>
                <Option name="type" value="collection" type="QString"/>
              </Option>
            </data_defined_properties>
            <layer locked="0" class="FontMarker" id="{d1709de4-6325-4512-a01a-b87eb78314b8}" pass="0" enabled="1">
              <Option type="Map">
                <Option name="angle" value="0" type="QString"/>
                <Option name="chr" value="A" type="QString"/>
                <Option name="color" value="0,0,0,255" type="QString"/>
                <Option name="font" value="Ubuntu" type="QString"/>
                <Option name="font_style" value="Light Italic" type="QString"/>
                <Option name="horizontal_anchor_point" value="0" type="QString"/>
                <Option name="joinstyle" value="bevel" type="QString"/>
                <Option name="offset" value="0,0.80000000000000004" type="QString"/>
                <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
                <Option name="offset_unit" value="MM" type="QString"/>
                <Option name="outline_color" value="255,255,255,255" type="QString"/>
                <Option name="outline_width" value="0" type="QString"/>
                <Option name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
                <Option name="outline_width_unit" value="MM" type="QString"/>
                <Option name="size" value="2.8" type="QString"/>
                <Option name="size_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
                <Option name="size_unit" value="RenderMetersInMapUnits" type="QString"/>
                <Option name="vertical_anchor_point" value="0" type="QString"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" value="" type="QString"/>
                  <Option name="properties" type="Map">
                    <Option name="char" type="Map">
                      <Option name="active" value="true" type="bool"/>
                      <Option name="expression" value="with_variable('val', &quot;form&quot;,&#xa;&#x9;lfb_label_landmarke(@val, @geometry_part_num)&#xa;)" type="QString"/>
                      <Option name="type" value="3" type="int"/>
                    </Option>
                  </Option>
                  <Option name="type" value="collection" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer locked="0" class="GeometryGenerator" id="{036a6528-f805-4d37-a230-b79f83e37df8}" pass="0" enabled="1">
          <Option type="Map">
            <Option name="SymbolType" value="Marker" type="QString"/>
            <Option name="geometryModifier" value="with_variable('val', &quot;form&quot;,&#xa;&#x9;collect_geometries(&#xa;&#x9;&#x9;array_foreach(&#xa;&#x9;&#x9;&#x9;lfb_landmarken(@val),&#xa;&#x9;&#x9;&#x9;project(&#xa;&#x9;&#x9;&#x9;&#x9;@geometry,&#xa;&#x9;&#x9;&#x9;&#x9;@element['distance'],&#xa;&#x9;&#x9;&#x9;&#x9;@element['azimuth']&#xa;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;)&#xa;&#x9;)&#xa;)" type="QString"/>
            <Option name="units" value="MapUnit" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol is_animated="0" name="@0@1" frame_rate="10" alpha="1" clip_to_extent="1" type="marker" force_rhr="0">
            <data_defined_properties>
              <Option type="Map">
                <Option name="name" value="" type="QString"/>
                <Option name="properties"/>
                <Option name="type" value="collection" type="QString"/>
              </Option>
            </data_defined_properties>
            <layer locked="0" class="SimpleMarker" id="{f4879583-0e22-4557-87b6-fed1f8c5493d}" pass="0" enabled="1">
              <Option type="Map">
                <Option name="angle" value="0" type="QString"/>
                <Option name="cap_style" value="square" type="QString"/>
                <Option name="color" value="35,35,35,255" type="QString"/>
                <Option name="horizontal_anchor_point" value="1" type="QString"/>
                <Option name="joinstyle" value="bevel" type="QString"/>
                <Option name="name" value="square" type="QString"/>
                <Option name="offset" value="0,0" type="QString"/>
                <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
                <Option name="offset_unit" value="MM" type="QString"/>
                <Option name="outline_color" value="255,255,255,255" type="QString"/>
                <Option name="outline_style" value="solid" type="QString"/>
                <Option name="outline_width" value="0.4" type="QString"/>
                <Option name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
                <Option name="outline_width_unit" value="MM" type="QString"/>
                <Option name="scale_method" value="area" type="QString"/>
                <Option name="size" value="1.6" type="QString"/>
                <Option name="size_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
                <Option name="size_unit" value="MM" type="QString"/>
                <Option name="vertical_anchor_point" value="1" type="QString"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" value="" type="QString"/>
                  <Option name="properties"/>
                  <Option name="type" value="collection" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer locked="0" class="GeometryGenerator" id="{b1902374-991f-4d42-8592-15e0d5799a4c}" pass="0" enabled="1">
          <Option type="Map">
            <Option name="SymbolType" value="Line" type="QString"/>
            <Option name="geometryModifier" value="with_variable('val', &quot;form&quot;,&#xa;&#x9;make_line(&#xa;&#x9;&#x9;$geometry,&#xa;&#x9;&#x9;project( &#xa;&#x9;&#x9;&#x9;@geometry,&#xa;&#x9;&#x9;&#x9;meters_to_map_units(22), &#xa;&#x9;&#x9;&#x9;radians(&#xa;&#x9;&#x9;&#x9;&#x9;azimuttransektploteins_to_degree(@val)&#xa;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;)&#xa;&#x9;)&#xa;)" type="QString"/>
            <Option name="units" value="MapUnit" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol is_animated="0" name="@0@2" frame_rate="10" alpha="0.396" clip_to_extent="1" type="line" force_rhr="0">
            <data_defined_properties>
              <Option type="Map">
                <Option name="name" value="" type="QString"/>
                <Option name="properties"/>
                <Option name="type" value="collection" type="QString"/>
              </Option>
            </data_defined_properties>
            <layer locked="0" class="SimpleLine" id="{d37516a8-f293-416e-8aa6-788ef9c47bbd}" pass="0" enabled="1">
              <Option type="Map">
                <Option name="align_dash_pattern" value="0" type="QString"/>
                <Option name="capstyle" value="square" type="QString"/>
                <Option name="customdash" value="5;2" type="QString"/>
                <Option name="customdash_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
                <Option name="customdash_unit" value="MM" type="QString"/>
                <Option name="dash_pattern_offset" value="0" type="QString"/>
                <Option name="dash_pattern_offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
                <Option name="dash_pattern_offset_unit" value="MM" type="QString"/>
                <Option name="draw_inside_polygon" value="0" type="QString"/>
                <Option name="joinstyle" value="bevel" type="QString"/>
                <Option name="line_color" value="35,35,35,255" type="QString"/>
                <Option name="line_style" value="solid" type="QString"/>
                <Option name="line_width" value="0.26" type="QString"/>
                <Option name="line_width_unit" value="MM" type="QString"/>
                <Option name="offset" value="0" type="QString"/>
                <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
                <Option name="offset_unit" value="MM" type="QString"/>
                <Option name="ring_filter" value="0" type="QString"/>
                <Option name="trim_distance_end" value="0" type="QString"/>
                <Option name="trim_distance_end_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
                <Option name="trim_distance_end_unit" value="MM" type="QString"/>
                <Option name="trim_distance_start" value="0" type="QString"/>
                <Option name="trim_distance_start_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
                <Option name="trim_distance_start_unit" value="MM" type="QString"/>
                <Option name="tweak_dash_pattern_on_corners" value="0" type="QString"/>
                <Option name="use_custom_dash" value="0" type="QString"/>
                <Option name="width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" value="" type="QString"/>
                  <Option name="properties"/>
                  <Option name="type" value="collection" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer locked="0" class="GeometryGenerator" id="{b58a09a4-97b8-4d70-83f5-cc3f997c4a1c}" pass="0" enabled="1">
          <Option type="Map">
            <Option name="SymbolType" value="Marker" type="QString"/>
            <Option name="geometryModifier" value="with_variable('val', &quot;form&quot;,&#xa;&#x9;make_point(&#xa;&#x9;&#x9;x(&#xa;&#x9;&#x9;&#x9;project( &#xa;&#x9;&#x9;&#x9;&#x9;@geometry,&#xa;&#x9;&#x9;&#x9;&#x9;meters_to_map_units(11), &#xa;&#x9;&#x9;&#x9;&#x9;radians(&#xa;&#x9;&#x9;&#x9;&#x9;&#x9;azimuttransektploteins_to_degree(@val)&#xa;&#x9;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;),&#xa;&#x9;&#x9;y(&#xa;&#x9;&#x9;&#x9;project( &#xa;&#x9;&#x9;&#x9;&#x9;@geometry,&#xa;&#x9;&#x9;&#x9;&#x9;meters_to_map_units(11), &#xa;&#x9;&#x9;&#x9;&#x9;radians(&#xa;&#x9;&#x9;&#x9;&#x9;&#x9;azimuttransektploteins_to_degree(@val)&#xa;&#x9;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;)&#xa;&#x9;)&#xa;)" type="QString"/>
            <Option name="units" value="MapUnit" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol is_animated="0" name="@0@3" frame_rate="10" alpha="1" clip_to_extent="1" type="marker" force_rhr="0">
            <data_defined_properties>
              <Option type="Map">
                <Option name="name" value="" type="QString"/>
                <Option name="properties"/>
                <Option name="type" value="collection" type="QString"/>
              </Option>
            </data_defined_properties>
            <layer locked="0" class="FontMarker" id="{f54aded5-4f5e-4d8f-85de-f560f4c10c8f}" pass="0" enabled="1">
              <Option type="Map">
                <Option name="angle" value="0" type="QString"/>
                <Option name="chr" value="A" type="QString"/>
                <Option name="color" value="35,35,35,255" type="QString"/>
                <Option name="font" value="Ubuntu" type="QString"/>
                <Option name="font_style" value="Light Italic" type="QString"/>
                <Option name="horizontal_anchor_point" value="1" type="QString"/>
                <Option name="joinstyle" value="bevel" type="QString"/>
                <Option name="offset" value="0,-2" type="QString"/>
                <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
                <Option name="offset_unit" value="RenderMetersInMapUnits" type="QString"/>
                <Option name="outline_color" value="35,35,35,255" type="QString"/>
                <Option name="outline_width" value="0" type="QString"/>
                <Option name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
                <Option name="outline_width_unit" value="MM" type="QString"/>
                <Option name="size" value="2" type="QString"/>
                <Option name="size_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
                <Option name="size_unit" value="RenderMetersInMapUnits" type="QString"/>
                <Option name="vertical_anchor_point" value="1" type="QString"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" value="" type="QString"/>
                  <Option name="properties" type="Map">
                    <Option name="angle" type="Map">
                      <Option name="active" value="true" type="bool"/>
                      <Option name="expression" value="with_variable('val', &quot;form&quot;,&#xa;&#x9;azimuttransektploteins_to_degree(@val) - 90&#xa;)" type="QString"/>
                      <Option name="type" value="3" type="int"/>
                    </Option>
                    <Option name="char" type="Map">
                      <Option name="active" value="true" type="bool"/>
                      <Option name="expression" value="with_variable('val', &quot;form&quot;,&#xa;&#x9;azimuttransektploteins(@val)&#xa;)" type="QString"/>
                      <Option name="type" value="3" type="int"/>
                    </Option>
                  </Option>
                  <Option name="type" value="collection" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer locked="0" class="GeometryGenerator" id="{c72874b1-3170-434f-bc32-49a138b62db1}" pass="0" enabled="1">
          <Option type="Map">
            <Option name="SymbolType" value="Marker" type="QString"/>
            <Option name="geometryModifier" value="with_variable('val', &quot;form&quot;,&#xa;&#x9;collect_geometries(&#xa;&#x9;&#x9;array_foreach(&#xa;&#x9;&#x9;&#x9;lfb_baumplot(@val),&#xa;&#x9;&#x9;&#x9;project(&#xa;&#x9;&#x9;&#x9;&#x9;@geometry,&#xa;&#x9;&#x9;&#x9;&#x9;@element['distance'],&#xa;&#x9;&#x9;&#x9;&#x9;@element['azimuth']&#xa;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;)&#xa;&#x9;)&#xa;)" type="QString"/>
            <Option name="units" value="MapUnit" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol is_animated="0" name="@0@4" frame_rate="10" alpha="1" clip_to_extent="1" type="marker" force_rhr="0">
            <data_defined_properties>
              <Option type="Map">
                <Option name="name" value="" type="QString"/>
                <Option name="properties"/>
                <Option name="type" value="collection" type="QString"/>
              </Option>
            </data_defined_properties>
            <layer locked="0" class="SimpleMarker" id="{43f852b4-ce69-451d-9b55-b51c766b72b8}" pass="0" enabled="1">
              <Option type="Map">
                <Option name="angle" value="0" type="QString"/>
                <Option name="cap_style" value="square" type="QString"/>
                <Option name="color" value="30,108,18,255" type="QString"/>
                <Option name="horizontal_anchor_point" value="1" type="QString"/>
                <Option name="joinstyle" value="bevel" type="QString"/>
                <Option name="name" value="circle" type="QString"/>
                <Option name="offset" value="0,0" type="QString"/>
                <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
                <Option name="offset_unit" value="RenderMetersInMapUnits" type="QString"/>
                <Option name="outline_color" value="255,255,255,255" type="QString"/>
                <Option name="outline_style" value="solid" type="QString"/>
                <Option name="outline_width" value="0" type="QString"/>
                <Option name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
                <Option name="outline_width_unit" value="RenderMetersInMapUnits" type="QString"/>
                <Option name="scale_method" value="diameter" type="QString"/>
                <Option name="size" value="5" type="QString"/>
                <Option name="size_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
                <Option name="size_unit" value="RenderMetersInMapUnits" type="QString"/>
                <Option name="vertical_anchor_point" value="1" type="QString"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" value="" type="QString"/>
                  <Option name="properties" type="Map">
                    <Option name="fillColor" type="Map">
                      <Option name="active" value="true" type="bool"/>
                      <Option name="expression" value="with_variable('val', &quot;form&quot;,&#xa;&#x9;lfb_tree_generated_color(@val, @geometry_part_num)&#xa;)" type="QString"/>
                      <Option name="type" value="3" type="int"/>
                    </Option>
                    <Option name="size" type="Map">
                      <Option name="active" value="true" type="bool"/>
                      <Option name="expression" value="with_variable('val', &quot;form&quot;,&#xa;&#x9;lfb_tree_size(@val, @geometry_part_num)&#xa;)" type="QString"/>
                      <Option name="type" value="3" type="int"/>
                    </Option>
                  </Option>
                  <Option name="type" value="collection" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer locked="0" class="GeometryGenerator" id="{95b167d9-5c3d-42e9-aaec-aeae11d7d347}" pass="0" enabled="1">
          <Option type="Map">
            <Option name="SymbolType" value="Marker" type="QString"/>
            <Option name="geometryModifier" value="with_variable('val', &quot;form&quot;,&#xa;&#x9;collect_geometries(&#xa;&#x9;&#x9;array_foreach(&#xa;&#x9;&#x9;&#x9;lfb_baumplot(@val),&#xa;&#x9;&#x9;&#x9;project(&#xa;&#x9;&#x9;&#x9;&#x9;@geometry,&#xa;&#x9;&#x9;&#x9;&#x9;@element['distance'],&#xa;&#x9;&#x9;&#x9;&#x9;@element['azimuth']&#xa;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;)&#xa;&#x9;)&#xa;)" type="QString"/>
            <Option name="units" value="MapUnit" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol is_animated="0" name="@0@5" frame_rate="10" alpha="1" clip_to_extent="1" type="marker" force_rhr="0">
            <data_defined_properties>
              <Option type="Map">
                <Option name="name" value="" type="QString"/>
                <Option name="properties"/>
                <Option name="type" value="collection" type="QString"/>
              </Option>
            </data_defined_properties>
            <layer locked="0" class="FontMarker" id="{55dbda7b-5df1-4855-9125-c30c25751de8}" pass="0" enabled="1">
              <Option type="Map">
                <Option name="angle" value="0" type="QString"/>
                <Option name="chr" value="A" type="QString"/>
                <Option name="color" value="35,35,35,255" type="QString"/>
                <Option name="font" value="Ubuntu" type="QString"/>
                <Option name="font_style" value="Light Italic" type="QString"/>
                <Option name="horizontal_anchor_point" value="0" type="QString"/>
                <Option name="joinstyle" value="bevel" type="QString"/>
                <Option name="offset" value="1,1.59999999999999987" type="QString"/>
                <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
                <Option name="offset_unit" value="RenderMetersInMapUnits" type="QString"/>
                <Option name="outline_color" value="35,35,35,255" type="QString"/>
                <Option name="outline_width" value="0.2" type="QString"/>
                <Option name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
                <Option name="outline_width_unit" value="RenderMetersInMapUnits" type="QString"/>
                <Option name="size" value="2.2" type="QString"/>
                <Option name="size_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
                <Option name="size_unit" value="RenderMetersInMapUnits" type="QString"/>
                <Option name="vertical_anchor_point" value="1" type="QString"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" value="" type="QString"/>
                  <Option name="properties" type="Map">
                    <Option name="char" type="Map">
                      <Option name="active" value="true" type="bool"/>
                      <Option name="expression" value="with_variable('val', &quot;form&quot;,&#xa;&#x9;lfb_label_baumart(@val, @geometry_part_num)&#xa;)" type="QString"/>
                      <Option name="type" value="3" type="int"/>
                    </Option>
                  </Option>
                  <Option name="type" value="collection" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer locked="0" class="SimpleMarker" id="{c9f23fb5-410c-4f9b-8a30-a58b56e76efb}" pass="0" enabled="1">
          <Option type="Map">
            <Option name="angle" value="0" type="QString"/>
            <Option name="cap_style" value="square" type="QString"/>
            <Option name="color" value="222,204,68,255" type="QString"/>
            <Option name="horizontal_anchor_point" value="1" type="QString"/>
            <Option name="joinstyle" value="bevel" type="QString"/>
            <Option name="name" value="asterisk_fill" type="QString"/>
            <Option name="offset" value="0,0" type="QString"/>
            <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="offset_unit" value="MM" type="QString"/>
            <Option name="outline_color" value="35,35,35,255" type="QString"/>
            <Option name="outline_style" value="solid" type="QString"/>
            <Option name="outline_width" value="0" type="QString"/>
            <Option name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="outline_width_unit" value="MM" type="QString"/>
            <Option name="scale_method" value="diameter" type="QString"/>
            <Option name="size" value="3" type="QString"/>
            <Option name="size_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="size_unit" value="MM" type="QString"/>
            <Option name="vertical_anchor_point" value="1" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="fillColor" type="Map">
                  <Option name="active" value="true" type="bool"/>
                  <Option name="expression" value="color_by_workflow('s')" type="QString"/>
                  <Option name="type" value="3" type="int"/>
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer locked="1" class="GeometryGenerator" id="{d157f02f-5e00-4b72-85ef-b4ef282ad333}" pass="0" enabled="1">
          <Option type="Map">
            <Option name="SymbolType" value="Marker" type="QString"/>
            <Option name="geometryModifier" value="with_variable('val', &quot;form&quot;,&#xa;&#x9;make_point(&#xa;&#x9;&#x9;x(&#xa;&#x9;&#x9;&#x9;project( &#xa;&#x9;&#x9;&#x9;&#x9;@geometry,&#xa;&#x9;&#x9;&#x9;&#x9;meters_to_map_units(22), &#xa;&#x9;&#x9;&#x9;&#x9;radians(&#xa;&#x9;&#x9;&#x9;&#x9;&#x9;azimuttransektploteins_to_degree(@val)&#xa;&#x9;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;),&#xa;&#x9;&#x9;y(&#xa;&#x9;&#x9;&#x9;project( &#xa;&#x9;&#x9;&#x9;&#x9;@geometry,&#xa;&#x9;&#x9;&#x9;&#x9;meters_to_map_units(22), &#xa;&#x9;&#x9;&#x9;&#x9;radians(&#xa;&#x9;&#x9;&#x9;&#x9;&#x9;azimuttransektploteins_to_degree(@val)&#xa;&#x9;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;)&#xa;&#x9;)&#xa;)" type="QString"/>
            <Option name="units" value="MapUnit" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol is_animated="0" name="@0@7" frame_rate="10" alpha="1" clip_to_extent="1" type="marker" force_rhr="0">
            <data_defined_properties>
              <Option type="Map">
                <Option name="name" value="" type="QString"/>
                <Option name="properties"/>
                <Option name="type" value="collection" type="QString"/>
              </Option>
            </data_defined_properties>
            <layer locked="0" class="SimpleMarker" id="{eaabff36-dfb8-439f-b90b-2d30a61d272c}" pass="0" enabled="1">
              <Option type="Map">
                <Option name="angle" value="0" type="QString"/>
                <Option name="cap_style" value="square" type="QString"/>
                <Option name="color" value="222,204,68,255" type="QString"/>
                <Option name="horizontal_anchor_point" value="1" type="QString"/>
                <Option name="joinstyle" value="bevel" type="QString"/>
                <Option name="name" value="star" type="QString"/>
                <Option name="offset" value="0,0" type="QString"/>
                <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
                <Option name="offset_unit" value="MM" type="QString"/>
                <Option name="outline_color" value="35,35,35,255" type="QString"/>
                <Option name="outline_style" value="solid" type="QString"/>
                <Option name="outline_width" value="0" type="QString"/>
                <Option name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
                <Option name="outline_width_unit" value="MM" type="QString"/>
                <Option name="scale_method" value="area" type="QString"/>
                <Option name="size" value="1.4" type="QString"/>
                <Option name="size_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
                <Option name="size_unit" value="MM" type="QString"/>
                <Option name="vertical_anchor_point" value="1" type="QString"/>
              </Option>
              <effect enabled="0" type="effectStack">
                <effect type="drawSource">
                  <Option type="Map">
                    <Option name="blend_mode" value="0" type="QString"/>
                    <Option name="draw_mode" value="2" type="QString"/>
                    <Option name="enabled" value="1" type="QString"/>
                    <Option name="opacity" value="1" type="QString"/>
                  </Option>
                </effect>
              </effect>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" value="" type="QString"/>
                  <Option name="properties" type="Map">
                    <Option name="fillColor" type="Map">
                      <Option name="active" value="true" type="bool"/>
                      <Option name="expression" value="CASE&#xa;&#x9;WHEN attribute('workflow') = 4 THEN '#decc44'&#xa;&#x9;WHEN attribute('workflow') > 1 AND attribute('workflow') &lt;= 5 THEN '#e62323'&#xa;&#x9;WHEN attribute('workflow') > 5 AND attribute('workflow') &lt;= 6 THEN '#729b6f'&#xa;&#x9;WHEN attribute('workflow') > 7 AND attribute('workflow') &lt;= 8 THEN '#f3a6b2'&#xa;&#x9;WHEN attribute('workflow') > 11 AND attribute('workflow') &lt;= 12 THEN '#1228d1'&#xa;&#x9;ELSE '#1228d1'&#xa;&#x9;&#xa;END" type="QString"/>
                      <Option name="type" value="3" type="int"/>
                    </Option>
                  </Option>
                  <Option name="type" value="collection" type="QString"/>
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
      <symbol is_animated="0" name="" frame_rate="10" alpha="1" clip_to_extent="1" type="marker" force_rhr="0">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" value="" type="QString"/>
            <Option name="properties"/>
            <Option name="type" value="collection" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer locked="0" class="SimpleMarker" id="{b074ea98-79da-4b10-a0c3-5a19890e155c}" pass="0" enabled="1">
          <Option type="Map">
            <Option name="angle" value="0" type="QString"/>
            <Option name="cap_style" value="square" type="QString"/>
            <Option name="color" value="255,0,0,255" type="QString"/>
            <Option name="horizontal_anchor_point" value="1" type="QString"/>
            <Option name="joinstyle" value="bevel" type="QString"/>
            <Option name="name" value="circle" type="QString"/>
            <Option name="offset" value="0,0" type="QString"/>
            <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="offset_unit" value="MM" type="QString"/>
            <Option name="outline_color" value="35,35,35,255" type="QString"/>
            <Option name="outline_style" value="solid" type="QString"/>
            <Option name="outline_width" value="0" type="QString"/>
            <Option name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="outline_width_unit" value="MM" type="QString"/>
            <Option name="scale_method" value="diameter" type="QString"/>
            <Option name="size" value="2" type="QString"/>
            <Option name="size_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="size_unit" value="MM" type="QString"/>
            <Option name="vertical_anchor_point" value="1" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </selectionSymbol>
  </selection>
  <labeling type="simple">
    <settings calloutType="simple">
      <text-style textColor="0,0,0,255" fontItalic="0" textOpacity="1" legendString="Aa" multilineHeightUnit="Percentage" forcedItalic="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontStrikeout="0" multilineHeight="1" fieldName="los_id" fontUnderline="0" capitalization="0" isExpression="0" forcedBold="0" fontSizeUnit="Point" textOrientation="horizontal" allowHtml="0" namedStyle="Regular" fontFamily="Ubuntu" fontKerning="1" fontSize="12" fontLetterSpacing="0" fontWordSpacing="0" fontWeight="50" previewBkgrdColor="255,255,255,255" blendMode="0" useSubstitutions="0">
        <families/>
        <text-buffer bufferNoFill="1" bufferSize="0.10000000000000001" bufferDraw="1" bufferJoinStyle="128" bufferOpacity="1" bufferSizeUnits="MM" bufferBlendMode="0" bufferColor="0,0,0,255" bufferSizeMapUnitScale="3x:0,0,0,0,0,0"/>
        <text-mask maskEnabled="0" maskJoinStyle="128" maskType="0" maskOpacity="1" maskSize="1.5" maskedSymbolLayers="" maskSizeMapUnitScale="3x:0,0,0,0,0,0" maskSizeUnits="MM"/>
        <background shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeType="0" shapeSizeX="0" shapeFillColor="255,255,255,255" shapeBorderWidth="0" shapeOffsetUnit="MM" shapeRotationType="0" shapeBlendMode="0" shapeSizeY="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeSizeType="0" shapeOpacity="1" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthUnit="MM" shapeRadiiY="0" shapeSizeUnit="MM" shapeOffsetX="0" shapeRadiiUnit="MM" shapeRadiiX="0" shapeBorderColor="128,128,128,255" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetY="0" shapeJoinStyle="64" shapeDraw="0" shapeRotation="0" shapeSVGFile="">
          <symbol is_animated="0" name="markerSymbol" frame_rate="10" alpha="1" clip_to_extent="1" type="marker" force_rhr="0">
            <data_defined_properties>
              <Option type="Map">
                <Option name="name" value="" type="QString"/>
                <Option name="properties"/>
                <Option name="type" value="collection" type="QString"/>
              </Option>
            </data_defined_properties>
            <layer locked="0" class="SimpleMarker" id="" pass="0" enabled="1">
              <Option type="Map">
                <Option name="angle" value="0" type="QString"/>
                <Option name="cap_style" value="square" type="QString"/>
                <Option name="color" value="183,72,75,255" type="QString"/>
                <Option name="horizontal_anchor_point" value="1" type="QString"/>
                <Option name="joinstyle" value="bevel" type="QString"/>
                <Option name="name" value="circle" type="QString"/>
                <Option name="offset" value="0,0" type="QString"/>
                <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
                <Option name="offset_unit" value="MM" type="QString"/>
                <Option name="outline_color" value="35,35,35,255" type="QString"/>
                <Option name="outline_style" value="solid" type="QString"/>
                <Option name="outline_width" value="0" type="QString"/>
                <Option name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
                <Option name="outline_width_unit" value="MM" type="QString"/>
                <Option name="scale_method" value="diameter" type="QString"/>
                <Option name="size" value="2" type="QString"/>
                <Option name="size_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
                <Option name="size_unit" value="MM" type="QString"/>
                <Option name="vertical_anchor_point" value="1" type="QString"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" value="" type="QString"/>
                  <Option name="properties"/>
                  <Option name="type" value="collection" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
          <symbol is_animated="0" name="fillSymbol" frame_rate="10" alpha="1" clip_to_extent="1" type="fill" force_rhr="0">
            <data_defined_properties>
              <Option type="Map">
                <Option name="name" value="" type="QString"/>
                <Option name="properties"/>
                <Option name="type" value="collection" type="QString"/>
              </Option>
            </data_defined_properties>
            <layer locked="0" class="SimpleFill" id="" pass="0" enabled="1">
              <Option type="Map">
                <Option name="border_width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
                <Option name="color" value="255,255,255,255" type="QString"/>
                <Option name="joinstyle" value="bevel" type="QString"/>
                <Option name="offset" value="0,0" type="QString"/>
                <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
                <Option name="offset_unit" value="MM" type="QString"/>
                <Option name="outline_color" value="128,128,128,255" type="QString"/>
                <Option name="outline_style" value="no" type="QString"/>
                <Option name="outline_width" value="0" type="QString"/>
                <Option name="outline_width_unit" value="MM" type="QString"/>
                <Option name="style" value="solid" type="QString"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" value="" type="QString"/>
                  <Option name="properties"/>
                  <Option name="type" value="collection" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </background>
        <shadow shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetGlobal="1" shadowDraw="0" shadowOffsetDist="1" shadowBlendMode="6" shadowRadiusUnit="MM" shadowColor="0,0,0,255" shadowOffsetUnit="MM" shadowScale="100" shadowOpacity="0.69999999999999996" shadowOffsetAngle="135" shadowRadiusAlphaOnly="0" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowUnder="0" shadowRadius="1.5"/>
        <dd_properties>
          <Option type="Map">
            <Option name="name" value="" type="QString"/>
            <Option name="properties"/>
            <Option name="type" value="collection" type="QString"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format rightDirectionSymbol=">" decimals="3" plussign="0" leftDirectionSymbol="&lt;" reverseDirectionSymbol="0" autoWrapLength="0" placeDirectionSymbol="0" useMaxLineLengthForAutoWrap="1" multilineAlign="3" addDirectionSymbol="0" formatNumbers="0" wrapChar=""/>
      <placement rotationAngle="0" fitInPolygonOnly="0" maxCurvedCharAngleOut="-25" repeatDistance="0" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" overrunDistance="0" offsetType="0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" centroidInside="0" geometryGeneratorEnabled="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" lineAnchorClipping="0" maxCurvedCharAngleIn="25" allowDegraded="0" layerType="PointGeometry" distUnits="MM" preserveRotation="1" placementFlags="10" geometryGenerator="" repeatDistanceUnits="MM" dist="0" overlapHandling="PreventOverlap" geometryGeneratorType="PointGeometry" polygonPlacementFlags="2" lineAnchorTextPoint="FollowPlacement" offsetUnits="MM" lineAnchorType="0" yOffset="0" placement="0" quadOffset="4" xOffset="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" distMapUnitScale="3x:0,0,0,0,0,0" lineAnchorPercent="0.5" priority="5" rotationUnit="AngleDegrees" centroidWhole="0" overrunDistanceUnit="MM"/>
      <rendering limitNumLabels="0" mergeLines="0" minFeatureSize="0" fontLimitPixelSize="0" scaleMax="0" unplacedVisibility="0" labelPerPart="0" obstacleFactor="1" drawLabels="1" fontMaxPixelSize="10000" fontMinPixelSize="3" zIndex="0" obstacleType="1" maxNumLabels="2000" scaleMin="0" obstacle="1" scaleVisibility="0" upsidedownLabels="0"/>
      <dd_properties>
        <Option type="Map">
          <Option name="name" value="" type="QString"/>
          <Option name="properties"/>
          <Option name="type" value="collection" type="QString"/>
        </Option>
      </dd_properties>
      <callout type="simple">
        <Option type="Map">
          <Option name="anchorPoint" value="pole_of_inaccessibility" type="QString"/>
          <Option name="blendMode" value="0" type="int"/>
          <Option name="ddProperties" type="Map">
            <Option name="name" value="" type="QString"/>
            <Option name="properties"/>
            <Option name="type" value="collection" type="QString"/>
          </Option>
          <Option name="drawToAllParts" value="false" type="bool"/>
          <Option name="enabled" value="0" type="QString"/>
          <Option name="labelAnchorPoint" value="point_on_exterior" type="QString"/>
          <Option name="lineSymbol" value="&lt;symbol is_animated=&quot;0&quot; name=&quot;symbol&quot; frame_rate=&quot;10&quot; alpha=&quot;1&quot; clip_to_extent=&quot;1&quot; type=&quot;line&quot; force_rhr=&quot;0&quot;>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option name=&quot;name&quot; value=&quot;&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option name=&quot;type&quot; value=&quot;collection&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;layer locked=&quot;0&quot; class=&quot;SimpleLine&quot; id=&quot;{a6a2b52d-6ec8-418c-a77a-863433452952}&quot; pass=&quot;0&quot; enabled=&quot;1&quot;>&lt;Option type=&quot;Map&quot;>&lt;Option name=&quot;align_dash_pattern&quot; value=&quot;0&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;capstyle&quot; value=&quot;square&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;customdash&quot; value=&quot;5;2&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;customdash_map_unit_scale&quot; value=&quot;3x:0,0,0,0,0,0&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;customdash_unit&quot; value=&quot;MM&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;dash_pattern_offset&quot; value=&quot;0&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;dash_pattern_offset_map_unit_scale&quot; value=&quot;3x:0,0,0,0,0,0&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;dash_pattern_offset_unit&quot; value=&quot;MM&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;draw_inside_polygon&quot; value=&quot;0&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;joinstyle&quot; value=&quot;bevel&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;line_color&quot; value=&quot;60,60,60,255&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;line_style&quot; value=&quot;solid&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;line_width&quot; value=&quot;0.3&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;line_width_unit&quot; value=&quot;MM&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;offset&quot; value=&quot;0&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;offset_map_unit_scale&quot; value=&quot;3x:0,0,0,0,0,0&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;offset_unit&quot; value=&quot;MM&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;ring_filter&quot; value=&quot;0&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;trim_distance_end&quot; value=&quot;0&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;trim_distance_end_map_unit_scale&quot; value=&quot;3x:0,0,0,0,0,0&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;trim_distance_end_unit&quot; value=&quot;MM&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;trim_distance_start&quot; value=&quot;0&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;trim_distance_start_map_unit_scale&quot; value=&quot;3x:0,0,0,0,0,0&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;trim_distance_start_unit&quot; value=&quot;MM&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;tweak_dash_pattern_on_corners&quot; value=&quot;0&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;use_custom_dash&quot; value=&quot;0&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;width_map_unit_scale&quot; value=&quot;3x:0,0,0,0,0,0&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option name=&quot;name&quot; value=&quot;&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option name=&quot;type&quot; value=&quot;collection&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" type="QString"/>
          <Option name="minLength" value="0" type="double"/>
          <Option name="minLengthMapUnitScale" value="3x:0,0,0,0,0,0" type="QString"/>
          <Option name="minLengthUnit" value="MM" type="QString"/>
          <Option name="offsetFromAnchor" value="0" type="double"/>
          <Option name="offsetFromAnchorMapUnitScale" value="3x:0,0,0,0,0,0" type="QString"/>
          <Option name="offsetFromAnchorUnit" value="MM" type="QString"/>
          <Option name="offsetFromLabel" value="0" type="double"/>
          <Option name="offsetFromLabelMapUnitScale" value="3x:0,0,0,0,0,0" type="QString"/>
          <Option name="offsetFromLabelUnit" value="MM" type="QString"/>
        </Option>
      </callout>
    </settings>
  </labeling>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerGeometryType>0</layerGeometryType>
</qgis>
