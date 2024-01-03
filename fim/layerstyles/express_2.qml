<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="3.34.2-Prizren" labelsEnabled="1" styleCategories="Symbology|Labeling">
  <renderer-v2 enableorderby="0" referencescale="-1" symbollevels="0" forceraster="0" type="singleSymbol">
    <symbols>
      <symbol is_animated="0" force_rhr="0" alpha="1" frame_rate="10" type="marker" name="0" clip_to_extent="1">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" type="QString" name="name"/>
            <Option name="properties"/>
            <Option value="collection" type="QString" name="type"/>
          </Option>
        </data_defined_properties>
        <layer pass="0" enabled="1" locked="0" id="{cd6e1e4a-b248-42bb-831f-9beb1ae7f247}" class="GeometryGenerator">
          <Option type="Map">
            <Option value="Marker" type="QString" name="SymbolType"/>
            <Option value="with_variable('val', &quot;form&quot;,&#xa;&#x9;collect_geometries(&#xa;&#x9;&#x9;array_foreach(&#xa;&#x9;&#x9;&#x9;lfb_landmarken(@val),&#xa;&#x9;&#x9;&#x9;project(&#xa;&#x9;&#x9;&#x9;&#x9;@geometry,&#xa;&#x9;&#x9;&#x9;&#x9;@element['distance'],&#xa;&#x9;&#x9;&#x9;&#x9;@element['azimuth']&#xa;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;)&#xa;&#x9;)&#xa;)" type="QString" name="geometryModifier"/>
            <Option value="MapUnit" type="QString" name="units"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol is_animated="0" force_rhr="0" alpha="1" frame_rate="10" type="marker" name="@0@0" clip_to_extent="1">
            <data_defined_properties>
              <Option type="Map">
                <Option value="" type="QString" name="name"/>
                <Option name="properties"/>
                <Option value="collection" type="QString" name="type"/>
              </Option>
            </data_defined_properties>
            <layer pass="0" enabled="1" locked="0" id="{d1709de4-6325-4512-a01a-b87eb78314b8}" class="FontMarker">
              <Option type="Map">
                <Option value="0" type="QString" name="angle"/>
                <Option value="A" type="QString" name="chr"/>
                <Option value="0,0,0,255" type="QString" name="color"/>
                <Option value="Ubuntu" type="QString" name="font"/>
                <Option value="Light Italic" type="QString" name="font_style"/>
                <Option value="0" type="QString" name="horizontal_anchor_point"/>
                <Option value="bevel" type="QString" name="joinstyle"/>
                <Option value="0,0.80000000000000004" type="QString" name="offset"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
                <Option value="MM" type="QString" name="offset_unit"/>
                <Option value="255,255,255,255" type="QString" name="outline_color"/>
                <Option value="0" type="QString" name="outline_width"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="outline_width_map_unit_scale"/>
                <Option value="MM" type="QString" name="outline_width_unit"/>
                <Option value="2" type="QString" name="size"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="size_map_unit_scale"/>
                <Option value="RenderMetersInMapUnits" type="QString" name="size_unit"/>
                <Option value="0" type="QString" name="vertical_anchor_point"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option value="" type="QString" name="name"/>
                  <Option type="Map" name="properties">
                    <Option type="Map" name="char">
                      <Option value="true" type="bool" name="active"/>
                      <Option value="with_variable('val', &quot;form&quot;,&#xa;&#x9;lfb_label_landmarke(@val, @geometry_part_num)&#xa;)" type="QString" name="expression"/>
                      <Option value="3" type="int" name="type"/>
                    </Option>
                  </Option>
                  <Option value="collection" type="QString" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer pass="0" enabled="1" locked="0" id="{036a6528-f805-4d37-a230-b79f83e37df8}" class="GeometryGenerator">
          <Option type="Map">
            <Option value="Marker" type="QString" name="SymbolType"/>
            <Option value="with_variable('val', &quot;form&quot;,&#xa;&#x9;collect_geometries(&#xa;&#x9;&#x9;array_foreach(&#xa;&#x9;&#x9;&#x9;lfb_landmarken(@val),&#xa;&#x9;&#x9;&#x9;project(&#xa;&#x9;&#x9;&#x9;&#x9;@geometry,&#xa;&#x9;&#x9;&#x9;&#x9;@element['distance'],&#xa;&#x9;&#x9;&#x9;&#x9;@element['azimuth']&#xa;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;)&#xa;&#x9;)&#xa;)" type="QString" name="geometryModifier"/>
            <Option value="MapUnit" type="QString" name="units"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol is_animated="0" force_rhr="0" alpha="1" frame_rate="10" type="marker" name="@0@1" clip_to_extent="1">
            <data_defined_properties>
              <Option type="Map">
                <Option value="" type="QString" name="name"/>
                <Option name="properties"/>
                <Option value="collection" type="QString" name="type"/>
              </Option>
            </data_defined_properties>
            <layer pass="0" enabled="1" locked="0" id="{f4879583-0e22-4557-87b6-fed1f8c5493d}" class="SimpleMarker">
              <Option type="Map">
                <Option value="0" type="QString" name="angle"/>
                <Option value="square" type="QString" name="cap_style"/>
                <Option value="35,35,35,255" type="QString" name="color"/>
                <Option value="1" type="QString" name="horizontal_anchor_point"/>
                <Option value="bevel" type="QString" name="joinstyle"/>
                <Option value="square" type="QString" name="name"/>
                <Option value="0,0" type="QString" name="offset"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
                <Option value="MM" type="QString" name="offset_unit"/>
                <Option value="255,255,255,255" type="QString" name="outline_color"/>
                <Option value="solid" type="QString" name="outline_style"/>
                <Option value="0.4" type="QString" name="outline_width"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="outline_width_map_unit_scale"/>
                <Option value="MM" type="QString" name="outline_width_unit"/>
                <Option value="area" type="QString" name="scale_method"/>
                <Option value="1.6" type="QString" name="size"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="size_map_unit_scale"/>
                <Option value="MM" type="QString" name="size_unit"/>
                <Option value="1" type="QString" name="vertical_anchor_point"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option value="" type="QString" name="name"/>
                  <Option name="properties"/>
                  <Option value="collection" type="QString" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer pass="0" enabled="1" locked="0" id="{b1902374-991f-4d42-8592-15e0d5799a4c}" class="GeometryGenerator">
          <Option type="Map">
            <Option value="Line" type="QString" name="SymbolType"/>
            <Option value="with_variable('val', &quot;form&quot;,&#xa;&#x9;make_line(&#xa;&#x9;&#x9;$geometry,&#xa;&#x9;&#x9;project( &#xa;&#x9;&#x9;&#x9;@geometry,&#xa;&#x9;&#x9;&#x9;meters_to_map_units(22), &#xa;&#x9;&#x9;&#x9;radians(&#xa;&#x9;&#x9;&#x9;&#x9;azimuttransektploteins_to_degree(@val)&#xa;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;)&#xa;&#x9;)&#xa;)" type="QString" name="geometryModifier"/>
            <Option value="MapUnit" type="QString" name="units"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol is_animated="0" force_rhr="0" alpha="0.396" frame_rate="10" type="line" name="@0@2" clip_to_extent="1">
            <data_defined_properties>
              <Option type="Map">
                <Option value="" type="QString" name="name"/>
                <Option name="properties"/>
                <Option value="collection" type="QString" name="type"/>
              </Option>
            </data_defined_properties>
            <layer pass="0" enabled="1" locked="0" id="{d37516a8-f293-416e-8aa6-788ef9c47bbd}" class="SimpleLine">
              <Option type="Map">
                <Option value="0" type="QString" name="align_dash_pattern"/>
                <Option value="square" type="QString" name="capstyle"/>
                <Option value="5;2" type="QString" name="customdash"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="customdash_map_unit_scale"/>
                <Option value="MM" type="QString" name="customdash_unit"/>
                <Option value="0" type="QString" name="dash_pattern_offset"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="dash_pattern_offset_map_unit_scale"/>
                <Option value="MM" type="QString" name="dash_pattern_offset_unit"/>
                <Option value="0" type="QString" name="draw_inside_polygon"/>
                <Option value="bevel" type="QString" name="joinstyle"/>
                <Option value="35,35,35,255" type="QString" name="line_color"/>
                <Option value="solid" type="QString" name="line_style"/>
                <Option value="0.26" type="QString" name="line_width"/>
                <Option value="MM" type="QString" name="line_width_unit"/>
                <Option value="0" type="QString" name="offset"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
                <Option value="MM" type="QString" name="offset_unit"/>
                <Option value="0" type="QString" name="ring_filter"/>
                <Option value="0" type="QString" name="trim_distance_end"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="trim_distance_end_map_unit_scale"/>
                <Option value="MM" type="QString" name="trim_distance_end_unit"/>
                <Option value="0" type="QString" name="trim_distance_start"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="trim_distance_start_map_unit_scale"/>
                <Option value="MM" type="QString" name="trim_distance_start_unit"/>
                <Option value="0" type="QString" name="tweak_dash_pattern_on_corners"/>
                <Option value="0" type="QString" name="use_custom_dash"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="width_map_unit_scale"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option value="" type="QString" name="name"/>
                  <Option name="properties"/>
                  <Option value="collection" type="QString" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer pass="0" enabled="1" locked="0" id="{b58a09a4-97b8-4d70-83f5-cc3f997c4a1c}" class="GeometryGenerator">
          <Option type="Map">
            <Option value="Marker" type="QString" name="SymbolType"/>
            <Option value="with_variable('val', &quot;form&quot;,&#xa;&#x9;make_point(&#xa;&#x9;&#x9;x(&#xa;&#x9;&#x9;&#x9;project( &#xa;&#x9;&#x9;&#x9;&#x9;@geometry,&#xa;&#x9;&#x9;&#x9;&#x9;meters_to_map_units(11), &#xa;&#x9;&#x9;&#x9;&#x9;radians(&#xa;&#x9;&#x9;&#x9;&#x9;&#x9;azimuttransektploteins_to_degree(@val)&#xa;&#x9;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;),&#xa;&#x9;&#x9;y(&#xa;&#x9;&#x9;&#x9;project( &#xa;&#x9;&#x9;&#x9;&#x9;@geometry,&#xa;&#x9;&#x9;&#x9;&#x9;meters_to_map_units(11), &#xa;&#x9;&#x9;&#x9;&#x9;radians(&#xa;&#x9;&#x9;&#x9;&#x9;&#x9;azimuttransektploteins_to_degree(@val)&#xa;&#x9;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;)&#xa;&#x9;)&#xa;)" type="QString" name="geometryModifier"/>
            <Option value="MapUnit" type="QString" name="units"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol is_animated="0" force_rhr="0" alpha="1" frame_rate="10" type="marker" name="@0@3" clip_to_extent="1">
            <data_defined_properties>
              <Option type="Map">
                <Option value="" type="QString" name="name"/>
                <Option name="properties"/>
                <Option value="collection" type="QString" name="type"/>
              </Option>
            </data_defined_properties>
            <layer pass="0" enabled="1" locked="0" id="{f54aded5-4f5e-4d8f-85de-f560f4c10c8f}" class="FontMarker">
              <Option type="Map">
                <Option value="0" type="QString" name="angle"/>
                <Option value="A" type="QString" name="chr"/>
                <Option value="35,35,35,255" type="QString" name="color"/>
                <Option value="Ubuntu" type="QString" name="font"/>
                <Option value="Light Italic" type="QString" name="font_style"/>
                <Option value="1" type="QString" name="horizontal_anchor_point"/>
                <Option value="bevel" type="QString" name="joinstyle"/>
                <Option value="0,-1.60000000000000009" type="QString" name="offset"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
                <Option value="RenderMetersInMapUnits" type="QString" name="offset_unit"/>
                <Option value="35,35,35,255" type="QString" name="outline_color"/>
                <Option value="0" type="QString" name="outline_width"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="outline_width_map_unit_scale"/>
                <Option value="MM" type="QString" name="outline_width_unit"/>
                <Option value="1.5" type="QString" name="size"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="size_map_unit_scale"/>
                <Option value="RenderMetersInMapUnits" type="QString" name="size_unit"/>
                <Option value="1" type="QString" name="vertical_anchor_point"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option value="" type="QString" name="name"/>
                  <Option type="Map" name="properties">
                    <Option type="Map" name="angle">
                      <Option value="true" type="bool" name="active"/>
                      <Option value="with_variable('val', &quot;form&quot;,&#xa;&#x9;azimuttransektploteins_to_degree(@val) - 90&#xa;)" type="QString" name="expression"/>
                      <Option value="3" type="int" name="type"/>
                    </Option>
                    <Option type="Map" name="char">
                      <Option value="true" type="bool" name="active"/>
                      <Option value="with_variable('val', &quot;form&quot;,&#xa;&#x9;azimuttransektploteins(@val)&#xa;)" type="QString" name="expression"/>
                      <Option value="3" type="int" name="type"/>
                    </Option>
                  </Option>
                  <Option value="collection" type="QString" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer pass="0" enabled="1" locked="0" id="{c72874b1-3170-434f-bc32-49a138b62db1}" class="GeometryGenerator">
          <Option type="Map">
            <Option value="Marker" type="QString" name="SymbolType"/>
            <Option value="with_variable('val', &quot;form&quot;,&#xa;&#x9;collect_geometries(&#xa;&#x9;&#x9;array_foreach(&#xa;&#x9;&#x9;&#x9;lfb_baumplot(@val),&#xa;&#x9;&#x9;&#x9;project(&#xa;&#x9;&#x9;&#x9;&#x9;@geometry,&#xa;&#x9;&#x9;&#x9;&#x9;@element['distance'],&#xa;&#x9;&#x9;&#x9;&#x9;@element['azimuth']&#xa;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;)&#xa;&#x9;)&#xa;)" type="QString" name="geometryModifier"/>
            <Option value="MapUnit" type="QString" name="units"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol is_animated="0" force_rhr="0" alpha="1" frame_rate="10" type="marker" name="@0@4" clip_to_extent="1">
            <data_defined_properties>
              <Option type="Map">
                <Option value="" type="QString" name="name"/>
                <Option name="properties"/>
                <Option value="collection" type="QString" name="type"/>
              </Option>
            </data_defined_properties>
            <layer pass="0" enabled="1" locked="0" id="{43f852b4-ce69-451d-9b55-b51c766b72b8}" class="SimpleMarker">
              <Option type="Map">
                <Option value="0" type="QString" name="angle"/>
                <Option value="square" type="QString" name="cap_style"/>
                <Option value="30,108,18,255" type="QString" name="color"/>
                <Option value="1" type="QString" name="horizontal_anchor_point"/>
                <Option value="bevel" type="QString" name="joinstyle"/>
                <Option value="circle" type="QString" name="name"/>
                <Option value="0,0" type="QString" name="offset"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
                <Option value="RenderMetersInMapUnits" type="QString" name="offset_unit"/>
                <Option value="255,255,255,255" type="QString" name="outline_color"/>
                <Option value="solid" type="QString" name="outline_style"/>
                <Option value="0" type="QString" name="outline_width"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="outline_width_map_unit_scale"/>
                <Option value="RenderMetersInMapUnits" type="QString" name="outline_width_unit"/>
                <Option value="diameter" type="QString" name="scale_method"/>
                <Option value="5" type="QString" name="size"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="size_map_unit_scale"/>
                <Option value="RenderMetersInMapUnits" type="QString" name="size_unit"/>
                <Option value="1" type="QString" name="vertical_anchor_point"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option value="" type="QString" name="name"/>
                  <Option type="Map" name="properties">
                    <Option type="Map" name="fillColor">
                      <Option value="true" type="bool" name="active"/>
                      <Option value="with_variable('val', &quot;form&quot;,&#xa;&#x9;lfb_tree_generated_color(@val, @geometry_part_num)&#xa;)" type="QString" name="expression"/>
                      <Option value="3" type="int" name="type"/>
                    </Option>
                    <Option type="Map" name="size">
                      <Option value="true" type="bool" name="active"/>
                      <Option value="with_variable('val', &quot;form&quot;,&#xa;&#x9;lfb_tree_size(@val, @geometry_part_num)&#xa;)" type="QString" name="expression"/>
                      <Option value="3" type="int" name="type"/>
                    </Option>
                  </Option>
                  <Option value="collection" type="QString" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer pass="0" enabled="1" locked="0" id="{95b167d9-5c3d-42e9-aaec-aeae11d7d347}" class="GeometryGenerator">
          <Option type="Map">
            <Option value="Marker" type="QString" name="SymbolType"/>
            <Option value="with_variable('val', &quot;form&quot;,&#xa;&#x9;collect_geometries(&#xa;&#x9;&#x9;array_foreach(&#xa;&#x9;&#x9;&#x9;lfb_baumplot(@val),&#xa;&#x9;&#x9;&#x9;project(&#xa;&#x9;&#x9;&#x9;&#x9;@geometry,&#xa;&#x9;&#x9;&#x9;&#x9;@element['distance'],&#xa;&#x9;&#x9;&#x9;&#x9;@element['azimuth']&#xa;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;)&#xa;&#x9;)&#xa;)" type="QString" name="geometryModifier"/>
            <Option value="MapUnit" type="QString" name="units"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol is_animated="0" force_rhr="0" alpha="1" frame_rate="10" type="marker" name="@0@5" clip_to_extent="1">
            <data_defined_properties>
              <Option type="Map">
                <Option value="" type="QString" name="name"/>
                <Option name="properties"/>
                <Option value="collection" type="QString" name="type"/>
              </Option>
            </data_defined_properties>
            <layer pass="0" enabled="1" locked="0" id="{55dbda7b-5df1-4855-9125-c30c25751de8}" class="FontMarker">
              <Option type="Map">
                <Option value="0" type="QString" name="angle"/>
                <Option value="A" type="QString" name="chr"/>
                <Option value="35,35,35,255" type="QString" name="color"/>
                <Option value="Ubuntu" type="QString" name="font"/>
                <Option value="Light Italic" type="QString" name="font_style"/>
                <Option value="1" type="QString" name="horizontal_anchor_point"/>
                <Option value="bevel" type="QString" name="joinstyle"/>
                <Option value="0.00000000000000006,0.4000000000000003" type="QString" name="offset"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
                <Option value="RenderMetersInMapUnits" type="QString" name="offset_unit"/>
                <Option value="35,35,35,255" type="QString" name="outline_color"/>
                <Option value="0" type="QString" name="outline_width"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="outline_width_map_unit_scale"/>
                <Option value="RenderMetersInMapUnits" type="QString" name="outline_width_unit"/>
                <Option value="0.6" type="QString" name="size"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="size_map_unit_scale"/>
                <Option value="RenderMetersInMapUnits" type="QString" name="size_unit"/>
                <Option value="1" type="QString" name="vertical_anchor_point"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option value="" type="QString" name="name"/>
                  <Option type="Map" name="properties">
                    <Option type="Map" name="char">
                      <Option value="true" type="bool" name="active"/>
                      <Option value="with_variable('val', &quot;form&quot;,&#xa;&#x9;lfb_label_baumart(@val, @geometry_part_num)&#xa;)" type="QString" name="expression"/>
                      <Option value="3" type="int" name="type"/>
                    </Option>
                  </Option>
                  <Option value="collection" type="QString" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer pass="0" enabled="1" locked="0" id="{c9f23fb5-410c-4f9b-8a30-a58b56e76efb}" class="SimpleMarker">
          <Option type="Map">
            <Option value="0" type="QString" name="angle"/>
            <Option value="square" type="QString" name="cap_style"/>
            <Option value="222,204,68,255" type="QString" name="color"/>
            <Option value="1" type="QString" name="horizontal_anchor_point"/>
            <Option value="bevel" type="QString" name="joinstyle"/>
            <Option value="asterisk_fill" type="QString" name="name"/>
            <Option value="0,0" type="QString" name="offset"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
            <Option value="MM" type="QString" name="offset_unit"/>
            <Option value="35,35,35,255" type="QString" name="outline_color"/>
            <Option value="solid" type="QString" name="outline_style"/>
            <Option value="0" type="QString" name="outline_width"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="outline_width_map_unit_scale"/>
            <Option value="MM" type="QString" name="outline_width_unit"/>
            <Option value="diameter" type="QString" name="scale_method"/>
            <Option value="3" type="QString" name="size"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="size_map_unit_scale"/>
            <Option value="MM" type="QString" name="size_unit"/>
            <Option value="1" type="QString" name="vertical_anchor_point"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="fillColor">
                  <Option value="true" type="bool" name="active"/>
                  <Option value="color_by_workflow('s')" type="QString" name="expression"/>
                  <Option value="3" type="int" name="type"/>
                </Option>
              </Option>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer pass="0" enabled="1" locked="1" id="{d157f02f-5e00-4b72-85ef-b4ef282ad333}" class="GeometryGenerator">
          <Option type="Map">
            <Option value="Marker" type="QString" name="SymbolType"/>
            <Option value="with_variable('val', &quot;form&quot;,&#xa;&#x9;make_point(&#xa;&#x9;&#x9;x(&#xa;&#x9;&#x9;&#x9;project( &#xa;&#x9;&#x9;&#x9;&#x9;@geometry,&#xa;&#x9;&#x9;&#x9;&#x9;meters_to_map_units(22), &#xa;&#x9;&#x9;&#x9;&#x9;radians(&#xa;&#x9;&#x9;&#x9;&#x9;&#x9;azimuttransektploteins_to_degree(@val)&#xa;&#x9;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;),&#xa;&#x9;&#x9;y(&#xa;&#x9;&#x9;&#x9;project( &#xa;&#x9;&#x9;&#x9;&#x9;@geometry,&#xa;&#x9;&#x9;&#x9;&#x9;meters_to_map_units(22), &#xa;&#x9;&#x9;&#x9;&#x9;radians(&#xa;&#x9;&#x9;&#x9;&#x9;&#x9;azimuttransektploteins_to_degree(@val)&#xa;&#x9;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;&#x9;)&#xa;&#x9;&#x9;)&#xa;&#x9;)&#xa;)" type="QString" name="geometryModifier"/>
            <Option value="MapUnit" type="QString" name="units"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol is_animated="0" force_rhr="0" alpha="1" frame_rate="10" type="marker" name="@0@7" clip_to_extent="1">
            <data_defined_properties>
              <Option type="Map">
                <Option value="" type="QString" name="name"/>
                <Option name="properties"/>
                <Option value="collection" type="QString" name="type"/>
              </Option>
            </data_defined_properties>
            <layer pass="0" enabled="1" locked="0" id="{eaabff36-dfb8-439f-b90b-2d30a61d272c}" class="SimpleMarker">
              <Option type="Map">
                <Option value="0" type="QString" name="angle"/>
                <Option value="square" type="QString" name="cap_style"/>
                <Option value="222,204,68,255" type="QString" name="color"/>
                <Option value="1" type="QString" name="horizontal_anchor_point"/>
                <Option value="bevel" type="QString" name="joinstyle"/>
                <Option value="star" type="QString" name="name"/>
                <Option value="0,0" type="QString" name="offset"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
                <Option value="MM" type="QString" name="offset_unit"/>
                <Option value="35,35,35,255" type="QString" name="outline_color"/>
                <Option value="solid" type="QString" name="outline_style"/>
                <Option value="0" type="QString" name="outline_width"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="outline_width_map_unit_scale"/>
                <Option value="MM" type="QString" name="outline_width_unit"/>
                <Option value="area" type="QString" name="scale_method"/>
                <Option value="1.4" type="QString" name="size"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="size_map_unit_scale"/>
                <Option value="MM" type="QString" name="size_unit"/>
                <Option value="1" type="QString" name="vertical_anchor_point"/>
              </Option>
              <effect enabled="0" type="effectStack">
                <effect type="drawSource">
                  <Option type="Map">
                    <Option value="0" type="QString" name="blend_mode"/>
                    <Option value="2" type="QString" name="draw_mode"/>
                    <Option value="1" type="QString" name="enabled"/>
                    <Option value="1" type="QString" name="opacity"/>
                  </Option>
                </effect>
              </effect>
              <data_defined_properties>
                <Option type="Map">
                  <Option value="" type="QString" name="name"/>
                  <Option type="Map" name="properties">
                    <Option type="Map" name="fillColor">
                      <Option value="true" type="bool" name="active"/>
                      <Option value="CASE&#xa;&#x9;WHEN attribute('workflow') = 4 THEN '#decc44'&#xa;&#x9;WHEN attribute('workflow') > 1 AND attribute('workflow') &lt;= 5 THEN '#e62323'&#xa;&#x9;WHEN attribute('workflow') > 5 AND attribute('workflow') &lt;= 6 THEN '#729b6f'&#xa;&#x9;WHEN attribute('workflow') > 7 AND attribute('workflow') &lt;= 8 THEN '#f3a6b2'&#xa;&#x9;WHEN attribute('workflow') > 11 AND attribute('workflow') &lt;= 12 THEN '#1228d1'&#xa;&#x9;ELSE '#1228d1'&#xa;&#x9;&#xa;END" type="QString" name="expression"/>
                      <Option value="3" type="int" name="type"/>
                    </Option>
                  </Option>
                  <Option value="collection" type="QString" name="type"/>
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
      <symbol is_animated="0" force_rhr="0" alpha="1" frame_rate="10" type="marker" name="" clip_to_extent="1">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" type="QString" name="name"/>
            <Option name="properties"/>
            <Option value="collection" type="QString" name="type"/>
          </Option>
        </data_defined_properties>
        <layer pass="0" enabled="1" locked="0" id="{b074ea98-79da-4b10-a0c3-5a19890e155c}" class="SimpleMarker">
          <Option type="Map">
            <Option value="0" type="QString" name="angle"/>
            <Option value="square" type="QString" name="cap_style"/>
            <Option value="255,0,0,255" type="QString" name="color"/>
            <Option value="1" type="QString" name="horizontal_anchor_point"/>
            <Option value="bevel" type="QString" name="joinstyle"/>
            <Option value="circle" type="QString" name="name"/>
            <Option value="0,0" type="QString" name="offset"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
            <Option value="MM" type="QString" name="offset_unit"/>
            <Option value="35,35,35,255" type="QString" name="outline_color"/>
            <Option value="solid" type="QString" name="outline_style"/>
            <Option value="0" type="QString" name="outline_width"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="outline_width_map_unit_scale"/>
            <Option value="MM" type="QString" name="outline_width_unit"/>
            <Option value="diameter" type="QString" name="scale_method"/>
            <Option value="2" type="QString" name="size"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="size_map_unit_scale"/>
            <Option value="MM" type="QString" name="size_unit"/>
            <Option value="1" type="QString" name="vertical_anchor_point"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </selectionSymbol>
  </selection>
  <labeling type="simple">
    <settings calloutType="simple">
      <text-style legendString="Aa" fontWeight="50" fontUnderline="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontWordSpacing="0" textColor="0,0,0,255" multilineHeight="1" fontFamily="Ubuntu" fontLetterSpacing="0" textOpacity="1" useSubstitutions="0" namedStyle="Regular" forcedBold="0" fontItalic="0" fontKerning="1" textOrientation="horizontal" fontSizeUnit="Point" fontStrikeout="0" fontSize="12" fieldName="los_id" isExpression="0" forcedItalic="0" blendMode="0" allowHtml="0" multilineHeightUnit="Percentage" previewBkgrdColor="255,255,255,255" capitalization="0">
        <families/>
        <text-buffer bufferJoinStyle="128" bufferNoFill="1" bufferBlendMode="0" bufferSizeUnits="MM" bufferColor="0,0,0,255" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferSize="0.10000000000000001" bufferDraw="1" bufferOpacity="1"/>
        <text-mask maskEnabled="0" maskSizeUnits="MM" maskSize="1.5" maskType="0" maskedSymbolLayers="" maskSizeMapUnitScale="3x:0,0,0,0,0,0" maskJoinStyle="128" maskOpacity="1"/>
        <background shapeSizeType="0" shapeOffsetY="0" shapeRadiiY="0" shapeSizeX="0" shapeFillColor="255,255,255,255" shapeSizeY="0" shapeRadiiUnit="MM" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeSVGFile="" shapeJoinStyle="64" shapeOpacity="1" shapeRadiiX="0" shapeRotation="0" shapeBorderColor="128,128,128,255" shapeType="0" shapeBlendMode="0" shapeRotationType="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetUnit="MM" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidth="0" shapeDraw="0" shapeOffsetX="0" shapeSizeUnit="MM" shapeBorderWidthUnit="MM">
          <symbol is_animated="0" force_rhr="0" alpha="1" frame_rate="10" type="marker" name="markerSymbol" clip_to_extent="1">
            <data_defined_properties>
              <Option type="Map">
                <Option value="" type="QString" name="name"/>
                <Option name="properties"/>
                <Option value="collection" type="QString" name="type"/>
              </Option>
            </data_defined_properties>
            <layer pass="0" enabled="1" locked="0" id="" class="SimpleMarker">
              <Option type="Map">
                <Option value="0" type="QString" name="angle"/>
                <Option value="square" type="QString" name="cap_style"/>
                <Option value="183,72,75,255" type="QString" name="color"/>
                <Option value="1" type="QString" name="horizontal_anchor_point"/>
                <Option value="bevel" type="QString" name="joinstyle"/>
                <Option value="circle" type="QString" name="name"/>
                <Option value="0,0" type="QString" name="offset"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
                <Option value="MM" type="QString" name="offset_unit"/>
                <Option value="35,35,35,255" type="QString" name="outline_color"/>
                <Option value="solid" type="QString" name="outline_style"/>
                <Option value="0" type="QString" name="outline_width"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="outline_width_map_unit_scale"/>
                <Option value="MM" type="QString" name="outline_width_unit"/>
                <Option value="diameter" type="QString" name="scale_method"/>
                <Option value="2" type="QString" name="size"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="size_map_unit_scale"/>
                <Option value="MM" type="QString" name="size_unit"/>
                <Option value="1" type="QString" name="vertical_anchor_point"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option value="" type="QString" name="name"/>
                  <Option name="properties"/>
                  <Option value="collection" type="QString" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
          <symbol is_animated="0" force_rhr="0" alpha="1" frame_rate="10" type="fill" name="fillSymbol" clip_to_extent="1">
            <data_defined_properties>
              <Option type="Map">
                <Option value="" type="QString" name="name"/>
                <Option name="properties"/>
                <Option value="collection" type="QString" name="type"/>
              </Option>
            </data_defined_properties>
            <layer pass="0" enabled="1" locked="0" id="" class="SimpleFill">
              <Option type="Map">
                <Option value="3x:0,0,0,0,0,0" type="QString" name="border_width_map_unit_scale"/>
                <Option value="255,255,255,255" type="QString" name="color"/>
                <Option value="bevel" type="QString" name="joinstyle"/>
                <Option value="0,0" type="QString" name="offset"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
                <Option value="MM" type="QString" name="offset_unit"/>
                <Option value="128,128,128,255" type="QString" name="outline_color"/>
                <Option value="no" type="QString" name="outline_style"/>
                <Option value="0" type="QString" name="outline_width"/>
                <Option value="MM" type="QString" name="outline_width_unit"/>
                <Option value="solid" type="QString" name="style"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option value="" type="QString" name="name"/>
                  <Option name="properties"/>
                  <Option value="collection" type="QString" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </background>
        <shadow shadowRadiusAlphaOnly="0" shadowColor="0,0,0,255" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowOpacity="0.69999999999999996" shadowScale="100" shadowOffsetGlobal="1" shadowOffsetUnit="MM" shadowRadiusUnit="MM" shadowDraw="0" shadowOffsetDist="1" shadowUnder="0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowBlendMode="6" shadowOffsetAngle="135" shadowRadius="1.5"/>
        <dd_properties>
          <Option type="Map">
            <Option value="" type="QString" name="name"/>
            <Option name="properties"/>
            <Option value="collection" type="QString" name="type"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format useMaxLineLengthForAutoWrap="1" formatNumbers="0" decimals="3" wrapChar="" leftDirectionSymbol="&lt;" reverseDirectionSymbol="0" rightDirectionSymbol=">" placeDirectionSymbol="0" autoWrapLength="0" multilineAlign="3" addDirectionSymbol="0" plussign="0"/>
      <placement preserveRotation="1" overlapHandling="PreventOverlap" overrunDistance="0" offsetType="0" distUnits="MM" lineAnchorType="0" lineAnchorTextPoint="FollowPlacement" rotationAngle="0" yOffset="0" overrunDistanceUnit="MM" placement="0" allowDegraded="0" maxCurvedCharAngleOut="-25" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" centroidWhole="0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" layerType="PointGeometry" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" polygonPlacementFlags="2" repeatDistance="0" repeatDistanceUnits="MM" rotationUnit="AngleDegrees" centroidInside="0" dist="0" distMapUnitScale="3x:0,0,0,0,0,0" placementFlags="10" geometryGenerator="" geometryGeneratorEnabled="0" maxCurvedCharAngleIn="25" priority="5" quadOffset="4" geometryGeneratorType="PointGeometry" lineAnchorPercent="0.5" lineAnchorClipping="0" offsetUnits="MM" xOffset="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" fitInPolygonOnly="0"/>
      <rendering scaleVisibility="0" obstacleFactor="1" obstacle="1" obstacleType="1" scaleMin="0" zIndex="0" fontLimitPixelSize="0" mergeLines="0" scaleMax="0" minFeatureSize="0" unplacedVisibility="0" fontMinPixelSize="3" labelPerPart="0" limitNumLabels="0" drawLabels="1" maxNumLabels="2000" upsidedownLabels="0" fontMaxPixelSize="10000"/>
      <dd_properties>
        <Option type="Map">
          <Option value="" type="QString" name="name"/>
          <Option name="properties"/>
          <Option value="collection" type="QString" name="type"/>
        </Option>
      </dd_properties>
      <callout type="simple">
        <Option type="Map">
          <Option value="pole_of_inaccessibility" type="QString" name="anchorPoint"/>
          <Option value="0" type="int" name="blendMode"/>
          <Option type="Map" name="ddProperties">
            <Option value="" type="QString" name="name"/>
            <Option name="properties"/>
            <Option value="collection" type="QString" name="type"/>
          </Option>
          <Option value="false" type="bool" name="drawToAllParts"/>
          <Option value="0" type="QString" name="enabled"/>
          <Option value="point_on_exterior" type="QString" name="labelAnchorPoint"/>
          <Option value="&lt;symbol is_animated=&quot;0&quot; force_rhr=&quot;0&quot; alpha=&quot;1&quot; frame_rate=&quot;10&quot; type=&quot;line&quot; name=&quot;symbol&quot; clip_to_extent=&quot;1&quot;>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;&quot; type=&quot;QString&quot; name=&quot;name&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option value=&quot;collection&quot; type=&quot;QString&quot; name=&quot;type&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;layer pass=&quot;0&quot; enabled=&quot;1&quot; locked=&quot;0&quot; id=&quot;{a6a2b52d-6ec8-418c-a77a-863433452952}&quot; class=&quot;SimpleLine&quot;>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;0&quot; type=&quot;QString&quot; name=&quot;align_dash_pattern&quot;/>&lt;Option value=&quot;square&quot; type=&quot;QString&quot; name=&quot;capstyle&quot;/>&lt;Option value=&quot;5;2&quot; type=&quot;QString&quot; name=&quot;customdash&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; type=&quot;QString&quot; name=&quot;customdash_map_unit_scale&quot;/>&lt;Option value=&quot;MM&quot; type=&quot;QString&quot; name=&quot;customdash_unit&quot;/>&lt;Option value=&quot;0&quot; type=&quot;QString&quot; name=&quot;dash_pattern_offset&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; type=&quot;QString&quot; name=&quot;dash_pattern_offset_map_unit_scale&quot;/>&lt;Option value=&quot;MM&quot; type=&quot;QString&quot; name=&quot;dash_pattern_offset_unit&quot;/>&lt;Option value=&quot;0&quot; type=&quot;QString&quot; name=&quot;draw_inside_polygon&quot;/>&lt;Option value=&quot;bevel&quot; type=&quot;QString&quot; name=&quot;joinstyle&quot;/>&lt;Option value=&quot;60,60,60,255&quot; type=&quot;QString&quot; name=&quot;line_color&quot;/>&lt;Option value=&quot;solid&quot; type=&quot;QString&quot; name=&quot;line_style&quot;/>&lt;Option value=&quot;0.3&quot; type=&quot;QString&quot; name=&quot;line_width&quot;/>&lt;Option value=&quot;MM&quot; type=&quot;QString&quot; name=&quot;line_width_unit&quot;/>&lt;Option value=&quot;0&quot; type=&quot;QString&quot; name=&quot;offset&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; type=&quot;QString&quot; name=&quot;offset_map_unit_scale&quot;/>&lt;Option value=&quot;MM&quot; type=&quot;QString&quot; name=&quot;offset_unit&quot;/>&lt;Option value=&quot;0&quot; type=&quot;QString&quot; name=&quot;ring_filter&quot;/>&lt;Option value=&quot;0&quot; type=&quot;QString&quot; name=&quot;trim_distance_end&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; type=&quot;QString&quot; name=&quot;trim_distance_end_map_unit_scale&quot;/>&lt;Option value=&quot;MM&quot; type=&quot;QString&quot; name=&quot;trim_distance_end_unit&quot;/>&lt;Option value=&quot;0&quot; type=&quot;QString&quot; name=&quot;trim_distance_start&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; type=&quot;QString&quot; name=&quot;trim_distance_start_map_unit_scale&quot;/>&lt;Option value=&quot;MM&quot; type=&quot;QString&quot; name=&quot;trim_distance_start_unit&quot;/>&lt;Option value=&quot;0&quot; type=&quot;QString&quot; name=&quot;tweak_dash_pattern_on_corners&quot;/>&lt;Option value=&quot;0&quot; type=&quot;QString&quot; name=&quot;use_custom_dash&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; type=&quot;QString&quot; name=&quot;width_map_unit_scale&quot;/>&lt;/Option>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;&quot; type=&quot;QString&quot; name=&quot;name&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option value=&quot;collection&quot; type=&quot;QString&quot; name=&quot;type&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" type="QString" name="lineSymbol"/>
          <Option value="0" type="double" name="minLength"/>
          <Option value="3x:0,0,0,0,0,0" type="QString" name="minLengthMapUnitScale"/>
          <Option value="MM" type="QString" name="minLengthUnit"/>
          <Option value="0" type="double" name="offsetFromAnchor"/>
          <Option value="3x:0,0,0,0,0,0" type="QString" name="offsetFromAnchorMapUnitScale"/>
          <Option value="MM" type="QString" name="offsetFromAnchorUnit"/>
          <Option value="0" type="double" name="offsetFromLabel"/>
          <Option value="3x:0,0,0,0,0,0" type="QString" name="offsetFromLabelMapUnitScale"/>
          <Option value="MM" type="QString" name="offsetFromLabelUnit"/>
        </Option>
      </callout>
    </settings>
  </labeling>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerGeometryType>0</layerGeometryType>
</qgis>
