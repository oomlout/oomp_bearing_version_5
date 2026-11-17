"""Editable bearing declarations, imported from the reviewed October 2026 catalogue.

Edit these explicit dictionaries, then run action_make_all.py.
Dimensions and illustrative internal geometry are deliberately separate.
The original source evidence is retained under source_file/solidcraft/.
"""

import copy


def declarations(**kwargs):
    options = []

    # 16001: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_16000_series_16001_size_12_mm_id_28_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_16000_series_16001_size_12_mm_id_28_mm_od_7_mm_depth'
    option['size'] = '16001'
    option['series'] = '16000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 12.0
    option['dimensions']['outside'] = 28.0
    option['dimensions']['width'] = 7.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 11
    option['internal_geometry']['balls_per_row'] = 11
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 12.0
    option['internal_geometry']['parameters']['outside'] = 28.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.42
    option['internal_geometry']['parameters']['pitch_radius'] = 10.0
    option['internal_geometry']['parameters']['ball_radius'] = 1.9600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 2.0090000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 8.7848
    option['internal_geometry']['parameters']['outer_shoulder'] = 11.2152
    option['internal_geometry']['parameters']['cage_half_width'] = 1.0780000000000003
    option['internal_geometry']['parameters']['cage_low'] = 1.862
    option['internal_geometry']['parameters']['cage_high'] = 2.254
    option['internal_geometry']['parameters']['window_radius'] = 0.9408000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '19'
    options.append(copy.deepcopy(option))

    # 16002: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_16000_series_16002_size_15_mm_id_32_mm_od_8_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_16000_series_16002_size_15_mm_id_32_mm_od_8_mm_depth'
    option['size'] = '16002'
    option['series'] = '16000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 15.0
    option['dimensions']['outside'] = 32.0
    option['dimensions']['width'] = 8.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 12
    option['internal_geometry']['balls_per_row'] = 12
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 15.0
    option['internal_geometry']['parameters']['outside'] = 32.0
    option['internal_geometry']['parameters']['width'] = 8.0
    option['internal_geometry']['parameters']['edge'] = 0.48
    option['internal_geometry']['parameters']['pitch_radius'] = 11.75
    option['internal_geometry']['parameters']['ball_radius'] = 2.24
    option['internal_geometry']['parameters']['groove_radius'] = 2.2960000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 10.3612
    option['internal_geometry']['parameters']['outer_shoulder'] = 13.1388
    option['internal_geometry']['parameters']['cage_half_width'] = 1.2320000000000002
    option['internal_geometry']['parameters']['cage_low'] = 2.128
    option['internal_geometry']['parameters']['cage_high'] = 2.576
    option['internal_geometry']['parameters']['window_radius'] = 1.0752000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '25'
    options.append(copy.deepcopy(option))

    # 16003: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_16000_series_16003_size_17_mm_id_35_mm_od_8_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_16000_series_16003_size_17_mm_id_35_mm_od_8_mm_depth'
    option['size'] = '16003'
    option['series'] = '16000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 17.0
    option['dimensions']['outside'] = 35.0
    option['dimensions']['width'] = 8.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 13
    option['internal_geometry']['balls_per_row'] = 13
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 17.0
    option['internal_geometry']['parameters']['outside'] = 35.0
    option['internal_geometry']['parameters']['width'] = 8.0
    option['internal_geometry']['parameters']['edge'] = 0.48
    option['internal_geometry']['parameters']['pitch_radius'] = 13.0
    option['internal_geometry']['parameters']['ball_radius'] = 2.24
    option['internal_geometry']['parameters']['groove_radius'] = 2.2960000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 11.6112
    option['internal_geometry']['parameters']['outer_shoulder'] = 14.3888
    option['internal_geometry']['parameters']['cage_half_width'] = 1.2320000000000002
    option['internal_geometry']['parameters']['cage_low'] = 2.128
    option['internal_geometry']['parameters']['cage_high'] = 2.576
    option['internal_geometry']['parameters']['window_radius'] = 1.0752000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '27'
    options.append(copy.deepcopy(option))

    # 16004: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_16000_series_16004_size_20_mm_id_42_mm_od_8_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_16000_series_16004_size_20_mm_id_42_mm_od_8_mm_depth'
    option['size'] = '16004'
    option['series'] = '16000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 20.0
    option['dimensions']['outside'] = 42.0
    option['dimensions']['width'] = 8.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 15
    option['internal_geometry']['balls_per_row'] = 15
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 20.0
    option['internal_geometry']['parameters']['outside'] = 42.0
    option['internal_geometry']['parameters']['width'] = 8.0
    option['internal_geometry']['parameters']['edge'] = 0.48
    option['internal_geometry']['parameters']['pitch_radius'] = 15.5
    option['internal_geometry']['parameters']['ball_radius'] = 2.24
    option['internal_geometry']['parameters']['groove_radius'] = 2.2960000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 14.1112
    option['internal_geometry']['parameters']['outer_shoulder'] = 16.8888
    option['internal_geometry']['parameters']['cage_half_width'] = 1.2320000000000002
    option['internal_geometry']['parameters']['cage_low'] = 2.128
    option['internal_geometry']['parameters']['cage_high'] = 2.576
    option['internal_geometry']['parameters']['window_radius'] = 1.0752000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '50'
    options.append(copy.deepcopy(option))

    # 16005: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_16000_series_16005_size_25_mm_id_47_mm_od_8_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_16000_series_16005_size_25_mm_id_47_mm_od_8_mm_depth'
    option['size'] = '16005'
    option['series'] = '16000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 25.0
    option['dimensions']['outside'] = 47.0
    option['dimensions']['width'] = 8.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 18
    option['internal_geometry']['balls_per_row'] = 18
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 25.0
    option['internal_geometry']['parameters']['outside'] = 47.0
    option['internal_geometry']['parameters']['width'] = 8.0
    option['internal_geometry']['parameters']['edge'] = 0.48
    option['internal_geometry']['parameters']['pitch_radius'] = 18.0
    option['internal_geometry']['parameters']['ball_radius'] = 2.24
    option['internal_geometry']['parameters']['groove_radius'] = 2.2960000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 16.6112
    option['internal_geometry']['parameters']['outer_shoulder'] = 19.3888
    option['internal_geometry']['parameters']['cage_half_width'] = 1.2320000000000002
    option['internal_geometry']['parameters']['cage_low'] = 2.128
    option['internal_geometry']['parameters']['cage_high'] = 2.576
    option['internal_geometry']['parameters']['window_radius'] = 1.0752000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '60'
    options.append(copy.deepcopy(option))

    # 16006: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_16000_series_16006_size_30_mm_id_55_mm_od_9_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_16000_series_16006_size_30_mm_id_55_mm_od_9_mm_depth'
    option['size'] = '16006'
    option['series'] = '16000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 30.0
    option['dimensions']['outside'] = 55.0
    option['dimensions']['width'] = 9.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 19
    option['internal_geometry']['balls_per_row'] = 19
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 30.0
    option['internal_geometry']['parameters']['outside'] = 55.0
    option['internal_geometry']['parameters']['width'] = 9.0
    option['internal_geometry']['parameters']['edge'] = 0.54
    option['internal_geometry']['parameters']['pitch_radius'] = 21.25
    option['internal_geometry']['parameters']['ball_radius'] = 2.5200000000000005
    option['internal_geometry']['parameters']['groove_radius'] = 2.5830000000000006
    option['internal_geometry']['parameters']['inner_shoulder'] = 19.6876
    option['internal_geometry']['parameters']['outer_shoulder'] = 22.8124
    option['internal_geometry']['parameters']['cage_half_width'] = 1.3860000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.394
    option['internal_geometry']['parameters']['cage_high'] = 2.898
    option['internal_geometry']['parameters']['window_radius'] = 1.2096000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '85'
    options.append(copy.deepcopy(option))

    # 16007: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_16000_series_16007_size_35_mm_id_62_mm_od_9_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_16000_series_16007_size_35_mm_id_62_mm_od_9_mm_depth'
    option['size'] = '16007'
    option['series'] = '16000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 35.0
    option['dimensions']['outside'] = 62.0
    option['dimensions']['width'] = 9.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 22
    option['internal_geometry']['balls_per_row'] = 22
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 35.0
    option['internal_geometry']['parameters']['outside'] = 62.0
    option['internal_geometry']['parameters']['width'] = 9.0
    option['internal_geometry']['parameters']['edge'] = 0.54
    option['internal_geometry']['parameters']['pitch_radius'] = 24.25
    option['internal_geometry']['parameters']['ball_radius'] = 2.5200000000000005
    option['internal_geometry']['parameters']['groove_radius'] = 2.5830000000000006
    option['internal_geometry']['parameters']['inner_shoulder'] = 22.6876
    option['internal_geometry']['parameters']['outer_shoulder'] = 25.8124
    option['internal_geometry']['parameters']['cage_half_width'] = 1.3860000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.394
    option['internal_geometry']['parameters']['cage_high'] = 2.898
    option['internal_geometry']['parameters']['window_radius'] = 1.2096000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '100'
    options.append(copy.deepcopy(option))

    # 16008: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_16000_series_16008_size_40_mm_id_68_mm_od_9_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_16000_series_16008_size_40_mm_id_68_mm_od_9_mm_depth'
    option['size'] = '16008'
    option['series'] = '16000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 40.0
    option['dimensions']['outside'] = 68.0
    option['dimensions']['width'] = 9.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 24
    option['internal_geometry']['balls_per_row'] = 24
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 40.0
    option['internal_geometry']['parameters']['outside'] = 68.0
    option['internal_geometry']['parameters']['width'] = 9.0
    option['internal_geometry']['parameters']['edge'] = 0.54
    option['internal_geometry']['parameters']['pitch_radius'] = 27.0
    option['internal_geometry']['parameters']['ball_radius'] = 2.5200000000000005
    option['internal_geometry']['parameters']['groove_radius'] = 2.5830000000000006
    option['internal_geometry']['parameters']['inner_shoulder'] = 25.4376
    option['internal_geometry']['parameters']['outer_shoulder'] = 28.5624
    option['internal_geometry']['parameters']['cage_half_width'] = 1.3860000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.394
    option['internal_geometry']['parameters']['cage_high'] = 2.898
    option['internal_geometry']['parameters']['window_radius'] = 1.2096000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '130'
    options.append(copy.deepcopy(option))

    # 16009: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_16000_series_16009_size_45_mm_id_75_mm_od_10_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_16000_series_16009_size_45_mm_id_75_mm_od_10_mm_depth'
    option['size'] = '16009'
    option['series'] = '16000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 45.0
    option['dimensions']['outside'] = 75.0
    option['dimensions']['width'] = 10.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 24
    option['internal_geometry']['balls_per_row'] = 24
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 45.0
    option['internal_geometry']['parameters']['outside'] = 75.0
    option['internal_geometry']['parameters']['width'] = 10.0
    option['internal_geometry']['parameters']['edge'] = 0.6
    option['internal_geometry']['parameters']['pitch_radius'] = 30.0
    option['internal_geometry']['parameters']['ball_radius'] = 2.8000000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 2.87
    option['internal_geometry']['parameters']['inner_shoulder'] = 28.264
    option['internal_geometry']['parameters']['outer_shoulder'] = 31.736
    option['internal_geometry']['parameters']['cage_half_width'] = 1.5400000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.66
    option['internal_geometry']['parameters']['cage_high'] = 3.22
    option['internal_geometry']['parameters']['window_radius'] = 1.344
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '170'
    options.append(copy.deepcopy(option))

    # 16010: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_16000_series_16010_size_50_mm_id_80_mm_od_10_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_16000_series_16010_size_50_mm_id_80_mm_od_10_mm_depth'
    option['size'] = '16010'
    option['series'] = '16000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 50.0
    option['dimensions']['outside'] = 80.0
    option['dimensions']['width'] = 10.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 26
    option['internal_geometry']['balls_per_row'] = 26
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 50.0
    option['internal_geometry']['parameters']['outside'] = 80.0
    option['internal_geometry']['parameters']['width'] = 10.0
    option['internal_geometry']['parameters']['edge'] = 0.6
    option['internal_geometry']['parameters']['pitch_radius'] = 32.5
    option['internal_geometry']['parameters']['ball_radius'] = 2.8000000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 2.87
    option['internal_geometry']['parameters']['inner_shoulder'] = 30.764
    option['internal_geometry']['parameters']['outer_shoulder'] = 34.236
    option['internal_geometry']['parameters']['cage_half_width'] = 1.5400000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.66
    option['internal_geometry']['parameters']['cage_high'] = 3.22
    option['internal_geometry']['parameters']['window_radius'] = 1.344
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '180'
    options.append(copy.deepcopy(option))

    # 16011: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_16000_series_16011_size_55_mm_id_90_mm_od_11_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_16000_series_16011_size_55_mm_id_90_mm_od_11_mm_depth'
    option['size'] = '16011'
    option['series'] = '16000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 55.0
    option['dimensions']['outside'] = 90.0
    option['dimensions']['width'] = 11.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 27
    option['internal_geometry']['balls_per_row'] = 27
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 55.0
    option['internal_geometry']['parameters']['outside'] = 90.0
    option['internal_geometry']['parameters']['width'] = 11.0
    option['internal_geometry']['parameters']['edge'] = 0.6599999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 36.25
    option['internal_geometry']['parameters']['ball_radius'] = 3.08
    option['internal_geometry']['parameters']['groove_radius'] = 3.157
    option['internal_geometry']['parameters']['inner_shoulder'] = 34.3404
    option['internal_geometry']['parameters']['outer_shoulder'] = 38.1596
    option['internal_geometry']['parameters']['cage_half_width'] = 1.6940000000000002
    option['internal_geometry']['parameters']['cage_low'] = 2.9259999999999997
    option['internal_geometry']['parameters']['cage_high'] = 3.542
    option['internal_geometry']['parameters']['window_radius'] = 1.4784
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '260'
    options.append(copy.deepcopy(option))

    # 16012: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_16000_series_16012_size_60_mm_id_95_mm_od_11_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_16000_series_16012_size_60_mm_id_95_mm_od_11_mm_depth'
    option['size'] = '16012'
    option['series'] = '16000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 60.0
    option['dimensions']['outside'] = 95.0
    option['dimensions']['width'] = 11.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 29
    option['internal_geometry']['balls_per_row'] = 29
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 60.0
    option['internal_geometry']['parameters']['outside'] = 95.0
    option['internal_geometry']['parameters']['width'] = 11.0
    option['internal_geometry']['parameters']['edge'] = 0.6599999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 38.75
    option['internal_geometry']['parameters']['ball_radius'] = 3.08
    option['internal_geometry']['parameters']['groove_radius'] = 3.157
    option['internal_geometry']['parameters']['inner_shoulder'] = 36.8404
    option['internal_geometry']['parameters']['outer_shoulder'] = 40.6596
    option['internal_geometry']['parameters']['cage_half_width'] = 1.6940000000000002
    option['internal_geometry']['parameters']['cage_low'] = 2.9259999999999997
    option['internal_geometry']['parameters']['cage_high'] = 3.542
    option['internal_geometry']['parameters']['window_radius'] = 1.4784
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '280'
    options.append(copy.deepcopy(option))

    # 16013: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_16000_series_16013_size_65_mm_id_100_mm_od_11_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_16000_series_16013_size_65_mm_id_100_mm_od_11_mm_depth'
    option['size'] = '16013'
    option['series'] = '16000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 65.0
    option['dimensions']['outside'] = 100.0
    option['dimensions']['width'] = 11.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 31
    option['internal_geometry']['balls_per_row'] = 31
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 65.0
    option['internal_geometry']['parameters']['outside'] = 100.0
    option['internal_geometry']['parameters']['width'] = 11.0
    option['internal_geometry']['parameters']['edge'] = 0.6599999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 41.25
    option['internal_geometry']['parameters']['ball_radius'] = 3.08
    option['internal_geometry']['parameters']['groove_radius'] = 3.157
    option['internal_geometry']['parameters']['inner_shoulder'] = 39.3404
    option['internal_geometry']['parameters']['outer_shoulder'] = 43.1596
    option['internal_geometry']['parameters']['cage_half_width'] = 1.6940000000000002
    option['internal_geometry']['parameters']['cage_low'] = 2.9259999999999997
    option['internal_geometry']['parameters']['cage_high'] = 3.542
    option['internal_geometry']['parameters']['window_radius'] = 1.4784
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '300'
    options.append(copy.deepcopy(option))

    # 16014: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_16000_series_16014_size_70_mm_id_110_mm_od_13_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_16000_series_16014_size_70_mm_id_110_mm_od_13_mm_depth'
    option['size'] = '16014'
    option['series'] = '16000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 70.0
    option['dimensions']['outside'] = 110.0
    option['dimensions']['width'] = 13.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 28
    option['internal_geometry']['balls_per_row'] = 28
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 70.0
    option['internal_geometry']['parameters']['outside'] = 110.0
    option['internal_geometry']['parameters']['width'] = 13.0
    option['internal_geometry']['parameters']['edge'] = 0.78
    option['internal_geometry']['parameters']['pitch_radius'] = 45.0
    option['internal_geometry']['parameters']['ball_radius'] = 3.6400000000000006
    option['internal_geometry']['parameters']['groove_radius'] = 3.7310000000000008
    option['internal_geometry']['parameters']['inner_shoulder'] = 42.7432
    option['internal_geometry']['parameters']['outer_shoulder'] = 47.2568
    option['internal_geometry']['parameters']['cage_half_width'] = 2.0020000000000007
    option['internal_geometry']['parameters']['cage_low'] = 3.458
    option['internal_geometry']['parameters']['cage_high'] = 4.186
    option['internal_geometry']['parameters']['window_radius'] = 1.7472000000000003
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '440'
    options.append(copy.deepcopy(option))

    # 16015: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_16000_series_16015_size_75_mm_id_115_mm_od_13_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_16000_series_16015_size_75_mm_id_115_mm_od_13_mm_depth'
    option['size'] = '16015'
    option['series'] = '16000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 75.0
    option['dimensions']['outside'] = 115.0
    option['dimensions']['width'] = 13.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 30
    option['internal_geometry']['balls_per_row'] = 30
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 75.0
    option['internal_geometry']['parameters']['outside'] = 115.0
    option['internal_geometry']['parameters']['width'] = 13.0
    option['internal_geometry']['parameters']['edge'] = 0.78
    option['internal_geometry']['parameters']['pitch_radius'] = 47.5
    option['internal_geometry']['parameters']['ball_radius'] = 3.6400000000000006
    option['internal_geometry']['parameters']['groove_radius'] = 3.7310000000000008
    option['internal_geometry']['parameters']['inner_shoulder'] = 45.2432
    option['internal_geometry']['parameters']['outer_shoulder'] = 49.7568
    option['internal_geometry']['parameters']['cage_half_width'] = 2.0020000000000007
    option['internal_geometry']['parameters']['cage_low'] = 3.458
    option['internal_geometry']['parameters']['cage_high'] = 4.186
    option['internal_geometry']['parameters']['window_radius'] = 1.7472000000000003
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '462'
    options.append(copy.deepcopy(option))

    # 16016: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_16000_series_16016_size_80_mm_id_125_mm_od_14_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_16000_series_16016_size_80_mm_id_125_mm_od_14_mm_depth'
    option['size'] = '16016'
    option['series'] = '16000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 80.0
    option['dimensions']['outside'] = 125.0
    option['dimensions']['width'] = 14.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 30
    option['internal_geometry']['balls_per_row'] = 30
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 80.0
    option['internal_geometry']['parameters']['outside'] = 125.0
    option['internal_geometry']['parameters']['width'] = 14.0
    option['internal_geometry']['parameters']['edge'] = 0.84
    option['internal_geometry']['parameters']['pitch_radius'] = 51.25
    option['internal_geometry']['parameters']['ball_radius'] = 3.9200000000000004
    option['internal_geometry']['parameters']['groove_radius'] = 4.018000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 48.8196
    option['internal_geometry']['parameters']['outer_shoulder'] = 53.6804
    option['internal_geometry']['parameters']['cage_half_width'] = 2.1560000000000006
    option['internal_geometry']['parameters']['cage_low'] = 3.724
    option['internal_geometry']['parameters']['cage_high'] = 4.508
    option['internal_geometry']['parameters']['window_radius'] = 1.8816000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '620'
    options.append(copy.deepcopy(option))

    # 16017: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_16000_series_16017_size_85_mm_id_130_mm_od_14_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_16000_series_16017_size_85_mm_id_130_mm_od_14_mm_depth'
    option['size'] = '16017'
    option['series'] = '16000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 85.0
    option['dimensions']['outside'] = 130.0
    option['dimensions']['width'] = 14.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 31
    option['internal_geometry']['balls_per_row'] = 31
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 85.0
    option['internal_geometry']['parameters']['outside'] = 130.0
    option['internal_geometry']['parameters']['width'] = 14.0
    option['internal_geometry']['parameters']['edge'] = 0.84
    option['internal_geometry']['parameters']['pitch_radius'] = 53.75
    option['internal_geometry']['parameters']['ball_radius'] = 3.9200000000000004
    option['internal_geometry']['parameters']['groove_radius'] = 4.018000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 51.3196
    option['internal_geometry']['parameters']['outer_shoulder'] = 56.1804
    option['internal_geometry']['parameters']['cage_half_width'] = 2.1560000000000006
    option['internal_geometry']['parameters']['cage_low'] = 3.724
    option['internal_geometry']['parameters']['cage_high'] = 4.508
    option['internal_geometry']['parameters']['window_radius'] = 1.8816000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '651'
    options.append(copy.deepcopy(option))

    # 16018: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_16000_series_16018_size_90_mm_id_140_mm_od_16_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_16000_series_16018_size_90_mm_id_140_mm_od_16_mm_depth'
    option['size'] = '16018'
    option['series'] = '16000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 90.0
    option['dimensions']['outside'] = 140.0
    option['dimensions']['width'] = 16.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 29
    option['internal_geometry']['balls_per_row'] = 29
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 90.0
    option['internal_geometry']['parameters']['outside'] = 140.0
    option['internal_geometry']['parameters']['width'] = 16.0
    option['internal_geometry']['parameters']['edge'] = 0.96
    option['internal_geometry']['parameters']['pitch_radius'] = 57.5
    option['internal_geometry']['parameters']['ball_radius'] = 4.48
    option['internal_geometry']['parameters']['groove_radius'] = 4.5920000000000005
    option['internal_geometry']['parameters']['inner_shoulder'] = 54.7224
    option['internal_geometry']['parameters']['outer_shoulder'] = 60.2776
    option['internal_geometry']['parameters']['cage_half_width'] = 2.4640000000000004
    option['internal_geometry']['parameters']['cage_low'] = 4.256
    option['internal_geometry']['parameters']['cage_high'] = 5.152
    option['internal_geometry']['parameters']['window_radius'] = 2.1504000000000003
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '872'
    options.append(copy.deepcopy(option))

    # 16019: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_16000_series_16019_size_95_mm_id_145_mm_od_16_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_16000_series_16019_size_95_mm_id_145_mm_od_16_mm_depth'
    option['size'] = '16019'
    option['series'] = '16000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 95.0
    option['dimensions']['outside'] = 145.0
    option['dimensions']['width'] = 16.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 31
    option['internal_geometry']['balls_per_row'] = 31
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 95.0
    option['internal_geometry']['parameters']['outside'] = 145.0
    option['internal_geometry']['parameters']['width'] = 16.0
    option['internal_geometry']['parameters']['edge'] = 0.96
    option['internal_geometry']['parameters']['pitch_radius'] = 60.0
    option['internal_geometry']['parameters']['ball_radius'] = 4.48
    option['internal_geometry']['parameters']['groove_radius'] = 4.5920000000000005
    option['internal_geometry']['parameters']['inner_shoulder'] = 57.2224
    option['internal_geometry']['parameters']['outer_shoulder'] = 62.7776
    option['internal_geometry']['parameters']['cage_half_width'] = 2.4640000000000004
    option['internal_geometry']['parameters']['cage_low'] = 4.256
    option['internal_geometry']['parameters']['cage_high'] = 5.152
    option['internal_geometry']['parameters']['window_radius'] = 2.1504000000000003
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '903'
    options.append(copy.deepcopy(option))

    # 16020: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_16000_series_16020_size_100_mm_id_150_mm_od_16_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_16000_series_16020_size_100_mm_id_150_mm_od_16_mm_depth'
    option['size'] = '16020'
    option['series'] = '16000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 100.0
    option['dimensions']['outside'] = 150.0
    option['dimensions']['width'] = 16.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 32
    option['internal_geometry']['balls_per_row'] = 32
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 100.0
    option['internal_geometry']['parameters']['outside'] = 150.0
    option['internal_geometry']['parameters']['width'] = 16.0
    option['internal_geometry']['parameters']['edge'] = 0.96
    option['internal_geometry']['parameters']['pitch_radius'] = 62.5
    option['internal_geometry']['parameters']['ball_radius'] = 4.48
    option['internal_geometry']['parameters']['groove_radius'] = 4.5920000000000005
    option['internal_geometry']['parameters']['inner_shoulder'] = 59.7224
    option['internal_geometry']['parameters']['outer_shoulder'] = 65.2776
    option['internal_geometry']['parameters']['cage_half_width'] = 2.4640000000000004
    option['internal_geometry']['parameters']['cage_low'] = 4.256
    option['internal_geometry']['parameters']['cage_high'] = 5.152
    option['internal_geometry']['parameters']['window_radius'] = 2.1504000000000003
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '944'
    options.append(copy.deepcopy(option))

    # 16021: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_16000_series_16021_size_105_mm_id_160_mm_od_18_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_16000_series_16021_size_105_mm_id_160_mm_od_18_mm_depth'
    option['size'] = '16021'
    option['series'] = '16000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 105.0
    option['dimensions']['outside'] = 160.0
    option['dimensions']['width'] = 18.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 30
    option['internal_geometry']['balls_per_row'] = 30
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 105.0
    option['internal_geometry']['parameters']['outside'] = 160.0
    option['internal_geometry']['parameters']['width'] = 18.0
    option['internal_geometry']['parameters']['edge'] = 1.08
    option['internal_geometry']['parameters']['pitch_radius'] = 66.25
    option['internal_geometry']['parameters']['ball_radius'] = 5.040000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 5.166000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 63.1252
    option['internal_geometry']['parameters']['outer_shoulder'] = 69.3748
    option['internal_geometry']['parameters']['cage_half_width'] = 2.7720000000000007
    option['internal_geometry']['parameters']['cage_low'] = 4.788
    option['internal_geometry']['parameters']['cage_high'] = 5.796
    option['internal_geometry']['parameters']['window_radius'] = 2.4192000000000005
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1,239'
    options.append(copy.deepcopy(option))

    # 16022: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_16000_series_16022_size_110_mm_id_170_mm_od_19_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_16000_series_16022_size_110_mm_id_170_mm_od_19_mm_depth'
    option['size'] = '16022'
    option['series'] = '16000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 110.0
    option['dimensions']['outside'] = 170.0
    option['dimensions']['width'] = 19.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 30
    option['internal_geometry']['balls_per_row'] = 30
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 110.0
    option['internal_geometry']['parameters']['outside'] = 170.0
    option['internal_geometry']['parameters']['width'] = 19.0
    option['internal_geometry']['parameters']['edge'] = 1.14
    option['internal_geometry']['parameters']['pitch_radius'] = 70.0
    option['internal_geometry']['parameters']['ball_radius'] = 5.32
    option['internal_geometry']['parameters']['groove_radius'] = 5.453
    option['internal_geometry']['parameters']['inner_shoulder'] = 66.7016
    option['internal_geometry']['parameters']['outer_shoulder'] = 73.2984
    option['internal_geometry']['parameters']['cage_half_width'] = 2.9260000000000006
    option['internal_geometry']['parameters']['cage_low'] = 5.054
    option['internal_geometry']['parameters']['cage_high'] = 6.117999999999999
    option['internal_geometry']['parameters']['window_radius'] = 2.5536
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1,508'
    options.append(copy.deepcopy(option))

    # 5200: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5200_series_5200_size_10_mm_id_30_mm_od_14.3_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5200_series_5200_size_10_mm_id_30_mm_od_14_3_mm_depth'
    option['size'] = '5200'
    option['series'] = '5200'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 10.0
    option['dimensions']['outside'] = 30.0
    option['dimensions']['width'] = 14.3
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 20
    option['internal_geometry']['balls_per_row'] = 10
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 10.0
    option['internal_geometry']['parameters']['outside'] = 30.0
    option['internal_geometry']['parameters']['width'] = 14.3
    option['internal_geometry']['parameters']['edge'] = 0.6
    option['internal_geometry']['parameters']['pitch_radius'] = 10.0
    option['internal_geometry']['parameters']['ball_radius'] = 2.145
    option['internal_geometry']['parameters']['groove_radius'] = 2.25225
    option['internal_geometry']['parameters']['inner_shoulder'] = 8.6701
    option['internal_geometry']['parameters']['outer_shoulder'] = 11.3299
    option['internal_geometry']['parameters']['cage_half_width'] = 1.17975
    option['internal_geometry']['parameters']['cage_low'] = 2.03775
    option['internal_geometry']['parameters']['cage_high'] = 2.4667499999999998
    option['internal_geometry']['parameters']['window_radius'] = 1.0296
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.053625000000000006
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '49'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_5200_series_5200_size_10_mm_id_30_mm_od_14.2_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # 5201: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5200_series_5201_size_12_mm_id_32_mm_od_15.9_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5200_series_5201_size_12_mm_id_32_mm_od_15_9_mm_depth'
    option['size'] = '5201'
    option['series'] = '5200'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 12.0
    option['dimensions']['outside'] = 32.0
    option['dimensions']['width'] = 15.9
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 20
    option['internal_geometry']['balls_per_row'] = 10
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 12.0
    option['internal_geometry']['parameters']['outside'] = 32.0
    option['internal_geometry']['parameters']['width'] = 15.9
    option['internal_geometry']['parameters']['edge'] = 0.6
    option['internal_geometry']['parameters']['pitch_radius'] = 11.0
    option['internal_geometry']['parameters']['ball_radius'] = 2.385
    option['internal_geometry']['parameters']['groove_radius'] = 2.50425
    option['internal_geometry']['parameters']['inner_shoulder'] = 9.5213
    option['internal_geometry']['parameters']['outer_shoulder'] = 12.4787
    option['internal_geometry']['parameters']['cage_half_width'] = 1.31175
    option['internal_geometry']['parameters']['cage_low'] = 2.2657499999999997
    option['internal_geometry']['parameters']['cage_high'] = 2.7427499999999996
    option['internal_geometry']['parameters']['window_radius'] = 1.1447999999999998
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.059625
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '12'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_5200_series_5201_size_12_mm_id_32_mm_od_15.8_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # 5202: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5200_series_5202_size_15_mm_id_35_mm_od_15.9_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5200_series_5202_size_15_mm_id_35_mm_od_15_9_mm_depth'
    option['size'] = '5202'
    option['series'] = '5200'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 15.0
    option['dimensions']['outside'] = 35.0
    option['dimensions']['width'] = 15.9
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 24
    option['internal_geometry']['balls_per_row'] = 12
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 15.0
    option['internal_geometry']['parameters']['outside'] = 35.0
    option['internal_geometry']['parameters']['width'] = 15.9
    option['internal_geometry']['parameters']['edge'] = 0.6
    option['internal_geometry']['parameters']['pitch_radius'] = 12.5
    option['internal_geometry']['parameters']['ball_radius'] = 2.385
    option['internal_geometry']['parameters']['groove_radius'] = 2.50425
    option['internal_geometry']['parameters']['inner_shoulder'] = 11.0213
    option['internal_geometry']['parameters']['outer_shoulder'] = 13.9787
    option['internal_geometry']['parameters']['cage_half_width'] = 1.31175
    option['internal_geometry']['parameters']['cage_low'] = 2.2657499999999997
    option['internal_geometry']['parameters']['cage_high'] = 2.7427499999999996
    option['internal_geometry']['parameters']['window_radius'] = 1.1447999999999998
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.059625
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '64'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_5200_series_5202_size_15_mm_id_35_mm_od_15.8_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # 5203: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5200_series_5203_size_17_mm_id_40_mm_od_17.5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5200_series_5203_size_17_mm_id_40_mm_od_17_5_mm_depth'
    option['size'] = '5203'
    option['series'] = '5200'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 17.0
    option['dimensions']['outside'] = 40.0
    option['dimensions']['width'] = 17.5
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 24
    option['internal_geometry']['balls_per_row'] = 12
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 17.0
    option['internal_geometry']['parameters']['outside'] = 40.0
    option['internal_geometry']['parameters']['width'] = 17.5
    option['internal_geometry']['parameters']['edge'] = 0.69
    option['internal_geometry']['parameters']['pitch_radius'] = 14.25
    option['internal_geometry']['parameters']['ball_radius'] = 2.625
    option['internal_geometry']['parameters']['groove_radius'] = 2.75625
    option['internal_geometry']['parameters']['inner_shoulder'] = 12.6225
    option['internal_geometry']['parameters']['outer_shoulder'] = 15.8775
    option['internal_geometry']['parameters']['cage_half_width'] = 1.44375
    option['internal_geometry']['parameters']['cage_low'] = 2.49375
    option['internal_geometry']['parameters']['cage_high'] = 3.01875
    option['internal_geometry']['parameters']['window_radius'] = 1.26
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.065625
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '96'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_5200_series_5203_size_17_mm_id_40_mm_od_17.4_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # 5204: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5200_series_5204_size_20_mm_id_47_mm_od_20.6_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5200_series_5204_size_20_mm_id_47_mm_od_20_6_mm_depth'
    option['size'] = '5204'
    option['series'] = '5200'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 20.0
    option['dimensions']['outside'] = 47.0
    option['dimensions']['width'] = 20.6
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 24
    option['internal_geometry']['balls_per_row'] = 12
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 20.0
    option['internal_geometry']['parameters']['outside'] = 47.0
    option['internal_geometry']['parameters']['width'] = 20.6
    option['internal_geometry']['parameters']['edge'] = 0.8099999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 16.75
    option['internal_geometry']['parameters']['ball_radius'] = 3.0900000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 3.2445000000000004
    option['internal_geometry']['parameters']['inner_shoulder'] = 14.8342
    option['internal_geometry']['parameters']['outer_shoulder'] = 18.6658
    option['internal_geometry']['parameters']['cage_half_width'] = 1.6995000000000002
    option['internal_geometry']['parameters']['cage_low'] = 2.9355
    option['internal_geometry']['parameters']['cage_high'] = 3.5535
    option['internal_geometry']['parameters']['window_radius'] = 1.4832
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.07725000000000001
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '153'
    options.append(copy.deepcopy(option))

    # 5205: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5200_series_5205_size_25_mm_id_52_mm_od_20.6_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5200_series_5205_size_25_mm_id_52_mm_od_20_6_mm_depth'
    option['size'] = '5205'
    option['series'] = '5200'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 25.0
    option['dimensions']['outside'] = 52.0
    option['dimensions']['width'] = 20.6
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 28
    option['internal_geometry']['balls_per_row'] = 14
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 25.0
    option['internal_geometry']['parameters']['outside'] = 52.0
    option['internal_geometry']['parameters']['width'] = 20.6
    option['internal_geometry']['parameters']['edge'] = 0.8099999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 19.25
    option['internal_geometry']['parameters']['ball_radius'] = 3.0900000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 3.2445000000000004
    option['internal_geometry']['parameters']['inner_shoulder'] = 17.3342
    option['internal_geometry']['parameters']['outer_shoulder'] = 21.1658
    option['internal_geometry']['parameters']['cage_half_width'] = 1.6995000000000002
    option['internal_geometry']['parameters']['cage_low'] = 2.9355
    option['internal_geometry']['parameters']['cage_high'] = 3.5535
    option['internal_geometry']['parameters']['window_radius'] = 1.4832
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.07725000000000001
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '175'
    options.append(copy.deepcopy(option))

    # 5206: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5200_series_5206_size_30_mm_id_62_mm_od_23.8_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5200_series_5206_size_30_mm_id_62_mm_od_23_8_mm_depth'
    option['size'] = '5206'
    option['series'] = '5200'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 30.0
    option['dimensions']['outside'] = 62.0
    option['dimensions']['width'] = 23.8
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 28
    option['internal_geometry']['balls_per_row'] = 14
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 30.0
    option['internal_geometry']['parameters']['outside'] = 62.0
    option['internal_geometry']['parameters']['width'] = 23.8
    option['internal_geometry']['parameters']['edge'] = 0.96
    option['internal_geometry']['parameters']['pitch_radius'] = 23.0
    option['internal_geometry']['parameters']['ball_radius'] = 3.57
    option['internal_geometry']['parameters']['groove_radius'] = 3.7485
    option['internal_geometry']['parameters']['inner_shoulder'] = 20.7866
    option['internal_geometry']['parameters']['outer_shoulder'] = 25.2134
    option['internal_geometry']['parameters']['cage_half_width'] = 1.9635
    option['internal_geometry']['parameters']['cage_low'] = 3.3914999999999997
    option['internal_geometry']['parameters']['cage_high'] = 4.105499999999999
    option['internal_geometry']['parameters']['window_radius'] = 1.7135999999999998
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.08925
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '286'
    options.append(copy.deepcopy(option))

    # 5207: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5200_series_5207_size_35_mm_id_72_mm_od_27_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5200_series_5207_size_35_mm_id_72_mm_od_27_mm_depth'
    option['size'] = '5207'
    option['series'] = '5200'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 35.0
    option['dimensions']['outside'] = 72.0
    option['dimensions']['width'] = 27.0
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 30
    option['internal_geometry']['balls_per_row'] = 15
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 35.0
    option['internal_geometry']['parameters']['outside'] = 72.0
    option['internal_geometry']['parameters']['width'] = 27.0
    option['internal_geometry']['parameters']['edge'] = 1.1099999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 26.75
    option['internal_geometry']['parameters']['ball_radius'] = 4.05
    option['internal_geometry']['parameters']['groove_radius'] = 4.2525
    option['internal_geometry']['parameters']['inner_shoulder'] = 24.239
    option['internal_geometry']['parameters']['outer_shoulder'] = 29.261
    option['internal_geometry']['parameters']['cage_half_width'] = 2.2275
    option['internal_geometry']['parameters']['cage_low'] = 3.8474999999999997
    option['internal_geometry']['parameters']['cage_high'] = 4.6575
    option['internal_geometry']['parameters']['window_radius'] = 1.944
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.10125
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '436'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_5200_series_5207_size_35_mm_id_72_mm_od_26.9_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # 5208: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5200_series_5208_size_40_mm_id_80_mm_od_30.2_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5200_series_5208_size_40_mm_id_80_mm_od_30_2_mm_depth'
    option['size'] = '5208'
    option['series'] = '5200'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 40.0
    option['dimensions']['outside'] = 80.0
    option['dimensions']['width'] = 30.2
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 30
    option['internal_geometry']['balls_per_row'] = 15
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 40.0
    option['internal_geometry']['parameters']['outside'] = 80.0
    option['internal_geometry']['parameters']['width'] = 30.2
    option['internal_geometry']['parameters']['edge'] = 1.2
    option['internal_geometry']['parameters']['pitch_radius'] = 30.0
    option['internal_geometry']['parameters']['ball_radius'] = 4.529999999999999
    option['internal_geometry']['parameters']['groove_radius'] = 4.7565
    option['internal_geometry']['parameters']['inner_shoulder'] = 27.1914
    option['internal_geometry']['parameters']['outer_shoulder'] = 32.8086
    option['internal_geometry']['parameters']['cage_half_width'] = 2.4915
    option['internal_geometry']['parameters']['cage_low'] = 4.303499999999999
    option['internal_geometry']['parameters']['cage_high'] = 5.2094999999999985
    option['internal_geometry']['parameters']['window_radius'] = 2.1743999999999994
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.11324999999999999
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '590'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_5200_series_5208_size_40_mm_id_80_mm_od_30.1_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # 5209: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5200_series_5209_size_45_mm_id_85_mm_od_30.2_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5200_series_5209_size_45_mm_id_85_mm_od_30_2_mm_depth'
    option['size'] = '5209'
    option['series'] = '5200'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 45.0
    option['dimensions']['outside'] = 85.0
    option['dimensions']['width'] = 30.2
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 32
    option['internal_geometry']['balls_per_row'] = 16
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 45.0
    option['internal_geometry']['parameters']['outside'] = 85.0
    option['internal_geometry']['parameters']['width'] = 30.2
    option['internal_geometry']['parameters']['edge'] = 1.2
    option['internal_geometry']['parameters']['pitch_radius'] = 32.5
    option['internal_geometry']['parameters']['ball_radius'] = 4.529999999999999
    option['internal_geometry']['parameters']['groove_radius'] = 4.7565
    option['internal_geometry']['parameters']['inner_shoulder'] = 29.6914
    option['internal_geometry']['parameters']['outer_shoulder'] = 35.3086
    option['internal_geometry']['parameters']['cage_half_width'] = 2.4915
    option['internal_geometry']['parameters']['cage_low'] = 4.303499999999999
    option['internal_geometry']['parameters']['cage_high'] = 5.2094999999999985
    option['internal_geometry']['parameters']['window_radius'] = 2.1743999999999994
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.11324999999999999
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '640'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_5200_series_5209_size_45_mm_id_85_mm_od_30.1_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # 5210: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5200_series_5210_size_50_mm_id_90_mm_od_30.2_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5200_series_5210_size_50_mm_id_90_mm_od_30_2_mm_depth'
    option['size'] = '5210'
    option['series'] = '5200'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 50.0
    option['dimensions']['outside'] = 90.0
    option['dimensions']['width'] = 30.2
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 34
    option['internal_geometry']['balls_per_row'] = 17
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 50.0
    option['internal_geometry']['parameters']['outside'] = 90.0
    option['internal_geometry']['parameters']['width'] = 30.2
    option['internal_geometry']['parameters']['edge'] = 1.2
    option['internal_geometry']['parameters']['pitch_radius'] = 35.0
    option['internal_geometry']['parameters']['ball_radius'] = 4.529999999999999
    option['internal_geometry']['parameters']['groove_radius'] = 4.7565
    option['internal_geometry']['parameters']['inner_shoulder'] = 32.1914
    option['internal_geometry']['parameters']['outer_shoulder'] = 37.8086
    option['internal_geometry']['parameters']['cage_half_width'] = 2.4915
    option['internal_geometry']['parameters']['cage_low'] = 4.303499999999999
    option['internal_geometry']['parameters']['cage_high'] = 5.2094999999999985
    option['internal_geometry']['parameters']['window_radius'] = 2.1743999999999994
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.11324999999999999
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '690'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_5200_series_5210_size_50_mm_id_90_mm_od_30.1_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # 5211: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5200_series_5211_size_55_mm_id_100_mm_od_33.3_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5200_series_5211_size_55_mm_id_100_mm_od_33_3_mm_depth'
    option['size'] = '5211'
    option['series'] = '5200'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 55.0
    option['dimensions']['outside'] = 100.0
    option['dimensions']['width'] = 33.3
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 34
    option['internal_geometry']['balls_per_row'] = 17
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 55.0
    option['internal_geometry']['parameters']['outside'] = 100.0
    option['internal_geometry']['parameters']['width'] = 33.3
    option['internal_geometry']['parameters']['edge'] = 1.3499999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 38.75
    option['internal_geometry']['parameters']['ball_radius'] = 4.994999999999999
    option['internal_geometry']['parameters']['groove_radius'] = 5.24475
    option['internal_geometry']['parameters']['inner_shoulder'] = 35.6531
    option['internal_geometry']['parameters']['outer_shoulder'] = 41.8469
    option['internal_geometry']['parameters']['cage_half_width'] = 2.7472499999999997
    option['internal_geometry']['parameters']['cage_low'] = 4.745249999999999
    option['internal_geometry']['parameters']['cage_high'] = 5.744249999999998
    option['internal_geometry']['parameters']['window_radius'] = 2.3975999999999997
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.12487499999999999
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1,117'
    options.append(copy.deepcopy(option))

    # 5212: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5200_series_5212_size_60_mm_id_110_mm_od_36.5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5200_series_5212_size_60_mm_id_110_mm_od_36_5_mm_depth'
    option['size'] = '5212'
    option['series'] = '5200'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 60.0
    option['dimensions']['outside'] = 110.0
    option['dimensions']['width'] = 36.5
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 34
    option['internal_geometry']['balls_per_row'] = 17
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 60.0
    option['internal_geometry']['parameters']['outside'] = 110.0
    option['internal_geometry']['parameters']['width'] = 36.5
    option['internal_geometry']['parameters']['edge'] = 1.5
    option['internal_geometry']['parameters']['pitch_radius'] = 42.5
    option['internal_geometry']['parameters']['ball_radius'] = 5.475
    option['internal_geometry']['parameters']['groove_radius'] = 5.74875
    option['internal_geometry']['parameters']['inner_shoulder'] = 39.1055
    option['internal_geometry']['parameters']['outer_shoulder'] = 45.8945
    option['internal_geometry']['parameters']['cage_half_width'] = 3.01125
    option['internal_geometry']['parameters']['cage_low'] = 5.201249999999999
    option['internal_geometry']['parameters']['cage_high'] = 6.296249999999999
    option['internal_geometry']['parameters']['window_radius'] = 2.6279999999999997
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.136875
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1,426'
    options.append(copy.deepcopy(option))

    # 5213: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5200_series_5213_size_65_mm_id_120_mm_od_38.1_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5200_series_5213_size_65_mm_id_120_mm_od_38_1_mm_depth'
    option['size'] = '5213'
    option['series'] = '5200'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 65.0
    option['dimensions']['outside'] = 120.0
    option['dimensions']['width'] = 38.1
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 36
    option['internal_geometry']['balls_per_row'] = 18
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 65.0
    option['internal_geometry']['parameters']['outside'] = 120.0
    option['internal_geometry']['parameters']['width'] = 38.1
    option['internal_geometry']['parameters']['edge'] = 1.65
    option['internal_geometry']['parameters']['pitch_radius'] = 46.25
    option['internal_geometry']['parameters']['ball_radius'] = 5.715
    option['internal_geometry']['parameters']['groove_radius'] = 6.00075
    option['internal_geometry']['parameters']['inner_shoulder'] = 42.7067
    option['internal_geometry']['parameters']['outer_shoulder'] = 49.7933
    option['internal_geometry']['parameters']['cage_half_width'] = 3.14325
    option['internal_geometry']['parameters']['cage_low'] = 5.42925
    option['internal_geometry']['parameters']['cage_high'] = 6.5722499999999995
    option['internal_geometry']['parameters']['window_radius'] = 2.7432
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.142875
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1,916'
    options.append(copy.deepcopy(option))

    # 5214: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5200_series_5214_size_70_mm_id_125_mm_od_39.7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5200_series_5214_size_70_mm_id_125_mm_od_39_7_mm_depth'
    option['size'] = '5214'
    option['series'] = '5200'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 70.0
    option['dimensions']['outside'] = 125.0
    option['dimensions']['width'] = 39.7
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 36
    option['internal_geometry']['balls_per_row'] = 18
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 70.0
    option['internal_geometry']['parameters']['outside'] = 125.0
    option['internal_geometry']['parameters']['width'] = 39.7
    option['internal_geometry']['parameters']['edge'] = 1.65
    option['internal_geometry']['parameters']['pitch_radius'] = 48.75
    option['internal_geometry']['parameters']['ball_radius'] = 5.955
    option['internal_geometry']['parameters']['groove_radius'] = 6.252750000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 45.057900000000004
    option['internal_geometry']['parameters']['outer_shoulder'] = 52.442099999999996
    option['internal_geometry']['parameters']['cage_half_width'] = 3.27525
    option['internal_geometry']['parameters']['cage_low'] = 5.6572499999999994
    option['internal_geometry']['parameters']['cage_high'] = 6.848249999999999
    option['internal_geometry']['parameters']['window_radius'] = 2.8584
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.148875
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '2,061'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_5200_series_5214_size_70_mm_id_125_mm_od_39.6_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # 5215: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5200_series_5215_size_75_mm_id_130_mm_od_41.3_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5200_series_5215_size_75_mm_id_130_mm_od_41_3_mm_depth'
    option['size'] = '5215'
    option['series'] = '5200'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 75.0
    option['dimensions']['outside'] = 130.0
    option['dimensions']['width'] = 41.3
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 38
    option['internal_geometry']['balls_per_row'] = 19
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 75.0
    option['internal_geometry']['parameters']['outside'] = 130.0
    option['internal_geometry']['parameters']['width'] = 41.3
    option['internal_geometry']['parameters']['edge'] = 1.65
    option['internal_geometry']['parameters']['pitch_radius'] = 51.25
    option['internal_geometry']['parameters']['ball_radius'] = 6.194999999999999
    option['internal_geometry']['parameters']['groove_radius'] = 6.50475
    option['internal_geometry']['parameters']['inner_shoulder'] = 47.4091
    option['internal_geometry']['parameters']['outer_shoulder'] = 55.0909
    option['internal_geometry']['parameters']['cage_half_width'] = 3.40725
    option['internal_geometry']['parameters']['cage_low'] = 5.885249999999999
    option['internal_geometry']['parameters']['cage_high'] = 7.124249999999999
    option['internal_geometry']['parameters']['window_radius'] = 2.9736
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.15487499999999998
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '2,479'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_5200_series_5215_size_75_mm_id_130_mm_od_41.2_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # 5216: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5200_series_5216_size_80_mm_id_140_mm_od_44.4_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5200_series_5216_size_80_mm_id_140_mm_od_44_4_mm_depth'
    option['size'] = '5216'
    option['series'] = '5200'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 80.0
    option['dimensions']['outside'] = 140.0
    option['dimensions']['width'] = 44.4
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 38
    option['internal_geometry']['balls_per_row'] = 19
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 80.0
    option['internal_geometry']['parameters']['outside'] = 140.0
    option['internal_geometry']['parameters']['width'] = 44.4
    option['internal_geometry']['parameters']['edge'] = 1.7999999999999998
    option['internal_geometry']['parameters']['pitch_radius'] = 55.0
    option['internal_geometry']['parameters']['ball_radius'] = 6.659999999999999
    option['internal_geometry']['parameters']['groove_radius'] = 6.992999999999999
    option['internal_geometry']['parameters']['inner_shoulder'] = 50.8708
    option['internal_geometry']['parameters']['outer_shoulder'] = 59.1292
    option['internal_geometry']['parameters']['cage_half_width'] = 3.663
    option['internal_geometry']['parameters']['cage_low'] = 6.326999999999999
    option['internal_geometry']['parameters']['cage_high'] = 7.658999999999999
    option['internal_geometry']['parameters']['window_radius'] = 3.1967999999999996
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.16649999999999998
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '2,978'
    options.append(copy.deepcopy(option))

    # 5300: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5300_series_5300_size_10_mm_id_35_mm_od_19_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5300_series_5300_size_10_mm_id_35_mm_od_19_mm_depth'
    option['size'] = '5300'
    option['series'] = '5300'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 10.0
    option['dimensions']['outside'] = 35.0
    option['dimensions']['width'] = 19.0
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.rbibearing.com/products/ball-bearings/5300-series/',
     'https://www.nskamericas.com/tools-resources/abc-bearings/angular-contact-ball-bearings/']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 18
    option['internal_geometry']['balls_per_row'] = 9
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 10.0
    option['internal_geometry']['parameters']['outside'] = 35.0
    option['internal_geometry']['parameters']['width'] = 19.0
    option['internal_geometry']['parameters']['edge'] = 0.75
    option['internal_geometry']['parameters']['pitch_radius'] = 11.25
    option['internal_geometry']['parameters']['ball_radius'] = 2.85
    option['internal_geometry']['parameters']['groove_radius'] = 2.9925
    option['internal_geometry']['parameters']['inner_shoulder'] = 9.483
    option['internal_geometry']['parameters']['outer_shoulder'] = 13.017
    option['internal_geometry']['parameters']['cage_half_width'] = 1.5675000000000001
    option['internal_geometry']['parameters']['cage_low'] = 2.7075
    option['internal_geometry']['parameters']['cage_high'] = 3.2775
    option['internal_geometry']['parameters']['window_radius'] = 1.3679999999999999
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.07125000000000001
    option['internal_geometry']['contact_angle_authority'] = 'selected_catalogue_convention'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '95'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_5300_series_5300_size_10_mm_id_35_mm_od_19.05_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://www.rbibearing.com/products/ball-bearings/5300-series/',
     'https://www.nskamericas.com/tools-resources/abc-bearings/angular-contact-ball-bearings/']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # 5301: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5300_series_5301_size_12_mm_id_37_mm_od_19_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5300_series_5301_size_12_mm_id_37_mm_od_19_mm_depth'
    option['size'] = '5301'
    option['series'] = '5300'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 12.0
    option['dimensions']['outside'] = 37.0
    option['dimensions']['width'] = 19.0
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.rbibearing.com/products/ball-bearings/5300-series/',
     'https://www.nskamericas.com/tools-resources/abc-bearings/angular-contact-ball-bearings/']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 18
    option['internal_geometry']['balls_per_row'] = 9
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 12.0
    option['internal_geometry']['parameters']['outside'] = 37.0
    option['internal_geometry']['parameters']['width'] = 19.0
    option['internal_geometry']['parameters']['edge'] = 0.75
    option['internal_geometry']['parameters']['pitch_radius'] = 12.25
    option['internal_geometry']['parameters']['ball_radius'] = 2.85
    option['internal_geometry']['parameters']['groove_radius'] = 2.9925
    option['internal_geometry']['parameters']['inner_shoulder'] = 10.483
    option['internal_geometry']['parameters']['outer_shoulder'] = 14.017
    option['internal_geometry']['parameters']['cage_half_width'] = 1.5675000000000001
    option['internal_geometry']['parameters']['cage_low'] = 2.7075
    option['internal_geometry']['parameters']['cage_high'] = 3.2775
    option['internal_geometry']['parameters']['window_radius'] = 1.3679999999999999
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.07125000000000001
    option['internal_geometry']['contact_angle_authority'] = 'selected_catalogue_convention'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '104'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_5300_series_5301_size_12_mm_id_37_mm_od_19.05_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://www.rbibearing.com/products/ball-bearings/5300-series/',
     'https://www.nskamericas.com/tools-resources/abc-bearings/angular-contact-ball-bearings/']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # 5302: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5300_series_5302_size_15_mm_id_42_mm_od_19_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5300_series_5302_size_15_mm_id_42_mm_od_19_mm_depth'
    option['size'] = '5302'
    option['series'] = '5300'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 15.0
    option['dimensions']['outside'] = 42.0
    option['dimensions']['width'] = 19.0
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 22
    option['internal_geometry']['balls_per_row'] = 11
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 15.0
    option['internal_geometry']['parameters']['outside'] = 42.0
    option['internal_geometry']['parameters']['width'] = 19.0
    option['internal_geometry']['parameters']['edge'] = 0.8099999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 14.25
    option['internal_geometry']['parameters']['ball_radius'] = 2.85
    option['internal_geometry']['parameters']['groove_radius'] = 2.9925
    option['internal_geometry']['parameters']['inner_shoulder'] = 12.483
    option['internal_geometry']['parameters']['outer_shoulder'] = 16.017
    option['internal_geometry']['parameters']['cage_half_width'] = 1.5675000000000001
    option['internal_geometry']['parameters']['cage_low'] = 2.7075
    option['internal_geometry']['parameters']['cage_high'] = 3.2775
    option['internal_geometry']['parameters']['window_radius'] = 1.3679999999999999
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.07125000000000001
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '132'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_5300_series_5302_size_15_mm_id_42_mm_od_19.05_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # 5303: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5300_series_5303_size_17_mm_id_47_mm_od_22.2_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5300_series_5303_size_17_mm_id_47_mm_od_22_2_mm_depth'
    option['size'] = '5303'
    option['series'] = '5300'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 17.0
    option['dimensions']['outside'] = 47.0
    option['dimensions']['width'] = 22.2
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 22
    option['internal_geometry']['balls_per_row'] = 11
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 17.0
    option['internal_geometry']['parameters']['outside'] = 47.0
    option['internal_geometry']['parameters']['width'] = 22.2
    option['internal_geometry']['parameters']['edge'] = 0.8999999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 16.0
    option['internal_geometry']['parameters']['ball_radius'] = 3.3299999999999996
    option['internal_geometry']['parameters']['groove_radius'] = 3.4964999999999997
    option['internal_geometry']['parameters']['inner_shoulder'] = 13.935400000000001
    option['internal_geometry']['parameters']['outer_shoulder'] = 18.0646
    option['internal_geometry']['parameters']['cage_half_width'] = 1.8315
    option['internal_geometry']['parameters']['cage_low'] = 3.1634999999999995
    option['internal_geometry']['parameters']['cage_high'] = 3.8294999999999995
    option['internal_geometry']['parameters']['window_radius'] = 1.5983999999999998
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.08324999999999999
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '195'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_5300_series_5303_size_17_mm_id_47_mm_od_22.22_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # 5304: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5300_series_5304_size_20_mm_id_52_mm_od_22.2_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5300_series_5304_size_20_mm_id_52_mm_od_22_2_mm_depth'
    option['size'] = '5304'
    option['series'] = '5300'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 20.0
    option['dimensions']['outside'] = 52.0
    option['dimensions']['width'] = 22.2
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 24
    option['internal_geometry']['balls_per_row'] = 12
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 20.0
    option['internal_geometry']['parameters']['outside'] = 52.0
    option['internal_geometry']['parameters']['width'] = 22.2
    option['internal_geometry']['parameters']['edge'] = 0.96
    option['internal_geometry']['parameters']['pitch_radius'] = 18.0
    option['internal_geometry']['parameters']['ball_radius'] = 3.3299999999999996
    option['internal_geometry']['parameters']['groove_radius'] = 3.4964999999999997
    option['internal_geometry']['parameters']['inner_shoulder'] = 15.935400000000001
    option['internal_geometry']['parameters']['outer_shoulder'] = 20.0646
    option['internal_geometry']['parameters']['cage_half_width'] = 1.8315
    option['internal_geometry']['parameters']['cage_low'] = 3.1634999999999995
    option['internal_geometry']['parameters']['cage_high'] = 3.8294999999999995
    option['internal_geometry']['parameters']['window_radius'] = 1.5983999999999998
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.08324999999999999
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '236'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_5300_series_5304_size_20_mm_id_52_mm_od_22.22_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # 5305: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5300_series_5305_size_25_mm_id_62_mm_od_25.4_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5300_series_5305_size_25_mm_id_62_mm_od_25_4_mm_depth'
    option['size'] = '5305'
    option['series'] = '5300'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 25.0
    option['dimensions']['outside'] = 62.0
    option['dimensions']['width'] = 25.4
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 26
    option['internal_geometry']['balls_per_row'] = 13
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 25.0
    option['internal_geometry']['parameters']['outside'] = 62.0
    option['internal_geometry']['parameters']['width'] = 25.4
    option['internal_geometry']['parameters']['edge'] = 1.1099999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 21.75
    option['internal_geometry']['parameters']['ball_radius'] = 3.8099999999999996
    option['internal_geometry']['parameters']['groove_radius'] = 4.0005
    option['internal_geometry']['parameters']['inner_shoulder'] = 19.3878
    option['internal_geometry']['parameters']['outer_shoulder'] = 24.1122
    option['internal_geometry']['parameters']['cage_half_width'] = 2.0955
    option['internal_geometry']['parameters']['cage_low'] = 3.6194999999999995
    option['internal_geometry']['parameters']['cage_high'] = 4.381499999999999
    option['internal_geometry']['parameters']['window_radius'] = 1.8287999999999998
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.09525
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '341'
    options.append(copy.deepcopy(option))

    # 5306: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5300_series_5306_size_30_mm_id_72_mm_od_30.2_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5300_series_5306_size_30_mm_id_72_mm_od_30_2_mm_depth'
    option['size'] = '5306'
    option['series'] = '5300'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 30.0
    option['dimensions']['outside'] = 72.0
    option['dimensions']['width'] = 30.2
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 24
    option['internal_geometry']['balls_per_row'] = 12
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 30.0
    option['internal_geometry']['parameters']['outside'] = 72.0
    option['internal_geometry']['parameters']['width'] = 30.2
    option['internal_geometry']['parameters']['edge'] = 1.26
    option['internal_geometry']['parameters']['pitch_radius'] = 25.5
    option['internal_geometry']['parameters']['ball_radius'] = 4.529999999999999
    option['internal_geometry']['parameters']['groove_radius'] = 4.7565
    option['internal_geometry']['parameters']['inner_shoulder'] = 22.6914
    option['internal_geometry']['parameters']['outer_shoulder'] = 28.3086
    option['internal_geometry']['parameters']['cage_half_width'] = 2.4915
    option['internal_geometry']['parameters']['cage_low'] = 4.303499999999999
    option['internal_geometry']['parameters']['cage_high'] = 5.2094999999999985
    option['internal_geometry']['parameters']['window_radius'] = 2.1743999999999994
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.11324999999999999
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '513'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_5300_series_5306_size_30_mm_id_72_mm_od_30.16_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # 5307: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5300_series_5307_size_35_mm_id_80_mm_od_34.9_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5300_series_5307_size_35_mm_id_80_mm_od_34_9_mm_depth'
    option['size'] = '5307'
    option['series'] = '5300'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 35.0
    option['dimensions']['outside'] = 80.0
    option['dimensions']['width'] = 34.9
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 24
    option['internal_geometry']['balls_per_row'] = 12
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 35.0
    option['internal_geometry']['parameters']['outside'] = 80.0
    option['internal_geometry']['parameters']['width'] = 34.9
    option['internal_geometry']['parameters']['edge'] = 1.3499999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 28.75
    option['internal_geometry']['parameters']['ball_radius'] = 5.234999999999999
    option['internal_geometry']['parameters']['groove_radius'] = 5.49675
    option['internal_geometry']['parameters']['inner_shoulder'] = 25.5043
    option['internal_geometry']['parameters']['outer_shoulder'] = 31.9957
    option['internal_geometry']['parameters']['cage_half_width'] = 2.87925
    option['internal_geometry']['parameters']['cage_low'] = 4.973249999999999
    option['internal_geometry']['parameters']['cage_high'] = 6.020249999999999
    option['internal_geometry']['parameters']['window_radius'] = 2.5127999999999995
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.130875
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '795'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_5300_series_5307_size_35_mm_id_80_mm_od_34.92_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # 5308: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5300_series_5308_size_40_mm_id_90_mm_od_36.5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5300_series_5308_size_40_mm_id_90_mm_od_36_5_mm_depth'
    option['size'] = '5308'
    option['series'] = '5300'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 40.0
    option['dimensions']['outside'] = 90.0
    option['dimensions']['width'] = 36.5
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 26
    option['internal_geometry']['balls_per_row'] = 13
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 40.0
    option['internal_geometry']['parameters']['outside'] = 90.0
    option['internal_geometry']['parameters']['width'] = 36.5
    option['internal_geometry']['parameters']['edge'] = 1.5
    option['internal_geometry']['parameters']['pitch_radius'] = 32.5
    option['internal_geometry']['parameters']['ball_radius'] = 5.475
    option['internal_geometry']['parameters']['groove_radius'] = 5.74875
    option['internal_geometry']['parameters']['inner_shoulder'] = 29.1055
    option['internal_geometry']['parameters']['outer_shoulder'] = 35.8945
    option['internal_geometry']['parameters']['cage_half_width'] = 3.01125
    option['internal_geometry']['parameters']['cage_low'] = 5.201249999999999
    option['internal_geometry']['parameters']['cage_high'] = 6.296249999999999
    option['internal_geometry']['parameters']['window_radius'] = 2.6279999999999997
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.136875
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1,049'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_5300_series_5308_size_40_mm_id_90_mm_od_36.51_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # 5309: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5300_series_5309_size_45_mm_id_100_mm_od_39.7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5300_series_5309_size_45_mm_id_100_mm_od_39_7_mm_depth'
    option['size'] = '5309'
    option['series'] = '5300'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 45.0
    option['dimensions']['outside'] = 100.0
    option['dimensions']['width'] = 39.7
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 28
    option['internal_geometry']['balls_per_row'] = 14
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 45.0
    option['internal_geometry']['parameters']['outside'] = 100.0
    option['internal_geometry']['parameters']['width'] = 39.7
    option['internal_geometry']['parameters']['edge'] = 1.65
    option['internal_geometry']['parameters']['pitch_radius'] = 36.25
    option['internal_geometry']['parameters']['ball_radius'] = 5.955
    option['internal_geometry']['parameters']['groove_radius'] = 6.252750000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 32.557900000000004
    option['internal_geometry']['parameters']['outer_shoulder'] = 39.942099999999996
    option['internal_geometry']['parameters']['cage_half_width'] = 3.27525
    option['internal_geometry']['parameters']['cage_low'] = 5.6572499999999994
    option['internal_geometry']['parameters']['cage_high'] = 6.848249999999999
    option['internal_geometry']['parameters']['window_radius'] = 2.8584
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.148875
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1,421'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_5300_series_5309_size_45_mm_id_100_mm_od_39.68_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # 5310: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5300_series_5310_size_50_mm_id_110_mm_od_44.4_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5300_series_5310_size_50_mm_id_110_mm_od_44_4_mm_depth'
    option['size'] = '5310'
    option['series'] = '5300'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 50.0
    option['dimensions']['outside'] = 110.0
    option['dimensions']['width'] = 44.4
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 26
    option['internal_geometry']['balls_per_row'] = 13
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 50.0
    option['internal_geometry']['parameters']['outside'] = 110.0
    option['internal_geometry']['parameters']['width'] = 44.4
    option['internal_geometry']['parameters']['edge'] = 1.7999999999999998
    option['internal_geometry']['parameters']['pitch_radius'] = 40.0
    option['internal_geometry']['parameters']['ball_radius'] = 6.659999999999999
    option['internal_geometry']['parameters']['groove_radius'] = 6.992999999999999
    option['internal_geometry']['parameters']['inner_shoulder'] = 35.8708
    option['internal_geometry']['parameters']['outer_shoulder'] = 44.1292
    option['internal_geometry']['parameters']['cage_half_width'] = 3.663
    option['internal_geometry']['parameters']['cage_low'] = 6.326999999999999
    option['internal_geometry']['parameters']['cage_high'] = 7.658999999999999
    option['internal_geometry']['parameters']['window_radius'] = 3.1967999999999996
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.16649999999999998
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1,930'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_5300_series_5310_size_50_mm_id_110_mm_od_44.45_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # 5311: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5300_series_5311_size_55_mm_id_120_mm_od_49.2_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5300_series_5311_size_55_mm_id_120_mm_od_49_2_mm_depth'
    option['size'] = '5311'
    option['series'] = '5300'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 55.0
    option['dimensions']['outside'] = 120.0
    option['dimensions']['width'] = 49.2
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 26
    option['internal_geometry']['balls_per_row'] = 13
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 55.0
    option['internal_geometry']['parameters']['outside'] = 120.0
    option['internal_geometry']['parameters']['width'] = 49.2
    option['internal_geometry']['parameters']['edge'] = 1.95
    option['internal_geometry']['parameters']['pitch_radius'] = 43.75
    option['internal_geometry']['parameters']['ball_radius'] = 7.38
    option['internal_geometry']['parameters']['groove_radius'] = 7.7490000000000006
    option['internal_geometry']['parameters']['inner_shoulder'] = 39.1744
    option['internal_geometry']['parameters']['outer_shoulder'] = 48.3256
    option['internal_geometry']['parameters']['cage_half_width'] = 4.059
    option['internal_geometry']['parameters']['cage_low'] = 7.010999999999999
    option['internal_geometry']['parameters']['cage_high'] = 8.487
    option['internal_geometry']['parameters']['window_radius'] = 3.5423999999999998
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.1845
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '2,297'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_5300_series_5311_size_55_mm_id_120_mm_od_49.21_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # 5312: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5300_series_5312_size_60_mm_id_130_mm_od_54_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5300_series_5312_size_60_mm_id_130_mm_od_54_mm_depth'
    option['size'] = '5312'
    option['series'] = '5300'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 60.0
    option['dimensions']['outside'] = 130.0
    option['dimensions']['width'] = 54.0
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 26
    option['internal_geometry']['balls_per_row'] = 13
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 60.0
    option['internal_geometry']['parameters']['outside'] = 130.0
    option['internal_geometry']['parameters']['width'] = 54.0
    option['internal_geometry']['parameters']['edge'] = 2.1
    option['internal_geometry']['parameters']['pitch_radius'] = 47.5
    option['internal_geometry']['parameters']['ball_radius'] = 8.1
    option['internal_geometry']['parameters']['groove_radius'] = 8.505
    option['internal_geometry']['parameters']['inner_shoulder'] = 42.478
    option['internal_geometry']['parameters']['outer_shoulder'] = 52.522
    option['internal_geometry']['parameters']['cage_half_width'] = 4.455
    option['internal_geometry']['parameters']['cage_low'] = 7.694999999999999
    option['internal_geometry']['parameters']['cage_high'] = 9.315
    option['internal_geometry']['parameters']['window_radius'] = 3.888
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.2025
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '3,160'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_5300_series_5312_size_60_mm_id_130_mm_od_53.97_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # 5313: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5300_series_5313_size_65_mm_id_140_mm_od_58.7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5300_series_5313_size_65_mm_id_140_mm_od_58_7_mm_depth'
    option['size'] = '5313'
    option['series'] = '5300'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 65.0
    option['dimensions']['outside'] = 140.0
    option['dimensions']['width'] = 58.7
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 26
    option['internal_geometry']['balls_per_row'] = 13
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 65.0
    option['internal_geometry']['parameters']['outside'] = 140.0
    option['internal_geometry']['parameters']['width'] = 58.7
    option['internal_geometry']['parameters']['edge'] = 2.25
    option['internal_geometry']['parameters']['pitch_radius'] = 51.25
    option['internal_geometry']['parameters']['ball_radius'] = 8.805
    option['internal_geometry']['parameters']['groove_radius'] = 9.24525
    option['internal_geometry']['parameters']['inner_shoulder'] = 45.7909
    option['internal_geometry']['parameters']['outer_shoulder'] = 56.7091
    option['internal_geometry']['parameters']['cage_half_width'] = 4.8427500000000006
    option['internal_geometry']['parameters']['cage_low'] = 8.364749999999999
    option['internal_geometry']['parameters']['cage_high'] = 10.125749999999998
    option['internal_geometry']['parameters']['window_radius'] = 4.2264
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.22012500000000002
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '3,909'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_5300_series_5313_size_65_mm_id_140_mm_od_58.73_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # 5314: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5300_series_5314_size_70_mm_id_150_mm_od_63.5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5300_series_5314_size_70_mm_id_150_mm_od_63_5_mm_depth'
    option['size'] = '5314'
    option['series'] = '5300'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 70.0
    option['dimensions']['outside'] = 150.0
    option['dimensions']['width'] = 63.5
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Bearing-and-Linear-Replacement-Guide.pdf']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 26
    option['internal_geometry']['balls_per_row'] = 13
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 70.0
    option['internal_geometry']['parameters']['outside'] = 150.0
    option['internal_geometry']['parameters']['width'] = 63.5
    option['internal_geometry']['parameters']['edge'] = 2.4
    option['internal_geometry']['parameters']['pitch_radius'] = 55.0
    option['internal_geometry']['parameters']['ball_radius'] = 9.525
    option['internal_geometry']['parameters']['groove_radius'] = 10.00125
    option['internal_geometry']['parameters']['inner_shoulder'] = 49.0945
    option['internal_geometry']['parameters']['outer_shoulder'] = 60.9055
    option['internal_geometry']['parameters']['cage_half_width'] = 5.2387500000000005
    option['internal_geometry']['parameters']['cage_low'] = 9.04875
    option['internal_geometry']['parameters']['cage_high'] = 10.95375
    option['internal_geometry']['parameters']['window_radius'] = 4.572
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.23812500000000003
    option['internal_geometry']['contact_angle_authority'] = 'manufacturer_family'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '4,903'
    options.append(copy.deepcopy(option))

    # 5315: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5300_series_5315_size_75_mm_id_160_mm_od_68.3_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5300_series_5315_size_75_mm_id_160_mm_od_68_3_mm_depth'
    option['size'] = '5315'
    option['series'] = '5300'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 75.0
    option['dimensions']['outside'] = 160.0
    option['dimensions']['width'] = 68.3
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.rbibearing.com/products/ball-bearings/5300-series/',
     'https://www.nskamericas.com/tools-resources/abc-bearings/angular-contact-ball-bearings/']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 26
    option['internal_geometry']['balls_per_row'] = 13
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 75.0
    option['internal_geometry']['parameters']['outside'] = 160.0
    option['internal_geometry']['parameters']['width'] = 68.3
    option['internal_geometry']['parameters']['edge'] = 2.55
    option['internal_geometry']['parameters']['pitch_radius'] = 58.75
    option['internal_geometry']['parameters']['ball_radius'] = 10.245
    option['internal_geometry']['parameters']['groove_radius'] = 10.757249999999999
    option['internal_geometry']['parameters']['inner_shoulder'] = 52.3981
    option['internal_geometry']['parameters']['outer_shoulder'] = 65.1019
    option['internal_geometry']['parameters']['cage_half_width'] = 5.63475
    option['internal_geometry']['parameters']['cage_low'] = 9.73275
    option['internal_geometry']['parameters']['cage_high'] = 11.781749999999999
    option['internal_geometry']['parameters']['window_radius'] = 4.917599999999999
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.256125
    option['internal_geometry']['contact_angle_authority'] = 'selected_catalogue_convention'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '5,493'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_5300_series_5315_size_75_mm_id_160_mm_od_68.26_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://www.rbibearing.com/products/ball-bearings/5300-series/',
     'https://www.nskamericas.com/tools-resources/abc-bearings/angular-contact-ball-bearings/']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # 5316: double row angular contact
    option = {}
    option['oomp_id'] = 'hardware_bearing_5300_series_5316_size_80_mm_id_170_mm_od_68.3_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_5300_series_5316_size_80_mm_id_170_mm_od_68_3_mm_depth'
    option['size'] = '5316'
    option['series'] = '5300'
    option['family'] = 'double_row_angular_contact'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 80.0
    option['dimensions']['outside'] = 170.0
    option['dimensions']['width'] = 68.3
    option['dimensions']['contact_angle_deg'] = 25.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.rbibearing.com/products/ball-bearings/5300-series/',
     'https://www.nskamericas.com/tools-resources/abc-bearings/angular-contact-ball-bearings/']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'double_row_angular_contact'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 28
    option['internal_geometry']['balls_per_row'] = 14
    option['internal_geometry']['row_count'] = 2
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 80.0
    option['internal_geometry']['parameters']['outside'] = 170.0
    option['internal_geometry']['parameters']['width'] = 68.3
    option['internal_geometry']['parameters']['edge'] = 2.6999999999999997
    option['internal_geometry']['parameters']['pitch_radius'] = 62.5
    option['internal_geometry']['parameters']['ball_radius'] = 10.245
    option['internal_geometry']['parameters']['groove_radius'] = 10.757249999999999
    option['internal_geometry']['parameters']['inner_shoulder'] = 56.1481
    option['internal_geometry']['parameters']['outer_shoulder'] = 68.8519
    option['internal_geometry']['parameters']['cage_half_width'] = 5.63475
    option['internal_geometry']['parameters']['cage_low'] = 9.73275
    option['internal_geometry']['parameters']['cage_high'] = 11.781749999999999
    option['internal_geometry']['parameters']['window_radius'] = 4.917599999999999
    option['internal_geometry']['parameters']['contact_angle_deg'] = 25.0
    option['internal_geometry']['parameters']['contact_offset'] = 0.256125
    option['internal_geometry']['contact_angle_authority'] = 'selected_catalogue_convention'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '6,810'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_5300_series_5316_size_80_mm_id_170_mm_od_68.26_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://www.rbibearing.com/products/ball-bearings/5300-series/',
     'https://www.nskamericas.com/tools-resources/abc-bearings/angular-contact-ball-bearings/']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # 6000: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6000_series_6000_size_10_mm_id_26_mm_od_8_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6000_series_6000_size_10_mm_id_26_mm_od_8_mm_depth'
    option['size'] = '6000'
    option['series'] = '6000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 10.0
    option['dimensions']['outside'] = 26.0
    option['dimensions']['width'] = 8.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 9
    option['internal_geometry']['balls_per_row'] = 9
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 10.0
    option['internal_geometry']['parameters']['outside'] = 26.0
    option['internal_geometry']['parameters']['width'] = 8.0
    option['internal_geometry']['parameters']['edge'] = 0.48
    option['internal_geometry']['parameters']['pitch_radius'] = 9.0
    option['internal_geometry']['parameters']['ball_radius'] = 2.24
    option['internal_geometry']['parameters']['groove_radius'] = 2.2960000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 7.6112
    option['internal_geometry']['parameters']['outer_shoulder'] = 10.3888
    option['internal_geometry']['parameters']['cage_half_width'] = 1.2320000000000002
    option['internal_geometry']['parameters']['cage_low'] = 2.128
    option['internal_geometry']['parameters']['cage_high'] = 2.576
    option['internal_geometry']['parameters']['window_radius'] = 1.0752000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '19'
    options.append(copy.deepcopy(option))

    # 6001: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6000_series_6001_size_12_mm_id_28_mm_od_8_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6000_series_6001_size_12_mm_id_28_mm_od_8_mm_depth'
    option['size'] = '6001'
    option['series'] = '6000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 12.0
    option['dimensions']['outside'] = 28.0
    option['dimensions']['width'] = 8.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 10
    option['internal_geometry']['balls_per_row'] = 10
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 12.0
    option['internal_geometry']['parameters']['outside'] = 28.0
    option['internal_geometry']['parameters']['width'] = 8.0
    option['internal_geometry']['parameters']['edge'] = 0.48
    option['internal_geometry']['parameters']['pitch_radius'] = 10.0
    option['internal_geometry']['parameters']['ball_radius'] = 2.24
    option['internal_geometry']['parameters']['groove_radius'] = 2.2960000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 8.6112
    option['internal_geometry']['parameters']['outer_shoulder'] = 11.3888
    option['internal_geometry']['parameters']['cage_half_width'] = 1.2320000000000002
    option['internal_geometry']['parameters']['cage_low'] = 2.128
    option['internal_geometry']['parameters']['cage_high'] = 2.576
    option['internal_geometry']['parameters']['window_radius'] = 1.0752000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '22'
    options.append(copy.deepcopy(option))

    # 6002: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6000_series_6002_size_15_mm_id_32_mm_od_9_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6000_series_6002_size_15_mm_id_32_mm_od_9_mm_depth'
    option['size'] = '6002'
    option['series'] = '6000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 15.0
    option['dimensions']['outside'] = 32.0
    option['dimensions']['width'] = 9.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 11
    option['internal_geometry']['balls_per_row'] = 11
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 15.0
    option['internal_geometry']['parameters']['outside'] = 32.0
    option['internal_geometry']['parameters']['width'] = 9.0
    option['internal_geometry']['parameters']['edge'] = 0.51
    option['internal_geometry']['parameters']['pitch_radius'] = 11.75
    option['internal_geometry']['parameters']['ball_radius'] = 2.3800000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 2.4395000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 10.2744
    option['internal_geometry']['parameters']['outer_shoulder'] = 13.2256
    option['internal_geometry']['parameters']['cage_half_width'] = 1.3090000000000004
    option['internal_geometry']['parameters']['cage_low'] = 2.261
    option['internal_geometry']['parameters']['cage_high'] = 2.737
    option['internal_geometry']['parameters']['window_radius'] = 1.1424
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '31'
    options.append(copy.deepcopy(option))

    # 6003: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6000_series_6003_size_17_mm_id_35_mm_od_10_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6000_series_6003_size_17_mm_id_35_mm_od_10_mm_depth'
    option['size'] = '6003'
    option['series'] = '6000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 17.0
    option['dimensions']['outside'] = 35.0
    option['dimensions']['width'] = 10.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 11
    option['internal_geometry']['balls_per_row'] = 11
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 17.0
    option['internal_geometry']['parameters']['outside'] = 35.0
    option['internal_geometry']['parameters']['width'] = 10.0
    option['internal_geometry']['parameters']['edge'] = 0.54
    option['internal_geometry']['parameters']['pitch_radius'] = 13.0
    option['internal_geometry']['parameters']['ball_radius'] = 2.5200000000000005
    option['internal_geometry']['parameters']['groove_radius'] = 2.5830000000000006
    option['internal_geometry']['parameters']['inner_shoulder'] = 11.4376
    option['internal_geometry']['parameters']['outer_shoulder'] = 14.5624
    option['internal_geometry']['parameters']['cage_half_width'] = 1.3860000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.394
    option['internal_geometry']['parameters']['cage_high'] = 2.898
    option['internal_geometry']['parameters']['window_radius'] = 1.2096000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '40'
    options.append(copy.deepcopy(option))

    # 6004: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6000_series_6004_size_20_mm_id_42_mm_od_12_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6000_series_6004_size_20_mm_id_42_mm_od_12_mm_depth'
    option['size'] = '6004'
    option['series'] = '6000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 20.0
    option['dimensions']['outside'] = 42.0
    option['dimensions']['width'] = 12.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 11
    option['internal_geometry']['balls_per_row'] = 11
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 20.0
    option['internal_geometry']['parameters']['outside'] = 42.0
    option['internal_geometry']['parameters']['width'] = 12.0
    option['internal_geometry']['parameters']['edge'] = 0.6599999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 15.5
    option['internal_geometry']['parameters']['ball_radius'] = 3.08
    option['internal_geometry']['parameters']['groove_radius'] = 3.157
    option['internal_geometry']['parameters']['inner_shoulder'] = 13.5904
    option['internal_geometry']['parameters']['outer_shoulder'] = 17.4096
    option['internal_geometry']['parameters']['cage_half_width'] = 1.6940000000000002
    option['internal_geometry']['parameters']['cage_low'] = 2.9259999999999997
    option['internal_geometry']['parameters']['cage_high'] = 3.542
    option['internal_geometry']['parameters']['window_radius'] = 1.4784
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '68'
    options.append(copy.deepcopy(option))

    # 6005: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6000_series_6005_size_25_mm_id_47_mm_od_12_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6000_series_6005_size_25_mm_id_47_mm_od_12_mm_depth'
    option['size'] = '6005'
    option['series'] = '6000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 25.0
    option['dimensions']['outside'] = 47.0
    option['dimensions']['width'] = 12.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 13
    option['internal_geometry']['balls_per_row'] = 13
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 25.0
    option['internal_geometry']['parameters']['outside'] = 47.0
    option['internal_geometry']['parameters']['width'] = 12.0
    option['internal_geometry']['parameters']['edge'] = 0.6599999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 18.0
    option['internal_geometry']['parameters']['ball_radius'] = 3.08
    option['internal_geometry']['parameters']['groove_radius'] = 3.157
    option['internal_geometry']['parameters']['inner_shoulder'] = 16.0904
    option['internal_geometry']['parameters']['outer_shoulder'] = 19.9096
    option['internal_geometry']['parameters']['cage_half_width'] = 1.6940000000000002
    option['internal_geometry']['parameters']['cage_low'] = 2.9259999999999997
    option['internal_geometry']['parameters']['cage_high'] = 3.542
    option['internal_geometry']['parameters']['window_radius'] = 1.4784
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '78'
    options.append(copy.deepcopy(option))

    # 6006: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6000_series_6006_size_30_mm_id_55_mm_od_13_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6000_series_6006_size_30_mm_id_55_mm_od_13_mm_depth'
    option['size'] = '6006'
    option['series'] = '6000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 30.0
    option['dimensions']['outside'] = 55.0
    option['dimensions']['width'] = 13.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 14
    option['internal_geometry']['balls_per_row'] = 14
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 30.0
    option['internal_geometry']['parameters']['outside'] = 55.0
    option['internal_geometry']['parameters']['width'] = 13.0
    option['internal_geometry']['parameters']['edge'] = 0.75
    option['internal_geometry']['parameters']['pitch_radius'] = 21.25
    option['internal_geometry']['parameters']['ball_radius'] = 3.5000000000000004
    option['internal_geometry']['parameters']['groove_radius'] = 3.5875000000000004
    option['internal_geometry']['parameters']['inner_shoulder'] = 19.08
    option['internal_geometry']['parameters']['outer_shoulder'] = 23.42
    option['internal_geometry']['parameters']['cage_half_width'] = 1.9250000000000005
    option['internal_geometry']['parameters']['cage_low'] = 3.325
    option['internal_geometry']['parameters']['cage_high'] = 4.025
    option['internal_geometry']['parameters']['window_radius'] = 1.6800000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '110'
    options.append(copy.deepcopy(option))

    # 6007: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6000_series_6007_size_35_mm_id_62_mm_od_14_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6000_series_6007_size_35_mm_id_62_mm_od_14_mm_depth'
    option['size'] = '6007'
    option['series'] = '6000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 35.0
    option['dimensions']['outside'] = 62.0
    option['dimensions']['width'] = 14.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 14
    option['internal_geometry']['balls_per_row'] = 14
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 35.0
    option['internal_geometry']['parameters']['outside'] = 62.0
    option['internal_geometry']['parameters']['width'] = 14.0
    option['internal_geometry']['parameters']['edge'] = 0.8099999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 24.25
    option['internal_geometry']['parameters']['ball_radius'] = 3.7800000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 3.8745000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 21.906399999999998
    option['internal_geometry']['parameters']['outer_shoulder'] = 26.593600000000002
    option['internal_geometry']['parameters']['cage_half_width'] = 2.079
    option['internal_geometry']['parameters']['cage_low'] = 3.591
    option['internal_geometry']['parameters']['cage_high'] = 4.3469999999999995
    option['internal_geometry']['parameters']['window_radius'] = 1.8144
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '15'
    options.append(copy.deepcopy(option))

    # 6008: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6000_series_6008_size_40_mm_id_68_mm_od_15_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6000_series_6008_size_40_mm_id_68_mm_od_15_mm_depth'
    option['size'] = '6008'
    option['series'] = '6000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 40.0
    option['dimensions']['outside'] = 68.0
    option['dimensions']['width'] = 15.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 15
    option['internal_geometry']['balls_per_row'] = 15
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 40.0
    option['internal_geometry']['parameters']['outside'] = 68.0
    option['internal_geometry']['parameters']['width'] = 15.0
    option['internal_geometry']['parameters']['edge'] = 0.84
    option['internal_geometry']['parameters']['pitch_radius'] = 27.0
    option['internal_geometry']['parameters']['ball_radius'] = 3.9200000000000004
    option['internal_geometry']['parameters']['groove_radius'] = 4.018000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 24.5696
    option['internal_geometry']['parameters']['outer_shoulder'] = 29.4304
    option['internal_geometry']['parameters']['cage_half_width'] = 2.1560000000000006
    option['internal_geometry']['parameters']['cage_low'] = 3.724
    option['internal_geometry']['parameters']['cage_high'] = 4.508
    option['internal_geometry']['parameters']['window_radius'] = 1.8816000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '185'
    options.append(copy.deepcopy(option))

    # 6009: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6000_series_6009_size_45_mm_id_75_mm_od_16_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6000_series_6009_size_45_mm_id_75_mm_od_16_mm_depth'
    option['size'] = '6009'
    option['series'] = '6000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 45.0
    option['dimensions']['outside'] = 75.0
    option['dimensions']['width'] = 16.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 16
    option['internal_geometry']['balls_per_row'] = 16
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 45.0
    option['internal_geometry']['parameters']['outside'] = 75.0
    option['internal_geometry']['parameters']['width'] = 16.0
    option['internal_geometry']['parameters']['edge'] = 0.8999999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 30.0
    option['internal_geometry']['parameters']['ball_radius'] = 4.2
    option['internal_geometry']['parameters']['groove_radius'] = 4.305000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 27.396
    option['internal_geometry']['parameters']['outer_shoulder'] = 32.604
    option['internal_geometry']['parameters']['cage_half_width'] = 2.3100000000000005
    option['internal_geometry']['parameters']['cage_low'] = 3.9899999999999998
    option['internal_geometry']['parameters']['cage_high'] = 4.83
    option['internal_geometry']['parameters']['window_radius'] = 2.016
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '230'
    options.append(copy.deepcopy(option))

    # 6010: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6000_series_6010_size_50_mm_id_80_mm_od_16_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6000_series_6010_size_50_mm_id_80_mm_od_16_mm_depth'
    option['size'] = '6010'
    option['series'] = '6000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 50.0
    option['dimensions']['outside'] = 80.0
    option['dimensions']['width'] = 16.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 17
    option['internal_geometry']['balls_per_row'] = 17
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 50.0
    option['internal_geometry']['parameters']['outside'] = 80.0
    option['internal_geometry']['parameters']['width'] = 16.0
    option['internal_geometry']['parameters']['edge'] = 0.8999999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 32.5
    option['internal_geometry']['parameters']['ball_radius'] = 4.2
    option['internal_geometry']['parameters']['groove_radius'] = 4.305000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 29.896
    option['internal_geometry']['parameters']['outer_shoulder'] = 35.104
    option['internal_geometry']['parameters']['cage_half_width'] = 2.3100000000000005
    option['internal_geometry']['parameters']['cage_low'] = 3.9899999999999998
    option['internal_geometry']['parameters']['cage_high'] = 4.83
    option['internal_geometry']['parameters']['window_radius'] = 2.016
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '26'
    options.append(copy.deepcopy(option))

    # 6011: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6000_series_6011_size_55_mm_id_90_mm_od_18_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6000_series_6011_size_55_mm_id_90_mm_od_18_mm_depth'
    option['size'] = '6011'
    option['series'] = '6000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 55.0
    option['dimensions']['outside'] = 90.0
    option['dimensions']['width'] = 18.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 17
    option['internal_geometry']['balls_per_row'] = 17
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 55.0
    option['internal_geometry']['parameters']['outside'] = 90.0
    option['internal_geometry']['parameters']['width'] = 18.0
    option['internal_geometry']['parameters']['edge'] = 1.05
    option['internal_geometry']['parameters']['pitch_radius'] = 36.25
    option['internal_geometry']['parameters']['ball_radius'] = 4.9
    option['internal_geometry']['parameters']['groove_radius'] = 5.0225
    option['internal_geometry']['parameters']['inner_shoulder'] = 33.212
    option['internal_geometry']['parameters']['outer_shoulder'] = 39.288
    option['internal_geometry']['parameters']['cage_half_width'] = 2.6950000000000003
    option['internal_geometry']['parameters']['cage_low'] = 4.655
    option['internal_geometry']['parameters']['cage_high'] = 5.635
    option['internal_geometry']['parameters']['window_radius'] = 2.352
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '36'
    options.append(copy.deepcopy(option))

    # 6012: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6000_series_6012_size_60_mm_id_95_mm_od_18_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6000_series_6012_size_60_mm_id_95_mm_od_18_mm_depth'
    option['size'] = '6012'
    option['series'] = '6000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 60.0
    option['dimensions']['outside'] = 95.0
    option['dimensions']['width'] = 18.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 18
    option['internal_geometry']['balls_per_row'] = 18
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 60.0
    option['internal_geometry']['parameters']['outside'] = 95.0
    option['internal_geometry']['parameters']['width'] = 18.0
    option['internal_geometry']['parameters']['edge'] = 1.05
    option['internal_geometry']['parameters']['pitch_radius'] = 38.75
    option['internal_geometry']['parameters']['ball_radius'] = 4.9
    option['internal_geometry']['parameters']['groove_radius'] = 5.0225
    option['internal_geometry']['parameters']['inner_shoulder'] = 35.712
    option['internal_geometry']['parameters']['outer_shoulder'] = 41.788
    option['internal_geometry']['parameters']['cage_half_width'] = 2.6950000000000003
    option['internal_geometry']['parameters']['cage_low'] = 4.655
    option['internal_geometry']['parameters']['cage_high'] = 5.635
    option['internal_geometry']['parameters']['window_radius'] = 2.352
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '38'
    options.append(copy.deepcopy(option))

    # 6013: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6000_series_6013_size_65_mm_id_100_mm_od_18_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6000_series_6013_size_65_mm_id_100_mm_od_18_mm_depth'
    option['size'] = '6013'
    option['series'] = '6000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 65.0
    option['dimensions']['outside'] = 100.0
    option['dimensions']['width'] = 18.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 19
    option['internal_geometry']['balls_per_row'] = 19
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 65.0
    option['internal_geometry']['parameters']['outside'] = 100.0
    option['internal_geometry']['parameters']['width'] = 18.0
    option['internal_geometry']['parameters']['edge'] = 1.05
    option['internal_geometry']['parameters']['pitch_radius'] = 41.25
    option['internal_geometry']['parameters']['ball_radius'] = 4.9
    option['internal_geometry']['parameters']['groove_radius'] = 5.0225
    option['internal_geometry']['parameters']['inner_shoulder'] = 38.212
    option['internal_geometry']['parameters']['outer_shoulder'] = 44.288
    option['internal_geometry']['parameters']['cage_half_width'] = 2.6950000000000003
    option['internal_geometry']['parameters']['cage_low'] = 4.655
    option['internal_geometry']['parameters']['cage_high'] = 5.635
    option['internal_geometry']['parameters']['window_radius'] = 2.352
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '434'
    options.append(copy.deepcopy(option))

    # 6014: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6000_series_6014_size_70_mm_id_110_mm_od_20_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6000_series_6014_size_70_mm_id_110_mm_od_20_mm_depth'
    option['size'] = '6014'
    option['series'] = '6000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 70.0
    option['dimensions']['outside'] = 110.0
    option['dimensions']['width'] = 20.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 18
    option['internal_geometry']['balls_per_row'] = 18
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 70.0
    option['internal_geometry']['parameters']['outside'] = 110.0
    option['internal_geometry']['parameters']['width'] = 20.0
    option['internal_geometry']['parameters']['edge'] = 1.2
    option['internal_geometry']['parameters']['pitch_radius'] = 45.0
    option['internal_geometry']['parameters']['ball_radius'] = 5.6000000000000005
    option['internal_geometry']['parameters']['groove_radius'] = 5.74
    option['internal_geometry']['parameters']['inner_shoulder'] = 41.528
    option['internal_geometry']['parameters']['outer_shoulder'] = 48.472
    option['internal_geometry']['parameters']['cage_half_width'] = 3.0800000000000005
    option['internal_geometry']['parameters']['cage_low'] = 5.32
    option['internal_geometry']['parameters']['cage_high'] = 6.44
    option['internal_geometry']['parameters']['window_radius'] = 2.688
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '601'
    options.append(copy.deepcopy(option))

    # 6015: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6000_series_6015_size_75_mm_id_115_mm_od_20_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6000_series_6015_size_75_mm_id_115_mm_od_20_mm_depth'
    option['size'] = '6015'
    option['series'] = '6000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 75.0
    option['dimensions']['outside'] = 115.0
    option['dimensions']['width'] = 20.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 19
    option['internal_geometry']['balls_per_row'] = 19
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 75.0
    option['internal_geometry']['parameters']['outside'] = 115.0
    option['internal_geometry']['parameters']['width'] = 20.0
    option['internal_geometry']['parameters']['edge'] = 1.2
    option['internal_geometry']['parameters']['pitch_radius'] = 47.5
    option['internal_geometry']['parameters']['ball_radius'] = 5.6000000000000005
    option['internal_geometry']['parameters']['groove_radius'] = 5.74
    option['internal_geometry']['parameters']['inner_shoulder'] = 44.028
    option['internal_geometry']['parameters']['outer_shoulder'] = 50.972
    option['internal_geometry']['parameters']['cage_half_width'] = 3.0800000000000005
    option['internal_geometry']['parameters']['cage_low'] = 5.32
    option['internal_geometry']['parameters']['cage_high'] = 6.44
    option['internal_geometry']['parameters']['window_radius'] = 2.688
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '637'
    options.append(copy.deepcopy(option))

    # 6016: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6000_series_6016_size_80_mm_id_125_mm_od_22_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6000_series_6016_size_80_mm_id_125_mm_od_22_mm_depth'
    option['size'] = '6016'
    option['series'] = '6000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 80.0
    option['dimensions']['outside'] = 125.0
    option['dimensions']['width'] = 22.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 19
    option['internal_geometry']['balls_per_row'] = 19
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 80.0
    option['internal_geometry']['parameters']['outside'] = 125.0
    option['internal_geometry']['parameters']['width'] = 22.0
    option['internal_geometry']['parameters']['edge'] = 1.3199999999999998
    option['internal_geometry']['parameters']['pitch_radius'] = 51.25
    option['internal_geometry']['parameters']['ball_radius'] = 6.16
    option['internal_geometry']['parameters']['groove_radius'] = 6.314
    option['internal_geometry']['parameters']['inner_shoulder'] = 47.4308
    option['internal_geometry']['parameters']['outer_shoulder'] = 55.0692
    option['internal_geometry']['parameters']['cage_half_width'] = 3.3880000000000003
    option['internal_geometry']['parameters']['cage_low'] = 5.851999999999999
    option['internal_geometry']['parameters']['cage_high'] = 7.084
    option['internal_geometry']['parameters']['window_radius'] = 2.9568
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '849'
    options.append(copy.deepcopy(option))

    # 6017: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6000_series_6017_size_85_mm_id_130_mm_od_22_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6000_series_6017_size_85_mm_id_130_mm_od_22_mm_depth'
    option['size'] = '6017'
    option['series'] = '6000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 85.0
    option['dimensions']['outside'] = 130.0
    option['dimensions']['width'] = 22.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 20
    option['internal_geometry']['balls_per_row'] = 20
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 85.0
    option['internal_geometry']['parameters']['outside'] = 130.0
    option['internal_geometry']['parameters']['width'] = 22.0
    option['internal_geometry']['parameters']['edge'] = 1.3199999999999998
    option['internal_geometry']['parameters']['pitch_radius'] = 53.75
    option['internal_geometry']['parameters']['ball_radius'] = 6.16
    option['internal_geometry']['parameters']['groove_radius'] = 6.314
    option['internal_geometry']['parameters']['inner_shoulder'] = 49.9308
    option['internal_geometry']['parameters']['outer_shoulder'] = 57.5692
    option['internal_geometry']['parameters']['cage_half_width'] = 3.3880000000000003
    option['internal_geometry']['parameters']['cage_low'] = 5.851999999999999
    option['internal_geometry']['parameters']['cage_high'] = 7.084
    option['internal_geometry']['parameters']['window_radius'] = 2.9568
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '889'
    options.append(copy.deepcopy(option))

    # 6018: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6000_series_6018_size_90_mm_id_140_mm_od_24_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6000_series_6018_size_90_mm_id_140_mm_od_24_mm_depth'
    option['size'] = '6018'
    option['series'] = '6000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 90.0
    option['dimensions']['outside'] = 140.0
    option['dimensions']['width'] = 24.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 19
    option['internal_geometry']['balls_per_row'] = 19
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 90.0
    option['internal_geometry']['parameters']['outside'] = 140.0
    option['internal_geometry']['parameters']['width'] = 24.0
    option['internal_geometry']['parameters']['edge'] = 1.44
    option['internal_geometry']['parameters']['pitch_radius'] = 57.5
    option['internal_geometry']['parameters']['ball_radius'] = 6.720000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 6.888000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 53.3336
    option['internal_geometry']['parameters']['outer_shoulder'] = 61.6664
    option['internal_geometry']['parameters']['cage_half_width'] = 3.6960000000000006
    option['internal_geometry']['parameters']['cage_low'] = 6.384
    option['internal_geometry']['parameters']['cage_high'] = 7.728
    option['internal_geometry']['parameters']['window_radius'] = 3.2256
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1,159'
    options.append(copy.deepcopy(option))

    # 6019: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6000_series_6019_size_95_mm_id_145_mm_od_24_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6000_series_6019_size_95_mm_id_145_mm_od_24_mm_depth'
    option['size'] = '6019'
    option['series'] = '6000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 95.0
    option['dimensions']['outside'] = 145.0
    option['dimensions']['width'] = 24.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 20
    option['internal_geometry']['balls_per_row'] = 20
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 95.0
    option['internal_geometry']['parameters']['outside'] = 145.0
    option['internal_geometry']['parameters']['width'] = 24.0
    option['internal_geometry']['parameters']['edge'] = 1.44
    option['internal_geometry']['parameters']['pitch_radius'] = 60.0
    option['internal_geometry']['parameters']['ball_radius'] = 6.720000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 6.888000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 55.8336
    option['internal_geometry']['parameters']['outer_shoulder'] = 64.1664
    option['internal_geometry']['parameters']['cage_half_width'] = 3.6960000000000006
    option['internal_geometry']['parameters']['cage_low'] = 6.384
    option['internal_geometry']['parameters']['cage_high'] = 7.728
    option['internal_geometry']['parameters']['window_radius'] = 3.2256
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1,209'
    options.append(copy.deepcopy(option))

    # 6020: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6000_series_6020_size_100_mm_id_150_mm_od_24_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6000_series_6020_size_100_mm_id_150_mm_od_24_mm_depth'
    option['size'] = '6020'
    option['series'] = '6000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 100.0
    option['dimensions']['outside'] = 150.0
    option['dimensions']['width'] = 24.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 21
    option['internal_geometry']['balls_per_row'] = 21
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 100.0
    option['internal_geometry']['parameters']['outside'] = 150.0
    option['internal_geometry']['parameters']['width'] = 24.0
    option['internal_geometry']['parameters']['edge'] = 1.44
    option['internal_geometry']['parameters']['pitch_radius'] = 62.5
    option['internal_geometry']['parameters']['ball_radius'] = 6.720000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 6.888000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 58.3336
    option['internal_geometry']['parameters']['outer_shoulder'] = 66.6664
    option['internal_geometry']['parameters']['cage_half_width'] = 3.6960000000000006
    option['internal_geometry']['parameters']['cage_low'] = 6.384
    option['internal_geometry']['parameters']['cage_high'] = 7.728
    option['internal_geometry']['parameters']['window_radius'] = 3.2256
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1,249'
    options.append(copy.deepcopy(option))

    # 6021: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6000_series_6021_size_105_mm_id_160_mm_od_26_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6000_series_6021_size_105_mm_id_160_mm_od_26_mm_depth'
    option['size'] = '6021'
    option['series'] = '6000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 105.0
    option['dimensions']['outside'] = 160.0
    option['dimensions']['width'] = 26.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 21
    option['internal_geometry']['balls_per_row'] = 21
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 105.0
    option['internal_geometry']['parameters']['outside'] = 160.0
    option['internal_geometry']['parameters']['width'] = 26.0
    option['internal_geometry']['parameters']['edge'] = 1.56
    option['internal_geometry']['parameters']['pitch_radius'] = 66.25
    option['internal_geometry']['parameters']['ball_radius'] = 7.280000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 7.4620000000000015
    option['internal_geometry']['parameters']['inner_shoulder'] = 61.7364
    option['internal_geometry']['parameters']['outer_shoulder'] = 70.7636
    option['internal_geometry']['parameters']['cage_half_width'] = 4.004000000000001
    option['internal_geometry']['parameters']['cage_low'] = 6.916
    option['internal_geometry']['parameters']['cage_high'] = 8.372
    option['internal_geometry']['parameters']['window_radius'] = 3.4944000000000006
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1,588'
    options.append(copy.deepcopy(option))

    # 6022: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6000_series_6022_size_110_mm_id_170_mm_od_28_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6000_series_6022_size_110_mm_id_170_mm_od_28_mm_depth'
    option['size'] = '6022'
    option['series'] = '6000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 110.0
    option['dimensions']['outside'] = 170.0
    option['dimensions']['width'] = 28.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 20
    option['internal_geometry']['balls_per_row'] = 20
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 110.0
    option['internal_geometry']['parameters']['outside'] = 170.0
    option['internal_geometry']['parameters']['width'] = 28.0
    option['internal_geometry']['parameters']['edge'] = 1.68
    option['internal_geometry']['parameters']['pitch_radius'] = 70.0
    option['internal_geometry']['parameters']['ball_radius'] = 7.840000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 8.036000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 65.1392
    option['internal_geometry']['parameters']['outer_shoulder'] = 74.8608
    option['internal_geometry']['parameters']['cage_half_width'] = 4.312000000000001
    option['internal_geometry']['parameters']['cage_low'] = 7.448
    option['internal_geometry']['parameters']['cage_high'] = 9.016
    option['internal_geometry']['parameters']['window_radius'] = 3.7632000000000003
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1,958'
    options.append(copy.deepcopy(option))

    # 6024: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6000_series_6024_size_120_mm_id_180_mm_od_28_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6000_series_6024_size_120_mm_id_180_mm_od_28_mm_depth'
    option['size'] = '6024'
    option['series'] = '6000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 120.0
    option['dimensions']['outside'] = 180.0
    option['dimensions']['width'] = 28.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 22
    option['internal_geometry']['balls_per_row'] = 22
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 120.0
    option['internal_geometry']['parameters']['outside'] = 180.0
    option['internal_geometry']['parameters']['width'] = 28.0
    option['internal_geometry']['parameters']['edge'] = 1.68
    option['internal_geometry']['parameters']['pitch_radius'] = 75.0
    option['internal_geometry']['parameters']['ball_radius'] = 7.840000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 8.036000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 70.1392
    option['internal_geometry']['parameters']['outer_shoulder'] = 79.8608
    option['internal_geometry']['parameters']['cage_half_width'] = 4.312000000000001
    option['internal_geometry']['parameters']['cage_low'] = 7.448
    option['internal_geometry']['parameters']['cage_high'] = 9.016
    option['internal_geometry']['parameters']['window_radius'] = 3.7632000000000003
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '2,177'
    options.append(copy.deepcopy(option))

    # 6026: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6000_series_6026_size_130_mm_id_200_mm_od_33_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6000_series_6026_size_130_mm_id_200_mm_od_33_mm_depth'
    option['size'] = '6026'
    option['series'] = '6000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 130.0
    option['dimensions']['outside'] = 200.0
    option['dimensions']['width'] = 33.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 20
    option['internal_geometry']['balls_per_row'] = 20
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 130.0
    option['internal_geometry']['parameters']['outside'] = 200.0
    option['internal_geometry']['parameters']['width'] = 33.0
    option['internal_geometry']['parameters']['edge'] = 1.98
    option['internal_geometry']['parameters']['pitch_radius'] = 82.5
    option['internal_geometry']['parameters']['ball_radius'] = 9.24
    option['internal_geometry']['parameters']['groove_radius'] = 9.471
    option['internal_geometry']['parameters']['inner_shoulder'] = 76.7712
    option['internal_geometry']['parameters']['outer_shoulder'] = 88.2288
    option['internal_geometry']['parameters']['cage_half_width'] = 5.082000000000001
    option['internal_geometry']['parameters']['cage_low'] = 8.778
    option['internal_geometry']['parameters']['cage_high'] = 10.626
    option['internal_geometry']['parameters']['window_radius'] = 4.4352
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '3,326'
    options.append(copy.deepcopy(option))

    # 6028: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6000_series_6028_size_140_mm_id_210_mm_od_33_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6000_series_6028_size_140_mm_id_210_mm_od_33_mm_depth'
    option['size'] = '6028'
    option['series'] = '6000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 140.0
    option['dimensions']['outside'] = 210.0
    option['dimensions']['width'] = 33.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 21
    option['internal_geometry']['balls_per_row'] = 21
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 140.0
    option['internal_geometry']['parameters']['outside'] = 210.0
    option['internal_geometry']['parameters']['width'] = 33.0
    option['internal_geometry']['parameters']['edge'] = 1.98
    option['internal_geometry']['parameters']['pitch_radius'] = 87.5
    option['internal_geometry']['parameters']['ball_radius'] = 9.24
    option['internal_geometry']['parameters']['groove_radius'] = 9.471
    option['internal_geometry']['parameters']['inner_shoulder'] = 81.7712
    option['internal_geometry']['parameters']['outer_shoulder'] = 93.2288
    option['internal_geometry']['parameters']['cage_half_width'] = 5.082000000000001
    option['internal_geometry']['parameters']['cage_low'] = 8.778
    option['internal_geometry']['parameters']['cage_high'] = 10.626
    option['internal_geometry']['parameters']['window_radius'] = 4.4352
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '3,556'
    options.append(copy.deepcopy(option))

    # 6030: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6000_series_6030_size_150_mm_id_225_mm_od_35_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6000_series_6030_size_150_mm_id_225_mm_od_35_mm_depth'
    option['size'] = '6030'
    option['series'] = '6000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 150.0
    option['dimensions']['outside'] = 225.0
    option['dimensions']['width'] = 35.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 22
    option['internal_geometry']['balls_per_row'] = 22
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 150.0
    option['internal_geometry']['parameters']['outside'] = 225.0
    option['internal_geometry']['parameters']['width'] = 35.0
    option['internal_geometry']['parameters']['edge'] = 2.1
    option['internal_geometry']['parameters']['pitch_radius'] = 93.75
    option['internal_geometry']['parameters']['ball_radius'] = 9.8
    option['internal_geometry']['parameters']['groove_radius'] = 10.045
    option['internal_geometry']['parameters']['inner_shoulder'] = 87.674
    option['internal_geometry']['parameters']['outer_shoulder'] = 99.826
    option['internal_geometry']['parameters']['cage_half_width'] = 5.390000000000001
    option['internal_geometry']['parameters']['cage_low'] = 9.31
    option['internal_geometry']['parameters']['cage_high'] = 11.27
    option['internal_geometry']['parameters']['window_radius'] = 4.704
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '4,375'
    options.append(copy.deepcopy(option))

    # 603: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_603_size_3_mm_id_9_mm_od_5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_603_size_3_mm_id_9_mm_od_5_mm_depth'
    option['size'] = '603'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 3.0
    option['dimensions']['outside'] = 9.0
    option['dimensions']['width'] = 5.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 3.0
    option['internal_geometry']['parameters']['outside'] = 9.0
    option['internal_geometry']['parameters']['width'] = 5.0
    option['internal_geometry']['parameters']['edge'] = 0.18
    option['internal_geometry']['parameters']['pitch_radius'] = 3.0
    option['internal_geometry']['parameters']['ball_radius'] = 0.8400000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 0.8610000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 2.4792
    option['internal_geometry']['parameters']['outer_shoulder'] = 3.5208
    option['internal_geometry']['parameters']['cage_half_width'] = 0.4620000000000001
    option['internal_geometry']['parameters']['cage_low'] = 0.798
    option['internal_geometry']['parameters']['cage_high'] = 0.966
    option['internal_geometry']['parameters']['window_radius'] = 0.4032
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1'
    options.append(copy.deepcopy(option))

    # 604: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_604_size_4_mm_id_12_mm_od_4_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_604_size_4_mm_id_12_mm_od_4_mm_depth'
    option['size'] = '604'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 4.0
    option['dimensions']['outside'] = 12.0
    option['dimensions']['width'] = 4.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 4.0
    option['internal_geometry']['parameters']['outside'] = 12.0
    option['internal_geometry']['parameters']['width'] = 4.0
    option['internal_geometry']['parameters']['edge'] = 0.24
    option['internal_geometry']['parameters']['pitch_radius'] = 4.0
    option['internal_geometry']['parameters']['ball_radius'] = 1.12
    option['internal_geometry']['parameters']['groove_radius'] = 1.1480000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 3.3056
    option['internal_geometry']['parameters']['outer_shoulder'] = 4.6944
    option['internal_geometry']['parameters']['cage_half_width'] = 0.6160000000000001
    option['internal_geometry']['parameters']['cage_low'] = 1.064
    option['internal_geometry']['parameters']['cage_high'] = 1.288
    option['internal_geometry']['parameters']['window_radius'] = 0.5376000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '2'
    options.append(copy.deepcopy(option))

    # 605: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_605_size_5_mm_id_14_mm_od_5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_605_size_5_mm_id_14_mm_od_5_mm_depth'
    option['size'] = '605'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 5.0
    option['dimensions']['outside'] = 14.0
    option['dimensions']['width'] = 5.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 5.0
    option['internal_geometry']['parameters']['outside'] = 14.0
    option['internal_geometry']['parameters']['width'] = 5.0
    option['internal_geometry']['parameters']['edge'] = 0.27
    option['internal_geometry']['parameters']['pitch_radius'] = 4.75
    option['internal_geometry']['parameters']['ball_radius'] = 1.2600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.2915000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 3.9688
    option['internal_geometry']['parameters']['outer_shoulder'] = 5.5312
    option['internal_geometry']['parameters']['cage_half_width'] = 0.6930000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.197
    option['internal_geometry']['parameters']['cage_high'] = 1.449
    option['internal_geometry']['parameters']['window_radius'] = 0.6048000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '3'
    options.append(copy.deepcopy(option))

    # 606: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_606_size_6_mm_id_17_mm_od_6_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_606_size_6_mm_id_17_mm_od_6_mm_depth'
    option['size'] = '606'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 6.0
    option['dimensions']['outside'] = 17.0
    option['dimensions']['width'] = 6.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 6.0
    option['internal_geometry']['parameters']['outside'] = 17.0
    option['internal_geometry']['parameters']['width'] = 6.0
    option['internal_geometry']['parameters']['edge'] = 0.32999999999999996
    option['internal_geometry']['parameters']['pitch_radius'] = 5.75
    option['internal_geometry']['parameters']['ball_radius'] = 1.54
    option['internal_geometry']['parameters']['groove_radius'] = 1.5785
    option['internal_geometry']['parameters']['inner_shoulder'] = 4.7952
    option['internal_geometry']['parameters']['outer_shoulder'] = 6.7048
    option['internal_geometry']['parameters']['cage_half_width'] = 0.8470000000000001
    option['internal_geometry']['parameters']['cage_low'] = 1.4629999999999999
    option['internal_geometry']['parameters']['cage_high'] = 1.771
    option['internal_geometry']['parameters']['window_radius'] = 0.7392
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '6'
    options.append(copy.deepcopy(option))

    # 607: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_607_size_7_mm_id_19_mm_od_6_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_607_size_7_mm_id_19_mm_od_6_mm_depth'
    option['size'] = '607'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 7.0
    option['dimensions']['outside'] = 19.0
    option['dimensions']['width'] = 6.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 7.0
    option['internal_geometry']['parameters']['outside'] = 19.0
    option['internal_geometry']['parameters']['width'] = 6.0
    option['internal_geometry']['parameters']['edge'] = 0.36
    option['internal_geometry']['parameters']['pitch_radius'] = 6.5
    option['internal_geometry']['parameters']['ball_radius'] = 1.6800000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.7220000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 5.4584
    option['internal_geometry']['parameters']['outer_shoulder'] = 7.5416
    option['internal_geometry']['parameters']['cage_half_width'] = 0.9240000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.596
    option['internal_geometry']['parameters']['cage_high'] = 1.932
    option['internal_geometry']['parameters']['window_radius'] = 0.8064
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '8'
    options.append(copy.deepcopy(option))

    # 608: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_608_size_8_mm_id_22_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_608_size_8_mm_id_22_mm_od_7_mm_depth'
    option['size'] = '608'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 8.0
    option['dimensions']['outside'] = 22.0
    option['dimensions']['width'] = 7.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 8.0
    option['internal_geometry']['parameters']['outside'] = 22.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.42
    option['internal_geometry']['parameters']['pitch_radius'] = 7.5
    option['internal_geometry']['parameters']['ball_radius'] = 1.9600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 2.0090000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 6.2848
    option['internal_geometry']['parameters']['outer_shoulder'] = 8.7152
    option['internal_geometry']['parameters']['cage_half_width'] = 1.0780000000000003
    option['internal_geometry']['parameters']['cage_low'] = 1.862
    option['internal_geometry']['parameters']['cage_high'] = 2.254
    option['internal_geometry']['parameters']['window_radius'] = 0.9408000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '12'
    options.append(copy.deepcopy(option))

    # 609: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_609_size_9_mm_id_24_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_609_size_9_mm_id_24_mm_od_7_mm_depth'
    option['size'] = '609'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 9.0
    option['dimensions']['outside'] = 24.0
    option['dimensions']['width'] = 7.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 9
    option['internal_geometry']['balls_per_row'] = 9
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 9.0
    option['internal_geometry']['parameters']['outside'] = 24.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.42
    option['internal_geometry']['parameters']['pitch_radius'] = 8.25
    option['internal_geometry']['parameters']['ball_radius'] = 1.9600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 2.0090000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 7.0348
    option['internal_geometry']['parameters']['outer_shoulder'] = 9.4652
    option['internal_geometry']['parameters']['cage_half_width'] = 1.0780000000000003
    option['internal_geometry']['parameters']['cage_low'] = 1.862
    option['internal_geometry']['parameters']['cage_high'] = 2.254
    option['internal_geometry']['parameters']['window_radius'] = 0.9408000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '16'
    options.append(copy.deepcopy(option))

    # 623: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_623_size_3_mm_id_10_mm_od_4_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_623_size_3_mm_id_10_mm_od_4_mm_depth'
    option['size'] = '623'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 3.0
    option['dimensions']['outside'] = 10.0
    option['dimensions']['width'] = 4.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 7
    option['internal_geometry']['balls_per_row'] = 7
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 3.0
    option['internal_geometry']['parameters']['outside'] = 10.0
    option['internal_geometry']['parameters']['width'] = 4.0
    option['internal_geometry']['parameters']['edge'] = 0.21
    option['internal_geometry']['parameters']['pitch_radius'] = 3.25
    option['internal_geometry']['parameters']['ball_radius'] = 0.9800000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 1.0045000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 2.6424
    option['internal_geometry']['parameters']['outer_shoulder'] = 3.8576
    option['internal_geometry']['parameters']['cage_half_width'] = 0.5390000000000001
    option['internal_geometry']['parameters']['cage_low'] = 0.931
    option['internal_geometry']['parameters']['cage_high'] = 1.127
    option['internal_geometry']['parameters']['window_radius'] = 0.47040000000000004
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '2'
    options.append(copy.deepcopy(option))

    # 624: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_624_size_4_mm_id_13_mm_od_5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_624_size_4_mm_id_13_mm_od_5_mm_depth'
    option['size'] = '624'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 4.0
    option['dimensions']['outside'] = 13.0
    option['dimensions']['width'] = 5.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 7
    option['internal_geometry']['balls_per_row'] = 7
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 4.0
    option['internal_geometry']['parameters']['outside'] = 13.0
    option['internal_geometry']['parameters']['width'] = 5.0
    option['internal_geometry']['parameters']['edge'] = 0.27
    option['internal_geometry']['parameters']['pitch_radius'] = 4.25
    option['internal_geometry']['parameters']['ball_radius'] = 1.2600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.2915000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 3.4688
    option['internal_geometry']['parameters']['outer_shoulder'] = 5.0312
    option['internal_geometry']['parameters']['cage_half_width'] = 0.6930000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.197
    option['internal_geometry']['parameters']['cage_high'] = 1.449
    option['internal_geometry']['parameters']['window_radius'] = 0.6048000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '3'
    options.append(copy.deepcopy(option))

    # 625: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_625_size_5_mm_id_16_mm_od_5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_625_size_5_mm_id_16_mm_od_5_mm_depth'
    option['size'] = '625'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 5.0
    option['dimensions']['outside'] = 16.0
    option['dimensions']['width'] = 5.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 5.0
    option['internal_geometry']['parameters']['outside'] = 16.0
    option['internal_geometry']['parameters']['width'] = 5.0
    option['internal_geometry']['parameters']['edge'] = 0.3
    option['internal_geometry']['parameters']['pitch_radius'] = 5.25
    option['internal_geometry']['parameters']['ball_radius'] = 1.4000000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 1.435
    option['internal_geometry']['parameters']['inner_shoulder'] = 4.382
    option['internal_geometry']['parameters']['outer_shoulder'] = 6.118
    option['internal_geometry']['parameters']['cage_half_width'] = 0.7700000000000001
    option['internal_geometry']['parameters']['cage_low'] = 1.33
    option['internal_geometry']['parameters']['cage_high'] = 1.61
    option['internal_geometry']['parameters']['window_radius'] = 0.672
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '4'
    options.append(copy.deepcopy(option))

    # 626: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_626_size_6_mm_id_19_mm_od_6_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_626_size_6_mm_id_19_mm_od_6_mm_depth'
    option['size'] = '626'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 6.0
    option['dimensions']['outside'] = 19.0
    option['dimensions']['width'] = 6.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 6.0
    option['internal_geometry']['parameters']['outside'] = 19.0
    option['internal_geometry']['parameters']['width'] = 6.0
    option['internal_geometry']['parameters']['edge'] = 0.36
    option['internal_geometry']['parameters']['pitch_radius'] = 6.25
    option['internal_geometry']['parameters']['ball_radius'] = 1.6800000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.7220000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 5.2084
    option['internal_geometry']['parameters']['outer_shoulder'] = 7.2916
    option['internal_geometry']['parameters']['cage_half_width'] = 0.9240000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.596
    option['internal_geometry']['parameters']['cage_high'] = 1.932
    option['internal_geometry']['parameters']['window_radius'] = 0.8064
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '8'
    options.append(copy.deepcopy(option))

    # 627: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_627_size_7_mm_id_22_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_627_size_7_mm_id_22_mm_od_7_mm_depth'
    option['size'] = '627'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 7.0
    option['dimensions']['outside'] = 22.0
    option['dimensions']['width'] = 7.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 7.0
    option['internal_geometry']['parameters']['outside'] = 22.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.42
    option['internal_geometry']['parameters']['pitch_radius'] = 7.25
    option['internal_geometry']['parameters']['ball_radius'] = 1.9600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 2.0090000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 6.0348
    option['internal_geometry']['parameters']['outer_shoulder'] = 8.4652
    option['internal_geometry']['parameters']['cage_half_width'] = 1.0780000000000003
    option['internal_geometry']['parameters']['cage_low'] = 1.862
    option['internal_geometry']['parameters']['cage_high'] = 2.254
    option['internal_geometry']['parameters']['window_radius'] = 0.9408000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '14'
    options.append(copy.deepcopy(option))

    # 628: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_628_size_8_mm_id_24_mm_od_8_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_628_size_8_mm_id_24_mm_od_8_mm_depth'
    option['size'] = '628'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 8.0
    option['dimensions']['outside'] = 24.0
    option['dimensions']['width'] = 8.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 8.0
    option['internal_geometry']['parameters']['outside'] = 24.0
    option['internal_geometry']['parameters']['width'] = 8.0
    option['internal_geometry']['parameters']['edge'] = 0.48
    option['internal_geometry']['parameters']['pitch_radius'] = 8.0
    option['internal_geometry']['parameters']['ball_radius'] = 2.24
    option['internal_geometry']['parameters']['groove_radius'] = 2.2960000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 6.6112
    option['internal_geometry']['parameters']['outer_shoulder'] = 9.3888
    option['internal_geometry']['parameters']['cage_half_width'] = 1.2320000000000002
    option['internal_geometry']['parameters']['cage_low'] = 2.128
    option['internal_geometry']['parameters']['cage_high'] = 2.576
    option['internal_geometry']['parameters']['window_radius'] = 1.0752000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '16'
    options.append(copy.deepcopy(option))

    # 629: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_629_size_9_mm_id_26_mm_od_8_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_629_size_9_mm_id_26_mm_od_8_mm_depth'
    option['size'] = '629'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 9.0
    option['dimensions']['outside'] = 26.0
    option['dimensions']['width'] = 8.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 9.0
    option['internal_geometry']['parameters']['outside'] = 26.0
    option['internal_geometry']['parameters']['width'] = 8.0
    option['internal_geometry']['parameters']['edge'] = 0.48
    option['internal_geometry']['parameters']['pitch_radius'] = 8.75
    option['internal_geometry']['parameters']['ball_radius'] = 2.24
    option['internal_geometry']['parameters']['groove_radius'] = 2.2960000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 7.3612
    option['internal_geometry']['parameters']['outer_shoulder'] = 10.1388
    option['internal_geometry']['parameters']['cage_half_width'] = 1.2320000000000002
    option['internal_geometry']['parameters']['cage_low'] = 2.128
    option['internal_geometry']['parameters']['cage_high'] = 2.576
    option['internal_geometry']['parameters']['window_radius'] = 1.0752000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '19'
    options.append(copy.deepcopy(option))

    # 633: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_633_size_3_mm_id_13_mm_od_5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_633_size_3_mm_id_13_mm_od_5_mm_depth'
    option['size'] = '633'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 3.0
    option['dimensions']['outside'] = 13.0
    option['dimensions']['width'] = 5.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 6
    option['internal_geometry']['balls_per_row'] = 6
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 3.0
    option['internal_geometry']['parameters']['outside'] = 13.0
    option['internal_geometry']['parameters']['width'] = 5.0
    option['internal_geometry']['parameters']['edge'] = 0.3
    option['internal_geometry']['parameters']['pitch_radius'] = 4.0
    option['internal_geometry']['parameters']['ball_radius'] = 1.4000000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 1.435
    option['internal_geometry']['parameters']['inner_shoulder'] = 3.1319999999999997
    option['internal_geometry']['parameters']['outer_shoulder'] = 4.868
    option['internal_geometry']['parameters']['cage_half_width'] = 0.7700000000000001
    option['internal_geometry']['parameters']['cage_low'] = 1.33
    option['internal_geometry']['parameters']['cage_high'] = 1.61
    option['internal_geometry']['parameters']['window_radius'] = 0.672
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '3'
    options.append(copy.deepcopy(option))

    # 634: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_634_size_4_mm_id_16_mm_od_5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_634_size_4_mm_id_16_mm_od_5_mm_depth'
    option['size'] = '634'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 4.0
    option['dimensions']['outside'] = 16.0
    option['dimensions']['width'] = 5.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 4.0
    option['internal_geometry']['parameters']['outside'] = 16.0
    option['internal_geometry']['parameters']['width'] = 5.0
    option['internal_geometry']['parameters']['edge'] = 0.3
    option['internal_geometry']['parameters']['pitch_radius'] = 5.0
    option['internal_geometry']['parameters']['ball_radius'] = 1.4000000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 1.435
    option['internal_geometry']['parameters']['inner_shoulder'] = 4.132
    option['internal_geometry']['parameters']['outer_shoulder'] = 5.868
    option['internal_geometry']['parameters']['cage_half_width'] = 0.7700000000000001
    option['internal_geometry']['parameters']['cage_low'] = 1.33
    option['internal_geometry']['parameters']['cage_high'] = 1.61
    option['internal_geometry']['parameters']['window_radius'] = 0.672
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '5'
    options.append(copy.deepcopy(option))

    # 635: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_635_size_5_mm_id_19_mm_od_6_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_635_size_5_mm_id_19_mm_od_6_mm_depth'
    option['size'] = '635'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 5.0
    option['dimensions']['outside'] = 19.0
    option['dimensions']['width'] = 6.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 5.0
    option['internal_geometry']['parameters']['outside'] = 19.0
    option['internal_geometry']['parameters']['width'] = 6.0
    option['internal_geometry']['parameters']['edge'] = 0.36
    option['internal_geometry']['parameters']['pitch_radius'] = 6.0
    option['internal_geometry']['parameters']['ball_radius'] = 1.6800000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.7220000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 4.9584
    option['internal_geometry']['parameters']['outer_shoulder'] = 7.0416
    option['internal_geometry']['parameters']['cage_half_width'] = 0.9240000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.596
    option['internal_geometry']['parameters']['cage_high'] = 1.932
    option['internal_geometry']['parameters']['window_radius'] = 0.8064
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '8'
    options.append(copy.deepcopy(option))

    # 636: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_636_size_6_mm_id_22_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_636_size_6_mm_id_22_mm_od_7_mm_depth'
    option['size'] = '636'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 6.0
    option['dimensions']['outside'] = 22.0
    option['dimensions']['width'] = 7.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 6.0
    option['internal_geometry']['parameters']['outside'] = 22.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.42
    option['internal_geometry']['parameters']['pitch_radius'] = 7.0
    option['internal_geometry']['parameters']['ball_radius'] = 1.9600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 2.0090000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 5.7848
    option['internal_geometry']['parameters']['outer_shoulder'] = 8.2152
    option['internal_geometry']['parameters']['cage_half_width'] = 1.0780000000000003
    option['internal_geometry']['parameters']['cage_low'] = 1.862
    option['internal_geometry']['parameters']['cage_high'] = 2.254
    option['internal_geometry']['parameters']['window_radius'] = 0.9408000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '13'
    options.append(copy.deepcopy(option))

    # 637: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_637_size_7_mm_id_26_mm_od_9_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_637_size_7_mm_id_26_mm_od_9_mm_depth'
    option['size'] = '637'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 7.0
    option['dimensions']['outside'] = 26.0
    option['dimensions']['width'] = 9.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 7
    option['internal_geometry']['balls_per_row'] = 7
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 7.0
    option['internal_geometry']['parameters']['outside'] = 26.0
    option['internal_geometry']['parameters']['width'] = 9.0
    option['internal_geometry']['parameters']['edge'] = 0.54
    option['internal_geometry']['parameters']['pitch_radius'] = 8.25
    option['internal_geometry']['parameters']['ball_radius'] = 2.5200000000000005
    option['internal_geometry']['parameters']['groove_radius'] = 2.5830000000000006
    option['internal_geometry']['parameters']['inner_shoulder'] = 6.6876
    option['internal_geometry']['parameters']['outer_shoulder'] = 9.8124
    option['internal_geometry']['parameters']['cage_half_width'] = 1.3860000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.394
    option['internal_geometry']['parameters']['cage_high'] = 2.898
    option['internal_geometry']['parameters']['window_radius'] = 1.2096000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '24'
    options.append(copy.deepcopy(option))

    # 638: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_638_size_8_mm_id_28_mm_od_9_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_638_size_8_mm_id_28_mm_od_9_mm_depth'
    option['size'] = '638'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 8.0
    option['dimensions']['outside'] = 28.0
    option['dimensions']['width'] = 9.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 8.0
    option['internal_geometry']['parameters']['outside'] = 28.0
    option['internal_geometry']['parameters']['width'] = 9.0
    option['internal_geometry']['parameters']['edge'] = 0.54
    option['internal_geometry']['parameters']['pitch_radius'] = 9.0
    option['internal_geometry']['parameters']['ball_radius'] = 2.5200000000000005
    option['internal_geometry']['parameters']['groove_radius'] = 2.5830000000000006
    option['internal_geometry']['parameters']['inner_shoulder'] = 7.4376
    option['internal_geometry']['parameters']['outer_shoulder'] = 10.5624
    option['internal_geometry']['parameters']['cage_half_width'] = 1.3860000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.394
    option['internal_geometry']['parameters']['cage_high'] = 2.898
    option['internal_geometry']['parameters']['window_radius'] = 1.2096000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '29'
    options.append(copy.deepcopy(option))

    # 639: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_639_size_9_mm_id_30_mm_od_10_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_639_size_9_mm_id_30_mm_od_10_mm_depth'
    option['size'] = '639'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 9.0
    option['dimensions']['outside'] = 30.0
    option['dimensions']['width'] = 10.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 7
    option['internal_geometry']['balls_per_row'] = 7
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 9.0
    option['internal_geometry']['parameters']['outside'] = 30.0
    option['internal_geometry']['parameters']['width'] = 10.0
    option['internal_geometry']['parameters']['edge'] = 0.6
    option['internal_geometry']['parameters']['pitch_radius'] = 9.75
    option['internal_geometry']['parameters']['ball_radius'] = 2.8000000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 2.87
    option['internal_geometry']['parameters']['inner_shoulder'] = 8.014
    option['internal_geometry']['parameters']['outer_shoulder'] = 11.486
    option['internal_geometry']['parameters']['cage_half_width'] = 1.5400000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.66
    option['internal_geometry']['parameters']['cage_high'] = 3.22
    option['internal_geometry']['parameters']['window_radius'] = 1.344
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '35'
    options.append(copy.deepcopy(option))

    # 673: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_673_size_3_mm_id_6_mm_od_2.5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_673_size_3_mm_id_6_mm_od_2_5_mm_depth'
    option['size'] = '673'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 3.0
    option['dimensions']['outside'] = 6.0
    option['dimensions']['width'] = 2.5
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 12
    option['internal_geometry']['balls_per_row'] = 12
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 3.0
    option['internal_geometry']['parameters']['outside'] = 6.0
    option['internal_geometry']['parameters']['width'] = 2.5
    option['internal_geometry']['parameters']['edge'] = 0.09
    option['internal_geometry']['parameters']['pitch_radius'] = 2.25
    option['internal_geometry']['parameters']['ball_radius'] = 0.42000000000000004
    option['internal_geometry']['parameters']['groove_radius'] = 0.43050000000000005
    option['internal_geometry']['parameters']['inner_shoulder'] = 1.9896
    option['internal_geometry']['parameters']['outer_shoulder'] = 2.5104
    option['internal_geometry']['parameters']['cage_half_width'] = 0.23100000000000004
    option['internal_geometry']['parameters']['cage_low'] = 0.399
    option['internal_geometry']['parameters']['cage_high'] = 0.483
    option['internal_geometry']['parameters']['window_radius'] = 0.2016
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '0'
    options.append(copy.deepcopy(option))

    # 674: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_674_size_4_mm_id_7_mm_od_2.5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_674_size_4_mm_id_7_mm_od_2_5_mm_depth'
    option['size'] = '674'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 4.0
    option['dimensions']['outside'] = 7.0
    option['dimensions']['width'] = 2.5
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 15
    option['internal_geometry']['balls_per_row'] = 15
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 4.0
    option['internal_geometry']['parameters']['outside'] = 7.0
    option['internal_geometry']['parameters']['width'] = 2.5
    option['internal_geometry']['parameters']['edge'] = 0.09
    option['internal_geometry']['parameters']['pitch_radius'] = 2.75
    option['internal_geometry']['parameters']['ball_radius'] = 0.42000000000000004
    option['internal_geometry']['parameters']['groove_radius'] = 0.43050000000000005
    option['internal_geometry']['parameters']['inner_shoulder'] = 2.4896
    option['internal_geometry']['parameters']['outer_shoulder'] = 3.0104
    option['internal_geometry']['parameters']['cage_half_width'] = 0.23100000000000004
    option['internal_geometry']['parameters']['cage_low'] = 0.399
    option['internal_geometry']['parameters']['cage_high'] = 0.483
    option['internal_geometry']['parameters']['window_radius'] = 0.2016
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '0'
    options.append(copy.deepcopy(option))

    # 675: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_675_size_5_mm_id_8_mm_od_2.5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_675_size_5_mm_id_8_mm_od_2_5_mm_depth'
    option['size'] = '675'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 5.0
    option['dimensions']['outside'] = 8.0
    option['dimensions']['width'] = 2.5
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 17
    option['internal_geometry']['balls_per_row'] = 17
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 5.0
    option['internal_geometry']['parameters']['outside'] = 8.0
    option['internal_geometry']['parameters']['width'] = 2.5
    option['internal_geometry']['parameters']['edge'] = 0.09
    option['internal_geometry']['parameters']['pitch_radius'] = 3.25
    option['internal_geometry']['parameters']['ball_radius'] = 0.42000000000000004
    option['internal_geometry']['parameters']['groove_radius'] = 0.43050000000000005
    option['internal_geometry']['parameters']['inner_shoulder'] = 2.9896
    option['internal_geometry']['parameters']['outer_shoulder'] = 3.5104
    option['internal_geometry']['parameters']['cage_half_width'] = 0.23100000000000004
    option['internal_geometry']['parameters']['cage_low'] = 0.399
    option['internal_geometry']['parameters']['cage_high'] = 0.483
    option['internal_geometry']['parameters']['window_radius'] = 0.2016
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '0'
    options.append(copy.deepcopy(option))

    # 676: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_676_size_6_mm_id_10_mm_od_3_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_676_size_6_mm_id_10_mm_od_3_mm_depth'
    option['size'] = '676'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 6.0
    option['dimensions']['outside'] = 10.0
    option['dimensions']['width'] = 3.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 16
    option['internal_geometry']['balls_per_row'] = 16
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 6.0
    option['internal_geometry']['parameters']['outside'] = 10.0
    option['internal_geometry']['parameters']['width'] = 3.0
    option['internal_geometry']['parameters']['edge'] = 0.12
    option['internal_geometry']['parameters']['pitch_radius'] = 4.0
    option['internal_geometry']['parameters']['ball_radius'] = 0.56
    option['internal_geometry']['parameters']['groove_radius'] = 0.5740000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 3.6528
    option['internal_geometry']['parameters']['outer_shoulder'] = 4.3472
    option['internal_geometry']['parameters']['cage_half_width'] = 0.30800000000000005
    option['internal_geometry']['parameters']['cage_low'] = 0.532
    option['internal_geometry']['parameters']['cage_high'] = 0.644
    option['internal_geometry']['parameters']['window_radius'] = 0.26880000000000004
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1'
    options.append(copy.deepcopy(option))

    # 677: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_677_size_7_mm_id_11_mm_od_3_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_677_size_7_mm_id_11_mm_od_3_mm_depth'
    option['size'] = '677'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 7.0
    option['dimensions']['outside'] = 11.0
    option['dimensions']['width'] = 3.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 18
    option['internal_geometry']['balls_per_row'] = 18
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 7.0
    option['internal_geometry']['parameters']['outside'] = 11.0
    option['internal_geometry']['parameters']['width'] = 3.0
    option['internal_geometry']['parameters']['edge'] = 0.12
    option['internal_geometry']['parameters']['pitch_radius'] = 4.5
    option['internal_geometry']['parameters']['ball_radius'] = 0.56
    option['internal_geometry']['parameters']['groove_radius'] = 0.5740000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 4.1528
    option['internal_geometry']['parameters']['outer_shoulder'] = 4.8472
    option['internal_geometry']['parameters']['cage_half_width'] = 0.30800000000000005
    option['internal_geometry']['parameters']['cage_low'] = 0.532
    option['internal_geometry']['parameters']['cage_high'] = 0.644
    option['internal_geometry']['parameters']['window_radius'] = 0.26880000000000004
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1'
    options.append(copy.deepcopy(option))

    # 678: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_678_size_8_mm_id_12_mm_od_3.5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_678_size_8_mm_id_12_mm_od_3_5_mm_depth'
    option['size'] = '678'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 8.0
    option['dimensions']['outside'] = 12.0
    option['dimensions']['width'] = 3.5
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 20
    option['internal_geometry']['balls_per_row'] = 20
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 8.0
    option['internal_geometry']['parameters']['outside'] = 12.0
    option['internal_geometry']['parameters']['width'] = 3.5
    option['internal_geometry']['parameters']['edge'] = 0.12
    option['internal_geometry']['parameters']['pitch_radius'] = 5.0
    option['internal_geometry']['parameters']['ball_radius'] = 0.56
    option['internal_geometry']['parameters']['groove_radius'] = 0.5740000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 4.6528
    option['internal_geometry']['parameters']['outer_shoulder'] = 5.3472
    option['internal_geometry']['parameters']['cage_half_width'] = 0.30800000000000005
    option['internal_geometry']['parameters']['cage_low'] = 0.532
    option['internal_geometry']['parameters']['cage_high'] = 0.644
    option['internal_geometry']['parameters']['window_radius'] = 0.26880000000000004
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1'
    options.append(copy.deepcopy(option))

    # 683: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_683_size_3_mm_id_7_mm_od_3_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_683_size_3_mm_id_7_mm_od_3_mm_depth'
    option['size'] = '683'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 3.0
    option['dimensions']['outside'] = 7.0
    option['dimensions']['width'] = 3.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 10
    option['internal_geometry']['balls_per_row'] = 10
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 3.0
    option['internal_geometry']['parameters']['outside'] = 7.0
    option['internal_geometry']['parameters']['width'] = 3.0
    option['internal_geometry']['parameters']['edge'] = 0.12
    option['internal_geometry']['parameters']['pitch_radius'] = 2.5
    option['internal_geometry']['parameters']['ball_radius'] = 0.56
    option['internal_geometry']['parameters']['groove_radius'] = 0.5740000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 2.1528
    option['internal_geometry']['parameters']['outer_shoulder'] = 2.8472
    option['internal_geometry']['parameters']['cage_half_width'] = 0.30800000000000005
    option['internal_geometry']['parameters']['cage_low'] = 0.532
    option['internal_geometry']['parameters']['cage_high'] = 0.644
    option['internal_geometry']['parameters']['window_radius'] = 0.26880000000000004
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '0'
    options.append(copy.deepcopy(option))

    # 684: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_684_size_4_mm_id_9_mm_od_4_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_684_size_4_mm_id_9_mm_od_4_mm_depth'
    option['size'] = '684'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 4.0
    option['dimensions']['outside'] = 9.0
    option['dimensions']['width'] = 4.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 10
    option['internal_geometry']['balls_per_row'] = 10
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 4.0
    option['internal_geometry']['parameters']['outside'] = 9.0
    option['internal_geometry']['parameters']['width'] = 4.0
    option['internal_geometry']['parameters']['edge'] = 0.15
    option['internal_geometry']['parameters']['pitch_radius'] = 3.25
    option['internal_geometry']['parameters']['ball_radius'] = 0.7000000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 0.7175
    option['internal_geometry']['parameters']['inner_shoulder'] = 2.816
    option['internal_geometry']['parameters']['outer_shoulder'] = 3.684
    option['internal_geometry']['parameters']['cage_half_width'] = 0.38500000000000006
    option['internal_geometry']['parameters']['cage_low'] = 0.665
    option['internal_geometry']['parameters']['cage_high'] = 0.805
    option['internal_geometry']['parameters']['window_radius'] = 0.336
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1'
    options.append(copy.deepcopy(option))

    # 685: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_685_size_5_mm_id_11_mm_od_5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_685_size_5_mm_id_11_mm_od_5_mm_depth'
    option['size'] = '685'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 5.0
    option['dimensions']['outside'] = 11.0
    option['dimensions']['width'] = 5.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 10
    option['internal_geometry']['balls_per_row'] = 10
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 5.0
    option['internal_geometry']['parameters']['outside'] = 11.0
    option['internal_geometry']['parameters']['width'] = 5.0
    option['internal_geometry']['parameters']['edge'] = 0.18
    option['internal_geometry']['parameters']['pitch_radius'] = 4.0
    option['internal_geometry']['parameters']['ball_radius'] = 0.8400000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 0.8610000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 3.4792
    option['internal_geometry']['parameters']['outer_shoulder'] = 4.5208
    option['internal_geometry']['parameters']['cage_half_width'] = 0.4620000000000001
    option['internal_geometry']['parameters']['cage_low'] = 0.798
    option['internal_geometry']['parameters']['cage_high'] = 0.966
    option['internal_geometry']['parameters']['window_radius'] = 0.4032
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1'
    options.append(copy.deepcopy(option))

    # 686: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_686_size_6_mm_id_13_mm_od_5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_686_size_6_mm_id_13_mm_od_5_mm_depth'
    option['size'] = '686'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 6.0
    option['dimensions']['outside'] = 13.0
    option['dimensions']['width'] = 5.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 11
    option['internal_geometry']['balls_per_row'] = 11
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 6.0
    option['internal_geometry']['parameters']['outside'] = 13.0
    option['internal_geometry']['parameters']['width'] = 5.0
    option['internal_geometry']['parameters']['edge'] = 0.21
    option['internal_geometry']['parameters']['pitch_radius'] = 4.75
    option['internal_geometry']['parameters']['ball_radius'] = 0.9800000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 1.0045000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 4.1424
    option['internal_geometry']['parameters']['outer_shoulder'] = 5.3576
    option['internal_geometry']['parameters']['cage_half_width'] = 0.5390000000000001
    option['internal_geometry']['parameters']['cage_low'] = 0.931
    option['internal_geometry']['parameters']['cage_high'] = 1.127
    option['internal_geometry']['parameters']['window_radius'] = 0.47040000000000004
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '2'
    options.append(copy.deepcopy(option))

    # 687: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_687_size_7_mm_id_14_mm_od_5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_687_size_7_mm_id_14_mm_od_5_mm_depth'
    option['size'] = '687'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 7.0
    option['dimensions']['outside'] = 14.0
    option['dimensions']['width'] = 5.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 12
    option['internal_geometry']['balls_per_row'] = 12
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 7.0
    option['internal_geometry']['parameters']['outside'] = 14.0
    option['internal_geometry']['parameters']['width'] = 5.0
    option['internal_geometry']['parameters']['edge'] = 0.21
    option['internal_geometry']['parameters']['pitch_radius'] = 5.25
    option['internal_geometry']['parameters']['ball_radius'] = 0.9800000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 1.0045000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 4.6424
    option['internal_geometry']['parameters']['outer_shoulder'] = 5.8576
    option['internal_geometry']['parameters']['cage_half_width'] = 0.5390000000000001
    option['internal_geometry']['parameters']['cage_low'] = 0.931
    option['internal_geometry']['parameters']['cage_high'] = 1.127
    option['internal_geometry']['parameters']['window_radius'] = 0.47040000000000004
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '2'
    options.append(copy.deepcopy(option))

    # 688: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_688_size_8_mm_id_16_mm_od_5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_688_size_8_mm_id_16_mm_od_5_mm_depth'
    option['size'] = '688'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 8.0
    option['dimensions']['outside'] = 16.0
    option['dimensions']['width'] = 5.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 12
    option['internal_geometry']['balls_per_row'] = 12
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 8.0
    option['internal_geometry']['parameters']['outside'] = 16.0
    option['internal_geometry']['parameters']['width'] = 5.0
    option['internal_geometry']['parameters']['edge'] = 0.24
    option['internal_geometry']['parameters']['pitch_radius'] = 6.0
    option['internal_geometry']['parameters']['ball_radius'] = 1.12
    option['internal_geometry']['parameters']['groove_radius'] = 1.1480000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 5.3056
    option['internal_geometry']['parameters']['outer_shoulder'] = 6.6944
    option['internal_geometry']['parameters']['cage_half_width'] = 0.6160000000000001
    option['internal_geometry']['parameters']['cage_low'] = 1.064
    option['internal_geometry']['parameters']['cage_high'] = 1.288
    option['internal_geometry']['parameters']['window_radius'] = 0.5376000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '3'
    options.append(copy.deepcopy(option))

    # 689: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_689_size_9_mm_id_17_mm_od_5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_689_size_9_mm_id_17_mm_od_5_mm_depth'
    option['size'] = '689'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 9.0
    option['dimensions']['outside'] = 17.0
    option['dimensions']['width'] = 5.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 13
    option['internal_geometry']['balls_per_row'] = 13
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 9.0
    option['internal_geometry']['parameters']['outside'] = 17.0
    option['internal_geometry']['parameters']['width'] = 5.0
    option['internal_geometry']['parameters']['edge'] = 0.24
    option['internal_geometry']['parameters']['pitch_radius'] = 6.5
    option['internal_geometry']['parameters']['ball_radius'] = 1.12
    option['internal_geometry']['parameters']['groove_radius'] = 1.1480000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 5.8056
    option['internal_geometry']['parameters']['outer_shoulder'] = 7.1944
    option['internal_geometry']['parameters']['cage_half_width'] = 0.6160000000000001
    option['internal_geometry']['parameters']['cage_low'] = 1.064
    option['internal_geometry']['parameters']['cage_high'] = 1.288
    option['internal_geometry']['parameters']['window_radius'] = 0.5376000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '3'
    options.append(copy.deepcopy(option))

    # 693: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_693_size_3_mm_id_8_mm_od_4_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_693_size_3_mm_id_8_mm_od_4_mm_depth'
    option['size'] = '693'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 3.0
    option['dimensions']['outside'] = 8.0
    option['dimensions']['width'] = 4.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 3.0
    option['internal_geometry']['parameters']['outside'] = 8.0
    option['internal_geometry']['parameters']['width'] = 4.0
    option['internal_geometry']['parameters']['edge'] = 0.15
    option['internal_geometry']['parameters']['pitch_radius'] = 2.75
    option['internal_geometry']['parameters']['ball_radius'] = 0.7000000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 0.7175
    option['internal_geometry']['parameters']['inner_shoulder'] = 2.316
    option['internal_geometry']['parameters']['outer_shoulder'] = 3.184
    option['internal_geometry']['parameters']['cage_half_width'] = 0.38500000000000006
    option['internal_geometry']['parameters']['cage_low'] = 0.665
    option['internal_geometry']['parameters']['cage_high'] = 0.805
    option['internal_geometry']['parameters']['window_radius'] = 0.336
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1'
    options.append(copy.deepcopy(option))

    # 694: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_694_size_4_mm_id_11_mm_od_4_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_694_size_4_mm_id_11_mm_od_4_mm_depth'
    option['size'] = '694'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 4.0
    option['dimensions']['outside'] = 11.0
    option['dimensions']['width'] = 4.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 4.0
    option['internal_geometry']['parameters']['outside'] = 11.0
    option['internal_geometry']['parameters']['width'] = 4.0
    option['internal_geometry']['parameters']['edge'] = 0.21
    option['internal_geometry']['parameters']['pitch_radius'] = 3.75
    option['internal_geometry']['parameters']['ball_radius'] = 0.9800000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 1.0045000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 3.1424
    option['internal_geometry']['parameters']['outer_shoulder'] = 4.3576
    option['internal_geometry']['parameters']['cage_half_width'] = 0.5390000000000001
    option['internal_geometry']['parameters']['cage_low'] = 0.931
    option['internal_geometry']['parameters']['cage_high'] = 1.127
    option['internal_geometry']['parameters']['window_radius'] = 0.47040000000000004
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '2'
    options.append(copy.deepcopy(option))

    # 695: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_695_size_5_mm_id_13_mm_od_4_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_695_size_5_mm_id_13_mm_od_4_mm_depth'
    option['size'] = '695'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 5.0
    option['dimensions']['outside'] = 13.0
    option['dimensions']['width'] = 4.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 9
    option['internal_geometry']['balls_per_row'] = 9
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 5.0
    option['internal_geometry']['parameters']['outside'] = 13.0
    option['internal_geometry']['parameters']['width'] = 4.0
    option['internal_geometry']['parameters']['edge'] = 0.24
    option['internal_geometry']['parameters']['pitch_radius'] = 4.5
    option['internal_geometry']['parameters']['ball_radius'] = 1.12
    option['internal_geometry']['parameters']['groove_radius'] = 1.1480000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 3.8056
    option['internal_geometry']['parameters']['outer_shoulder'] = 5.1944
    option['internal_geometry']['parameters']['cage_half_width'] = 0.6160000000000001
    option['internal_geometry']['parameters']['cage_low'] = 1.064
    option['internal_geometry']['parameters']['cage_high'] = 1.288
    option['internal_geometry']['parameters']['window_radius'] = 0.5376000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '2'
    options.append(copy.deepcopy(option))

    # 696: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_696_size_6_mm_id_15_mm_od_5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_696_size_6_mm_id_15_mm_od_5_mm_depth'
    option['size'] = '696'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 6.0
    option['dimensions']['outside'] = 15.0
    option['dimensions']['width'] = 5.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 9
    option['internal_geometry']['balls_per_row'] = 9
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 6.0
    option['internal_geometry']['parameters']['outside'] = 15.0
    option['internal_geometry']['parameters']['width'] = 5.0
    option['internal_geometry']['parameters']['edge'] = 0.27
    option['internal_geometry']['parameters']['pitch_radius'] = 5.25
    option['internal_geometry']['parameters']['ball_radius'] = 1.2600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.2915000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 4.4688
    option['internal_geometry']['parameters']['outer_shoulder'] = 6.0312
    option['internal_geometry']['parameters']['cage_half_width'] = 0.6930000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.197
    option['internal_geometry']['parameters']['cage_high'] = 1.449
    option['internal_geometry']['parameters']['window_radius'] = 0.6048000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '4'
    options.append(copy.deepcopy(option))

    # 697: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_697_size_7_mm_id_17_mm_od_5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_697_size_7_mm_id_17_mm_od_5_mm_depth'
    option['size'] = '697'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 7.0
    option['dimensions']['outside'] = 17.0
    option['dimensions']['width'] = 5.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 9
    option['internal_geometry']['balls_per_row'] = 9
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 7.0
    option['internal_geometry']['parameters']['outside'] = 17.0
    option['internal_geometry']['parameters']['width'] = 5.0
    option['internal_geometry']['parameters']['edge'] = 0.3
    option['internal_geometry']['parameters']['pitch_radius'] = 6.0
    option['internal_geometry']['parameters']['ball_radius'] = 1.4000000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 1.435
    option['internal_geometry']['parameters']['inner_shoulder'] = 5.132
    option['internal_geometry']['parameters']['outer_shoulder'] = 6.868
    option['internal_geometry']['parameters']['cage_half_width'] = 0.7700000000000001
    option['internal_geometry']['parameters']['cage_low'] = 1.33
    option['internal_geometry']['parameters']['cage_high'] = 1.61
    option['internal_geometry']['parameters']['window_radius'] = 0.672
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '5'
    options.append(copy.deepcopy(option))

    # 698: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_698_size_8_mm_id_19_mm_od_6_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_698_size_8_mm_id_19_mm_od_6_mm_depth'
    option['size'] = '698'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 8.0
    option['dimensions']['outside'] = 19.0
    option['dimensions']['width'] = 6.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 10
    option['internal_geometry']['balls_per_row'] = 10
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 8.0
    option['internal_geometry']['parameters']['outside'] = 19.0
    option['internal_geometry']['parameters']['width'] = 6.0
    option['internal_geometry']['parameters']['edge'] = 0.32999999999999996
    option['internal_geometry']['parameters']['pitch_radius'] = 6.75
    option['internal_geometry']['parameters']['ball_radius'] = 1.54
    option['internal_geometry']['parameters']['groove_radius'] = 1.5785
    option['internal_geometry']['parameters']['inner_shoulder'] = 5.7952
    option['internal_geometry']['parameters']['outer_shoulder'] = 7.7048
    option['internal_geometry']['parameters']['cage_half_width'] = 0.8470000000000001
    option['internal_geometry']['parameters']['cage_low'] = 1.4629999999999999
    option['internal_geometry']['parameters']['cage_high'] = 1.771
    option['internal_geometry']['parameters']['window_radius'] = 0.7392
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '7'
    options.append(copy.deepcopy(option))

    # 699: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_600_series_699_size_9_mm_id_20_mm_od_6_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_600_series_699_size_9_mm_id_20_mm_od_6_mm_depth'
    option['size'] = '699'
    option['series'] = '600'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 9.0
    option['dimensions']['outside'] = 20.0
    option['dimensions']['width'] = 6.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 10
    option['internal_geometry']['balls_per_row'] = 10
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 9.0
    option['internal_geometry']['parameters']['outside'] = 20.0
    option['internal_geometry']['parameters']['width'] = 6.0
    option['internal_geometry']['parameters']['edge'] = 0.32999999999999996
    option['internal_geometry']['parameters']['pitch_radius'] = 7.25
    option['internal_geometry']['parameters']['ball_radius'] = 1.54
    option['internal_geometry']['parameters']['groove_radius'] = 1.5785
    option['internal_geometry']['parameters']['inner_shoulder'] = 6.2952
    option['internal_geometry']['parameters']['outer_shoulder'] = 8.2048
    option['internal_geometry']['parameters']['cage_half_width'] = 0.8470000000000001
    option['internal_geometry']['parameters']['cage_low'] = 1.4629999999999999
    option['internal_geometry']['parameters']['cage_high'] = 1.771
    option['internal_geometry']['parameters']['window_radius'] = 0.7392
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '8'
    options.append(copy.deepcopy(option))

    # 61800: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_61800_series_61800_size_10_mm_id_19_mm_od_5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_61800_series_61800_size_10_mm_id_19_mm_od_5_mm_depth'
    option['size'] = '61800'
    option['series'] = '61800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 10.0
    option['dimensions']['outside'] = 19.0
    option['dimensions']['width'] = 5.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 13
    option['internal_geometry']['balls_per_row'] = 13
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 10.0
    option['internal_geometry']['parameters']['outside'] = 19.0
    option['internal_geometry']['parameters']['width'] = 5.0
    option['internal_geometry']['parameters']['edge'] = 0.27
    option['internal_geometry']['parameters']['pitch_radius'] = 7.25
    option['internal_geometry']['parameters']['ball_radius'] = 1.2600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.2915000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 6.4688
    option['internal_geometry']['parameters']['outer_shoulder'] = 8.0312
    option['internal_geometry']['parameters']['cage_half_width'] = 0.6930000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.197
    option['internal_geometry']['parameters']['cage_high'] = 1.449
    option['internal_geometry']['parameters']['window_radius'] = 0.6048000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '5'
    options.append(copy.deepcopy(option))

    # 61801: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_61800_series_61801_size_12_mm_id_21_mm_od_5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_61800_series_61801_size_12_mm_id_21_mm_od_5_mm_depth'
    option['size'] = '61801'
    option['series'] = '61800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 12.0
    option['dimensions']['outside'] = 21.0
    option['dimensions']['width'] = 5.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 15
    option['internal_geometry']['balls_per_row'] = 15
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 12.0
    option['internal_geometry']['parameters']['outside'] = 21.0
    option['internal_geometry']['parameters']['width'] = 5.0
    option['internal_geometry']['parameters']['edge'] = 0.27
    option['internal_geometry']['parameters']['pitch_radius'] = 8.25
    option['internal_geometry']['parameters']['ball_radius'] = 1.2600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.2915000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 7.4688
    option['internal_geometry']['parameters']['outer_shoulder'] = 9.0312
    option['internal_geometry']['parameters']['cage_half_width'] = 0.6930000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.197
    option['internal_geometry']['parameters']['cage_high'] = 1.449
    option['internal_geometry']['parameters']['window_radius'] = 0.6048000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '6'
    options.append(copy.deepcopy(option))

    # 61802: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_61800_series_61802_size_15_mm_id_24_mm_od_5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_61800_series_61802_size_15_mm_id_24_mm_od_5_mm_depth'
    option['size'] = '61802'
    option['series'] = '61800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 15.0
    option['dimensions']['outside'] = 24.0
    option['dimensions']['width'] = 5.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 17
    option['internal_geometry']['balls_per_row'] = 17
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 15.0
    option['internal_geometry']['parameters']['outside'] = 24.0
    option['internal_geometry']['parameters']['width'] = 5.0
    option['internal_geometry']['parameters']['edge'] = 0.27
    option['internal_geometry']['parameters']['pitch_radius'] = 9.75
    option['internal_geometry']['parameters']['ball_radius'] = 1.2600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.2915000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 8.9688
    option['internal_geometry']['parameters']['outer_shoulder'] = 10.5312
    option['internal_geometry']['parameters']['cage_half_width'] = 0.6930000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.197
    option['internal_geometry']['parameters']['cage_high'] = 1.449
    option['internal_geometry']['parameters']['window_radius'] = 0.6048000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '7'
    options.append(copy.deepcopy(option))

    # 61803: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_61800_series_61803_size_17_mm_id_26_mm_od_5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_61800_series_61803_size_17_mm_id_26_mm_od_5_mm_depth'
    option['size'] = '61803'
    option['series'] = '61800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 17.0
    option['dimensions']['outside'] = 26.0
    option['dimensions']['width'] = 5.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 19
    option['internal_geometry']['balls_per_row'] = 19
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 17.0
    option['internal_geometry']['parameters']['outside'] = 26.0
    option['internal_geometry']['parameters']['width'] = 5.0
    option['internal_geometry']['parameters']['edge'] = 0.27
    option['internal_geometry']['parameters']['pitch_radius'] = 10.75
    option['internal_geometry']['parameters']['ball_radius'] = 1.2600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.2915000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 9.9688
    option['internal_geometry']['parameters']['outer_shoulder'] = 11.5312
    option['internal_geometry']['parameters']['cage_half_width'] = 0.6930000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.197
    option['internal_geometry']['parameters']['cage_high'] = 1.449
    option['internal_geometry']['parameters']['window_radius'] = 0.6048000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '8'
    options.append(copy.deepcopy(option))

    # 61804: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_61800_series_61804_size_20_mm_id_32_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_61800_series_61804_size_20_mm_id_32_mm_od_7_mm_depth'
    option['size'] = '61804'
    option['series'] = '61800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 20.0
    option['dimensions']['outside'] = 32.0
    option['dimensions']['width'] = 7.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 17
    option['internal_geometry']['balls_per_row'] = 17
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 20.0
    option['internal_geometry']['parameters']['outside'] = 32.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.36
    option['internal_geometry']['parameters']['pitch_radius'] = 13.0
    option['internal_geometry']['parameters']['ball_radius'] = 1.6800000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.7220000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 11.9584
    option['internal_geometry']['parameters']['outer_shoulder'] = 14.0416
    option['internal_geometry']['parameters']['cage_half_width'] = 0.9240000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.596
    option['internal_geometry']['parameters']['cage_high'] = 1.932
    option['internal_geometry']['parameters']['window_radius'] = 0.8064
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '19'
    options.append(copy.deepcopy(option))

    # 61805: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_61800_series_61805_size_25_mm_id_37_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_61800_series_61805_size_25_mm_id_37_mm_od_7_mm_depth'
    option['size'] = '61805'
    option['series'] = '61800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 25.0
    option['dimensions']['outside'] = 37.0
    option['dimensions']['width'] = 7.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 21
    option['internal_geometry']['balls_per_row'] = 21
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 25.0
    option['internal_geometry']['parameters']['outside'] = 37.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.36
    option['internal_geometry']['parameters']['pitch_radius'] = 15.5
    option['internal_geometry']['parameters']['ball_radius'] = 1.6800000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.7220000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 14.4584
    option['internal_geometry']['parameters']['outer_shoulder'] = 16.5416
    option['internal_geometry']['parameters']['cage_half_width'] = 0.9240000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.596
    option['internal_geometry']['parameters']['cage_high'] = 1.932
    option['internal_geometry']['parameters']['window_radius'] = 0.8064
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '22'
    options.append(copy.deepcopy(option))

    # 61806: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_61800_series_61806_size_30_mm_id_42_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_61800_series_61806_size_30_mm_id_42_mm_od_7_mm_depth'
    option['size'] = '61806'
    option['series'] = '61800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 30.0
    option['dimensions']['outside'] = 42.0
    option['dimensions']['width'] = 7.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 24
    option['internal_geometry']['balls_per_row'] = 24
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 30.0
    option['internal_geometry']['parameters']['outside'] = 42.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.36
    option['internal_geometry']['parameters']['pitch_radius'] = 18.0
    option['internal_geometry']['parameters']['ball_radius'] = 1.6800000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.7220000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 16.9584
    option['internal_geometry']['parameters']['outer_shoulder'] = 19.0416
    option['internal_geometry']['parameters']['cage_half_width'] = 0.9240000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.596
    option['internal_geometry']['parameters']['cage_high'] = 1.932
    option['internal_geometry']['parameters']['window_radius'] = 0.8064
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '26'
    options.append(copy.deepcopy(option))

    # 61807: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_61800_series_61807_size_35_mm_id_47_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_61800_series_61807_size_35_mm_id_47_mm_od_7_mm_depth'
    option['size'] = '61807'
    option['series'] = '61800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 35.0
    option['dimensions']['outside'] = 47.0
    option['dimensions']['width'] = 7.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 28
    option['internal_geometry']['balls_per_row'] = 28
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 35.0
    option['internal_geometry']['parameters']['outside'] = 47.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.36
    option['internal_geometry']['parameters']['pitch_radius'] = 20.5
    option['internal_geometry']['parameters']['ball_radius'] = 1.6800000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.7220000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 19.4584
    option['internal_geometry']['parameters']['outer_shoulder'] = 21.5416
    option['internal_geometry']['parameters']['cage_half_width'] = 0.9240000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.596
    option['internal_geometry']['parameters']['cage_high'] = 1.932
    option['internal_geometry']['parameters']['window_radius'] = 0.8064
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '29'
    options.append(copy.deepcopy(option))

    # 61808: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_61800_series_61808_size_40_mm_id_52_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_61800_series_61808_size_40_mm_id_52_mm_od_7_mm_depth'
    option['size'] = '61808'
    option['series'] = '61800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 40.0
    option['dimensions']['outside'] = 52.0
    option['dimensions']['width'] = 7.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 31
    option['internal_geometry']['balls_per_row'] = 31
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 40.0
    option['internal_geometry']['parameters']['outside'] = 52.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.36
    option['internal_geometry']['parameters']['pitch_radius'] = 23.0
    option['internal_geometry']['parameters']['ball_radius'] = 1.6800000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.7220000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 21.9584
    option['internal_geometry']['parameters']['outer_shoulder'] = 24.0416
    option['internal_geometry']['parameters']['cage_half_width'] = 0.9240000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.596
    option['internal_geometry']['parameters']['cage_high'] = 1.932
    option['internal_geometry']['parameters']['window_radius'] = 0.8064
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '33'
    options.append(copy.deepcopy(option))

    # 61809: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_61800_series_61809_size_45_mm_id_58_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_61800_series_61809_size_45_mm_id_58_mm_od_7_mm_depth'
    option['size'] = '61809'
    option['series'] = '61800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 45.0
    option['dimensions']['outside'] = 58.0
    option['dimensions']['width'] = 7.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 32
    option['internal_geometry']['balls_per_row'] = 32
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 45.0
    option['internal_geometry']['parameters']['outside'] = 58.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.39
    option['internal_geometry']['parameters']['pitch_radius'] = 25.75
    option['internal_geometry']['parameters']['ball_radius'] = 1.8200000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 1.8655000000000004
    option['internal_geometry']['parameters']['inner_shoulder'] = 24.6216
    option['internal_geometry']['parameters']['outer_shoulder'] = 26.8784
    option['internal_geometry']['parameters']['cage_half_width'] = 1.0010000000000003
    option['internal_geometry']['parameters']['cage_low'] = 1.729
    option['internal_geometry']['parameters']['cage_high'] = 2.093
    option['internal_geometry']['parameters']['window_radius'] = 0.8736000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '40'
    options.append(copy.deepcopy(option))

    # 61810: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_61800_series_61810_size_50_mm_id_65_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_61800_series_61810_size_50_mm_id_65_mm_od_7_mm_depth'
    option['size'] = '61810'
    option['series'] = '61800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 50.0
    option['dimensions']['outside'] = 65.0
    option['dimensions']['width'] = 7.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 34
    option['internal_geometry']['balls_per_row'] = 34
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 50.0
    option['internal_geometry']['parameters']['outside'] = 65.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.42
    option['internal_geometry']['parameters']['pitch_radius'] = 28.75
    option['internal_geometry']['parameters']['ball_radius'] = 1.9600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 2.0090000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 27.5348
    option['internal_geometry']['parameters']['outer_shoulder'] = 29.9652
    option['internal_geometry']['parameters']['cage_half_width'] = 1.0780000000000003
    option['internal_geometry']['parameters']['cage_low'] = 1.862
    option['internal_geometry']['parameters']['cage_high'] = 2.254
    option['internal_geometry']['parameters']['window_radius'] = 0.9408000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '52'
    options.append(copy.deepcopy(option))

    # 61811: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_61800_series_61811_size_55_mm_id_72_mm_od_9_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_61800_series_61811_size_55_mm_id_72_mm_od_9_mm_depth'
    option['size'] = '61811'
    option['series'] = '61800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 55.0
    option['dimensions']['outside'] = 72.0
    option['dimensions']['width'] = 9.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 30
    option['internal_geometry']['balls_per_row'] = 30
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 55.0
    option['internal_geometry']['parameters']['outside'] = 72.0
    option['internal_geometry']['parameters']['width'] = 9.0
    option['internal_geometry']['parameters']['edge'] = 0.51
    option['internal_geometry']['parameters']['pitch_radius'] = 31.75
    option['internal_geometry']['parameters']['ball_radius'] = 2.3800000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 2.4395000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 30.2744
    option['internal_geometry']['parameters']['outer_shoulder'] = 33.2256
    option['internal_geometry']['parameters']['cage_half_width'] = 1.3090000000000004
    option['internal_geometry']['parameters']['cage_low'] = 2.261
    option['internal_geometry']['parameters']['cage_high'] = 2.737
    option['internal_geometry']['parameters']['window_radius'] = 1.1424
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '83'
    options.append(copy.deepcopy(option))

    # 61812: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_61800_series_61812_size_60_mm_id_78_mm_od_10_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_61800_series_61812_size_60_mm_id_78_mm_od_10_mm_depth'
    option['size'] = '61812'
    option['series'] = '61800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 60.0
    option['dimensions']['outside'] = 78.0
    option['dimensions']['width'] = 10.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 31
    option['internal_geometry']['balls_per_row'] = 31
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 60.0
    option['internal_geometry']['parameters']['outside'] = 78.0
    option['internal_geometry']['parameters']['width'] = 10.0
    option['internal_geometry']['parameters']['edge'] = 0.54
    option['internal_geometry']['parameters']['pitch_radius'] = 34.5
    option['internal_geometry']['parameters']['ball_radius'] = 2.5200000000000005
    option['internal_geometry']['parameters']['groove_radius'] = 2.5830000000000006
    option['internal_geometry']['parameters']['inner_shoulder'] = 32.9376
    option['internal_geometry']['parameters']['outer_shoulder'] = 36.0624
    option['internal_geometry']['parameters']['cage_half_width'] = 1.3860000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.394
    option['internal_geometry']['parameters']['cage_high'] = 2.898
    option['internal_geometry']['parameters']['window_radius'] = 1.2096000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '104'
    options.append(copy.deepcopy(option))

    # 61813: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_61800_series_61813_size_65_mm_id_85_mm_od_10_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_61800_series_61813_size_65_mm_id_85_mm_od_10_mm_depth'
    option['size'] = '61813'
    option['series'] = '61800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 65.0
    option['dimensions']['outside'] = 85.0
    option['dimensions']['width'] = 10.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 31
    option['internal_geometry']['balls_per_row'] = 31
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 65.0
    option['internal_geometry']['parameters']['outside'] = 85.0
    option['internal_geometry']['parameters']['width'] = 10.0
    option['internal_geometry']['parameters']['edge'] = 0.6
    option['internal_geometry']['parameters']['pitch_radius'] = 37.5
    option['internal_geometry']['parameters']['ball_radius'] = 2.8000000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 2.87
    option['internal_geometry']['parameters']['inner_shoulder'] = 35.764
    option['internal_geometry']['parameters']['outer_shoulder'] = 39.236
    option['internal_geometry']['parameters']['cage_half_width'] = 1.5400000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.66
    option['internal_geometry']['parameters']['cage_high'] = 3.22
    option['internal_geometry']['parameters']['window_radius'] = 1.344
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '126'
    options.append(copy.deepcopy(option))

    # 61814: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_61800_series_61814_size_70_mm_id_90_mm_od_10_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_61800_series_61814_size_70_mm_id_90_mm_od_10_mm_depth'
    option['size'] = '61814'
    option['series'] = '61800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 70.0
    option['dimensions']['outside'] = 90.0
    option['dimensions']['width'] = 10.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 33
    option['internal_geometry']['balls_per_row'] = 33
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 70.0
    option['internal_geometry']['parameters']['outside'] = 90.0
    option['internal_geometry']['parameters']['width'] = 10.0
    option['internal_geometry']['parameters']['edge'] = 0.6
    option['internal_geometry']['parameters']['pitch_radius'] = 40.0
    option['internal_geometry']['parameters']['ball_radius'] = 2.8000000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 2.87
    option['internal_geometry']['parameters']['inner_shoulder'] = 38.264
    option['internal_geometry']['parameters']['outer_shoulder'] = 41.736
    option['internal_geometry']['parameters']['cage_half_width'] = 1.5400000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.66
    option['internal_geometry']['parameters']['cage_high'] = 3.22
    option['internal_geometry']['parameters']['window_radius'] = 1.344
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '134'
    options.append(copy.deepcopy(option))

    # 61815: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_61800_series_61815_size_75_mm_id_95_mm_od_10_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_61800_series_61815_size_75_mm_id_95_mm_od_10_mm_depth'
    option['size'] = '61815'
    option['series'] = '61800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 75.0
    option['dimensions']['outside'] = 95.0
    option['dimensions']['width'] = 10.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 35
    option['internal_geometry']['balls_per_row'] = 35
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 75.0
    option['internal_geometry']['parameters']['outside'] = 95.0
    option['internal_geometry']['parameters']['width'] = 10.0
    option['internal_geometry']['parameters']['edge'] = 0.6
    option['internal_geometry']['parameters']['pitch_radius'] = 42.5
    option['internal_geometry']['parameters']['ball_radius'] = 2.8000000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 2.87
    option['internal_geometry']['parameters']['inner_shoulder'] = 40.764
    option['internal_geometry']['parameters']['outer_shoulder'] = 44.236
    option['internal_geometry']['parameters']['cage_half_width'] = 1.5400000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.66
    option['internal_geometry']['parameters']['cage_high'] = 3.22
    option['internal_geometry']['parameters']['window_radius'] = 1.344
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '142'
    options.append(copy.deepcopy(option))

    # 61816: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_61800_series_61816_size_80_mm_id_100_mm_od_10_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_61800_series_61816_size_80_mm_id_100_mm_od_10_mm_depth'
    option['size'] = '61816'
    option['series'] = '61800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 80.0
    option['dimensions']['outside'] = 100.0
    option['dimensions']['width'] = 10.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 37
    option['internal_geometry']['balls_per_row'] = 37
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 80.0
    option['internal_geometry']['parameters']['outside'] = 100.0
    option['internal_geometry']['parameters']['width'] = 10.0
    option['internal_geometry']['parameters']['edge'] = 0.6
    option['internal_geometry']['parameters']['pitch_radius'] = 45.0
    option['internal_geometry']['parameters']['ball_radius'] = 2.8000000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 2.87
    option['internal_geometry']['parameters']['inner_shoulder'] = 43.264
    option['internal_geometry']['parameters']['outer_shoulder'] = 46.736
    option['internal_geometry']['parameters']['cage_half_width'] = 1.5400000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.66
    option['internal_geometry']['parameters']['cage_high'] = 3.22
    option['internal_geometry']['parameters']['window_radius'] = 1.344
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '150'
    options.append(copy.deepcopy(option))

    # 61817: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_61800_series_61817_size_85_mm_id_110_mm_od_13_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_61800_series_61817_size_85_mm_id_110_mm_od_13_mm_depth'
    option['size'] = '61817'
    option['series'] = '61800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 85.0
    option['dimensions']['outside'] = 110.0
    option['dimensions']['width'] = 13.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 32
    option['internal_geometry']['balls_per_row'] = 32
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 85.0
    option['internal_geometry']['parameters']['outside'] = 110.0
    option['internal_geometry']['parameters']['width'] = 13.0
    option['internal_geometry']['parameters']['edge'] = 0.75
    option['internal_geometry']['parameters']['pitch_radius'] = 48.75
    option['internal_geometry']['parameters']['ball_radius'] = 3.5000000000000004
    option['internal_geometry']['parameters']['groove_radius'] = 3.5875000000000004
    option['internal_geometry']['parameters']['inner_shoulder'] = 46.58
    option['internal_geometry']['parameters']['outer_shoulder'] = 50.92
    option['internal_geometry']['parameters']['cage_half_width'] = 1.9250000000000005
    option['internal_geometry']['parameters']['cage_low'] = 3.325
    option['internal_geometry']['parameters']['cage_high'] = 4.025
    option['internal_geometry']['parameters']['window_radius'] = 1.6800000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '266'
    options.append(copy.deepcopy(option))

    # 61818: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_61800_series_61818_size_90_mm_id_115_mm_od_13_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_61800_series_61818_size_90_mm_id_115_mm_od_13_mm_depth'
    option['size'] = '61818'
    option['series'] = '61800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 90.0
    option['dimensions']['outside'] = 115.0
    option['dimensions']['width'] = 13.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 34
    option['internal_geometry']['balls_per_row'] = 34
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 90.0
    option['internal_geometry']['parameters']['outside'] = 115.0
    option['internal_geometry']['parameters']['width'] = 13.0
    option['internal_geometry']['parameters']['edge'] = 0.75
    option['internal_geometry']['parameters']['pitch_radius'] = 51.25
    option['internal_geometry']['parameters']['ball_radius'] = 3.5000000000000004
    option['internal_geometry']['parameters']['groove_radius'] = 3.5875000000000004
    option['internal_geometry']['parameters']['inner_shoulder'] = 49.08
    option['internal_geometry']['parameters']['outer_shoulder'] = 53.42
    option['internal_geometry']['parameters']['cage_half_width'] = 1.9250000000000005
    option['internal_geometry']['parameters']['cage_low'] = 3.325
    option['internal_geometry']['parameters']['cage_high'] = 4.025
    option['internal_geometry']['parameters']['window_radius'] = 1.6800000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '279'
    options.append(copy.deepcopy(option))

    # 61819: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_61800_series_61819_size_95_mm_id_120_mm_od_13_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_61800_series_61819_size_95_mm_id_120_mm_od_13_mm_depth'
    option['size'] = '61819'
    option['series'] = '61800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 95.0
    option['dimensions']['outside'] = 120.0
    option['dimensions']['width'] = 13.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 35
    option['internal_geometry']['balls_per_row'] = 35
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 95.0
    option['internal_geometry']['parameters']['outside'] = 120.0
    option['internal_geometry']['parameters']['width'] = 13.0
    option['internal_geometry']['parameters']['edge'] = 0.75
    option['internal_geometry']['parameters']['pitch_radius'] = 53.75
    option['internal_geometry']['parameters']['ball_radius'] = 3.5000000000000004
    option['internal_geometry']['parameters']['groove_radius'] = 3.5875000000000004
    option['internal_geometry']['parameters']['inner_shoulder'] = 51.58
    option['internal_geometry']['parameters']['outer_shoulder'] = 55.92
    option['internal_geometry']['parameters']['cage_half_width'] = 1.9250000000000005
    option['internal_geometry']['parameters']['cage_low'] = 3.325
    option['internal_geometry']['parameters']['cage_high'] = 4.025
    option['internal_geometry']['parameters']['window_radius'] = 1.6800000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '704'
    options.append(copy.deepcopy(option))

    # 61820: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_61800_series_61820_size_100_mm_id_125_mm_od_13_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_61800_series_61820_size_100_mm_id_125_mm_od_13_mm_depth'
    option['size'] = '61820'
    option['series'] = '61800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 100.0
    option['dimensions']['outside'] = 125.0
    option['dimensions']['width'] = 13.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 37
    option['internal_geometry']['balls_per_row'] = 37
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 100.0
    option['internal_geometry']['parameters']['outside'] = 125.0
    option['internal_geometry']['parameters']['width'] = 13.0
    option['internal_geometry']['parameters']['edge'] = 0.75
    option['internal_geometry']['parameters']['pitch_radius'] = 56.25
    option['internal_geometry']['parameters']['ball_radius'] = 3.5000000000000004
    option['internal_geometry']['parameters']['groove_radius'] = 3.5875000000000004
    option['internal_geometry']['parameters']['inner_shoulder'] = 54.08
    option['internal_geometry']['parameters']['outer_shoulder'] = 58.42
    option['internal_geometry']['parameters']['cage_half_width'] = 1.9250000000000005
    option['internal_geometry']['parameters']['cage_low'] = 3.325
    option['internal_geometry']['parameters']['cage_high'] = 4.025
    option['internal_geometry']['parameters']['window_radius'] = 1.6800000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '309'
    options.append(copy.deepcopy(option))

    # 61821: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_61800_series_61821_size_105_mm_id_130_mm_od_13_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_61800_series_61821_size_105_mm_id_130_mm_od_13_mm_depth'
    option['size'] = '61821'
    option['series'] = '61800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 105.0
    option['dimensions']['outside'] = 130.0
    option['dimensions']['width'] = 13.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 39
    option['internal_geometry']['balls_per_row'] = 39
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 105.0
    option['internal_geometry']['parameters']['outside'] = 130.0
    option['internal_geometry']['parameters']['width'] = 13.0
    option['internal_geometry']['parameters']['edge'] = 0.75
    option['internal_geometry']['parameters']['pitch_radius'] = 58.75
    option['internal_geometry']['parameters']['ball_radius'] = 3.5000000000000004
    option['internal_geometry']['parameters']['groove_radius'] = 3.5875000000000004
    option['internal_geometry']['parameters']['inner_shoulder'] = 56.58
    option['internal_geometry']['parameters']['outer_shoulder'] = 60.92
    option['internal_geometry']['parameters']['cage_half_width'] = 1.9250000000000005
    option['internal_geometry']['parameters']['cage_low'] = 3.325
    option['internal_geometry']['parameters']['cage_high'] = 4.025
    option['internal_geometry']['parameters']['window_radius'] = 1.6800000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '324'
    options.append(copy.deepcopy(option))

    # 61822: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_61800_series_61822_size_110_mm_id_140_mm_od_16_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_61800_series_61822_size_110_mm_id_140_mm_od_16_mm_depth'
    option['size'] = '61822'
    option['series'] = '61800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 110.0
    option['dimensions']['outside'] = 140.0
    option['dimensions']['width'] = 16.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 34
    option['internal_geometry']['balls_per_row'] = 34
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 110.0
    option['internal_geometry']['parameters']['outside'] = 140.0
    option['internal_geometry']['parameters']['width'] = 16.0
    option['internal_geometry']['parameters']['edge'] = 0.8999999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 62.5
    option['internal_geometry']['parameters']['ball_radius'] = 4.2
    option['internal_geometry']['parameters']['groove_radius'] = 4.305000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 59.896
    option['internal_geometry']['parameters']['outer_shoulder'] = 65.104
    option['internal_geometry']['parameters']['cage_half_width'] = 2.3100000000000005
    option['internal_geometry']['parameters']['cage_low'] = 3.9899999999999998
    option['internal_geometry']['parameters']['cage_high'] = 4.83
    option['internal_geometry']['parameters']['window_radius'] = 2.016
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '605'
    options.append(copy.deepcopy(option))

    # 61824: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_61800_series_61824_size_120_mm_id_150_mm_od_16_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_61800_series_61824_size_120_mm_id_150_mm_od_16_mm_depth'
    option['size'] = '61824'
    option['series'] = '61800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 120.0
    option['dimensions']['outside'] = 150.0
    option['dimensions']['width'] = 16.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 37
    option['internal_geometry']['balls_per_row'] = 37
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 120.0
    option['internal_geometry']['parameters']['outside'] = 150.0
    option['internal_geometry']['parameters']['width'] = 16.0
    option['internal_geometry']['parameters']['edge'] = 0.8999999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 67.5
    option['internal_geometry']['parameters']['ball_radius'] = 4.2
    option['internal_geometry']['parameters']['groove_radius'] = 4.305000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 64.896
    option['internal_geometry']['parameters']['outer_shoulder'] = 70.104
    option['internal_geometry']['parameters']['cage_half_width'] = 2.3100000000000005
    option['internal_geometry']['parameters']['cage_low'] = 3.9899999999999998
    option['internal_geometry']['parameters']['cage_high'] = 4.83
    option['internal_geometry']['parameters']['window_radius'] = 2.016
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '654'
    options.append(copy.deepcopy(option))

    # 61826: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_61800_series_61826_size_130_mm_id_165_mm_od_18_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_61800_series_61826_size_130_mm_id_165_mm_od_18_mm_depth'
    option['size'] = '61826'
    option['series'] = '61800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 130.0
    option['dimensions']['outside'] = 165.0
    option['dimensions']['width'] = 18.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 34
    option['internal_geometry']['balls_per_row'] = 34
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 130.0
    option['internal_geometry']['parameters']['outside'] = 165.0
    option['internal_geometry']['parameters']['width'] = 18.0
    option['internal_geometry']['parameters']['edge'] = 1.05
    option['internal_geometry']['parameters']['pitch_radius'] = 73.75
    option['internal_geometry']['parameters']['ball_radius'] = 4.9
    option['internal_geometry']['parameters']['groove_radius'] = 5.0225
    option['internal_geometry']['parameters']['inner_shoulder'] = 70.712
    option['internal_geometry']['parameters']['outer_shoulder'] = 76.788
    option['internal_geometry']['parameters']['cage_half_width'] = 2.6950000000000003
    option['internal_geometry']['parameters']['cage_low'] = 4.655
    option['internal_geometry']['parameters']['cage_high'] = 5.635
    option['internal_geometry']['parameters']['window_radius'] = 2.352
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '938'
    options.append(copy.deepcopy(option))

    # 61828: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_61800_series_61828_size_140_mm_id_175_mm_od_18_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_61800_series_61828_size_140_mm_id_175_mm_od_18_mm_depth'
    option['size'] = '61828'
    option['series'] = '61800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 140.0
    option['dimensions']['outside'] = 175.0
    option['dimensions']['width'] = 18.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 37
    option['internal_geometry']['balls_per_row'] = 37
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 140.0
    option['internal_geometry']['parameters']['outside'] = 175.0
    option['internal_geometry']['parameters']['width'] = 18.0
    option['internal_geometry']['parameters']['edge'] = 1.05
    option['internal_geometry']['parameters']['pitch_radius'] = 78.75
    option['internal_geometry']['parameters']['ball_radius'] = 4.9
    option['internal_geometry']['parameters']['groove_radius'] = 5.0225
    option['internal_geometry']['parameters']['inner_shoulder'] = 75.712
    option['internal_geometry']['parameters']['outer_shoulder'] = 81.788
    option['internal_geometry']['parameters']['cage_half_width'] = 2.6950000000000003
    option['internal_geometry']['parameters']['cage_low'] = 4.655
    option['internal_geometry']['parameters']['cage_high'] = 5.635
    option['internal_geometry']['parameters']['window_radius'] = 2.352
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '999'
    options.append(copy.deepcopy(option))

    # 61830: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_61800_series_61830_size_150_mm_id_190_mm_od_20_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_61800_series_61830_size_150_mm_id_190_mm_od_20_mm_depth'
    option['size'] = '61830'
    option['series'] = '61800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 150.0
    option['dimensions']['outside'] = 190.0
    option['dimensions']['width'] = 20.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 35
    option['internal_geometry']['balls_per_row'] = 35
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 150.0
    option['internal_geometry']['parameters']['outside'] = 190.0
    option['internal_geometry']['parameters']['width'] = 20.0
    option['internal_geometry']['parameters']['edge'] = 1.2
    option['internal_geometry']['parameters']['pitch_radius'] = 85.0
    option['internal_geometry']['parameters']['ball_radius'] = 5.6000000000000005
    option['internal_geometry']['parameters']['groove_radius'] = 5.74
    option['internal_geometry']['parameters']['inner_shoulder'] = 81.528
    option['internal_geometry']['parameters']['outer_shoulder'] = 88.472
    option['internal_geometry']['parameters']['cage_half_width'] = 3.0800000000000005
    option['internal_geometry']['parameters']['cage_low'] = 5.32
    option['internal_geometry']['parameters']['cage_high'] = 6.44
    option['internal_geometry']['parameters']['window_radius'] = 2.688
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1,398'
    options.append(copy.deepcopy(option))

    # 62200: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_62000_series_62200_size_10_mm_id_30_mm_od_14_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_62000_series_62200_size_10_mm_id_30_mm_od_14_mm_depth'
    option['size'] = '62200'
    option['series'] = '62000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 10.0
    option['dimensions']['outside'] = 30.0
    option['dimensions']['width'] = 14.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 10.0
    option['internal_geometry']['parameters']['outside'] = 30.0
    option['internal_geometry']['parameters']['width'] = 14.0
    option['internal_geometry']['parameters']['edge'] = 0.6
    option['internal_geometry']['parameters']['pitch_radius'] = 10.0
    option['internal_geometry']['parameters']['ball_radius'] = 2.8000000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 2.87
    option['internal_geometry']['parameters']['inner_shoulder'] = 8.264
    option['internal_geometry']['parameters']['outer_shoulder'] = 11.736
    option['internal_geometry']['parameters']['cage_half_width'] = 1.5400000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.66
    option['internal_geometry']['parameters']['cage_high'] = 3.22
    option['internal_geometry']['parameters']['window_radius'] = 1.344
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '44'
    options.append(copy.deepcopy(option))

    # 62201: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_62000_series_62201_size_12_mm_id_32_mm_od_14_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_62000_series_62201_size_12_mm_id_32_mm_od_14_mm_depth'
    option['size'] = '62201'
    option['series'] = '62000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 12.0
    option['dimensions']['outside'] = 32.0
    option['dimensions']['width'] = 14.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 12.0
    option['internal_geometry']['parameters']['outside'] = 32.0
    option['internal_geometry']['parameters']['width'] = 14.0
    option['internal_geometry']['parameters']['edge'] = 0.6
    option['internal_geometry']['parameters']['pitch_radius'] = 11.0
    option['internal_geometry']['parameters']['ball_radius'] = 2.8000000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 2.87
    option['internal_geometry']['parameters']['inner_shoulder'] = 9.264
    option['internal_geometry']['parameters']['outer_shoulder'] = 12.736
    option['internal_geometry']['parameters']['cage_half_width'] = 1.5400000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.66
    option['internal_geometry']['parameters']['cage_high'] = 3.22
    option['internal_geometry']['parameters']['window_radius'] = 1.344
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '53'
    options.append(copy.deepcopy(option))

    # 62202: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_62000_series_62202_size_15_mm_id_35_mm_od_14_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_62000_series_62202_size_15_mm_id_35_mm_od_14_mm_depth'
    option['size'] = '62202'
    option['series'] = '62000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 15.0
    option['dimensions']['outside'] = 35.0
    option['dimensions']['width'] = 14.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 10
    option['internal_geometry']['balls_per_row'] = 10
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 15.0
    option['internal_geometry']['parameters']['outside'] = 35.0
    option['internal_geometry']['parameters']['width'] = 14.0
    option['internal_geometry']['parameters']['edge'] = 0.6
    option['internal_geometry']['parameters']['pitch_radius'] = 12.5
    option['internal_geometry']['parameters']['ball_radius'] = 2.8000000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 2.87
    option['internal_geometry']['parameters']['inner_shoulder'] = 10.764
    option['internal_geometry']['parameters']['outer_shoulder'] = 14.236
    option['internal_geometry']['parameters']['cage_half_width'] = 1.5400000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.66
    option['internal_geometry']['parameters']['cage_high'] = 3.22
    option['internal_geometry']['parameters']['window_radius'] = 1.344
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '65'
    options.append(copy.deepcopy(option))

    # 62203: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_62000_series_62203_size_17_mm_id_40_mm_od_16_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_62000_series_62203_size_17_mm_id_40_mm_od_16_mm_depth'
    option['size'] = '62203'
    option['series'] = '62000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 17.0
    option['dimensions']['outside'] = 40.0
    option['dimensions']['width'] = 16.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 10
    option['internal_geometry']['balls_per_row'] = 10
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 17.0
    option['internal_geometry']['parameters']['outside'] = 40.0
    option['internal_geometry']['parameters']['width'] = 16.0
    option['internal_geometry']['parameters']['edge'] = 0.69
    option['internal_geometry']['parameters']['pitch_radius'] = 14.25
    option['internal_geometry']['parameters']['ball_radius'] = 3.22
    option['internal_geometry']['parameters']['groove_radius'] = 3.3005000000000004
    option['internal_geometry']['parameters']['inner_shoulder'] = 12.2536
    option['internal_geometry']['parameters']['outer_shoulder'] = 16.2464
    option['internal_geometry']['parameters']['cage_half_width'] = 1.7710000000000004
    option['internal_geometry']['parameters']['cage_low'] = 3.059
    option['internal_geometry']['parameters']['cage_high'] = 3.703
    option['internal_geometry']['parameters']['window_radius'] = 1.5456
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '96'
    options.append(copy.deepcopy(option))

    # 62204: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_62000_series_62204_size_20_mm_id_47_mm_od_18_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_62000_series_62204_size_20_mm_id_47_mm_od_18_mm_depth'
    option['size'] = '62204'
    option['series'] = '62000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 20.0
    option['dimensions']['outside'] = 47.0
    option['dimensions']['width'] = 18.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 10
    option['internal_geometry']['balls_per_row'] = 10
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 20.0
    option['internal_geometry']['parameters']['outside'] = 47.0
    option['internal_geometry']['parameters']['width'] = 18.0
    option['internal_geometry']['parameters']['edge'] = 0.8099999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 16.75
    option['internal_geometry']['parameters']['ball_radius'] = 3.7800000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 3.8745000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 14.4064
    option['internal_geometry']['parameters']['outer_shoulder'] = 19.093600000000002
    option['internal_geometry']['parameters']['cage_half_width'] = 2.079
    option['internal_geometry']['parameters']['cage_low'] = 3.591
    option['internal_geometry']['parameters']['cage_high'] = 4.3469999999999995
    option['internal_geometry']['parameters']['window_radius'] = 1.8144
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '145'
    options.append(copy.deepcopy(option))

    # 62205: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_62000_series_62205_size_25_mm_id_52_mm_od_18_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_62000_series_62205_size_25_mm_id_52_mm_od_18_mm_depth'
    option['size'] = '62205'
    option['series'] = '62000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 25.0
    option['dimensions']['outside'] = 52.0
    option['dimensions']['width'] = 18.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 11
    option['internal_geometry']['balls_per_row'] = 11
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 25.0
    option['internal_geometry']['parameters']['outside'] = 52.0
    option['internal_geometry']['parameters']['width'] = 18.0
    option['internal_geometry']['parameters']['edge'] = 0.8099999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 19.25
    option['internal_geometry']['parameters']['ball_radius'] = 3.7800000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 3.8745000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 16.906399999999998
    option['internal_geometry']['parameters']['outer_shoulder'] = 21.593600000000002
    option['internal_geometry']['parameters']['cage_half_width'] = 2.079
    option['internal_geometry']['parameters']['cage_low'] = 3.591
    option['internal_geometry']['parameters']['cage_high'] = 4.3469999999999995
    option['internal_geometry']['parameters']['window_radius'] = 1.8144
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '172'
    options.append(copy.deepcopy(option))

    # 62206: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_62000_series_62206_size_30_mm_id_62_mm_od_20_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_62000_series_62206_size_30_mm_id_62_mm_od_20_mm_depth'
    option['size'] = '62206'
    option['series'] = '62000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 30.0
    option['dimensions']['outside'] = 62.0
    option['dimensions']['width'] = 20.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 11
    option['internal_geometry']['balls_per_row'] = 11
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 30.0
    option['internal_geometry']['parameters']['outside'] = 62.0
    option['internal_geometry']['parameters']['width'] = 20.0
    option['internal_geometry']['parameters']['edge'] = 0.96
    option['internal_geometry']['parameters']['pitch_radius'] = 23.0
    option['internal_geometry']['parameters']['ball_radius'] = 4.48
    option['internal_geometry']['parameters']['groove_radius'] = 4.5920000000000005
    option['internal_geometry']['parameters']['inner_shoulder'] = 20.2224
    option['internal_geometry']['parameters']['outer_shoulder'] = 25.7776
    option['internal_geometry']['parameters']['cage_half_width'] = 2.4640000000000004
    option['internal_geometry']['parameters']['cage_low'] = 4.256
    option['internal_geometry']['parameters']['cage_high'] = 5.152
    option['internal_geometry']['parameters']['window_radius'] = 2.1504000000000003
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '275'
    options.append(copy.deepcopy(option))

    # 62207: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_62000_series_62207_size_35_mm_id_72_mm_od_23_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_62000_series_62207_size_35_mm_id_72_mm_od_23_mm_depth'
    option['size'] = '62207'
    option['series'] = '62000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 35.0
    option['dimensions']['outside'] = 72.0
    option['dimensions']['width'] = 23.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 11
    option['internal_geometry']['balls_per_row'] = 11
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 35.0
    option['internal_geometry']['parameters']['outside'] = 72.0
    option['internal_geometry']['parameters']['width'] = 23.0
    option['internal_geometry']['parameters']['edge'] = 1.1099999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 26.75
    option['internal_geometry']['parameters']['ball_radius'] = 5.180000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 5.309500000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 23.5384
    option['internal_geometry']['parameters']['outer_shoulder'] = 29.9616
    option['internal_geometry']['parameters']['cage_half_width'] = 2.8490000000000006
    option['internal_geometry']['parameters']['cage_low'] = 4.921
    option['internal_geometry']['parameters']['cage_high'] = 5.957
    option['internal_geometry']['parameters']['window_radius'] = 2.4864
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '410'
    options.append(copy.deepcopy(option))

    # 62208: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_62000_series_62208_size_40_mm_id_80_mm_od_23_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_62000_series_62208_size_40_mm_id_80_mm_od_23_mm_depth'
    option['size'] = '62208'
    option['series'] = '62000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 40.0
    option['dimensions']['outside'] = 80.0
    option['dimensions']['width'] = 23.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 12
    option['internal_geometry']['balls_per_row'] = 12
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 40.0
    option['internal_geometry']['parameters']['outside'] = 80.0
    option['internal_geometry']['parameters']['width'] = 23.0
    option['internal_geometry']['parameters']['edge'] = 1.2
    option['internal_geometry']['parameters']['pitch_radius'] = 30.0
    option['internal_geometry']['parameters']['ball_radius'] = 5.6000000000000005
    option['internal_geometry']['parameters']['groove_radius'] = 5.74
    option['internal_geometry']['parameters']['inner_shoulder'] = 26.528
    option['internal_geometry']['parameters']['outer_shoulder'] = 33.472
    option['internal_geometry']['parameters']['cage_half_width'] = 3.0800000000000005
    option['internal_geometry']['parameters']['cage_low'] = 5.32
    option['internal_geometry']['parameters']['cage_high'] = 6.44
    option['internal_geometry']['parameters']['window_radius'] = 2.688
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '615'
    options.append(copy.deepcopy(option))

    # 62209: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_62000_series_62209_size_45_mm_id_85_mm_od_23_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_62000_series_62209_size_45_mm_id_85_mm_od_23_mm_depth'
    option['size'] = '62209'
    option['series'] = '62000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 45.0
    option['dimensions']['outside'] = 85.0
    option['dimensions']['width'] = 23.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 13
    option['internal_geometry']['balls_per_row'] = 13
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 45.0
    option['internal_geometry']['parameters']['outside'] = 85.0
    option['internal_geometry']['parameters']['width'] = 23.0
    option['internal_geometry']['parameters']['edge'] = 1.2
    option['internal_geometry']['parameters']['pitch_radius'] = 32.5
    option['internal_geometry']['parameters']['ball_radius'] = 5.6000000000000005
    option['internal_geometry']['parameters']['groove_radius'] = 5.74
    option['internal_geometry']['parameters']['inner_shoulder'] = 29.028
    option['internal_geometry']['parameters']['outer_shoulder'] = 35.972
    option['internal_geometry']['parameters']['cage_half_width'] = 3.0800000000000005
    option['internal_geometry']['parameters']['cage_low'] = 5.32
    option['internal_geometry']['parameters']['cage_high'] = 6.44
    option['internal_geometry']['parameters']['window_radius'] = 2.688
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '624'
    options.append(copy.deepcopy(option))

    # 62210: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_62000_series_62210_size_50_mm_id_90_mm_od_23_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_62000_series_62210_size_50_mm_id_90_mm_od_23_mm_depth'
    option['size'] = '62210'
    option['series'] = '62000'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 50.0
    option['dimensions']['outside'] = 90.0
    option['dimensions']['width'] = 23.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 14
    option['internal_geometry']['balls_per_row'] = 14
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 50.0
    option['internal_geometry']['parameters']['outside'] = 90.0
    option['internal_geometry']['parameters']['width'] = 23.0
    option['internal_geometry']['parameters']['edge'] = 1.2
    option['internal_geometry']['parameters']['pitch_radius'] = 35.0
    option['internal_geometry']['parameters']['ball_radius'] = 5.6000000000000005
    option['internal_geometry']['parameters']['groove_radius'] = 5.74
    option['internal_geometry']['parameters']['inner_shoulder'] = 31.528
    option['internal_geometry']['parameters']['outer_shoulder'] = 38.472
    option['internal_geometry']['parameters']['cage_half_width'] = 3.0800000000000005
    option['internal_geometry']['parameters']['cage_low'] = 5.32
    option['internal_geometry']['parameters']['cage_high'] = 6.44
    option['internal_geometry']['parameters']['window_radius'] = 2.688
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '725'
    options.append(copy.deepcopy(option))

    # 6200: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6200_series_6200_size_10_mm_id_30_mm_od_9_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6200_series_6200_size_10_mm_id_30_mm_od_9_mm_depth'
    option['size'] = '6200'
    option['series'] = '6200'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 10.0
    option['dimensions']['outside'] = 30.0
    option['dimensions']['width'] = 9.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 9
    option['internal_geometry']['balls_per_row'] = 9
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 10.0
    option['internal_geometry']['parameters']['outside'] = 30.0
    option['internal_geometry']['parameters']['width'] = 9.0
    option['internal_geometry']['parameters']['edge'] = 0.54
    option['internal_geometry']['parameters']['pitch_radius'] = 10.0
    option['internal_geometry']['parameters']['ball_radius'] = 2.5200000000000005
    option['internal_geometry']['parameters']['groove_radius'] = 2.5830000000000006
    option['internal_geometry']['parameters']['inner_shoulder'] = 8.4376
    option['internal_geometry']['parameters']['outer_shoulder'] = 11.5624
    option['internal_geometry']['parameters']['cage_half_width'] = 1.3860000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.394
    option['internal_geometry']['parameters']['cage_high'] = 2.898
    option['internal_geometry']['parameters']['window_radius'] = 1.2096000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '32'
    options.append(copy.deepcopy(option))

    # 6201: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6200_series_6201_size_12_mm_id_32_mm_od_10_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6200_series_6201_size_12_mm_id_32_mm_od_10_mm_depth'
    option['size'] = '6201'
    option['series'] = '6200'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 12.0
    option['dimensions']['outside'] = 32.0
    option['dimensions']['width'] = 10.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 12.0
    option['internal_geometry']['parameters']['outside'] = 32.0
    option['internal_geometry']['parameters']['width'] = 10.0
    option['internal_geometry']['parameters']['edge'] = 0.6
    option['internal_geometry']['parameters']['pitch_radius'] = 11.0
    option['internal_geometry']['parameters']['ball_radius'] = 2.8000000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 2.87
    option['internal_geometry']['parameters']['inner_shoulder'] = 9.264
    option['internal_geometry']['parameters']['outer_shoulder'] = 12.736
    option['internal_geometry']['parameters']['cage_half_width'] = 1.5400000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.66
    option['internal_geometry']['parameters']['cage_high'] = 3.22
    option['internal_geometry']['parameters']['window_radius'] = 1.344
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '35'
    options.append(copy.deepcopy(option))

    # 6202: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6200_series_6202_size_15_mm_id_35_mm_od_11_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6200_series_6202_size_15_mm_id_35_mm_od_11_mm_depth'
    option['size'] = '6202'
    option['series'] = '6200'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 15.0
    option['dimensions']['outside'] = 35.0
    option['dimensions']['width'] = 11.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 10
    option['internal_geometry']['balls_per_row'] = 10
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 15.0
    option['internal_geometry']['parameters']['outside'] = 35.0
    option['internal_geometry']['parameters']['width'] = 11.0
    option['internal_geometry']['parameters']['edge'] = 0.6
    option['internal_geometry']['parameters']['pitch_radius'] = 12.5
    option['internal_geometry']['parameters']['ball_radius'] = 2.8000000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 2.87
    option['internal_geometry']['parameters']['inner_shoulder'] = 10.764
    option['internal_geometry']['parameters']['outer_shoulder'] = 14.236
    option['internal_geometry']['parameters']['cage_half_width'] = 1.5400000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.66
    option['internal_geometry']['parameters']['cage_high'] = 3.22
    option['internal_geometry']['parameters']['window_radius'] = 1.344
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '45'
    options.append(copy.deepcopy(option))

    # 6203: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6200_series_6203_size_17_mm_id_40_mm_od_12_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6200_series_6203_size_17_mm_id_40_mm_od_12_mm_depth'
    option['size'] = '6203'
    option['series'] = '6200'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 17.0
    option['dimensions']['outside'] = 40.0
    option['dimensions']['width'] = 12.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 10
    option['internal_geometry']['balls_per_row'] = 10
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 17.0
    option['internal_geometry']['parameters']['outside'] = 40.0
    option['internal_geometry']['parameters']['width'] = 12.0
    option['internal_geometry']['parameters']['edge'] = 0.69
    option['internal_geometry']['parameters']['pitch_radius'] = 14.25
    option['internal_geometry']['parameters']['ball_radius'] = 3.22
    option['internal_geometry']['parameters']['groove_radius'] = 3.3005000000000004
    option['internal_geometry']['parameters']['inner_shoulder'] = 12.2536
    option['internal_geometry']['parameters']['outer_shoulder'] = 16.2464
    option['internal_geometry']['parameters']['cage_half_width'] = 1.7710000000000004
    option['internal_geometry']['parameters']['cage_low'] = 3.059
    option['internal_geometry']['parameters']['cage_high'] = 3.703
    option['internal_geometry']['parameters']['window_radius'] = 1.5456
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '64'
    options.append(copy.deepcopy(option))

    # 6204: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6200_series_6204_size_20_mm_id_47_mm_od_14_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6200_series_6204_size_20_mm_id_47_mm_od_14_mm_depth'
    option['size'] = '6204'
    option['series'] = '6200'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 20.0
    option['dimensions']['outside'] = 47.0
    option['dimensions']['width'] = 14.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 10
    option['internal_geometry']['balls_per_row'] = 10
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 20.0
    option['internal_geometry']['parameters']['outside'] = 47.0
    option['internal_geometry']['parameters']['width'] = 14.0
    option['internal_geometry']['parameters']['edge'] = 0.8099999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 16.75
    option['internal_geometry']['parameters']['ball_radius'] = 3.7800000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 3.8745000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 14.4064
    option['internal_geometry']['parameters']['outer_shoulder'] = 19.093600000000002
    option['internal_geometry']['parameters']['cage_half_width'] = 2.079
    option['internal_geometry']['parameters']['cage_low'] = 3.591
    option['internal_geometry']['parameters']['cage_high'] = 4.3469999999999995
    option['internal_geometry']['parameters']['window_radius'] = 1.8144
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '103'
    options.append(copy.deepcopy(option))

    # 6205: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6200_series_6205_size_25_mm_id_52_mm_od_15_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6200_series_6205_size_25_mm_id_52_mm_od_15_mm_depth'
    option['size'] = '6205'
    option['series'] = '6200'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 25.0
    option['dimensions']['outside'] = 52.0
    option['dimensions']['width'] = 15.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 11
    option['internal_geometry']['balls_per_row'] = 11
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 25.0
    option['internal_geometry']['parameters']['outside'] = 52.0
    option['internal_geometry']['parameters']['width'] = 15.0
    option['internal_geometry']['parameters']['edge'] = 0.8099999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 19.25
    option['internal_geometry']['parameters']['ball_radius'] = 3.7800000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 3.8745000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 16.906399999999998
    option['internal_geometry']['parameters']['outer_shoulder'] = 21.593600000000002
    option['internal_geometry']['parameters']['cage_half_width'] = 2.079
    option['internal_geometry']['parameters']['cage_low'] = 3.591
    option['internal_geometry']['parameters']['cage_high'] = 4.3469999999999995
    option['internal_geometry']['parameters']['window_radius'] = 1.8144
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '127'
    options.append(copy.deepcopy(option))

    # 6206: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6200_series_6206_size_30_mm_id_62_mm_od_16_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6200_series_6206_size_30_mm_id_62_mm_od_16_mm_depth'
    option['size'] = '6206'
    option['series'] = '6200'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 30.0
    option['dimensions']['outside'] = 62.0
    option['dimensions']['width'] = 16.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 11
    option['internal_geometry']['balls_per_row'] = 11
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 30.0
    option['internal_geometry']['parameters']['outside'] = 62.0
    option['internal_geometry']['parameters']['width'] = 16.0
    option['internal_geometry']['parameters']['edge'] = 0.96
    option['internal_geometry']['parameters']['pitch_radius'] = 23.0
    option['internal_geometry']['parameters']['ball_radius'] = 4.48
    option['internal_geometry']['parameters']['groove_radius'] = 4.5920000000000005
    option['internal_geometry']['parameters']['inner_shoulder'] = 20.2224
    option['internal_geometry']['parameters']['outer_shoulder'] = 25.7776
    option['internal_geometry']['parameters']['cage_half_width'] = 2.4640000000000004
    option['internal_geometry']['parameters']['cage_low'] = 4.256
    option['internal_geometry']['parameters']['cage_high'] = 5.152
    option['internal_geometry']['parameters']['window_radius'] = 2.1504000000000003
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '200'
    options.append(copy.deepcopy(option))

    # 6207: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6200_series_6207_size_35_mm_id_72_mm_od_17_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6200_series_6207_size_35_mm_id_72_mm_od_17_mm_depth'
    option['size'] = '6207'
    option['series'] = '6200'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 35.0
    option['dimensions']['outside'] = 72.0
    option['dimensions']['width'] = 17.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 12
    option['internal_geometry']['balls_per_row'] = 12
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 35.0
    option['internal_geometry']['parameters']['outside'] = 72.0
    option['internal_geometry']['parameters']['width'] = 17.0
    option['internal_geometry']['parameters']['edge'] = 1.02
    option['internal_geometry']['parameters']['pitch_radius'] = 26.75
    option['internal_geometry']['parameters']['ball_radius'] = 4.760000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 4.8790000000000004
    option['internal_geometry']['parameters']['inner_shoulder'] = 23.7988
    option['internal_geometry']['parameters']['outer_shoulder'] = 29.7012
    option['internal_geometry']['parameters']['cage_half_width'] = 2.6180000000000008
    option['internal_geometry']['parameters']['cage_low'] = 4.522
    option['internal_geometry']['parameters']['cage_high'] = 5.474
    option['internal_geometry']['parameters']['window_radius'] = 2.2848
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '288'
    options.append(copy.deepcopy(option))

    # 6208: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6200_series_6208_size_40_mm_id_80_mm_od_18_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6200_series_6208_size_40_mm_id_80_mm_od_18_mm_depth'
    option['size'] = '6208'
    option['series'] = '6200'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 40.0
    option['dimensions']['outside'] = 80.0
    option['dimensions']['width'] = 18.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.nsk.com/in-en/engineering/6208-dgbb-sr.html']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 9
    option['internal_geometry']['balls_per_row'] = 9
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 40.0
    option['internal_geometry']['parameters']['outside'] = 80.0
    option['internal_geometry']['parameters']['width'] = 18.0
    option['internal_geometry']['parameters']['edge'] = 1.08
    option['internal_geometry']['parameters']['pitch_radius'] = 30.0
    option['internal_geometry']['parameters']['ball_radius'] = 5.953
    option['internal_geometry']['parameters']['groove_radius'] = 6.101825000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 26.30914
    option['internal_geometry']['parameters']['outer_shoulder'] = 33.69086
    option['internal_geometry']['parameters']['cage_half_width'] = 3.2741500000000006
    option['internal_geometry']['parameters']['cage_low'] = 5.65535
    option['internal_geometry']['parameters']['cage_high'] = 6.84595
    option['internal_geometry']['parameters']['window_radius'] = 2.85744
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'manufacturer_sourced'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '368'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_6200_series_6208_size_40_mm_id_80_mm_od_15_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://www.nsk.com/in-en/engineering/6208-dgbb-sr.html']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # 6209: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6200_series_6209_size_45_mm_id_85_mm_od_19_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6200_series_6209_size_45_mm_id_85_mm_od_19_mm_depth'
    option['size'] = '6209'
    option['series'] = '6200'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 45.0
    option['dimensions']['outside'] = 85.0
    option['dimensions']['width'] = 19.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 14
    option['internal_geometry']['balls_per_row'] = 14
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 45.0
    option['internal_geometry']['parameters']['outside'] = 85.0
    option['internal_geometry']['parameters']['width'] = 19.0
    option['internal_geometry']['parameters']['edge'] = 1.14
    option['internal_geometry']['parameters']['pitch_radius'] = 32.5
    option['internal_geometry']['parameters']['ball_radius'] = 5.32
    option['internal_geometry']['parameters']['groove_radius'] = 5.453
    option['internal_geometry']['parameters']['inner_shoulder'] = 29.2016
    option['internal_geometry']['parameters']['outer_shoulder'] = 35.7984
    option['internal_geometry']['parameters']['cage_half_width'] = 2.9260000000000006
    option['internal_geometry']['parameters']['cage_low'] = 5.054
    option['internal_geometry']['parameters']['cage_high'] = 6.117999999999999
    option['internal_geometry']['parameters']['window_radius'] = 2.5536
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '415'
    options.append(copy.deepcopy(option))

    # 6210: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6200_series_6210_size_50_mm_id_90_mm_od_20_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6200_series_6210_size_50_mm_id_90_mm_od_20_mm_depth'
    option['size'] = '6210'
    option['series'] = '6200'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 50.0
    option['dimensions']['outside'] = 90.0
    option['dimensions']['width'] = 20.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 14
    option['internal_geometry']['balls_per_row'] = 14
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 50.0
    option['internal_geometry']['parameters']['outside'] = 90.0
    option['internal_geometry']['parameters']['width'] = 20.0
    option['internal_geometry']['parameters']['edge'] = 1.2
    option['internal_geometry']['parameters']['pitch_radius'] = 35.0
    option['internal_geometry']['parameters']['ball_radius'] = 5.6000000000000005
    option['internal_geometry']['parameters']['groove_radius'] = 5.74
    option['internal_geometry']['parameters']['inner_shoulder'] = 31.528
    option['internal_geometry']['parameters']['outer_shoulder'] = 38.472
    option['internal_geometry']['parameters']['cage_half_width'] = 3.0800000000000005
    option['internal_geometry']['parameters']['cage_low'] = 5.32
    option['internal_geometry']['parameters']['cage_high'] = 6.44
    option['internal_geometry']['parameters']['window_radius'] = 2.688
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '463'
    options.append(copy.deepcopy(option))

    # 6211: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6200_series_6211_size_55_mm_id_100_mm_od_21_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6200_series_6211_size_55_mm_id_100_mm_od_21_mm_depth'
    option['size'] = '6211'
    option['series'] = '6200'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 55.0
    option['dimensions']['outside'] = 100.0
    option['dimensions']['width'] = 21.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 15
    option['internal_geometry']['balls_per_row'] = 15
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 55.0
    option['internal_geometry']['parameters']['outside'] = 100.0
    option['internal_geometry']['parameters']['width'] = 21.0
    option['internal_geometry']['parameters']['edge'] = 1.26
    option['internal_geometry']['parameters']['pitch_radius'] = 38.75
    option['internal_geometry']['parameters']['ball_radius'] = 5.880000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 6.027000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 35.1044
    option['internal_geometry']['parameters']['outer_shoulder'] = 42.3956
    option['internal_geometry']['parameters']['cage_half_width'] = 3.234000000000001
    option['internal_geometry']['parameters']['cage_low'] = 5.586
    option['internal_geometry']['parameters']['cage_high'] = 6.7620000000000005
    option['internal_geometry']['parameters']['window_radius'] = 2.8224000000000005
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '606'
    options.append(copy.deepcopy(option))

    # 6212: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6200_series_6212_size_60_mm_id_110_mm_od_22_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6200_series_6212_size_60_mm_id_110_mm_od_22_mm_depth'
    option['size'] = '6212'
    option['series'] = '6200'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 60.0
    option['dimensions']['outside'] = 110.0
    option['dimensions']['width'] = 22.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 15
    option['internal_geometry']['balls_per_row'] = 15
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 60.0
    option['internal_geometry']['parameters']['outside'] = 110.0
    option['internal_geometry']['parameters']['width'] = 22.0
    option['internal_geometry']['parameters']['edge'] = 1.3199999999999998
    option['internal_geometry']['parameters']['pitch_radius'] = 42.5
    option['internal_geometry']['parameters']['ball_radius'] = 6.16
    option['internal_geometry']['parameters']['groove_radius'] = 6.314
    option['internal_geometry']['parameters']['inner_shoulder'] = 38.6808
    option['internal_geometry']['parameters']['outer_shoulder'] = 46.3192
    option['internal_geometry']['parameters']['cage_half_width'] = 3.3880000000000003
    option['internal_geometry']['parameters']['cage_low'] = 5.851999999999999
    option['internal_geometry']['parameters']['cage_high'] = 7.084
    option['internal_geometry']['parameters']['window_radius'] = 2.9568
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '782'
    options.append(copy.deepcopy(option))

    # 6213: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6200_series_6213_size_65_mm_id_120_mm_od_23_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6200_series_6213_size_65_mm_id_120_mm_od_23_mm_depth'
    option['size'] = '6213'
    option['series'] = '6200'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 65.0
    option['dimensions']['outside'] = 120.0
    option['dimensions']['width'] = 23.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 16
    option['internal_geometry']['balls_per_row'] = 16
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 65.0
    option['internal_geometry']['parameters']['outside'] = 120.0
    option['internal_geometry']['parameters']['width'] = 23.0
    option['internal_geometry']['parameters']['edge'] = 1.38
    option['internal_geometry']['parameters']['pitch_radius'] = 46.25
    option['internal_geometry']['parameters']['ball_radius'] = 6.44
    option['internal_geometry']['parameters']['groove_radius'] = 6.601000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 42.2572
    option['internal_geometry']['parameters']['outer_shoulder'] = 50.2428
    option['internal_geometry']['parameters']['cage_half_width'] = 3.5420000000000007
    option['internal_geometry']['parameters']['cage_low'] = 6.118
    option['internal_geometry']['parameters']['cage_high'] = 7.406
    option['internal_geometry']['parameters']['window_radius'] = 3.0912
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '989'
    options.append(copy.deepcopy(option))

    # 6214: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6200_series_6214_size_70_mm_id_125_mm_od_24_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6200_series_6214_size_70_mm_id_125_mm_od_24_mm_depth'
    option['size'] = '6214'
    option['series'] = '6200'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 70.0
    option['dimensions']['outside'] = 125.0
    option['dimensions']['width'] = 24.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 16
    option['internal_geometry']['balls_per_row'] = 16
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 70.0
    option['internal_geometry']['parameters']['outside'] = 125.0
    option['internal_geometry']['parameters']['width'] = 24.0
    option['internal_geometry']['parameters']['edge'] = 1.44
    option['internal_geometry']['parameters']['pitch_radius'] = 48.75
    option['internal_geometry']['parameters']['ball_radius'] = 6.720000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 6.888000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 44.5836
    option['internal_geometry']['parameters']['outer_shoulder'] = 52.9164
    option['internal_geometry']['parameters']['cage_half_width'] = 3.6960000000000006
    option['internal_geometry']['parameters']['cage_low'] = 6.384
    option['internal_geometry']['parameters']['cage_high'] = 7.728
    option['internal_geometry']['parameters']['window_radius'] = 3.2256
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1,069'
    options.append(copy.deepcopy(option))

    # 6215: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6200_series_6215_size_75_mm_id_130_mm_od_25_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6200_series_6215_size_75_mm_id_130_mm_od_25_mm_depth'
    option['size'] = '6215'
    option['series'] = '6200'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 75.0
    option['dimensions']['outside'] = 130.0
    option['dimensions']['width'] = 25.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 16
    option['internal_geometry']['balls_per_row'] = 16
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 75.0
    option['internal_geometry']['parameters']['outside'] = 130.0
    option['internal_geometry']['parameters']['width'] = 25.0
    option['internal_geometry']['parameters']['edge'] = 1.5
    option['internal_geometry']['parameters']['pitch_radius'] = 51.25
    option['internal_geometry']['parameters']['ball_radius'] = 7.000000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 7.175000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 46.91
    option['internal_geometry']['parameters']['outer_shoulder'] = 55.59
    option['internal_geometry']['parameters']['cage_half_width'] = 3.850000000000001
    option['internal_geometry']['parameters']['cage_low'] = 6.65
    option['internal_geometry']['parameters']['cage_high'] = 8.05
    option['internal_geometry']['parameters']['window_radius'] = 3.3600000000000003
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1,179'
    options.append(copy.deepcopy(option))

    # 6216: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6200_series_6216_size_80_mm_id_140_mm_od_26_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6200_series_6216_size_80_mm_id_140_mm_od_26_mm_depth'
    option['size'] = '6216'
    option['series'] = '6200'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 80.0
    option['dimensions']['outside'] = 140.0
    option['dimensions']['width'] = 26.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 17
    option['internal_geometry']['balls_per_row'] = 17
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 80.0
    option['internal_geometry']['parameters']['outside'] = 140.0
    option['internal_geometry']['parameters']['width'] = 26.0
    option['internal_geometry']['parameters']['edge'] = 1.56
    option['internal_geometry']['parameters']['pitch_radius'] = 55.0
    option['internal_geometry']['parameters']['ball_radius'] = 7.280000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 7.4620000000000015
    option['internal_geometry']['parameters']['inner_shoulder'] = 50.4864
    option['internal_geometry']['parameters']['outer_shoulder'] = 59.5136
    option['internal_geometry']['parameters']['cage_half_width'] = 4.004000000000001
    option['internal_geometry']['parameters']['cage_low'] = 6.916
    option['internal_geometry']['parameters']['cage_high'] = 8.372
    option['internal_geometry']['parameters']['window_radius'] = 3.4944000000000006
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1,398'
    options.append(copy.deepcopy(option))

    # 6217: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6200_series_6217_size_85_mm_id_150_mm_od_28_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6200_series_6217_size_85_mm_id_150_mm_od_28_mm_depth'
    option['size'] = '6217'
    option['series'] = '6200'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 85.0
    option['dimensions']['outside'] = 150.0
    option['dimensions']['width'] = 28.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 17
    option['internal_geometry']['balls_per_row'] = 17
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 85.0
    option['internal_geometry']['parameters']['outside'] = 150.0
    option['internal_geometry']['parameters']['width'] = 28.0
    option['internal_geometry']['parameters']['edge'] = 1.68
    option['internal_geometry']['parameters']['pitch_radius'] = 58.75
    option['internal_geometry']['parameters']['ball_radius'] = 7.840000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 8.036000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 53.8892
    option['internal_geometry']['parameters']['outer_shoulder'] = 63.6108
    option['internal_geometry']['parameters']['cage_half_width'] = 4.312000000000001
    option['internal_geometry']['parameters']['cage_low'] = 7.448
    option['internal_geometry']['parameters']['cage_high'] = 9.016
    option['internal_geometry']['parameters']['window_radius'] = 3.7632000000000003
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1,788'
    options.append(copy.deepcopy(option))

    # 6218: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6200_series_6218_size_90_mm_id_160_mm_od_30_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6200_series_6218_size_90_mm_id_160_mm_od_30_mm_depth'
    option['size'] = '6218'
    option['series'] = '6200'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 90.0
    option['dimensions']['outside'] = 160.0
    option['dimensions']['width'] = 30.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 17
    option['internal_geometry']['balls_per_row'] = 17
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 90.0
    option['internal_geometry']['parameters']['outside'] = 160.0
    option['internal_geometry']['parameters']['width'] = 30.0
    option['internal_geometry']['parameters']['edge'] = 1.7999999999999998
    option['internal_geometry']['parameters']['pitch_radius'] = 62.5
    option['internal_geometry']['parameters']['ball_radius'] = 8.4
    option['internal_geometry']['parameters']['groove_radius'] = 8.610000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 57.292
    option['internal_geometry']['parameters']['outer_shoulder'] = 67.708
    option['internal_geometry']['parameters']['cage_half_width'] = 4.620000000000001
    option['internal_geometry']['parameters']['cage_low'] = 7.9799999999999995
    option['internal_geometry']['parameters']['cage_high'] = 9.66
    option['internal_geometry']['parameters']['window_radius'] = 4.032
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '2,147'
    options.append(copy.deepcopy(option))

    # 6219: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6200_series_6219_size_95_mm_id_170_mm_od_32_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6200_series_6219_size_95_mm_id_170_mm_od_32_mm_depth'
    option['size'] = '6219'
    option['series'] = '6200'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 95.0
    option['dimensions']['outside'] = 170.0
    option['dimensions']['width'] = 32.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 17
    option['internal_geometry']['balls_per_row'] = 17
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 95.0
    option['internal_geometry']['parameters']['outside'] = 170.0
    option['internal_geometry']['parameters']['width'] = 32.0
    option['internal_geometry']['parameters']['edge'] = 1.92
    option['internal_geometry']['parameters']['pitch_radius'] = 66.25
    option['internal_geometry']['parameters']['ball_radius'] = 8.96
    option['internal_geometry']['parameters']['groove_radius'] = 9.184000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 60.6948
    option['internal_geometry']['parameters']['outer_shoulder'] = 71.8052
    option['internal_geometry']['parameters']['cage_half_width'] = 4.928000000000001
    option['internal_geometry']['parameters']['cage_low'] = 8.512
    option['internal_geometry']['parameters']['cage_high'] = 10.304
    option['internal_geometry']['parameters']['window_radius'] = 4.300800000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '2,617'
    options.append(copy.deepcopy(option))

    # 6220: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6200_series_6220_size_100_mm_id_180_mm_od_34_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6200_series_6220_size_100_mm_id_180_mm_od_34_mm_depth'
    option['size'] = '6220'
    option['series'] = '6200'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 100.0
    option['dimensions']['outside'] = 180.0
    option['dimensions']['width'] = 34.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 17
    option['internal_geometry']['balls_per_row'] = 17
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 100.0
    option['internal_geometry']['parameters']['outside'] = 180.0
    option['internal_geometry']['parameters']['width'] = 34.0
    option['internal_geometry']['parameters']['edge'] = 2.04
    option['internal_geometry']['parameters']['pitch_radius'] = 70.0
    option['internal_geometry']['parameters']['ball_radius'] = 9.520000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 9.758000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 64.0976
    option['internal_geometry']['parameters']['outer_shoulder'] = 75.9024
    option['internal_geometry']['parameters']['cage_half_width'] = 5.2360000000000015
    option['internal_geometry']['parameters']['cage_low'] = 9.044
    option['internal_geometry']['parameters']['cage_high'] = 10.948
    option['internal_geometry']['parameters']['window_radius'] = 4.5696
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '3,136'
    options.append(copy.deepcopy(option))

    # 6221: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6200_series_6221_size_105_mm_id_190_mm_od_36_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6200_series_6221_size_105_mm_id_190_mm_od_36_mm_depth'
    option['size'] = '6221'
    option['series'] = '6200'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 105.0
    option['dimensions']['outside'] = 190.0
    option['dimensions']['width'] = 36.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 16
    option['internal_geometry']['balls_per_row'] = 16
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 105.0
    option['internal_geometry']['parameters']['outside'] = 190.0
    option['internal_geometry']['parameters']['width'] = 36.0
    option['internal_geometry']['parameters']['edge'] = 2.16
    option['internal_geometry']['parameters']['pitch_radius'] = 73.75
    option['internal_geometry']['parameters']['ball_radius'] = 10.080000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 10.332000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 67.5004
    option['internal_geometry']['parameters']['outer_shoulder'] = 79.9996
    option['internal_geometry']['parameters']['cage_half_width'] = 5.544000000000001
    option['internal_geometry']['parameters']['cage_low'] = 9.576
    option['internal_geometry']['parameters']['cage_high'] = 11.592
    option['internal_geometry']['parameters']['window_radius'] = 4.838400000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '3,696'
    options.append(copy.deepcopy(option))

    # 6222: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6200_series_6222_size_110_mm_id_200_mm_od_38_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6200_series_6222_size_110_mm_id_200_mm_od_38_mm_depth'
    option['size'] = '6222'
    option['series'] = '6200'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 110.0
    option['dimensions']['outside'] = 200.0
    option['dimensions']['width'] = 38.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 16
    option['internal_geometry']['balls_per_row'] = 16
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 110.0
    option['internal_geometry']['parameters']['outside'] = 200.0
    option['internal_geometry']['parameters']['width'] = 38.0
    option['internal_geometry']['parameters']['edge'] = 2.28
    option['internal_geometry']['parameters']['pitch_radius'] = 77.5
    option['internal_geometry']['parameters']['ball_radius'] = 10.64
    option['internal_geometry']['parameters']['groove_radius'] = 10.906
    option['internal_geometry']['parameters']['inner_shoulder'] = 70.9032
    option['internal_geometry']['parameters']['outer_shoulder'] = 84.0968
    option['internal_geometry']['parameters']['cage_half_width'] = 5.852000000000001
    option['internal_geometry']['parameters']['cage_low'] = 10.108
    option['internal_geometry']['parameters']['cage_high'] = 12.235999999999999
    option['internal_geometry']['parameters']['window_radius'] = 5.1072
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '4,355'
    options.append(copy.deepcopy(option))

    # 6224: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6200_series_6224_size_120_mm_id_215_mm_od_40_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6200_series_6224_size_120_mm_id_215_mm_od_40_mm_depth'
    option['size'] = '6224'
    option['series'] = '6200'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 120.0
    option['dimensions']['outside'] = 215.0
    option['dimensions']['width'] = 40.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 17
    option['internal_geometry']['balls_per_row'] = 17
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 120.0
    option['internal_geometry']['parameters']['outside'] = 215.0
    option['internal_geometry']['parameters']['width'] = 40.0
    option['internal_geometry']['parameters']['edge'] = 2.4
    option['internal_geometry']['parameters']['pitch_radius'] = 83.75
    option['internal_geometry']['parameters']['ball_radius'] = 11.200000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 11.48
    option['internal_geometry']['parameters']['inner_shoulder'] = 76.806
    option['internal_geometry']['parameters']['outer_shoulder'] = 90.694
    option['internal_geometry']['parameters']['cage_half_width'] = 6.160000000000001
    option['internal_geometry']['parameters']['cage_low'] = 10.64
    option['internal_geometry']['parameters']['cage_high'] = 12.88
    option['internal_geometry']['parameters']['window_radius'] = 5.376
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '5,623'
    options.append(copy.deepcopy(option))

    # 6226: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6200_series_6226_size_130_mm_id_230_mm_od_40_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6200_series_6226_size_130_mm_id_230_mm_od_40_mm_depth'
    option['size'] = '6226'
    option['series'] = '6200'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 130.0
    option['dimensions']['outside'] = 230.0
    option['dimensions']['width'] = 40.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 18
    option['internal_geometry']['balls_per_row'] = 18
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 130.0
    option['internal_geometry']['parameters']['outside'] = 230.0
    option['internal_geometry']['parameters']['width'] = 40.0
    option['internal_geometry']['parameters']['edge'] = 2.4
    option['internal_geometry']['parameters']['pitch_radius'] = 90.0
    option['internal_geometry']['parameters']['ball_radius'] = 11.200000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 11.48
    option['internal_geometry']['parameters']['inner_shoulder'] = 83.056
    option['internal_geometry']['parameters']['outer_shoulder'] = 96.944
    option['internal_geometry']['parameters']['cage_half_width'] = 6.160000000000001
    option['internal_geometry']['parameters']['cage_low'] = 10.64
    option['internal_geometry']['parameters']['cage_high'] = 12.88
    option['internal_geometry']['parameters']['window_radius'] = 5.376
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '6,233'
    options.append(copy.deepcopy(option))

    # 6228: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6200_series_6228_size_140_mm_id_250_mm_od_42_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6200_series_6228_size_140_mm_id_250_mm_od_42_mm_depth'
    option['size'] = '6228'
    option['series'] = '6200'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 140.0
    option['dimensions']['outside'] = 250.0
    option['dimensions']['width'] = 42.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 19
    option['internal_geometry']['balls_per_row'] = 19
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 140.0
    option['internal_geometry']['parameters']['outside'] = 250.0
    option['internal_geometry']['parameters']['width'] = 42.0
    option['internal_geometry']['parameters']['edge'] = 2.52
    option['internal_geometry']['parameters']['pitch_radius'] = 97.5
    option['internal_geometry']['parameters']['ball_radius'] = 11.760000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 12.054000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 90.2088
    option['internal_geometry']['parameters']['outer_shoulder'] = 104.7912
    option['internal_geometry']['parameters']['cage_half_width'] = 6.468000000000002
    option['internal_geometry']['parameters']['cage_low'] = 11.172
    option['internal_geometry']['parameters']['cage_high'] = 13.524000000000001
    option['internal_geometry']['parameters']['window_radius'] = 5.644800000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '8,060'
    options.append(copy.deepcopy(option))

    # 6230: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6200_series_6230_size_150_mm_id_270_mm_od_45_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6200_series_6230_size_150_mm_id_270_mm_od_45_mm_depth'
    option['size'] = '6230'
    option['series'] = '6200'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 150.0
    option['dimensions']['outside'] = 270.0
    option['dimensions']['width'] = 45.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 19
    option['internal_geometry']['balls_per_row'] = 19
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 150.0
    option['internal_geometry']['parameters']['outside'] = 270.0
    option['internal_geometry']['parameters']['width'] = 45.0
    option['internal_geometry']['parameters']['edge'] = 2.6999999999999997
    option['internal_geometry']['parameters']['pitch_radius'] = 105.0
    option['internal_geometry']['parameters']['ball_radius'] = 12.600000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 12.915000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 97.188
    option['internal_geometry']['parameters']['outer_shoulder'] = 112.812
    option['internal_geometry']['parameters']['cage_half_width'] = 6.9300000000000015
    option['internal_geometry']['parameters']['cage_low'] = 11.97
    option['internal_geometry']['parameters']['cage_high'] = 14.49
    option['internal_geometry']['parameters']['window_radius'] = 6.048
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '10,288'
    options.append(copy.deepcopy(option))

    # 6300: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6300_series_6300_size_10_mm_id_35_mm_od_11_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6300_series_6300_size_10_mm_id_35_mm_od_11_mm_depth'
    option['size'] = '6300'
    option['series'] = '6300'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 10.0
    option['dimensions']['outside'] = 35.0
    option['dimensions']['width'] = 11.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 10.0
    option['internal_geometry']['parameters']['outside'] = 35.0
    option['internal_geometry']['parameters']['width'] = 11.0
    option['internal_geometry']['parameters']['edge'] = 0.6599999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 11.25
    option['internal_geometry']['parameters']['ball_radius'] = 3.08
    option['internal_geometry']['parameters']['groove_radius'] = 3.157
    option['internal_geometry']['parameters']['inner_shoulder'] = 9.3404
    option['internal_geometry']['parameters']['outer_shoulder'] = 13.1596
    option['internal_geometry']['parameters']['cage_half_width'] = 1.6940000000000002
    option['internal_geometry']['parameters']['cage_low'] = 2.9259999999999997
    option['internal_geometry']['parameters']['cage_high'] = 3.542
    option['internal_geometry']['parameters']['window_radius'] = 1.4784
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '54'
    options.append(copy.deepcopy(option))

    # 6301: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6300_series_6301_size_12_mm_id_37_mm_od_12_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6300_series_6301_size_12_mm_id_37_mm_od_12_mm_depth'
    option['size'] = '6301'
    option['series'] = '6300'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 12.0
    option['dimensions']['outside'] = 37.0
    option['dimensions']['width'] = 12.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 12.0
    option['internal_geometry']['parameters']['outside'] = 37.0
    option['internal_geometry']['parameters']['width'] = 12.0
    option['internal_geometry']['parameters']['edge'] = 0.72
    option['internal_geometry']['parameters']['pitch_radius'] = 12.25
    option['internal_geometry']['parameters']['ball_radius'] = 3.3600000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 3.4440000000000004
    option['internal_geometry']['parameters']['inner_shoulder'] = 10.1668
    option['internal_geometry']['parameters']['outer_shoulder'] = 14.3332
    option['internal_geometry']['parameters']['cage_half_width'] = 1.8480000000000003
    option['internal_geometry']['parameters']['cage_low'] = 3.192
    option['internal_geometry']['parameters']['cage_high'] = 3.864
    option['internal_geometry']['parameters']['window_radius'] = 1.6128
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '59'
    options.append(copy.deepcopy(option))

    # 6302: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6300_series_6302_size_15_mm_id_42_mm_od_13_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6300_series_6302_size_15_mm_id_42_mm_od_13_mm_depth'
    option['size'] = '6302'
    option['series'] = '6300'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 15.0
    option['dimensions']['outside'] = 42.0
    option['dimensions']['width'] = 13.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 15.0
    option['internal_geometry']['parameters']['outside'] = 42.0
    option['internal_geometry']['parameters']['width'] = 13.0
    option['internal_geometry']['parameters']['edge'] = 0.78
    option['internal_geometry']['parameters']['pitch_radius'] = 14.25
    option['internal_geometry']['parameters']['ball_radius'] = 3.6400000000000006
    option['internal_geometry']['parameters']['groove_radius'] = 3.7310000000000008
    option['internal_geometry']['parameters']['inner_shoulder'] = 11.9932
    option['internal_geometry']['parameters']['outer_shoulder'] = 16.5068
    option['internal_geometry']['parameters']['cage_half_width'] = 2.0020000000000007
    option['internal_geometry']['parameters']['cage_low'] = 3.458
    option['internal_geometry']['parameters']['cage_high'] = 4.186
    option['internal_geometry']['parameters']['window_radius'] = 1.7472000000000003
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '82'
    options.append(copy.deepcopy(option))

    # 6303: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6300_series_6303_size_17_mm_id_47_mm_od_14_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6300_series_6303_size_17_mm_id_47_mm_od_14_mm_depth'
    option['size'] = '6303'
    option['series'] = '6300'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 17.0
    option['dimensions']['outside'] = 47.0
    option['dimensions']['width'] = 14.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 9
    option['internal_geometry']['balls_per_row'] = 9
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 17.0
    option['internal_geometry']['parameters']['outside'] = 47.0
    option['internal_geometry']['parameters']['width'] = 14.0
    option['internal_geometry']['parameters']['edge'] = 0.84
    option['internal_geometry']['parameters']['pitch_radius'] = 16.0
    option['internal_geometry']['parameters']['ball_radius'] = 3.9200000000000004
    option['internal_geometry']['parameters']['groove_radius'] = 4.018000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 13.5696
    option['internal_geometry']['parameters']['outer_shoulder'] = 18.4304
    option['internal_geometry']['parameters']['cage_half_width'] = 2.1560000000000006
    option['internal_geometry']['parameters']['cage_low'] = 3.724
    option['internal_geometry']['parameters']['cage_high'] = 4.508
    option['internal_geometry']['parameters']['window_radius'] = 1.8816000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '109'
    options.append(copy.deepcopy(option))

    # 6304: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6300_series_6304_size_20_mm_id_52_mm_od_15_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6300_series_6304_size_20_mm_id_52_mm_od_15_mm_depth'
    option['size'] = '6304'
    option['series'] = '6300'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 20.0
    option['dimensions']['outside'] = 52.0
    option['dimensions']['width'] = 15.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 9
    option['internal_geometry']['balls_per_row'] = 9
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 20.0
    option['internal_geometry']['parameters']['outside'] = 52.0
    option['internal_geometry']['parameters']['width'] = 15.0
    option['internal_geometry']['parameters']['edge'] = 0.8999999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 18.0
    option['internal_geometry']['parameters']['ball_radius'] = 4.2
    option['internal_geometry']['parameters']['groove_radius'] = 4.305000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 15.396
    option['internal_geometry']['parameters']['outer_shoulder'] = 20.604
    option['internal_geometry']['parameters']['cage_half_width'] = 2.3100000000000005
    option['internal_geometry']['parameters']['cage_low'] = 3.9899999999999998
    option['internal_geometry']['parameters']['cage_high'] = 4.83
    option['internal_geometry']['parameters']['window_radius'] = 2.016
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '141'
    options.append(copy.deepcopy(option))

    # 6305: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6300_series_6305_size_25_mm_id_62_mm_od_17_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6300_series_6305_size_25_mm_id_62_mm_od_17_mm_depth'
    option['size'] = '6305'
    option['series'] = '6300'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 25.0
    option['dimensions']['outside'] = 62.0
    option['dimensions']['width'] = 17.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 10
    option['internal_geometry']['balls_per_row'] = 10
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 25.0
    option['internal_geometry']['parameters']['outside'] = 62.0
    option['internal_geometry']['parameters']['width'] = 17.0
    option['internal_geometry']['parameters']['edge'] = 1.02
    option['internal_geometry']['parameters']['pitch_radius'] = 21.75
    option['internal_geometry']['parameters']['ball_radius'] = 4.760000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 4.8790000000000004
    option['internal_geometry']['parameters']['inner_shoulder'] = 18.7988
    option['internal_geometry']['parameters']['outer_shoulder'] = 24.7012
    option['internal_geometry']['parameters']['cage_half_width'] = 2.6180000000000008
    option['internal_geometry']['parameters']['cage_low'] = 4.522
    option['internal_geometry']['parameters']['cage_high'] = 5.474
    option['internal_geometry']['parameters']['window_radius'] = 2.2848
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '218'
    options.append(copy.deepcopy(option))

    # 6306: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6300_series_6306_size_30_mm_id_72_mm_od_19_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6300_series_6306_size_30_mm_id_72_mm_od_19_mm_depth'
    option['size'] = '6306'
    option['series'] = '6300'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 30.0
    option['dimensions']['outside'] = 72.0
    option['dimensions']['width'] = 19.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 11
    option['internal_geometry']['balls_per_row'] = 11
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 30.0
    option['internal_geometry']['parameters']['outside'] = 72.0
    option['internal_geometry']['parameters']['width'] = 19.0
    option['internal_geometry']['parameters']['edge'] = 1.14
    option['internal_geometry']['parameters']['pitch_radius'] = 25.5
    option['internal_geometry']['parameters']['ball_radius'] = 5.32
    option['internal_geometry']['parameters']['groove_radius'] = 5.453
    option['internal_geometry']['parameters']['inner_shoulder'] = 22.2016
    option['internal_geometry']['parameters']['outer_shoulder'] = 28.7984
    option['internal_geometry']['parameters']['cage_half_width'] = 2.9260000000000006
    option['internal_geometry']['parameters']['cage_low'] = 5.054
    option['internal_geometry']['parameters']['cage_high'] = 6.117999999999999
    option['internal_geometry']['parameters']['window_radius'] = 2.5536
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '350'
    options.append(copy.deepcopy(option))

    # 6307: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6300_series_6307_size_35_mm_id_80_mm_od_21_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6300_series_6307_size_35_mm_id_80_mm_od_21_mm_depth'
    option['size'] = '6307'
    option['series'] = '6300'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 35.0
    option['dimensions']['outside'] = 80.0
    option['dimensions']['width'] = 21.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 11
    option['internal_geometry']['balls_per_row'] = 11
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 35.0
    option['internal_geometry']['parameters']['outside'] = 80.0
    option['internal_geometry']['parameters']['width'] = 21.0
    option['internal_geometry']['parameters']['edge'] = 1.26
    option['internal_geometry']['parameters']['pitch_radius'] = 28.75
    option['internal_geometry']['parameters']['ball_radius'] = 5.880000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 6.027000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 25.1044
    option['internal_geometry']['parameters']['outer_shoulder'] = 32.3956
    option['internal_geometry']['parameters']['cage_half_width'] = 3.234000000000001
    option['internal_geometry']['parameters']['cage_low'] = 5.586
    option['internal_geometry']['parameters']['cage_high'] = 6.7620000000000005
    option['internal_geometry']['parameters']['window_radius'] = 2.8224000000000005
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '454'
    options.append(copy.deepcopy(option))

    # 6308: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6300_series_6308_size_40_mm_id_90_mm_od_23_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6300_series_6308_size_40_mm_id_90_mm_od_23_mm_depth'
    option['size'] = '6308'
    option['series'] = '6300'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 40.0
    option['dimensions']['outside'] = 90.0
    option['dimensions']['width'] = 23.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 11
    option['internal_geometry']['balls_per_row'] = 11
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 40.0
    option['internal_geometry']['parameters']['outside'] = 90.0
    option['internal_geometry']['parameters']['width'] = 23.0
    option['internal_geometry']['parameters']['edge'] = 1.38
    option['internal_geometry']['parameters']['pitch_radius'] = 32.5
    option['internal_geometry']['parameters']['ball_radius'] = 6.44
    option['internal_geometry']['parameters']['groove_radius'] = 6.601000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 28.5072
    option['internal_geometry']['parameters']['outer_shoulder'] = 36.4928
    option['internal_geometry']['parameters']['cage_half_width'] = 3.5420000000000007
    option['internal_geometry']['parameters']['cage_low'] = 6.118
    option['internal_geometry']['parameters']['cage_high'] = 7.406
    option['internal_geometry']['parameters']['window_radius'] = 3.0912
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '640'
    options.append(copy.deepcopy(option))

    # 6309: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6300_series_6309_size_45_mm_id_100_mm_od_25_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6300_series_6309_size_45_mm_id_100_mm_od_25_mm_depth'
    option['size'] = '6309'
    option['series'] = '6300'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 45.0
    option['dimensions']['outside'] = 100.0
    option['dimensions']['width'] = 25.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 11
    option['internal_geometry']['balls_per_row'] = 11
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 45.0
    option['internal_geometry']['parameters']['outside'] = 100.0
    option['internal_geometry']['parameters']['width'] = 25.0
    option['internal_geometry']['parameters']['edge'] = 1.5
    option['internal_geometry']['parameters']['pitch_radius'] = 36.25
    option['internal_geometry']['parameters']['ball_radius'] = 7.000000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 7.175000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 31.91
    option['internal_geometry']['parameters']['outer_shoulder'] = 40.59
    option['internal_geometry']['parameters']['cage_half_width'] = 3.850000000000001
    option['internal_geometry']['parameters']['cage_low'] = 6.65
    option['internal_geometry']['parameters']['cage_high'] = 8.05
    option['internal_geometry']['parameters']['window_radius'] = 3.3600000000000003
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '872'
    options.append(copy.deepcopy(option))

    # 6310: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6300_series_6310_size_50_mm_id_110_mm_od_27_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6300_series_6310_size_50_mm_id_110_mm_od_27_mm_depth'
    option['size'] = '6310'
    option['series'] = '6300'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 50.0
    option['dimensions']['outside'] = 110.0
    option['dimensions']['width'] = 27.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 12
    option['internal_geometry']['balls_per_row'] = 12
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 50.0
    option['internal_geometry']['parameters']['outside'] = 110.0
    option['internal_geometry']['parameters']['width'] = 27.0
    option['internal_geometry']['parameters']['edge'] = 1.6199999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 40.0
    option['internal_geometry']['parameters']['ball_radius'] = 7.5600000000000005
    option['internal_geometry']['parameters']['groove_radius'] = 7.7490000000000006
    option['internal_geometry']['parameters']['inner_shoulder'] = 35.312799999999996
    option['internal_geometry']['parameters']['outer_shoulder'] = 44.687200000000004
    option['internal_geometry']['parameters']['cage_half_width'] = 4.158
    option['internal_geometry']['parameters']['cage_low'] = 7.182
    option['internal_geometry']['parameters']['cage_high'] = 8.693999999999999
    option['internal_geometry']['parameters']['window_radius'] = 3.6288
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1,067'
    options.append(copy.deepcopy(option))

    # 6311: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6300_series_6311_size_55_mm_id_120_mm_od_29_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6300_series_6311_size_55_mm_id_120_mm_od_29_mm_depth'
    option['size'] = '6311'
    option['series'] = '6300'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 55.0
    option['dimensions']['outside'] = 120.0
    option['dimensions']['width'] = 29.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 12
    option['internal_geometry']['balls_per_row'] = 12
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 55.0
    option['internal_geometry']['parameters']['outside'] = 120.0
    option['internal_geometry']['parameters']['width'] = 29.0
    option['internal_geometry']['parameters']['edge'] = 1.74
    option['internal_geometry']['parameters']['pitch_radius'] = 43.75
    option['internal_geometry']['parameters']['ball_radius'] = 8.120000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 8.323
    option['internal_geometry']['parameters']['inner_shoulder'] = 38.7156
    option['internal_geometry']['parameters']['outer_shoulder'] = 48.7844
    option['internal_geometry']['parameters']['cage_half_width'] = 4.466000000000001
    option['internal_geometry']['parameters']['cage_low'] = 7.714
    option['internal_geometry']['parameters']['cage_high'] = 9.338000000000001
    option['internal_geometry']['parameters']['window_radius'] = 3.8976
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1,367'
    options.append(copy.deepcopy(option))

    # 6312: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6300_series_6312_size_60_mm_id_130_mm_od_31_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6300_series_6312_size_60_mm_id_130_mm_od_31_mm_depth'
    option['size'] = '6312'
    option['series'] = '6300'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 60.0
    option['dimensions']['outside'] = 130.0
    option['dimensions']['width'] = 31.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 12
    option['internal_geometry']['balls_per_row'] = 12
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 60.0
    option['internal_geometry']['parameters']['outside'] = 130.0
    option['internal_geometry']['parameters']['width'] = 31.0
    option['internal_geometry']['parameters']['edge'] = 1.8599999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 47.5
    option['internal_geometry']['parameters']['ball_radius'] = 8.680000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 8.897000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 42.1184
    option['internal_geometry']['parameters']['outer_shoulder'] = 52.8816
    option['internal_geometry']['parameters']['cage_half_width'] = 4.774000000000001
    option['internal_geometry']['parameters']['cage_low'] = 8.246
    option['internal_geometry']['parameters']['cage_high'] = 9.982000000000001
    option['internal_geometry']['parameters']['window_radius'] = 4.1664
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1,698'
    options.append(copy.deepcopy(option))

    # 6313: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6300_series_6313_size_65_mm_id_140_mm_od_33_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6300_series_6313_size_65_mm_id_140_mm_od_33_mm_depth'
    option['size'] = '6313'
    option['series'] = '6300'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 65.0
    option['dimensions']['outside'] = 140.0
    option['dimensions']['width'] = 33.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 12
    option['internal_geometry']['balls_per_row'] = 12
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 65.0
    option['internal_geometry']['parameters']['outside'] = 140.0
    option['internal_geometry']['parameters']['width'] = 33.0
    option['internal_geometry']['parameters']['edge'] = 1.98
    option['internal_geometry']['parameters']['pitch_radius'] = 51.25
    option['internal_geometry']['parameters']['ball_radius'] = 9.24
    option['internal_geometry']['parameters']['groove_radius'] = 9.471
    option['internal_geometry']['parameters']['inner_shoulder'] = 45.5212
    option['internal_geometry']['parameters']['outer_shoulder'] = 56.9788
    option['internal_geometry']['parameters']['cage_half_width'] = 5.082000000000001
    option['internal_geometry']['parameters']['cage_low'] = 8.778
    option['internal_geometry']['parameters']['cage_high'] = 10.626
    option['internal_geometry']['parameters']['window_radius'] = 4.4352
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '2,079'
    options.append(copy.deepcopy(option))

    # 6314: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6300_series_6314_size_70_mm_id_150_mm_od_35_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6300_series_6314_size_70_mm_id_150_mm_od_35_mm_depth'
    option['size'] = '6314'
    option['series'] = '6300'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 70.0
    option['dimensions']['outside'] = 150.0
    option['dimensions']['width'] = 35.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 12
    option['internal_geometry']['balls_per_row'] = 12
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 70.0
    option['internal_geometry']['parameters']['outside'] = 150.0
    option['internal_geometry']['parameters']['width'] = 35.0
    option['internal_geometry']['parameters']['edge'] = 2.1
    option['internal_geometry']['parameters']['pitch_radius'] = 55.0
    option['internal_geometry']['parameters']['ball_radius'] = 9.8
    option['internal_geometry']['parameters']['groove_radius'] = 10.045
    option['internal_geometry']['parameters']['inner_shoulder'] = 48.924
    option['internal_geometry']['parameters']['outer_shoulder'] = 61.076
    option['internal_geometry']['parameters']['cage_half_width'] = 5.390000000000001
    option['internal_geometry']['parameters']['cage_low'] = 9.31
    option['internal_geometry']['parameters']['cage_high'] = 11.27
    option['internal_geometry']['parameters']['window_radius'] = 4.704
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '2,515'
    options.append(copy.deepcopy(option))

    # 6315: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6300_series_6315_size_75_mm_id_160_mm_od_37_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6300_series_6315_size_75_mm_id_160_mm_od_37_mm_depth'
    option['size'] = '6315'
    option['series'] = '6300'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 75.0
    option['dimensions']['outside'] = 160.0
    option['dimensions']['width'] = 37.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 13
    option['internal_geometry']['balls_per_row'] = 13
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 75.0
    option['internal_geometry']['parameters']['outside'] = 160.0
    option['internal_geometry']['parameters']['width'] = 37.0
    option['internal_geometry']['parameters']['edge'] = 2.2199999999999998
    option['internal_geometry']['parameters']['pitch_radius'] = 58.75
    option['internal_geometry']['parameters']['ball_radius'] = 10.360000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 10.619000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 52.3268
    option['internal_geometry']['parameters']['outer_shoulder'] = 65.1732
    option['internal_geometry']['parameters']['cage_half_width'] = 5.698000000000001
    option['internal_geometry']['parameters']['cage_low'] = 9.842
    option['internal_geometry']['parameters']['cage_high'] = 11.914
    option['internal_geometry']['parameters']['window_radius'] = 4.9728
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '3,015'
    options.append(copy.deepcopy(option))

    # 6316: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6300_series_6316_size_80_mm_id_170_mm_od_39_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6300_series_6316_size_80_mm_id_170_mm_od_39_mm_depth'
    option['size'] = '6316'
    option['series'] = '6300'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 80.0
    option['dimensions']['outside'] = 170.0
    option['dimensions']['width'] = 39.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 13
    option['internal_geometry']['balls_per_row'] = 13
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 80.0
    option['internal_geometry']['parameters']['outside'] = 170.0
    option['internal_geometry']['parameters']['width'] = 39.0
    option['internal_geometry']['parameters']['edge'] = 2.34
    option['internal_geometry']['parameters']['pitch_radius'] = 62.5
    option['internal_geometry']['parameters']['ball_radius'] = 10.920000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 11.193000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 55.7296
    option['internal_geometry']['parameters']['outer_shoulder'] = 69.2704
    option['internal_geometry']['parameters']['cage_half_width'] = 6.006000000000001
    option['internal_geometry']['parameters']['cage_low'] = 10.374
    option['internal_geometry']['parameters']['cage_high'] = 12.558000000000002
    option['internal_geometry']['parameters']['window_radius'] = 5.241600000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '3,587'
    options.append(copy.deepcopy(option))

    # 6317: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6300_series_6317_size_85_mm_id_180_mm_od_41_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6300_series_6317_size_85_mm_id_180_mm_od_41_mm_depth'
    option['size'] = '6317'
    option['series'] = '6300'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 85.0
    option['dimensions']['outside'] = 180.0
    option['dimensions']['width'] = 41.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 13
    option['internal_geometry']['balls_per_row'] = 13
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 85.0
    option['internal_geometry']['parameters']['outside'] = 180.0
    option['internal_geometry']['parameters']['width'] = 41.0
    option['internal_geometry']['parameters']['edge'] = 2.46
    option['internal_geometry']['parameters']['pitch_radius'] = 66.25
    option['internal_geometry']['parameters']['ball_radius'] = 11.48
    option['internal_geometry']['parameters']['groove_radius'] = 11.767000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 59.1324
    option['internal_geometry']['parameters']['outer_shoulder'] = 73.3676
    option['internal_geometry']['parameters']['cage_half_width'] = 6.314000000000001
    option['internal_geometry']['parameters']['cage_low'] = 10.906
    option['internal_geometry']['parameters']['cage_high'] = 13.202
    option['internal_geometry']['parameters']['window_radius'] = 5.5104
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '4,227'
    options.append(copy.deepcopy(option))

    # 6318: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6300_series_6318_size_90_mm_id_190_mm_od_43_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6300_series_6318_size_90_mm_id_190_mm_od_43_mm_depth'
    option['size'] = '6318'
    option['series'] = '6300'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 90.0
    option['dimensions']['outside'] = 190.0
    option['dimensions']['width'] = 43.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 13
    option['internal_geometry']['balls_per_row'] = 13
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 90.0
    option['internal_geometry']['parameters']['outside'] = 190.0
    option['internal_geometry']['parameters']['width'] = 43.0
    option['internal_geometry']['parameters']['edge'] = 2.58
    option['internal_geometry']['parameters']['pitch_radius'] = 70.0
    option['internal_geometry']['parameters']['ball_radius'] = 12.040000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 12.341000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 62.5352
    option['internal_geometry']['parameters']['outer_shoulder'] = 77.4648
    option['internal_geometry']['parameters']['cage_half_width'] = 6.622000000000001
    option['internal_geometry']['parameters']['cage_low'] = 11.438
    option['internal_geometry']['parameters']['cage_high'] = 13.846
    option['internal_geometry']['parameters']['window_radius'] = 5.7792
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '4,903'
    options.append(copy.deepcopy(option))

    # 6319: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6300_series_6319_size_95_mm_id_200_mm_od_45_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6300_series_6319_size_95_mm_id_200_mm_od_45_mm_depth'
    option['size'] = '6319'
    option['series'] = '6300'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 95.0
    option['dimensions']['outside'] = 200.0
    option['dimensions']['width'] = 45.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 13
    option['internal_geometry']['balls_per_row'] = 13
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 95.0
    option['internal_geometry']['parameters']['outside'] = 200.0
    option['internal_geometry']['parameters']['width'] = 45.0
    option['internal_geometry']['parameters']['edge'] = 2.6999999999999997
    option['internal_geometry']['parameters']['pitch_radius'] = 73.75
    option['internal_geometry']['parameters']['ball_radius'] = 12.600000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 12.915000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 65.938
    option['internal_geometry']['parameters']['outer_shoulder'] = 81.562
    option['internal_geometry']['parameters']['cage_half_width'] = 6.9300000000000015
    option['internal_geometry']['parameters']['cage_low'] = 11.97
    option['internal_geometry']['parameters']['cage_high'] = 14.49
    option['internal_geometry']['parameters']['window_radius'] = 6.048
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '5,661'
    options.append(copy.deepcopy(option))

    # 6320: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6300_series_6320_size_100_mm_id_215_mm_od_47_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6300_series_6320_size_100_mm_id_215_mm_od_47_mm_depth'
    option['size'] = '6320'
    option['series'] = '6300'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 100.0
    option['dimensions']['outside'] = 215.0
    option['dimensions']['width'] = 47.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 13
    option['internal_geometry']['balls_per_row'] = 13
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 100.0
    option['internal_geometry']['parameters']['outside'] = 215.0
    option['internal_geometry']['parameters']['width'] = 47.0
    option['internal_geometry']['parameters']['edge'] = 2.82
    option['internal_geometry']['parameters']['pitch_radius'] = 78.75
    option['internal_geometry']['parameters']['ball_radius'] = 13.160000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 13.489000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 70.5908
    option['internal_geometry']['parameters']['outer_shoulder'] = 86.9092
    option['internal_geometry']['parameters']['cage_half_width'] = 7.238000000000001
    option['internal_geometry']['parameters']['cage_low'] = 12.502
    option['internal_geometry']['parameters']['cage_high'] = 15.134
    option['internal_geometry']['parameters']['window_radius'] = 6.316800000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '6,992'
    options.append(copy.deepcopy(option))

    # 6321: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6300_series_6321_size_105_mm_id_225_mm_od_49_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6300_series_6321_size_105_mm_id_225_mm_od_49_mm_depth'
    option['size'] = '6321'
    option['series'] = '6300'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 105.0
    option['dimensions']['outside'] = 225.0
    option['dimensions']['width'] = 49.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 13
    option['internal_geometry']['balls_per_row'] = 13
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 105.0
    option['internal_geometry']['parameters']['outside'] = 225.0
    option['internal_geometry']['parameters']['width'] = 49.0
    option['internal_geometry']['parameters']['edge'] = 2.94
    option['internal_geometry']['parameters']['pitch_radius'] = 82.5
    option['internal_geometry']['parameters']['ball_radius'] = 13.72
    option['internal_geometry']['parameters']['groove_radius'] = 14.063
    option['internal_geometry']['parameters']['inner_shoulder'] = 73.9936
    option['internal_geometry']['parameters']['outer_shoulder'] = 91.0064
    option['internal_geometry']['parameters']['cage_half_width'] = 7.546000000000001
    option['internal_geometry']['parameters']['cage_low'] = 13.034
    option['internal_geometry']['parameters']['cage_high'] = 15.777999999999999
    option['internal_geometry']['parameters']['window_radius'] = 6.5856
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '8,040'
    options.append(copy.deepcopy(option))

    # 6322: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6300_series_6322_size_110_mm_id_240_mm_od_50_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6300_series_6322_size_110_mm_id_240_mm_od_50_mm_depth'
    option['size'] = '6322'
    option['series'] = '6300'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 110.0
    option['dimensions']['outside'] = 240.0
    option['dimensions']['width'] = 50.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 14
    option['internal_geometry']['balls_per_row'] = 14
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 110.0
    option['internal_geometry']['parameters']['outside'] = 240.0
    option['internal_geometry']['parameters']['width'] = 50.0
    option['internal_geometry']['parameters']['edge'] = 3.0
    option['internal_geometry']['parameters']['pitch_radius'] = 87.5
    option['internal_geometry']['parameters']['ball_radius'] = 14.000000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 14.350000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 78.82
    option['internal_geometry']['parameters']['outer_shoulder'] = 96.18
    option['internal_geometry']['parameters']['cage_half_width'] = 7.700000000000002
    option['internal_geometry']['parameters']['cage_low'] = 13.3
    option['internal_geometry']['parameters']['cage_high'] = 16.1
    option['internal_geometry']['parameters']['window_radius'] = 6.720000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '9,529'
    options.append(copy.deepcopy(option))

    # 6324: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6300_series_6324_size_120_mm_id_260_mm_od_55_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6300_series_6324_size_120_mm_id_260_mm_od_55_mm_depth'
    option['size'] = '6324'
    option['series'] = '6300'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 120.0
    option['dimensions']['outside'] = 260.0
    option['dimensions']['width'] = 55.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 14
    option['internal_geometry']['balls_per_row'] = 14
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 120.0
    option['internal_geometry']['parameters']['outside'] = 260.0
    option['internal_geometry']['parameters']['width'] = 55.0
    option['internal_geometry']['parameters']['edge'] = 3.3
    option['internal_geometry']['parameters']['pitch_radius'] = 95.0
    option['internal_geometry']['parameters']['ball_radius'] = 15.400000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 15.785000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 85.452
    option['internal_geometry']['parameters']['outer_shoulder'] = 104.548
    option['internal_geometry']['parameters']['cage_half_width'] = 8.470000000000002
    option['internal_geometry']['parameters']['cage_low'] = 14.63
    option['internal_geometry']['parameters']['cage_high'] = 17.71
    option['internal_geometry']['parameters']['window_radius'] = 7.392
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '12,785'
    options.append(copy.deepcopy(option))

    # 6326: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6300_series_6326_size_130_mm_id_280_mm_od_58_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6300_series_6326_size_130_mm_id_280_mm_od_58_mm_depth'
    option['size'] = '6326'
    option['series'] = '6300'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 130.0
    option['dimensions']['outside'] = 280.0
    option['dimensions']['width'] = 58.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 14
    option['internal_geometry']['balls_per_row'] = 14
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 130.0
    option['internal_geometry']['parameters']['outside'] = 280.0
    option['internal_geometry']['parameters']['width'] = 58.0
    option['internal_geometry']['parameters']['edge'] = 3.48
    option['internal_geometry']['parameters']['pitch_radius'] = 102.5
    option['internal_geometry']['parameters']['ball_radius'] = 16.240000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 16.646
    option['internal_geometry']['parameters']['inner_shoulder'] = 92.4312
    option['internal_geometry']['parameters']['outer_shoulder'] = 112.5688
    option['internal_geometry']['parameters']['cage_half_width'] = 8.932000000000002
    option['internal_geometry']['parameters']['cage_low'] = 15.428
    option['internal_geometry']['parameters']['cage_high'] = 18.676000000000002
    option['internal_geometry']['parameters']['window_radius'] = 7.7952
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '18,278'
    options.append(copy.deepcopy(option))

    # 6328: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6300_series_6328_size_140_mm_id_300_mm_od_62_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6300_series_6328_size_140_mm_id_300_mm_od_62_mm_depth'
    option['size'] = '6328'
    option['series'] = '6300'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 140.0
    option['dimensions']['outside'] = 300.0
    option['dimensions']['width'] = 62.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 14
    option['internal_geometry']['balls_per_row'] = 14
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 140.0
    option['internal_geometry']['parameters']['outside'] = 300.0
    option['internal_geometry']['parameters']['width'] = 62.0
    option['internal_geometry']['parameters']['edge'] = 3.7199999999999998
    option['internal_geometry']['parameters']['pitch_radius'] = 110.0
    option['internal_geometry']['parameters']['ball_radius'] = 17.360000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 17.794000000000004
    option['internal_geometry']['parameters']['inner_shoulder'] = 99.2368
    option['internal_geometry']['parameters']['outer_shoulder'] = 120.7632
    option['internal_geometry']['parameters']['cage_half_width'] = 9.548000000000002
    option['internal_geometry']['parameters']['cage_low'] = 16.492
    option['internal_geometry']['parameters']['cage_high'] = 19.964000000000002
    option['internal_geometry']['parameters']['window_radius'] = 8.3328
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '22,273'
    options.append(copy.deepcopy(option))

    # 6330: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6300_series_6330_size_150_mm_id_320_mm_od_65_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6300_series_6330_size_150_mm_id_320_mm_od_65_mm_depth'
    option['size'] = '6330'
    option['series'] = '6300'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 150.0
    option['dimensions']['outside'] = 320.0
    option['dimensions']['width'] = 65.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 14
    option['internal_geometry']['balls_per_row'] = 14
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 150.0
    option['internal_geometry']['parameters']['outside'] = 320.0
    option['internal_geometry']['parameters']['width'] = 65.0
    option['internal_geometry']['parameters']['edge'] = 3.9
    option['internal_geometry']['parameters']['pitch_radius'] = 117.5
    option['internal_geometry']['parameters']['ball_radius'] = 18.200000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 18.655
    option['internal_geometry']['parameters']['inner_shoulder'] = 106.216
    option['internal_geometry']['parameters']['outer_shoulder'] = 128.784
    option['internal_geometry']['parameters']['cage_half_width'] = 10.010000000000002
    option['internal_geometry']['parameters']['cage_low'] = 17.290000000000003
    option['internal_geometry']['parameters']['cage_high'] = 20.930000000000003
    option['internal_geometry']['parameters']['window_radius'] = 8.736
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '26,668'
    options.append(copy.deepcopy(option))

    # 6700: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6700_series_6700_size_10_mm_id_15_mm_od_3_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6700_series_6700_size_10_mm_id_15_mm_od_3_mm_depth'
    option['size'] = '6700'
    option['series'] = '6700'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 10.0
    option['dimensions']['outside'] = 15.0
    option['dimensions']['width'] = 3.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://www.astbearings.com/catalog/thin_section_metric/6700']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 11
    option['internal_geometry']['balls_per_row'] = 11
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 10.0
    option['internal_geometry']['parameters']['outside'] = 15.0
    option['internal_geometry']['parameters']['width'] = 3.0
    option['internal_geometry']['parameters']['edge'] = 0.15
    option['internal_geometry']['parameters']['pitch_radius'] = 6.25
    option['internal_geometry']['parameters']['ball_radius'] = 0.794
    option['internal_geometry']['parameters']['groove_radius'] = 0.8138500000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 5.75772
    option['internal_geometry']['parameters']['outer_shoulder'] = 6.74228
    option['internal_geometry']['parameters']['cage_half_width'] = 0.43670000000000003
    option['internal_geometry']['parameters']['cage_low'] = 0.7543
    option['internal_geometry']['parameters']['cage_high'] = 0.9131
    option['internal_geometry']['parameters']['window_radius'] = 0.38112
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'manufacturer_sourced'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['availability_note'] = 'Listed in the cited catalogue; current stock and lead time not confirmed.'
    option['catalogue_metadata']['bearing_closure_reference'] = 'Open'
    option['catalogue_metadata']['catalogue_model'] = '6700'
    option['catalogue_metadata']['catalogue_supplier'] = 'AST Bearings'
    option['catalogue_metadata']['description'] = 'Thin section deep groove ball bearing, 10 x 15 x 3 mm (bore x OD x width).'
    option['catalogue_metadata']['source_checked'] = '2026-10-06'
    option['catalogue_metadata']['source_url'] = 'https://www.astbearings.com/catalog/thin_section_metric/6700'
    option['catalogue_metadata']['weight'] = '1.4'
    option['catalogue_metadata']['weight_note'] = ('Approximate catalogue mass for the cited open bearing; varies by manufacturer and '
     'closure.')
    option['catalogue_metadata']['weight_unit'] = 'g'
    option['catalogue_metadata']['md5'] = 'cd88654c09a86f1765e5a3e58afb7aad'
    option['catalogue_metadata']['md5_5'] = 'cd886'
    option['catalogue_metadata']['md5_5_upper'] = 'CD886'
    option['catalogue_metadata']['md5_6'] = 'cd8865'
    option['catalogue_metadata']['md5_6_upper'] = 'CD8865'
    option['catalogue_metadata']['md5_10'] = 'cd88654c09'
    option['catalogue_metadata']['md5_10_upper'] = 'CD88654C09'
    option['catalogue_metadata']['md5_6_alpha'] = '80pd1'
    option['catalogue_metadata']['md5_6_alpha_upper'] = '80PD1'
    option['catalogue_metadata']['bip_39_full_array'] = ['snow',
     'drip',
     'fantasy',
     'battle',
     'manage',
     'merry',
     'nurse',
     'refuse',
     'tortoise',
     'fit',
     'team',
     'fog']
    option['catalogue_metadata']['bip_39_full_space'] = 'snow drip fantasy battle manage merry nurse refuse tortoise fit team fog'
    option['catalogue_metadata']['bip_39_full_no_space'] = 'snowdripfantasybattlemanagemerrynurserefusetortoisefitteamfog'
    option['catalogue_metadata']['bip_39_full_underscore'] = 'snow_drip_fantasy_battle_manage_merry_nurse_refuse_tortoise_fit_team_fog'
    option['catalogue_metadata']['bip_39_2_word_array'] = ['snow', 'drip']
    option['catalogue_metadata']['bip_39_2_word_space'] = 'snow drip'
    option['catalogue_metadata']['bip_39_2_word_no_space'] = 'snowdrip'
    option['catalogue_metadata']['bip_39_2_word_underscore'] = 'snow_drip'
    option['catalogue_metadata']['bip_39_3_word_array'] = ['snow', 'drip', 'fantasy']
    option['catalogue_metadata']['bip_39_3_word_space'] = 'snow drip fantasy'
    option['catalogue_metadata']['bip_39_3_word_no_space'] = 'snowdripfantasy'
    option['catalogue_metadata']['bip_39_3_word_underscore'] = 'snow_drip_fantasy'
    options.append(copy.deepcopy(option))

    # 6701: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6700_series_6701_size_12_mm_id_18_mm_od_4_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6700_series_6701_size_12_mm_id_18_mm_od_4_mm_depth'
    option['size'] = '6701'
    option['series'] = '6700'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 12.0
    option['dimensions']['outside'] = 18.0
    option['dimensions']['width'] = 4.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 20
    option['internal_geometry']['balls_per_row'] = 20
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 12.0
    option['internal_geometry']['parameters']['outside'] = 18.0
    option['internal_geometry']['parameters']['width'] = 4.0
    option['internal_geometry']['parameters']['edge'] = 0.18
    option['internal_geometry']['parameters']['pitch_radius'] = 7.5
    option['internal_geometry']['parameters']['ball_radius'] = 0.8400000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 0.8610000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 6.9792
    option['internal_geometry']['parameters']['outer_shoulder'] = 8.0208
    option['internal_geometry']['parameters']['cage_half_width'] = 0.4620000000000001
    option['internal_geometry']['parameters']['cage_low'] = 0.798
    option['internal_geometry']['parameters']['cage_high'] = 0.966
    option['internal_geometry']['parameters']['window_radius'] = 0.4032
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '2'
    options.append(copy.deepcopy(option))

    # 6702: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6700_series_6702_size_15_mm_id_21_mm_od_4_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6700_series_6702_size_15_mm_id_21_mm_od_4_mm_depth'
    option['size'] = '6702'
    option['series'] = '6700'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 15.0
    option['dimensions']['outside'] = 21.0
    option['dimensions']['width'] = 4.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 24
    option['internal_geometry']['balls_per_row'] = 24
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 15.0
    option['internal_geometry']['parameters']['outside'] = 21.0
    option['internal_geometry']['parameters']['width'] = 4.0
    option['internal_geometry']['parameters']['edge'] = 0.18
    option['internal_geometry']['parameters']['pitch_radius'] = 9.0
    option['internal_geometry']['parameters']['ball_radius'] = 0.8400000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 0.8610000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 8.4792
    option['internal_geometry']['parameters']['outer_shoulder'] = 9.5208
    option['internal_geometry']['parameters']['cage_half_width'] = 0.4620000000000001
    option['internal_geometry']['parameters']['cage_low'] = 0.798
    option['internal_geometry']['parameters']['cage_high'] = 0.966
    option['internal_geometry']['parameters']['window_radius'] = 0.4032
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '2'
    options.append(copy.deepcopy(option))

    # 6703: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6700_series_6703_size_17_mm_id_23_mm_od_4_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6700_series_6703_size_17_mm_id_23_mm_od_4_mm_depth'
    option['size'] = '6703'
    option['series'] = '6700'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 17.0
    option['dimensions']['outside'] = 23.0
    option['dimensions']['width'] = 4.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 27
    option['internal_geometry']['balls_per_row'] = 27
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 17.0
    option['internal_geometry']['parameters']['outside'] = 23.0
    option['internal_geometry']['parameters']['width'] = 4.0
    option['internal_geometry']['parameters']['edge'] = 0.18
    option['internal_geometry']['parameters']['pitch_radius'] = 10.0
    option['internal_geometry']['parameters']['ball_radius'] = 0.8400000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 0.8610000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 9.4792
    option['internal_geometry']['parameters']['outer_shoulder'] = 10.5208
    option['internal_geometry']['parameters']['cage_half_width'] = 0.4620000000000001
    option['internal_geometry']['parameters']['cage_low'] = 0.798
    option['internal_geometry']['parameters']['cage_high'] = 0.966
    option['internal_geometry']['parameters']['window_radius'] = 0.4032
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '3'
    options.append(copy.deepcopy(option))

    # 6704: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6700_series_6704_size_20_mm_id_27_mm_od_4_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6700_series_6704_size_20_mm_id_27_mm_od_4_mm_depth'
    option['size'] = '6704'
    option['series'] = '6700'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 20.0
    option['dimensions']['outside'] = 27.0
    option['dimensions']['width'] = 4.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 27
    option['internal_geometry']['balls_per_row'] = 27
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 20.0
    option['internal_geometry']['parameters']['outside'] = 27.0
    option['internal_geometry']['parameters']['width'] = 4.0
    option['internal_geometry']['parameters']['edge'] = 0.21
    option['internal_geometry']['parameters']['pitch_radius'] = 11.75
    option['internal_geometry']['parameters']['ball_radius'] = 0.9800000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 1.0045000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 11.1424
    option['internal_geometry']['parameters']['outer_shoulder'] = 12.3576
    option['internal_geometry']['parameters']['cage_half_width'] = 0.5390000000000001
    option['internal_geometry']['parameters']['cage_low'] = 0.931
    option['internal_geometry']['parameters']['cage_high'] = 1.127
    option['internal_geometry']['parameters']['window_radius'] = 0.47040000000000004
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '5'
    options.append(copy.deepcopy(option))

    # 6705: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6700_series_6705_size_25_mm_id_32_mm_od_4_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6700_series_6705_size_25_mm_id_32_mm_od_4_mm_depth'
    option['size'] = '6705'
    option['series'] = '6700'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 25.0
    option['dimensions']['outside'] = 32.0
    option['dimensions']['width'] = 4.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 33
    option['internal_geometry']['balls_per_row'] = 33
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 25.0
    option['internal_geometry']['parameters']['outside'] = 32.0
    option['internal_geometry']['parameters']['width'] = 4.0
    option['internal_geometry']['parameters']['edge'] = 0.21
    option['internal_geometry']['parameters']['pitch_radius'] = 14.25
    option['internal_geometry']['parameters']['ball_radius'] = 0.9800000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 1.0045000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 13.6424
    option['internal_geometry']['parameters']['outer_shoulder'] = 14.8576
    option['internal_geometry']['parameters']['cage_half_width'] = 0.5390000000000001
    option['internal_geometry']['parameters']['cage_low'] = 0.931
    option['internal_geometry']['parameters']['cage_high'] = 1.127
    option['internal_geometry']['parameters']['window_radius'] = 0.47040000000000004
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '7'
    options.append(copy.deepcopy(option))

    # 6706: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6700_series_6706_size_30_mm_id_37_mm_od_4_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6700_series_6706_size_30_mm_id_37_mm_od_4_mm_depth'
    option['size'] = '6706'
    option['series'] = '6700'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 30.0
    option['dimensions']['outside'] = 37.0
    option['dimensions']['width'] = 4.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 39
    option['internal_geometry']['balls_per_row'] = 39
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 30.0
    option['internal_geometry']['parameters']['outside'] = 37.0
    option['internal_geometry']['parameters']['width'] = 4.0
    option['internal_geometry']['parameters']['edge'] = 0.21
    option['internal_geometry']['parameters']['pitch_radius'] = 16.75
    option['internal_geometry']['parameters']['ball_radius'] = 0.9800000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 1.0045000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 16.1424
    option['internal_geometry']['parameters']['outer_shoulder'] = 17.3576
    option['internal_geometry']['parameters']['cage_half_width'] = 0.5390000000000001
    option['internal_geometry']['parameters']['cage_low'] = 0.931
    option['internal_geometry']['parameters']['cage_high'] = 1.127
    option['internal_geometry']['parameters']['window_radius'] = 0.47040000000000004
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '8'
    options.append(copy.deepcopy(option))

    # 6707: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6700_series_6707_size_35_mm_id_44_mm_od_5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6700_series_6707_size_35_mm_id_44_mm_od_5_mm_depth'
    option['size'] = '6707'
    option['series'] = '6700'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 35.0
    option['dimensions']['outside'] = 44.0
    option['dimensions']['width'] = 5.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 36
    option['internal_geometry']['balls_per_row'] = 36
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 35.0
    option['internal_geometry']['parameters']['outside'] = 44.0
    option['internal_geometry']['parameters']['width'] = 5.0
    option['internal_geometry']['parameters']['edge'] = 0.27
    option['internal_geometry']['parameters']['pitch_radius'] = 19.75
    option['internal_geometry']['parameters']['ball_radius'] = 1.2600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.2915000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 18.9688
    option['internal_geometry']['parameters']['outer_shoulder'] = 20.5312
    option['internal_geometry']['parameters']['cage_half_width'] = 0.6930000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.197
    option['internal_geometry']['parameters']['cage_high'] = 1.449
    option['internal_geometry']['parameters']['window_radius'] = 0.6048000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '10'
    options.append(copy.deepcopy(option))

    # 6708: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6700_series_6708_size_40_mm_id_50_mm_od_6_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6700_series_6708_size_40_mm_id_50_mm_od_6_mm_depth'
    option['size'] = '6708'
    option['series'] = '6700'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 40.0
    option['dimensions']['outside'] = 50.0
    option['dimensions']['width'] = 6.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 37
    option['internal_geometry']['balls_per_row'] = 37
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 40.0
    option['internal_geometry']['parameters']['outside'] = 50.0
    option['internal_geometry']['parameters']['width'] = 6.0
    option['internal_geometry']['parameters']['edge'] = 0.3
    option['internal_geometry']['parameters']['pitch_radius'] = 22.5
    option['internal_geometry']['parameters']['ball_radius'] = 1.4000000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 1.435
    option['internal_geometry']['parameters']['inner_shoulder'] = 21.632
    option['internal_geometry']['parameters']['outer_shoulder'] = 23.368
    option['internal_geometry']['parameters']['cage_half_width'] = 0.7700000000000001
    option['internal_geometry']['parameters']['cage_low'] = 1.33
    option['internal_geometry']['parameters']['cage_high'] = 1.61
    option['internal_geometry']['parameters']['window_radius'] = 0.672
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['availability_note'] = 'Listed in the cited catalogue; current stock and lead time not confirmed.'
    option['catalogue_metadata']['bearing_closure_reference'] = 'Open'
    option['catalogue_metadata']['catalogue_model'] = '6708'
    option['catalogue_metadata']['catalogue_supplier'] = 'AST Bearings'
    option['catalogue_metadata']['description'] = 'Thin section deep groove ball bearing, 40 x 50 x 6 mm (bore x OD x width).'
    option['catalogue_metadata']['source_checked'] = '2026-10-06'
    option['catalogue_metadata']['source_url'] = 'https://www.astbearings.com/catalog/thin_section_metric/6708'
    option['catalogue_metadata']['weight'] = '23'
    option['catalogue_metadata']['weight_note'] = ('Approximate catalogue mass for the cited open bearing; varies by manufacturer and '
     'closure.')
    option['catalogue_metadata']['weight_unit'] = 'g'
    options.append(copy.deepcopy(option))

    # 6709: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6700_series_6709_size_45_mm_id_55_mm_od_6_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6700_series_6709_size_45_mm_id_55_mm_od_6_mm_depth'
    option['size'] = '6709'
    option['series'] = '6700'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 45.0
    option['dimensions']['outside'] = 55.0
    option['dimensions']['width'] = 6.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 41
    option['internal_geometry']['balls_per_row'] = 41
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 45.0
    option['internal_geometry']['parameters']['outside'] = 55.0
    option['internal_geometry']['parameters']['width'] = 6.0
    option['internal_geometry']['parameters']['edge'] = 0.3
    option['internal_geometry']['parameters']['pitch_radius'] = 25.0
    option['internal_geometry']['parameters']['ball_radius'] = 1.4000000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 1.435
    option['internal_geometry']['parameters']['inner_shoulder'] = 24.132
    option['internal_geometry']['parameters']['outer_shoulder'] = 25.868
    option['internal_geometry']['parameters']['cage_half_width'] = 0.7700000000000001
    option['internal_geometry']['parameters']['cage_low'] = 1.33
    option['internal_geometry']['parameters']['cage_high'] = 1.61
    option['internal_geometry']['parameters']['window_radius'] = 0.672
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['availability_note'] = 'Listed in the cited catalogue; current stock and lead time not confirmed.'
    option['catalogue_metadata']['bearing_closure_reference'] = 'Open'
    option['catalogue_metadata']['catalogue_model'] = '6709'
    option['catalogue_metadata']['catalogue_supplier'] = 'AST Bearings'
    option['catalogue_metadata']['description'] = 'Thin section deep groove ball bearing, 45 x 55 x 6 mm (bore x OD x width).'
    option['catalogue_metadata']['source_checked'] = '2026-10-06'
    option['catalogue_metadata']['source_url'] = 'https://www.astbearings.com/catalog/thin_section_metric/6709'
    option['catalogue_metadata']['weight'] = '25'
    option['catalogue_metadata']['weight_note'] = ('Approximate catalogue mass for the cited open bearing; varies by manufacturer and '
     'closure.')
    option['catalogue_metadata']['weight_unit'] = 'g'
    options.append(copy.deepcopy(option))

    # 6710: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6700_series_6710_size_50_mm_id_62_mm_od_6_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6700_series_6710_size_50_mm_id_62_mm_od_6_mm_depth'
    option['size'] = '6710'
    option['series'] = '6700'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 50.0
    option['dimensions']['outside'] = 62.0
    option['dimensions']['width'] = 6.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 38
    option['internal_geometry']['balls_per_row'] = 38
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 50.0
    option['internal_geometry']['parameters']['outside'] = 62.0
    option['internal_geometry']['parameters']['width'] = 6.0
    option['internal_geometry']['parameters']['edge'] = 0.36
    option['internal_geometry']['parameters']['pitch_radius'] = 28.0
    option['internal_geometry']['parameters']['ball_radius'] = 1.6800000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.7220000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 26.9584
    option['internal_geometry']['parameters']['outer_shoulder'] = 29.0416
    option['internal_geometry']['parameters']['cage_half_width'] = 0.9240000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.596
    option['internal_geometry']['parameters']['cage_high'] = 1.932
    option['internal_geometry']['parameters']['window_radius'] = 0.8064
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['availability_note'] = 'Listed in the cited catalogue; current stock and lead time not confirmed.'
    option['catalogue_metadata']['bearing_closure_reference'] = 'Open'
    option['catalogue_metadata']['catalogue_model'] = '6710'
    option['catalogue_metadata']['catalogue_supplier'] = 'AST Bearings'
    option['catalogue_metadata']['description'] = 'Thin section deep groove ball bearing, 50 x 62 x 6 mm (bore x OD x width).'
    option['catalogue_metadata']['source_checked'] = '2026-10-06'
    option['catalogue_metadata']['source_url'] = 'https://www.astbearings.com/catalog/thin_section_metric/6710'
    option['catalogue_metadata']['weight'] = '64'
    option['catalogue_metadata']['weight_note'] = ('Approximate catalogue mass for the cited open bearing; varies by manufacturer and '
     'closure.')
    option['catalogue_metadata']['weight_unit'] = 'g'
    options.append(copy.deepcopy(option))

    # 6711: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6700_series_6711_size_55_mm_id_68_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6700_series_6711_size_55_mm_id_68_mm_od_7_mm_depth'
    option['size'] = '6711'
    option['series'] = '6700'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 55.0
    option['dimensions']['outside'] = 68.0
    option['dimensions']['width'] = 7.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 39
    option['internal_geometry']['balls_per_row'] = 39
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 55.0
    option['internal_geometry']['parameters']['outside'] = 68.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.39
    option['internal_geometry']['parameters']['pitch_radius'] = 30.75
    option['internal_geometry']['parameters']['ball_radius'] = 1.8200000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 1.8655000000000004
    option['internal_geometry']['parameters']['inner_shoulder'] = 29.6216
    option['internal_geometry']['parameters']['outer_shoulder'] = 31.8784
    option['internal_geometry']['parameters']['cage_half_width'] = 1.0010000000000003
    option['internal_geometry']['parameters']['cage_low'] = 1.729
    option['internal_geometry']['parameters']['cage_high'] = 2.093
    option['internal_geometry']['parameters']['window_radius'] = 0.8736000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['availability_note'] = 'Listed in the cited catalogue; current stock and lead time not confirmed.'
    option['catalogue_metadata']['bearing_closure_reference'] = 'Open'
    option['catalogue_metadata']['catalogue_model'] = '61711'
    option['catalogue_metadata']['catalogue_supplier'] = 'C&H Bearing'
    option['catalogue_metadata']['description'] = 'Thin section deep groove ball bearing, 55 x 68 x 7 mm (bore x OD x width).'
    option['catalogue_metadata']['source_checked'] = '2026-10-06'
    option['catalogue_metadata']['source_url'] = 'https://www.chenghuibearing.com/product-model/61711/'
    option['catalogue_metadata']['weight'] = '42'
    option['catalogue_metadata']['weight_note'] = ('Approximate catalogue mass for the cited open bearing; varies by manufacturer and '
     'closure.')
    option['catalogue_metadata']['weight_unit'] = 'g'
    options.append(copy.deepcopy(option))

    # 6712: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6700_series_6712_size_60_mm_id_75_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6700_series_6712_size_60_mm_id_75_mm_od_7_mm_depth'
    option['size'] = '6712'
    option['series'] = '6700'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 60.0
    option['dimensions']['outside'] = 75.0
    option['dimensions']['width'] = 7.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 40
    option['internal_geometry']['balls_per_row'] = 40
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 60.0
    option['internal_geometry']['parameters']['outside'] = 75.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.42
    option['internal_geometry']['parameters']['pitch_radius'] = 33.75
    option['internal_geometry']['parameters']['ball_radius'] = 1.9600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 2.0090000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 32.5348
    option['internal_geometry']['parameters']['outer_shoulder'] = 34.9652
    option['internal_geometry']['parameters']['cage_half_width'] = 1.0780000000000003
    option['internal_geometry']['parameters']['cage_low'] = 1.862
    option['internal_geometry']['parameters']['cage_high'] = 2.254
    option['internal_geometry']['parameters']['window_radius'] = 0.9408000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['availability_note'] = 'Listed in the cited catalogue; current stock and lead time not confirmed.'
    option['catalogue_metadata']['bearing_closure_reference'] = 'Open'
    option['catalogue_metadata']['catalogue_model'] = '61712'
    option['catalogue_metadata']['catalogue_supplier'] = 'C&H Bearing'
    option['catalogue_metadata']['description'] = 'Thin section deep groove ball bearing, 60 x 75 x 7 mm (bore x OD x width).'
    option['catalogue_metadata']['dimension_note'] = ('C&H and Kecheng list 60x75x7; Maysme lists 60x72x7. This entry follows the C&H 61712 '
     'drawing; do not assume the alternative OD fits.')
    option['catalogue_metadata']['source_checked'] = '2026-10-06'
    option['catalogue_metadata']['source_url'] = 'https://www.chenghuibearing.com/product-model/61712/'
    option['catalogue_metadata']['weight'] = '55'
    option['catalogue_metadata']['weight_note'] = ('Approximate catalogue mass for the cited open bearing; varies by manufacturer and '
     'closure.')
    option['catalogue_metadata']['weight_unit'] = 'g'
    options.append(copy.deepcopy(option))

    # 6713: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6700_series_6713_size_65_mm_id_80_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6700_series_6713_size_65_mm_id_80_mm_od_7_mm_depth'
    option['size'] = '6713'
    option['series'] = '6700'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 65.0
    option['dimensions']['outside'] = 80.0
    option['dimensions']['width'] = 7.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 43
    option['internal_geometry']['balls_per_row'] = 43
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 65.0
    option['internal_geometry']['parameters']['outside'] = 80.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.42
    option['internal_geometry']['parameters']['pitch_radius'] = 36.25
    option['internal_geometry']['parameters']['ball_radius'] = 1.9600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 2.0090000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 35.0348
    option['internal_geometry']['parameters']['outer_shoulder'] = 37.4652
    option['internal_geometry']['parameters']['cage_half_width'] = 1.0780000000000003
    option['internal_geometry']['parameters']['cage_low'] = 1.862
    option['internal_geometry']['parameters']['cage_high'] = 2.254
    option['internal_geometry']['parameters']['window_radius'] = 0.9408000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['availability_note'] = 'Listed in the cited catalogue; current stock and lead time not confirmed.'
    option['catalogue_metadata']['bearing_closure_reference'] = 'Open'
    option['catalogue_metadata']['catalogue_model'] = '61713'
    option['catalogue_metadata']['catalogue_supplier'] = 'C&H Bearing'
    option['catalogue_metadata']['description'] = 'Thin section deep groove ball bearing, 65 x 80 x 7 mm (bore x OD x width).'
    option['catalogue_metadata']['source_checked'] = '2026-10-06'
    option['catalogue_metadata']['source_url'] = 'https://www.chenghuibearing.com/product-model/61713/'
    option['catalogue_metadata']['weight'] = '59'
    option['catalogue_metadata']['weight_note'] = ('Approximate catalogue mass for the cited open bearing; varies by manufacturer and '
     'closure.')
    option['catalogue_metadata']['weight_unit'] = 'g'
    options.append(copy.deepcopy(option))

    # 6714: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6700_series_6714_size_70_mm_id_85_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6700_series_6714_size_70_mm_id_85_mm_od_7_mm_depth'
    option['size'] = '6714'
    option['series'] = '6700'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 70.0
    option['dimensions']['outside'] = 85.0
    option['dimensions']['width'] = 7.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 45
    option['internal_geometry']['balls_per_row'] = 45
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 70.0
    option['internal_geometry']['parameters']['outside'] = 85.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.42
    option['internal_geometry']['parameters']['pitch_radius'] = 38.75
    option['internal_geometry']['parameters']['ball_radius'] = 1.9600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 2.0090000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 37.5348
    option['internal_geometry']['parameters']['outer_shoulder'] = 39.9652
    option['internal_geometry']['parameters']['cage_half_width'] = 1.0780000000000003
    option['internal_geometry']['parameters']['cage_low'] = 1.862
    option['internal_geometry']['parameters']['cage_high'] = 2.254
    option['internal_geometry']['parameters']['window_radius'] = 0.9408000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['availability_note'] = 'Listed in the cited catalogue; current stock and lead time not confirmed.'
    option['catalogue_metadata']['bearing_closure_reference'] = 'Open'
    option['catalogue_metadata']['catalogue_model'] = '61714'
    option['catalogue_metadata']['catalogue_supplier'] = 'C&H Bearing'
    option['catalogue_metadata']['description'] = 'Thin section deep groove ball bearing, 70 x 85 x 7 mm (bore x OD x width).'
    option['catalogue_metadata']['source_checked'] = '2026-10-06'
    option['catalogue_metadata']['source_url'] = 'https://www.chenghuibearing.com/product-model/61714/'
    option['catalogue_metadata']['weight'] = '63'
    option['catalogue_metadata']['weight_note'] = ('Approximate catalogue mass for the cited open bearing; varies by manufacturer and '
     'closure.')
    option['catalogue_metadata']['weight_unit'] = 'g'
    options.append(copy.deepcopy(option))

    # 6715: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6700_series_6715_size_75_mm_id_90_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6700_series_6715_size_75_mm_id_90_mm_od_7_mm_depth'
    option['size'] = '6715'
    option['series'] = '6700'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 75.0
    option['dimensions']['outside'] = 90.0
    option['dimensions']['width'] = 7.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 48
    option['internal_geometry']['balls_per_row'] = 48
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 75.0
    option['internal_geometry']['parameters']['outside'] = 90.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.42
    option['internal_geometry']['parameters']['pitch_radius'] = 41.25
    option['internal_geometry']['parameters']['ball_radius'] = 1.9600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 2.0090000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 40.0348
    option['internal_geometry']['parameters']['outer_shoulder'] = 42.4652
    option['internal_geometry']['parameters']['cage_half_width'] = 1.0780000000000003
    option['internal_geometry']['parameters']['cage_low'] = 1.862
    option['internal_geometry']['parameters']['cage_high'] = 2.254
    option['internal_geometry']['parameters']['window_radius'] = 0.9408000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['availability_note'] = 'Listed in the cited catalogue; current stock and lead time not confirmed.'
    option['catalogue_metadata']['bearing_closure_reference'] = 'Open'
    option['catalogue_metadata']['catalogue_model'] = '61715'
    option['catalogue_metadata']['catalogue_supplier'] = 'C&H Bearing'
    option['catalogue_metadata']['description'] = 'Thin section deep groove ball bearing, 75 x 90 x 7 mm (bore x OD x width).'
    option['catalogue_metadata']['source_checked'] = '2026-10-06'
    option['catalogue_metadata']['source_url'] = 'https://www.chenghuibearing.com/product-model/61715/'
    option['catalogue_metadata']['weight'] = '68'
    option['catalogue_metadata']['weight_note'] = ('Approximate catalogue mass for the cited open bearing; varies by manufacturer and '
     'closure.')
    option['catalogue_metadata']['weight_unit'] = 'g'
    options.append(copy.deepcopy(option))

    # 6716: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6700_series_6716_size_80_mm_id_95_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6700_series_6716_size_80_mm_id_95_mm_od_7_mm_depth'
    option['size'] = '6716'
    option['series'] = '6700'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 80.0
    option['dimensions']['outside'] = 95.0
    option['dimensions']['width'] = 7.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 51
    option['internal_geometry']['balls_per_row'] = 51
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 80.0
    option['internal_geometry']['parameters']['outside'] = 95.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.42
    option['internal_geometry']['parameters']['pitch_radius'] = 43.75
    option['internal_geometry']['parameters']['ball_radius'] = 1.9600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 2.0090000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 42.5348
    option['internal_geometry']['parameters']['outer_shoulder'] = 44.9652
    option['internal_geometry']['parameters']['cage_half_width'] = 1.0780000000000003
    option['internal_geometry']['parameters']['cage_low'] = 1.862
    option['internal_geometry']['parameters']['cage_high'] = 2.254
    option['internal_geometry']['parameters']['window_radius'] = 0.9408000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['availability_note'] = 'Listed in the cited catalogue; current stock and lead time not confirmed.'
    option['catalogue_metadata']['bearing_closure_reference'] = 'Open'
    option['catalogue_metadata']['catalogue_model'] = '61716'
    option['catalogue_metadata']['catalogue_supplier'] = 'C&H Bearing'
    option['catalogue_metadata']['description'] = 'Thin section deep groove ball bearing, 80 x 95 x 7 mm (bore x OD x width).'
    option['catalogue_metadata']['source_checked'] = '2026-10-06'
    option['catalogue_metadata']['source_url'] = 'https://www.chenghuibearing.com/product-model/61716/'
    option['catalogue_metadata']['weight'] = '72'
    option['catalogue_metadata']['weight_note'] = ('Approximate catalogue mass for the cited open bearing; varies by manufacturer and '
     'closure.')
    option['catalogue_metadata']['weight_unit'] = 'g'
    options.append(copy.deepcopy(option))

    # 6717: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6700_series_6717_size_85_mm_id_105_mm_od_10_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6700_series_6717_size_85_mm_id_105_mm_od_10_mm_depth'
    option['size'] = '6717'
    option['series'] = '6700'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 85.0
    option['dimensions']['outside'] = 105.0
    option['dimensions']['width'] = 10.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 39
    option['internal_geometry']['balls_per_row'] = 39
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 85.0
    option['internal_geometry']['parameters']['outside'] = 105.0
    option['internal_geometry']['parameters']['width'] = 10.0
    option['internal_geometry']['parameters']['edge'] = 0.6
    option['internal_geometry']['parameters']['pitch_radius'] = 47.5
    option['internal_geometry']['parameters']['ball_radius'] = 2.8000000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 2.87
    option['internal_geometry']['parameters']['inner_shoulder'] = 45.764
    option['internal_geometry']['parameters']['outer_shoulder'] = 49.236
    option['internal_geometry']['parameters']['cage_half_width'] = 1.5400000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.66
    option['internal_geometry']['parameters']['cage_high'] = 3.22
    option['internal_geometry']['parameters']['window_radius'] = 1.344
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['availability_note'] = 'Listed in the cited catalogue; current stock and lead time not confirmed.'
    option['catalogue_metadata']['bearing_closure_reference'] = 'Open'
    option['catalogue_metadata']['catalogue_model'] = '61717'
    option['catalogue_metadata']['catalogue_supplier'] = 'C&H Bearing'
    option['catalogue_metadata']['description'] = 'Thin section deep groove ball bearing, 85 x 105 x 10 mm (bore x OD x width).'
    option['catalogue_metadata']['source_checked'] = '2026-10-06'
    option['catalogue_metadata']['source_url'] = 'https://www.chenghuibearing.com/product-model/61717/'
    option['catalogue_metadata']['weight'] = '149'
    option['catalogue_metadata']['weight_note'] = ('Approximate catalogue mass for the cited open bearing; varies by manufacturer and '
     'closure.')
    option['catalogue_metadata']['weight_unit'] = 'g'
    options.append(copy.deepcopy(option))

    # 6718: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6700_series_6718_size_90_mm_id_110_mm_od_10_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6700_series_6718_size_90_mm_id_110_mm_od_10_mm_depth'
    option['size'] = '6718'
    option['series'] = '6700'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 90.0
    option['dimensions']['outside'] = 110.0
    option['dimensions']['width'] = 10.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 41
    option['internal_geometry']['balls_per_row'] = 41
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 90.0
    option['internal_geometry']['parameters']['outside'] = 110.0
    option['internal_geometry']['parameters']['width'] = 10.0
    option['internal_geometry']['parameters']['edge'] = 0.6
    option['internal_geometry']['parameters']['pitch_radius'] = 50.0
    option['internal_geometry']['parameters']['ball_radius'] = 2.8000000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 2.87
    option['internal_geometry']['parameters']['inner_shoulder'] = 48.264
    option['internal_geometry']['parameters']['outer_shoulder'] = 51.736
    option['internal_geometry']['parameters']['cage_half_width'] = 1.5400000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.66
    option['internal_geometry']['parameters']['cage_high'] = 3.22
    option['internal_geometry']['parameters']['window_radius'] = 1.344
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['availability_note'] = 'Listed in the cited catalogue; current stock and lead time not confirmed.'
    option['catalogue_metadata']['bearing_closure_reference'] = 'Open'
    option['catalogue_metadata']['catalogue_model'] = '61718'
    option['catalogue_metadata']['catalogue_supplier'] = 'C&H Bearing'
    option['catalogue_metadata']['description'] = 'Thin section deep groove ball bearing, 90 x 110 x 10 mm (bore x OD x width).'
    option['catalogue_metadata']['source_checked'] = '2026-10-06'
    option['catalogue_metadata']['source_url'] = 'https://www.chenghuibearing.com/product-model/61718/'
    option['catalogue_metadata']['weight'] = '157'
    option['catalogue_metadata']['weight_note'] = ('Approximate catalogue mass for the cited open bearing; varies by manufacturer and '
     'closure.')
    option['catalogue_metadata']['weight_unit'] = 'g'
    options.append(copy.deepcopy(option))

    # 6719: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6700_series_6719_size_95_mm_id_115_mm_od_10_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6700_series_6719_size_95_mm_id_115_mm_od_10_mm_depth'
    option['size'] = '6719'
    option['series'] = '6700'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 95.0
    option['dimensions']['outside'] = 115.0
    option['dimensions']['width'] = 10.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 43
    option['internal_geometry']['balls_per_row'] = 43
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 95.0
    option['internal_geometry']['parameters']['outside'] = 115.0
    option['internal_geometry']['parameters']['width'] = 10.0
    option['internal_geometry']['parameters']['edge'] = 0.6
    option['internal_geometry']['parameters']['pitch_radius'] = 52.5
    option['internal_geometry']['parameters']['ball_radius'] = 2.8000000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 2.87
    option['internal_geometry']['parameters']['inner_shoulder'] = 50.764
    option['internal_geometry']['parameters']['outer_shoulder'] = 54.236
    option['internal_geometry']['parameters']['cage_half_width'] = 1.5400000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.66
    option['internal_geometry']['parameters']['cage_high'] = 3.22
    option['internal_geometry']['parameters']['window_radius'] = 1.344
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['availability_note'] = 'Listed in the cited catalogue; current stock and lead time not confirmed.'
    option['catalogue_metadata']['bearing_closure_reference'] = 'Open'
    option['catalogue_metadata']['catalogue_model'] = '61719'
    option['catalogue_metadata']['catalogue_supplier'] = 'C&H Bearing'
    option['catalogue_metadata']['description'] = 'Thin section deep groove ball bearing, 95 x 115 x 10 mm (bore x OD x width).'
    option['catalogue_metadata']['source_checked'] = '2026-10-06'
    option['catalogue_metadata']['source_url'] = 'https://www.chenghuibearing.com/product-model/61719/'
    option['catalogue_metadata']['weight'] = '164'
    option['catalogue_metadata']['weight_note'] = ('Approximate catalogue mass for the cited open bearing; varies by manufacturer and '
     'closure.')
    option['catalogue_metadata']['weight_unit'] = 'g'
    options.append(copy.deepcopy(option))

    # 6720: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6700_series_6720_size_100_mm_id_120_mm_od_10_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6700_series_6720_size_100_mm_id_120_mm_od_10_mm_depth'
    option['size'] = '6720'
    option['series'] = '6700'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 100.0
    option['dimensions']['outside'] = 120.0
    option['dimensions']['width'] = 10.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 45
    option['internal_geometry']['balls_per_row'] = 45
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 100.0
    option['internal_geometry']['parameters']['outside'] = 120.0
    option['internal_geometry']['parameters']['width'] = 10.0
    option['internal_geometry']['parameters']['edge'] = 0.6
    option['internal_geometry']['parameters']['pitch_radius'] = 55.0
    option['internal_geometry']['parameters']['ball_radius'] = 2.8000000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 2.87
    option['internal_geometry']['parameters']['inner_shoulder'] = 53.264
    option['internal_geometry']['parameters']['outer_shoulder'] = 56.736
    option['internal_geometry']['parameters']['cage_half_width'] = 1.5400000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.66
    option['internal_geometry']['parameters']['cage_high'] = 3.22
    option['internal_geometry']['parameters']['window_radius'] = 1.344
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['availability_note'] = 'Listed in the cited catalogue; current stock and lead time not confirmed.'
    option['catalogue_metadata']['bearing_closure_reference'] = 'Open'
    option['catalogue_metadata']['catalogue_model'] = '61720'
    option['catalogue_metadata']['catalogue_supplier'] = 'C&H Bearing'
    option['catalogue_metadata']['description'] = 'Thin section deep groove ball bearing, 100 x 120 x 10 mm (bore x OD x width).'
    option['catalogue_metadata']['source_checked'] = '2026-10-06'
    option['catalogue_metadata']['source_url'] = 'https://www.chenghuibearing.com/product-model/61720/'
    option['catalogue_metadata']['weight'] = '173'
    option['catalogue_metadata']['weight_note'] = ('Approximate catalogue mass for the cited open bearing; varies by manufacturer and '
     'closure.')
    option['catalogue_metadata']['weight_unit'] = 'g'
    options.append(copy.deepcopy(option))

    # 6800: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6800_series_6800_size_10_mm_id_19_mm_od_5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6800_series_6800_size_10_mm_id_19_mm_od_5_mm_depth'
    option['size'] = '6800'
    option['series'] = '6800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 10.0
    option['dimensions']['outside'] = 19.0
    option['dimensions']['width'] = 5.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 13
    option['internal_geometry']['balls_per_row'] = 13
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 10.0
    option['internal_geometry']['parameters']['outside'] = 19.0
    option['internal_geometry']['parameters']['width'] = 5.0
    option['internal_geometry']['parameters']['edge'] = 0.27
    option['internal_geometry']['parameters']['pitch_radius'] = 7.25
    option['internal_geometry']['parameters']['ball_radius'] = 1.2600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.2915000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 6.4688
    option['internal_geometry']['parameters']['outer_shoulder'] = 8.0312
    option['internal_geometry']['parameters']['cage_half_width'] = 0.6930000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.197
    option['internal_geometry']['parameters']['cage_high'] = 1.449
    option['internal_geometry']['parameters']['window_radius'] = 0.6048000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '5'
    options.append(copy.deepcopy(option))

    # 6801: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6800_series_6801_size_12_mm_id_21_mm_od_5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6800_series_6801_size_12_mm_id_21_mm_od_5_mm_depth'
    option['size'] = '6801'
    option['series'] = '6800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 12.0
    option['dimensions']['outside'] = 21.0
    option['dimensions']['width'] = 5.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 15
    option['internal_geometry']['balls_per_row'] = 15
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 12.0
    option['internal_geometry']['parameters']['outside'] = 21.0
    option['internal_geometry']['parameters']['width'] = 5.0
    option['internal_geometry']['parameters']['edge'] = 0.27
    option['internal_geometry']['parameters']['pitch_radius'] = 8.25
    option['internal_geometry']['parameters']['ball_radius'] = 1.2600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.2915000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 7.4688
    option['internal_geometry']['parameters']['outer_shoulder'] = 9.0312
    option['internal_geometry']['parameters']['cage_half_width'] = 0.6930000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.197
    option['internal_geometry']['parameters']['cage_high'] = 1.449
    option['internal_geometry']['parameters']['window_radius'] = 0.6048000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '6'
    options.append(copy.deepcopy(option))

    # 6802: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6800_series_6802_size_15_mm_id_24_mm_od_5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6800_series_6802_size_15_mm_id_24_mm_od_5_mm_depth'
    option['size'] = '6802'
    option['series'] = '6800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 15.0
    option['dimensions']['outside'] = 24.0
    option['dimensions']['width'] = 5.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 17
    option['internal_geometry']['balls_per_row'] = 17
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 15.0
    option['internal_geometry']['parameters']['outside'] = 24.0
    option['internal_geometry']['parameters']['width'] = 5.0
    option['internal_geometry']['parameters']['edge'] = 0.27
    option['internal_geometry']['parameters']['pitch_radius'] = 9.75
    option['internal_geometry']['parameters']['ball_radius'] = 1.2600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.2915000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 8.9688
    option['internal_geometry']['parameters']['outer_shoulder'] = 10.5312
    option['internal_geometry']['parameters']['cage_half_width'] = 0.6930000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.197
    option['internal_geometry']['parameters']['cage_high'] = 1.449
    option['internal_geometry']['parameters']['window_radius'] = 0.6048000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '7'
    options.append(copy.deepcopy(option))

    # 6803: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6800_series_6803_size_17_mm_id_26_mm_od_5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6800_series_6803_size_17_mm_id_26_mm_od_5_mm_depth'
    option['size'] = '6803'
    option['series'] = '6800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 17.0
    option['dimensions']['outside'] = 26.0
    option['dimensions']['width'] = 5.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 19
    option['internal_geometry']['balls_per_row'] = 19
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 17.0
    option['internal_geometry']['parameters']['outside'] = 26.0
    option['internal_geometry']['parameters']['width'] = 5.0
    option['internal_geometry']['parameters']['edge'] = 0.27
    option['internal_geometry']['parameters']['pitch_radius'] = 10.75
    option['internal_geometry']['parameters']['ball_radius'] = 1.2600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.2915000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 9.9688
    option['internal_geometry']['parameters']['outer_shoulder'] = 11.5312
    option['internal_geometry']['parameters']['cage_half_width'] = 0.6930000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.197
    option['internal_geometry']['parameters']['cage_high'] = 1.449
    option['internal_geometry']['parameters']['window_radius'] = 0.6048000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '8'
    options.append(copy.deepcopy(option))

    # 6804: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6800_series_6804_size_20_mm_id_32_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6800_series_6804_size_20_mm_id_32_mm_od_7_mm_depth'
    option['size'] = '6804'
    option['series'] = '6800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 20.0
    option['dimensions']['outside'] = 32.0
    option['dimensions']['width'] = 7.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 17
    option['internal_geometry']['balls_per_row'] = 17
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 20.0
    option['internal_geometry']['parameters']['outside'] = 32.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.36
    option['internal_geometry']['parameters']['pitch_radius'] = 13.0
    option['internal_geometry']['parameters']['ball_radius'] = 1.6800000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.7220000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 11.9584
    option['internal_geometry']['parameters']['outer_shoulder'] = 14.0416
    option['internal_geometry']['parameters']['cage_half_width'] = 0.9240000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.596
    option['internal_geometry']['parameters']['cage_high'] = 1.932
    option['internal_geometry']['parameters']['window_radius'] = 0.8064
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '19'
    options.append(copy.deepcopy(option))

    # 6805: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6800_series_6805_size_25_mm_id_37_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6800_series_6805_size_25_mm_id_37_mm_od_7_mm_depth'
    option['size'] = '6805'
    option['series'] = '6800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 25.0
    option['dimensions']['outside'] = 37.0
    option['dimensions']['width'] = 7.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 21
    option['internal_geometry']['balls_per_row'] = 21
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 25.0
    option['internal_geometry']['parameters']['outside'] = 37.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.36
    option['internal_geometry']['parameters']['pitch_radius'] = 15.5
    option['internal_geometry']['parameters']['ball_radius'] = 1.6800000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.7220000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 14.4584
    option['internal_geometry']['parameters']['outer_shoulder'] = 16.5416
    option['internal_geometry']['parameters']['cage_half_width'] = 0.9240000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.596
    option['internal_geometry']['parameters']['cage_high'] = 1.932
    option['internal_geometry']['parameters']['window_radius'] = 0.8064
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '22'
    options.append(copy.deepcopy(option))

    # 6806: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6800_series_6806_size_30_mm_id_42_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6800_series_6806_size_30_mm_id_42_mm_od_7_mm_depth'
    option['size'] = '6806'
    option['series'] = '6800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 30.0
    option['dimensions']['outside'] = 42.0
    option['dimensions']['width'] = 7.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 24
    option['internal_geometry']['balls_per_row'] = 24
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 30.0
    option['internal_geometry']['parameters']['outside'] = 42.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.36
    option['internal_geometry']['parameters']['pitch_radius'] = 18.0
    option['internal_geometry']['parameters']['ball_radius'] = 1.6800000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.7220000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 16.9584
    option['internal_geometry']['parameters']['outer_shoulder'] = 19.0416
    option['internal_geometry']['parameters']['cage_half_width'] = 0.9240000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.596
    option['internal_geometry']['parameters']['cage_high'] = 1.932
    option['internal_geometry']['parameters']['window_radius'] = 0.8064
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '26'
    options.append(copy.deepcopy(option))

    # 6807: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6800_series_6807_size_35_mm_id_47_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6800_series_6807_size_35_mm_id_47_mm_od_7_mm_depth'
    option['size'] = '6807'
    option['series'] = '6800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 35.0
    option['dimensions']['outside'] = 47.0
    option['dimensions']['width'] = 7.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 28
    option['internal_geometry']['balls_per_row'] = 28
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 35.0
    option['internal_geometry']['parameters']['outside'] = 47.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.36
    option['internal_geometry']['parameters']['pitch_radius'] = 20.5
    option['internal_geometry']['parameters']['ball_radius'] = 1.6800000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.7220000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 19.4584
    option['internal_geometry']['parameters']['outer_shoulder'] = 21.5416
    option['internal_geometry']['parameters']['cage_half_width'] = 0.9240000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.596
    option['internal_geometry']['parameters']['cage_high'] = 1.932
    option['internal_geometry']['parameters']['window_radius'] = 0.8064
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '29'
    options.append(copy.deepcopy(option))

    # 6808: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6800_series_6808_size_40_mm_id_52_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6800_series_6808_size_40_mm_id_52_mm_od_7_mm_depth'
    option['size'] = '6808'
    option['series'] = '6800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 40.0
    option['dimensions']['outside'] = 52.0
    option['dimensions']['width'] = 7.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 31
    option['internal_geometry']['balls_per_row'] = 31
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 40.0
    option['internal_geometry']['parameters']['outside'] = 52.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.36
    option['internal_geometry']['parameters']['pitch_radius'] = 23.0
    option['internal_geometry']['parameters']['ball_radius'] = 1.6800000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.7220000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 21.9584
    option['internal_geometry']['parameters']['outer_shoulder'] = 24.0416
    option['internal_geometry']['parameters']['cage_half_width'] = 0.9240000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.596
    option['internal_geometry']['parameters']['cage_high'] = 1.932
    option['internal_geometry']['parameters']['window_radius'] = 0.8064
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '33'
    options.append(copy.deepcopy(option))

    # 6809: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6800_series_6809_size_45_mm_id_58_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6800_series_6809_size_45_mm_id_58_mm_od_7_mm_depth'
    option['size'] = '6809'
    option['series'] = '6800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 45.0
    option['dimensions']['outside'] = 58.0
    option['dimensions']['width'] = 7.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 32
    option['internal_geometry']['balls_per_row'] = 32
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 45.0
    option['internal_geometry']['parameters']['outside'] = 58.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.39
    option['internal_geometry']['parameters']['pitch_radius'] = 25.75
    option['internal_geometry']['parameters']['ball_radius'] = 1.8200000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 1.8655000000000004
    option['internal_geometry']['parameters']['inner_shoulder'] = 24.6216
    option['internal_geometry']['parameters']['outer_shoulder'] = 26.8784
    option['internal_geometry']['parameters']['cage_half_width'] = 1.0010000000000003
    option['internal_geometry']['parameters']['cage_low'] = 1.729
    option['internal_geometry']['parameters']['cage_high'] = 2.093
    option['internal_geometry']['parameters']['window_radius'] = 0.8736000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '40'
    options.append(copy.deepcopy(option))

    # 6810: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6800_series_6810_size_50_mm_id_65_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6800_series_6810_size_50_mm_id_65_mm_od_7_mm_depth'
    option['size'] = '6810'
    option['series'] = '6800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 50.0
    option['dimensions']['outside'] = 65.0
    option['dimensions']['width'] = 7.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 34
    option['internal_geometry']['balls_per_row'] = 34
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 50.0
    option['internal_geometry']['parameters']['outside'] = 65.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.42
    option['internal_geometry']['parameters']['pitch_radius'] = 28.75
    option['internal_geometry']['parameters']['ball_radius'] = 1.9600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 2.0090000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 27.5348
    option['internal_geometry']['parameters']['outer_shoulder'] = 29.9652
    option['internal_geometry']['parameters']['cage_half_width'] = 1.0780000000000003
    option['internal_geometry']['parameters']['cage_low'] = 1.862
    option['internal_geometry']['parameters']['cage_high'] = 2.254
    option['internal_geometry']['parameters']['window_radius'] = 0.9408000000000001
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '52'
    options.append(copy.deepcopy(option))

    # 6811: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6800_series_6811_size_55_mm_id_72_mm_od_9_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6800_series_6811_size_55_mm_id_72_mm_od_9_mm_depth'
    option['size'] = '6811'
    option['series'] = '6800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 55.0
    option['dimensions']['outside'] = 72.0
    option['dimensions']['width'] = 9.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 30
    option['internal_geometry']['balls_per_row'] = 30
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 55.0
    option['internal_geometry']['parameters']['outside'] = 72.0
    option['internal_geometry']['parameters']['width'] = 9.0
    option['internal_geometry']['parameters']['edge'] = 0.51
    option['internal_geometry']['parameters']['pitch_radius'] = 31.75
    option['internal_geometry']['parameters']['ball_radius'] = 2.3800000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 2.4395000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 30.2744
    option['internal_geometry']['parameters']['outer_shoulder'] = 33.2256
    option['internal_geometry']['parameters']['cage_half_width'] = 1.3090000000000004
    option['internal_geometry']['parameters']['cage_low'] = 2.261
    option['internal_geometry']['parameters']['cage_high'] = 2.737
    option['internal_geometry']['parameters']['window_radius'] = 1.1424
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '83'
    options.append(copy.deepcopy(option))

    # 6812: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6800_series_6812_size_60_mm_id_78_mm_od_10_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6800_series_6812_size_60_mm_id_78_mm_od_10_mm_depth'
    option['size'] = '6812'
    option['series'] = '6800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 60.0
    option['dimensions']['outside'] = 78.0
    option['dimensions']['width'] = 10.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 31
    option['internal_geometry']['balls_per_row'] = 31
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 60.0
    option['internal_geometry']['parameters']['outside'] = 78.0
    option['internal_geometry']['parameters']['width'] = 10.0
    option['internal_geometry']['parameters']['edge'] = 0.54
    option['internal_geometry']['parameters']['pitch_radius'] = 34.5
    option['internal_geometry']['parameters']['ball_radius'] = 2.5200000000000005
    option['internal_geometry']['parameters']['groove_radius'] = 2.5830000000000006
    option['internal_geometry']['parameters']['inner_shoulder'] = 32.9376
    option['internal_geometry']['parameters']['outer_shoulder'] = 36.0624
    option['internal_geometry']['parameters']['cage_half_width'] = 1.3860000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.394
    option['internal_geometry']['parameters']['cage_high'] = 2.898
    option['internal_geometry']['parameters']['window_radius'] = 1.2096000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '104'
    options.append(copy.deepcopy(option))

    # 6813: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6800_series_6813_size_65_mm_id_85_mm_od_10_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6800_series_6813_size_65_mm_id_85_mm_od_10_mm_depth'
    option['size'] = '6813'
    option['series'] = '6800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 65.0
    option['dimensions']['outside'] = 85.0
    option['dimensions']['width'] = 10.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 31
    option['internal_geometry']['balls_per_row'] = 31
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 65.0
    option['internal_geometry']['parameters']['outside'] = 85.0
    option['internal_geometry']['parameters']['width'] = 10.0
    option['internal_geometry']['parameters']['edge'] = 0.6
    option['internal_geometry']['parameters']['pitch_radius'] = 37.5
    option['internal_geometry']['parameters']['ball_radius'] = 2.8000000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 2.87
    option['internal_geometry']['parameters']['inner_shoulder'] = 35.764
    option['internal_geometry']['parameters']['outer_shoulder'] = 39.236
    option['internal_geometry']['parameters']['cage_half_width'] = 1.5400000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.66
    option['internal_geometry']['parameters']['cage_high'] = 3.22
    option['internal_geometry']['parameters']['window_radius'] = 1.344
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '126'
    options.append(copy.deepcopy(option))

    # 6814: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6800_series_6814_size_70_mm_id_90_mm_od_10_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6800_series_6814_size_70_mm_id_90_mm_od_10_mm_depth'
    option['size'] = '6814'
    option['series'] = '6800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 70.0
    option['dimensions']['outside'] = 90.0
    option['dimensions']['width'] = 10.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 33
    option['internal_geometry']['balls_per_row'] = 33
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 70.0
    option['internal_geometry']['parameters']['outside'] = 90.0
    option['internal_geometry']['parameters']['width'] = 10.0
    option['internal_geometry']['parameters']['edge'] = 0.6
    option['internal_geometry']['parameters']['pitch_radius'] = 40.0
    option['internal_geometry']['parameters']['ball_radius'] = 2.8000000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 2.87
    option['internal_geometry']['parameters']['inner_shoulder'] = 38.264
    option['internal_geometry']['parameters']['outer_shoulder'] = 41.736
    option['internal_geometry']['parameters']['cage_half_width'] = 1.5400000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.66
    option['internal_geometry']['parameters']['cage_high'] = 3.22
    option['internal_geometry']['parameters']['window_radius'] = 1.344
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '134'
    options.append(copy.deepcopy(option))

    # 6815: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6800_series_6815_size_75_mm_id_95_mm_od_10_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6800_series_6815_size_75_mm_id_95_mm_od_10_mm_depth'
    option['size'] = '6815'
    option['series'] = '6800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 75.0
    option['dimensions']['outside'] = 95.0
    option['dimensions']['width'] = 10.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 35
    option['internal_geometry']['balls_per_row'] = 35
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 75.0
    option['internal_geometry']['parameters']['outside'] = 95.0
    option['internal_geometry']['parameters']['width'] = 10.0
    option['internal_geometry']['parameters']['edge'] = 0.6
    option['internal_geometry']['parameters']['pitch_radius'] = 42.5
    option['internal_geometry']['parameters']['ball_radius'] = 2.8000000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 2.87
    option['internal_geometry']['parameters']['inner_shoulder'] = 40.764
    option['internal_geometry']['parameters']['outer_shoulder'] = 44.236
    option['internal_geometry']['parameters']['cage_half_width'] = 1.5400000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.66
    option['internal_geometry']['parameters']['cage_high'] = 3.22
    option['internal_geometry']['parameters']['window_radius'] = 1.344
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '142'
    options.append(copy.deepcopy(option))

    # 6816: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6800_series_6816_size_80_mm_id_100_mm_od_10_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6800_series_6816_size_80_mm_id_100_mm_od_10_mm_depth'
    option['size'] = '6816'
    option['series'] = '6800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 80.0
    option['dimensions']['outside'] = 100.0
    option['dimensions']['width'] = 10.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 37
    option['internal_geometry']['balls_per_row'] = 37
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 80.0
    option['internal_geometry']['parameters']['outside'] = 100.0
    option['internal_geometry']['parameters']['width'] = 10.0
    option['internal_geometry']['parameters']['edge'] = 0.6
    option['internal_geometry']['parameters']['pitch_radius'] = 45.0
    option['internal_geometry']['parameters']['ball_radius'] = 2.8000000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 2.87
    option['internal_geometry']['parameters']['inner_shoulder'] = 43.264
    option['internal_geometry']['parameters']['outer_shoulder'] = 46.736
    option['internal_geometry']['parameters']['cage_half_width'] = 1.5400000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.66
    option['internal_geometry']['parameters']['cage_high'] = 3.22
    option['internal_geometry']['parameters']['window_radius'] = 1.344
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '150'
    options.append(copy.deepcopy(option))

    # 6817: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6800_series_6817_size_85_mm_id_110_mm_od_13_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6800_series_6817_size_85_mm_id_110_mm_od_13_mm_depth'
    option['size'] = '6817'
    option['series'] = '6800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 85.0
    option['dimensions']['outside'] = 110.0
    option['dimensions']['width'] = 13.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 32
    option['internal_geometry']['balls_per_row'] = 32
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 85.0
    option['internal_geometry']['parameters']['outside'] = 110.0
    option['internal_geometry']['parameters']['width'] = 13.0
    option['internal_geometry']['parameters']['edge'] = 0.75
    option['internal_geometry']['parameters']['pitch_radius'] = 48.75
    option['internal_geometry']['parameters']['ball_radius'] = 3.5000000000000004
    option['internal_geometry']['parameters']['groove_radius'] = 3.5875000000000004
    option['internal_geometry']['parameters']['inner_shoulder'] = 46.58
    option['internal_geometry']['parameters']['outer_shoulder'] = 50.92
    option['internal_geometry']['parameters']['cage_half_width'] = 1.9250000000000005
    option['internal_geometry']['parameters']['cage_low'] = 3.325
    option['internal_geometry']['parameters']['cage_high'] = 4.025
    option['internal_geometry']['parameters']['window_radius'] = 1.6800000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '266'
    options.append(copy.deepcopy(option))

    # 6818: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6800_series_6818_size_90_mm_id_115_mm_od_13_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6800_series_6818_size_90_mm_id_115_mm_od_13_mm_depth'
    option['size'] = '6818'
    option['series'] = '6800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 90.0
    option['dimensions']['outside'] = 115.0
    option['dimensions']['width'] = 13.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 34
    option['internal_geometry']['balls_per_row'] = 34
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 90.0
    option['internal_geometry']['parameters']['outside'] = 115.0
    option['internal_geometry']['parameters']['width'] = 13.0
    option['internal_geometry']['parameters']['edge'] = 0.75
    option['internal_geometry']['parameters']['pitch_radius'] = 51.25
    option['internal_geometry']['parameters']['ball_radius'] = 3.5000000000000004
    option['internal_geometry']['parameters']['groove_radius'] = 3.5875000000000004
    option['internal_geometry']['parameters']['inner_shoulder'] = 49.08
    option['internal_geometry']['parameters']['outer_shoulder'] = 53.42
    option['internal_geometry']['parameters']['cage_half_width'] = 1.9250000000000005
    option['internal_geometry']['parameters']['cage_low'] = 3.325
    option['internal_geometry']['parameters']['cage_high'] = 4.025
    option['internal_geometry']['parameters']['window_radius'] = 1.6800000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '279'
    options.append(copy.deepcopy(option))

    # 6819: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6800_series_6819_size_95_mm_id_120_mm_od_13_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6800_series_6819_size_95_mm_id_120_mm_od_13_mm_depth'
    option['size'] = '6819'
    option['series'] = '6800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 95.0
    option['dimensions']['outside'] = 120.0
    option['dimensions']['width'] = 13.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 35
    option['internal_geometry']['balls_per_row'] = 35
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 95.0
    option['internal_geometry']['parameters']['outside'] = 120.0
    option['internal_geometry']['parameters']['width'] = 13.0
    option['internal_geometry']['parameters']['edge'] = 0.75
    option['internal_geometry']['parameters']['pitch_radius'] = 53.75
    option['internal_geometry']['parameters']['ball_radius'] = 3.5000000000000004
    option['internal_geometry']['parameters']['groove_radius'] = 3.5875000000000004
    option['internal_geometry']['parameters']['inner_shoulder'] = 51.58
    option['internal_geometry']['parameters']['outer_shoulder'] = 55.92
    option['internal_geometry']['parameters']['cage_half_width'] = 1.9250000000000005
    option['internal_geometry']['parameters']['cage_low'] = 3.325
    option['internal_geometry']['parameters']['cage_high'] = 4.025
    option['internal_geometry']['parameters']['window_radius'] = 1.6800000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '704'
    options.append(copy.deepcopy(option))

    # 6820: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6800_series_6820_size_100_mm_id_125_mm_od_13_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6800_series_6820_size_100_mm_id_125_mm_od_13_mm_depth'
    option['size'] = '6820'
    option['series'] = '6800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 100.0
    option['dimensions']['outside'] = 125.0
    option['dimensions']['width'] = 13.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 37
    option['internal_geometry']['balls_per_row'] = 37
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 100.0
    option['internal_geometry']['parameters']['outside'] = 125.0
    option['internal_geometry']['parameters']['width'] = 13.0
    option['internal_geometry']['parameters']['edge'] = 0.75
    option['internal_geometry']['parameters']['pitch_radius'] = 56.25
    option['internal_geometry']['parameters']['ball_radius'] = 3.5000000000000004
    option['internal_geometry']['parameters']['groove_radius'] = 3.5875000000000004
    option['internal_geometry']['parameters']['inner_shoulder'] = 54.08
    option['internal_geometry']['parameters']['outer_shoulder'] = 58.42
    option['internal_geometry']['parameters']['cage_half_width'] = 1.9250000000000005
    option['internal_geometry']['parameters']['cage_low'] = 3.325
    option['internal_geometry']['parameters']['cage_high'] = 4.025
    option['internal_geometry']['parameters']['window_radius'] = 1.6800000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '309'
    options.append(copy.deepcopy(option))

    # 6821: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6800_series_6821_size_105_mm_id_130_mm_od_13_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6800_series_6821_size_105_mm_id_130_mm_od_13_mm_depth'
    option['size'] = '6821'
    option['series'] = '6800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 105.0
    option['dimensions']['outside'] = 130.0
    option['dimensions']['width'] = 13.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 39
    option['internal_geometry']['balls_per_row'] = 39
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 105.0
    option['internal_geometry']['parameters']['outside'] = 130.0
    option['internal_geometry']['parameters']['width'] = 13.0
    option['internal_geometry']['parameters']['edge'] = 0.75
    option['internal_geometry']['parameters']['pitch_radius'] = 58.75
    option['internal_geometry']['parameters']['ball_radius'] = 3.5000000000000004
    option['internal_geometry']['parameters']['groove_radius'] = 3.5875000000000004
    option['internal_geometry']['parameters']['inner_shoulder'] = 56.58
    option['internal_geometry']['parameters']['outer_shoulder'] = 60.92
    option['internal_geometry']['parameters']['cage_half_width'] = 1.9250000000000005
    option['internal_geometry']['parameters']['cage_low'] = 3.325
    option['internal_geometry']['parameters']['cage_high'] = 4.025
    option['internal_geometry']['parameters']['window_radius'] = 1.6800000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '324'
    options.append(copy.deepcopy(option))

    # 6822: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6800_series_6822_size_110_mm_id_140_mm_od_16_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6800_series_6822_size_110_mm_id_140_mm_od_16_mm_depth'
    option['size'] = '6822'
    option['series'] = '6800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 110.0
    option['dimensions']['outside'] = 140.0
    option['dimensions']['width'] = 16.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 34
    option['internal_geometry']['balls_per_row'] = 34
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 110.0
    option['internal_geometry']['parameters']['outside'] = 140.0
    option['internal_geometry']['parameters']['width'] = 16.0
    option['internal_geometry']['parameters']['edge'] = 0.8999999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 62.5
    option['internal_geometry']['parameters']['ball_radius'] = 4.2
    option['internal_geometry']['parameters']['groove_radius'] = 4.305000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 59.896
    option['internal_geometry']['parameters']['outer_shoulder'] = 65.104
    option['internal_geometry']['parameters']['cage_half_width'] = 2.3100000000000005
    option['internal_geometry']['parameters']['cage_low'] = 3.9899999999999998
    option['internal_geometry']['parameters']['cage_high'] = 4.83
    option['internal_geometry']['parameters']['window_radius'] = 2.016
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '605'
    options.append(copy.deepcopy(option))

    # 6824: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6800_series_6824_size_120_mm_id_150_mm_od_16_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6800_series_6824_size_120_mm_id_150_mm_od_16_mm_depth'
    option['size'] = '6824'
    option['series'] = '6800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 120.0
    option['dimensions']['outside'] = 150.0
    option['dimensions']['width'] = 16.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 37
    option['internal_geometry']['balls_per_row'] = 37
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 120.0
    option['internal_geometry']['parameters']['outside'] = 150.0
    option['internal_geometry']['parameters']['width'] = 16.0
    option['internal_geometry']['parameters']['edge'] = 0.8999999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 67.5
    option['internal_geometry']['parameters']['ball_radius'] = 4.2
    option['internal_geometry']['parameters']['groove_radius'] = 4.305000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 64.896
    option['internal_geometry']['parameters']['outer_shoulder'] = 70.104
    option['internal_geometry']['parameters']['cage_half_width'] = 2.3100000000000005
    option['internal_geometry']['parameters']['cage_low'] = 3.9899999999999998
    option['internal_geometry']['parameters']['cage_high'] = 4.83
    option['internal_geometry']['parameters']['window_radius'] = 2.016
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '654'
    options.append(copy.deepcopy(option))

    # 6826: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6800_series_6826_size_130_mm_id_165_mm_od_18_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6800_series_6826_size_130_mm_id_165_mm_od_18_mm_depth'
    option['size'] = '6826'
    option['series'] = '6800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 130.0
    option['dimensions']['outside'] = 165.0
    option['dimensions']['width'] = 18.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 34
    option['internal_geometry']['balls_per_row'] = 34
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 130.0
    option['internal_geometry']['parameters']['outside'] = 165.0
    option['internal_geometry']['parameters']['width'] = 18.0
    option['internal_geometry']['parameters']['edge'] = 1.05
    option['internal_geometry']['parameters']['pitch_radius'] = 73.75
    option['internal_geometry']['parameters']['ball_radius'] = 4.9
    option['internal_geometry']['parameters']['groove_radius'] = 5.0225
    option['internal_geometry']['parameters']['inner_shoulder'] = 70.712
    option['internal_geometry']['parameters']['outer_shoulder'] = 76.788
    option['internal_geometry']['parameters']['cage_half_width'] = 2.6950000000000003
    option['internal_geometry']['parameters']['cage_low'] = 4.655
    option['internal_geometry']['parameters']['cage_high'] = 5.635
    option['internal_geometry']['parameters']['window_radius'] = 2.352
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '938'
    options.append(copy.deepcopy(option))

    # 6828: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6800_series_6828_size_140_mm_id_175_mm_od_18_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6800_series_6828_size_140_mm_id_175_mm_od_18_mm_depth'
    option['size'] = '6828'
    option['series'] = '6800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 140.0
    option['dimensions']['outside'] = 175.0
    option['dimensions']['width'] = 18.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 37
    option['internal_geometry']['balls_per_row'] = 37
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 140.0
    option['internal_geometry']['parameters']['outside'] = 175.0
    option['internal_geometry']['parameters']['width'] = 18.0
    option['internal_geometry']['parameters']['edge'] = 1.05
    option['internal_geometry']['parameters']['pitch_radius'] = 78.75
    option['internal_geometry']['parameters']['ball_radius'] = 4.9
    option['internal_geometry']['parameters']['groove_radius'] = 5.0225
    option['internal_geometry']['parameters']['inner_shoulder'] = 75.712
    option['internal_geometry']['parameters']['outer_shoulder'] = 81.788
    option['internal_geometry']['parameters']['cage_half_width'] = 2.6950000000000003
    option['internal_geometry']['parameters']['cage_low'] = 4.655
    option['internal_geometry']['parameters']['cage_high'] = 5.635
    option['internal_geometry']['parameters']['window_radius'] = 2.352
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '999'
    options.append(copy.deepcopy(option))

    # 6830: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6800_series_6830_size_150_mm_id_190_mm_od_20_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6800_series_6830_size_150_mm_id_190_mm_od_20_mm_depth'
    option['size'] = '6830'
    option['series'] = '6800'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 150.0
    option['dimensions']['outside'] = 190.0
    option['dimensions']['width'] = 20.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 35
    option['internal_geometry']['balls_per_row'] = 35
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 150.0
    option['internal_geometry']['parameters']['outside'] = 190.0
    option['internal_geometry']['parameters']['width'] = 20.0
    option['internal_geometry']['parameters']['edge'] = 1.2
    option['internal_geometry']['parameters']['pitch_radius'] = 85.0
    option['internal_geometry']['parameters']['ball_radius'] = 5.6000000000000005
    option['internal_geometry']['parameters']['groove_radius'] = 5.74
    option['internal_geometry']['parameters']['inner_shoulder'] = 81.528
    option['internal_geometry']['parameters']['outer_shoulder'] = 88.472
    option['internal_geometry']['parameters']['cage_half_width'] = 3.0800000000000005
    option['internal_geometry']['parameters']['cage_low'] = 5.32
    option['internal_geometry']['parameters']['cage_high'] = 6.44
    option['internal_geometry']['parameters']['window_radius'] = 2.688
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1,398'
    options.append(copy.deepcopy(option))

    # 6900: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6900_series_6900_size_10_mm_id_22_mm_od_6_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6900_series_6900_size_10_mm_id_22_mm_od_6_mm_depth'
    option['size'] = '6900'
    option['series'] = '6900'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 10.0
    option['dimensions']['outside'] = 22.0
    option['dimensions']['width'] = 6.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 10
    option['internal_geometry']['balls_per_row'] = 10
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 10.0
    option['internal_geometry']['parameters']['outside'] = 22.0
    option['internal_geometry']['parameters']['width'] = 6.0
    option['internal_geometry']['parameters']['edge'] = 0.36
    option['internal_geometry']['parameters']['pitch_radius'] = 8.0
    option['internal_geometry']['parameters']['ball_radius'] = 1.6800000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.7220000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 6.9584
    option['internal_geometry']['parameters']['outer_shoulder'] = 9.0416
    option['internal_geometry']['parameters']['cage_half_width'] = 0.9240000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.596
    option['internal_geometry']['parameters']['cage_high'] = 1.932
    option['internal_geometry']['parameters']['window_radius'] = 0.8064
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '5'
    options.append(copy.deepcopy(option))

    # 6901: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6900_series_6901_size_12_mm_id_24_mm_od_6_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6900_series_6901_size_12_mm_id_24_mm_od_6_mm_depth'
    option['size'] = '6901'
    option['series'] = '6900'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 12.0
    option['dimensions']['outside'] = 24.0
    option['dimensions']['width'] = 6.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 12
    option['internal_geometry']['balls_per_row'] = 12
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 12.0
    option['internal_geometry']['parameters']['outside'] = 24.0
    option['internal_geometry']['parameters']['width'] = 6.0
    option['internal_geometry']['parameters']['edge'] = 0.36
    option['internal_geometry']['parameters']['pitch_radius'] = 9.0
    option['internal_geometry']['parameters']['ball_radius'] = 1.6800000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.7220000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 7.9584
    option['internal_geometry']['parameters']['outer_shoulder'] = 10.0416
    option['internal_geometry']['parameters']['cage_half_width'] = 0.9240000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.596
    option['internal_geometry']['parameters']['cage_high'] = 1.932
    option['internal_geometry']['parameters']['window_radius'] = 0.8064
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '5'
    options.append(copy.deepcopy(option))

    # 6902: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6900_series_6902_size_15_mm_id_28_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6900_series_6902_size_15_mm_id_28_mm_od_7_mm_depth'
    option['size'] = '6902'
    option['series'] = '6900'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 15.0
    option['dimensions']['outside'] = 28.0
    option['dimensions']['width'] = 7.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 13
    option['internal_geometry']['balls_per_row'] = 13
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 15.0
    option['internal_geometry']['parameters']['outside'] = 28.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.39
    option['internal_geometry']['parameters']['pitch_radius'] = 10.75
    option['internal_geometry']['parameters']['ball_radius'] = 1.8200000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 1.8655000000000004
    option['internal_geometry']['parameters']['inner_shoulder'] = 9.6216
    option['internal_geometry']['parameters']['outer_shoulder'] = 11.8784
    option['internal_geometry']['parameters']['cage_half_width'] = 1.0010000000000003
    option['internal_geometry']['parameters']['cage_low'] = 1.729
    option['internal_geometry']['parameters']['cage_high'] = 2.093
    option['internal_geometry']['parameters']['window_radius'] = 0.8736000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '8'
    options.append(copy.deepcopy(option))

    # 6903: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6900_series_6903_size_17_mm_id_30_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6900_series_6903_size_17_mm_id_30_mm_od_7_mm_depth'
    option['size'] = '6903'
    option['series'] = '6900'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 17.0
    option['dimensions']['outside'] = 30.0
    option['dimensions']['width'] = 7.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 14
    option['internal_geometry']['balls_per_row'] = 14
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 17.0
    option['internal_geometry']['parameters']['outside'] = 30.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.39
    option['internal_geometry']['parameters']['pitch_radius'] = 11.75
    option['internal_geometry']['parameters']['ball_radius'] = 1.8200000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 1.8655000000000004
    option['internal_geometry']['parameters']['inner_shoulder'] = 10.6216
    option['internal_geometry']['parameters']['outer_shoulder'] = 12.8784
    option['internal_geometry']['parameters']['cage_half_width'] = 1.0010000000000003
    option['internal_geometry']['parameters']['cage_low'] = 1.729
    option['internal_geometry']['parameters']['cage_high'] = 2.093
    option['internal_geometry']['parameters']['window_radius'] = 0.8736000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '8'
    options.append(copy.deepcopy(option))

    # 6904: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6900_series_6904_size_20_mm_id_37_mm_od_9_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6900_series_6904_size_20_mm_id_37_mm_od_9_mm_depth'
    option['size'] = '6904'
    option['series'] = '6900'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 20.0
    option['dimensions']['outside'] = 37.0
    option['dimensions']['width'] = 9.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 13
    option['internal_geometry']['balls_per_row'] = 13
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 20.0
    option['internal_geometry']['parameters']['outside'] = 37.0
    option['internal_geometry']['parameters']['width'] = 9.0
    option['internal_geometry']['parameters']['edge'] = 0.51
    option['internal_geometry']['parameters']['pitch_radius'] = 14.25
    option['internal_geometry']['parameters']['ball_radius'] = 2.3800000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 2.4395000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 12.7744
    option['internal_geometry']['parameters']['outer_shoulder'] = 15.7256
    option['internal_geometry']['parameters']['cage_half_width'] = 1.3090000000000004
    option['internal_geometry']['parameters']['cage_low'] = 2.261
    option['internal_geometry']['parameters']['cage_high'] = 2.737
    option['internal_geometry']['parameters']['window_radius'] = 1.1424
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '16'
    options.append(copy.deepcopy(option))

    # 6905: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6900_series_6905_size_25_mm_id_42_mm_od_9_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6900_series_6905_size_25_mm_id_42_mm_od_9_mm_depth'
    option['size'] = '6905'
    option['series'] = '6900'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 25.0
    option['dimensions']['outside'] = 42.0
    option['dimensions']['width'] = 9.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 16
    option['internal_geometry']['balls_per_row'] = 16
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 25.0
    option['internal_geometry']['parameters']['outside'] = 42.0
    option['internal_geometry']['parameters']['width'] = 9.0
    option['internal_geometry']['parameters']['edge'] = 0.51
    option['internal_geometry']['parameters']['pitch_radius'] = 16.75
    option['internal_geometry']['parameters']['ball_radius'] = 2.3800000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 2.4395000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 15.2744
    option['internal_geometry']['parameters']['outer_shoulder'] = 18.2256
    option['internal_geometry']['parameters']['cage_half_width'] = 1.3090000000000004
    option['internal_geometry']['parameters']['cage_low'] = 2.261
    option['internal_geometry']['parameters']['cage_high'] = 2.737
    option['internal_geometry']['parameters']['window_radius'] = 1.1424
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '19'
    options.append(copy.deepcopy(option))

    # 6906: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6900_series_6906_size_30_mm_id_47_mm_od_9_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6900_series_6906_size_30_mm_id_47_mm_od_9_mm_depth'
    option['size'] = '6906'
    option['series'] = '6900'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 30.0
    option['dimensions']['outside'] = 47.0
    option['dimensions']['width'] = 9.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 18
    option['internal_geometry']['balls_per_row'] = 18
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 30.0
    option['internal_geometry']['parameters']['outside'] = 47.0
    option['internal_geometry']['parameters']['width'] = 9.0
    option['internal_geometry']['parameters']['edge'] = 0.51
    option['internal_geometry']['parameters']['pitch_radius'] = 19.25
    option['internal_geometry']['parameters']['ball_radius'] = 2.3800000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 2.4395000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 17.7744
    option['internal_geometry']['parameters']['outer_shoulder'] = 20.7256
    option['internal_geometry']['parameters']['cage_half_width'] = 1.3090000000000004
    option['internal_geometry']['parameters']['cage_low'] = 2.261
    option['internal_geometry']['parameters']['cage_high'] = 2.737
    option['internal_geometry']['parameters']['window_radius'] = 1.1424
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '20'
    options.append(copy.deepcopy(option))

    # 6907: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6900_series_6907_size_35_mm_id_55_mm_od_10_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6900_series_6907_size_35_mm_id_55_mm_od_10_mm_depth'
    option['size'] = '6907'
    option['series'] = '6900'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 35.0
    option['dimensions']['outside'] = 55.0
    option['dimensions']['width'] = 10.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 18
    option['internal_geometry']['balls_per_row'] = 18
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 35.0
    option['internal_geometry']['parameters']['outside'] = 55.0
    option['internal_geometry']['parameters']['width'] = 10.0
    option['internal_geometry']['parameters']['edge'] = 0.6
    option['internal_geometry']['parameters']['pitch_radius'] = 22.5
    option['internal_geometry']['parameters']['ball_radius'] = 2.8000000000000003
    option['internal_geometry']['parameters']['groove_radius'] = 2.87
    option['internal_geometry']['parameters']['inner_shoulder'] = 20.764
    option['internal_geometry']['parameters']['outer_shoulder'] = 24.236
    option['internal_geometry']['parameters']['cage_half_width'] = 1.5400000000000003
    option['internal_geometry']['parameters']['cage_low'] = 2.66
    option['internal_geometry']['parameters']['cage_high'] = 3.22
    option['internal_geometry']['parameters']['window_radius'] = 1.344
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '33'
    options.append(copy.deepcopy(option))

    # 6908: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6900_series_6908_size_40_mm_id_62_mm_od_12_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6900_series_6908_size_40_mm_id_62_mm_od_12_mm_depth'
    option['size'] = '6908'
    option['series'] = '6900'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 40.0
    option['dimensions']['outside'] = 62.0
    option['dimensions']['width'] = 12.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 19
    option['internal_geometry']['balls_per_row'] = 19
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 40.0
    option['internal_geometry']['parameters']['outside'] = 62.0
    option['internal_geometry']['parameters']['width'] = 12.0
    option['internal_geometry']['parameters']['edge'] = 0.6599999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 25.5
    option['internal_geometry']['parameters']['ball_radius'] = 3.08
    option['internal_geometry']['parameters']['groove_radius'] = 3.157
    option['internal_geometry']['parameters']['inner_shoulder'] = 23.5904
    option['internal_geometry']['parameters']['outer_shoulder'] = 27.4096
    option['internal_geometry']['parameters']['cage_half_width'] = 1.6940000000000002
    option['internal_geometry']['parameters']['cage_low'] = 2.9259999999999997
    option['internal_geometry']['parameters']['cage_high'] = 3.542
    option['internal_geometry']['parameters']['window_radius'] = 1.4784
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '51'
    options.append(copy.deepcopy(option))

    # 6909: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6900_series_6909_size_45_mm_id_68_mm_od_12_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6900_series_6909_size_45_mm_id_68_mm_od_12_mm_depth'
    option['size'] = '6909'
    option['series'] = '6900'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 45.0
    option['dimensions']['outside'] = 68.0
    option['dimensions']['width'] = 12.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 20
    option['internal_geometry']['balls_per_row'] = 20
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 45.0
    option['internal_geometry']['parameters']['outside'] = 68.0
    option['internal_geometry']['parameters']['width'] = 12.0
    option['internal_geometry']['parameters']['edge'] = 0.69
    option['internal_geometry']['parameters']['pitch_radius'] = 28.25
    option['internal_geometry']['parameters']['ball_radius'] = 3.22
    option['internal_geometry']['parameters']['groove_radius'] = 3.3005000000000004
    option['internal_geometry']['parameters']['inner_shoulder'] = 26.2536
    option['internal_geometry']['parameters']['outer_shoulder'] = 30.2464
    option['internal_geometry']['parameters']['cage_half_width'] = 1.7710000000000004
    option['internal_geometry']['parameters']['cage_low'] = 3.059
    option['internal_geometry']['parameters']['cage_high'] = 3.703
    option['internal_geometry']['parameters']['window_radius'] = 1.5456
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '60'
    options.append(copy.deepcopy(option))

    # 6910: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6900_series_6910_size_50_mm_id_72_mm_od_12_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6900_series_6910_size_50_mm_id_72_mm_od_12_mm_depth'
    option['size'] = '6910'
    option['series'] = '6900'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 50.0
    option['dimensions']['outside'] = 72.0
    option['dimensions']['width'] = 12.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 22
    option['internal_geometry']['balls_per_row'] = 22
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 50.0
    option['internal_geometry']['parameters']['outside'] = 72.0
    option['internal_geometry']['parameters']['width'] = 12.0
    option['internal_geometry']['parameters']['edge'] = 0.6599999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 30.5
    option['internal_geometry']['parameters']['ball_radius'] = 3.08
    option['internal_geometry']['parameters']['groove_radius'] = 3.157
    option['internal_geometry']['parameters']['inner_shoulder'] = 28.5904
    option['internal_geometry']['parameters']['outer_shoulder'] = 32.4096
    option['internal_geometry']['parameters']['cage_half_width'] = 1.6940000000000002
    option['internal_geometry']['parameters']['cage_low'] = 2.9259999999999997
    option['internal_geometry']['parameters']['cage_high'] = 3.542
    option['internal_geometry']['parameters']['window_radius'] = 1.4784
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '60'
    options.append(copy.deepcopy(option))

    # 6911: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6900_series_6911_size_55_mm_id_80_mm_od_13_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6900_series_6911_size_55_mm_id_80_mm_od_13_mm_depth'
    option['size'] = '6911'
    option['series'] = '6900'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 55.0
    option['dimensions']['outside'] = 80.0
    option['dimensions']['width'] = 13.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 22
    option['internal_geometry']['balls_per_row'] = 22
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 55.0
    option['internal_geometry']['parameters']['outside'] = 80.0
    option['internal_geometry']['parameters']['width'] = 13.0
    option['internal_geometry']['parameters']['edge'] = 0.75
    option['internal_geometry']['parameters']['pitch_radius'] = 33.75
    option['internal_geometry']['parameters']['ball_radius'] = 3.5000000000000004
    option['internal_geometry']['parameters']['groove_radius'] = 3.5875000000000004
    option['internal_geometry']['parameters']['inner_shoulder'] = 31.58
    option['internal_geometry']['parameters']['outer_shoulder'] = 35.92
    option['internal_geometry']['parameters']['cage_half_width'] = 1.9250000000000005
    option['internal_geometry']['parameters']['cage_low'] = 3.325
    option['internal_geometry']['parameters']['cage_high'] = 4.025
    option['internal_geometry']['parameters']['window_radius'] = 1.6800000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '84'
    options.append(copy.deepcopy(option))

    # 6912: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6900_series_6912_size_60_mm_id_85_mm_od_13_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6900_series_6912_size_60_mm_id_85_mm_od_13_mm_depth'
    option['size'] = '6912'
    option['series'] = '6900'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 60.0
    option['dimensions']['outside'] = 85.0
    option['dimensions']['width'] = 13.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 24
    option['internal_geometry']['balls_per_row'] = 24
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 60.0
    option['internal_geometry']['parameters']['outside'] = 85.0
    option['internal_geometry']['parameters']['width'] = 13.0
    option['internal_geometry']['parameters']['edge'] = 0.75
    option['internal_geometry']['parameters']['pitch_radius'] = 36.25
    option['internal_geometry']['parameters']['ball_radius'] = 3.5000000000000004
    option['internal_geometry']['parameters']['groove_radius'] = 3.5875000000000004
    option['internal_geometry']['parameters']['inner_shoulder'] = 34.08
    option['internal_geometry']['parameters']['outer_shoulder'] = 38.42
    option['internal_geometry']['parameters']['cage_half_width'] = 1.9250000000000005
    option['internal_geometry']['parameters']['cage_low'] = 3.325
    option['internal_geometry']['parameters']['cage_high'] = 4.025
    option['internal_geometry']['parameters']['window_radius'] = 1.6800000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '47'
    options.append(copy.deepcopy(option))

    # 6913: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6900_series_6913_size_65_mm_id_90_mm_od_13_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6900_series_6913_size_65_mm_id_90_mm_od_13_mm_depth'
    option['size'] = '6913'
    option['series'] = '6900'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 65.0
    option['dimensions']['outside'] = 90.0
    option['dimensions']['width'] = 13.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 25
    option['internal_geometry']['balls_per_row'] = 25
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 65.0
    option['internal_geometry']['parameters']['outside'] = 90.0
    option['internal_geometry']['parameters']['width'] = 13.0
    option['internal_geometry']['parameters']['edge'] = 0.75
    option['internal_geometry']['parameters']['pitch_radius'] = 38.75
    option['internal_geometry']['parameters']['ball_radius'] = 3.5000000000000004
    option['internal_geometry']['parameters']['groove_radius'] = 3.5875000000000004
    option['internal_geometry']['parameters']['inner_shoulder'] = 36.58
    option['internal_geometry']['parameters']['outer_shoulder'] = 40.92
    option['internal_geometry']['parameters']['cage_half_width'] = 1.9250000000000005
    option['internal_geometry']['parameters']['cage_low'] = 3.325
    option['internal_geometry']['parameters']['cage_high'] = 4.025
    option['internal_geometry']['parameters']['window_radius'] = 1.6800000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '96'
    options.append(copy.deepcopy(option))

    # 6914: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6900_series_6914_size_70_mm_id_100_mm_od_16_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6900_series_6914_size_70_mm_id_100_mm_od_16_mm_depth'
    option['size'] = '6914'
    option['series'] = '6900'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 70.0
    option['dimensions']['outside'] = 100.0
    option['dimensions']['width'] = 16.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 23
    option['internal_geometry']['balls_per_row'] = 23
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 70.0
    option['internal_geometry']['parameters']['outside'] = 100.0
    option['internal_geometry']['parameters']['width'] = 16.0
    option['internal_geometry']['parameters']['edge'] = 0.8999999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 42.5
    option['internal_geometry']['parameters']['ball_radius'] = 4.2
    option['internal_geometry']['parameters']['groove_radius'] = 4.305000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 39.896
    option['internal_geometry']['parameters']['outer_shoulder'] = 45.104
    option['internal_geometry']['parameters']['cage_half_width'] = 2.3100000000000005
    option['internal_geometry']['parameters']['cage_low'] = 3.9899999999999998
    option['internal_geometry']['parameters']['cage_high'] = 4.83
    option['internal_geometry']['parameters']['window_radius'] = 2.016
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '155'
    options.append(copy.deepcopy(option))

    # 6915: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6900_series_6915_size_75_mm_id_105_mm_od_16_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6900_series_6915_size_75_mm_id_105_mm_od_16_mm_depth'
    option['size'] = '6915'
    option['series'] = '6900'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 75.0
    option['dimensions']['outside'] = 105.0
    option['dimensions']['width'] = 16.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 24
    option['internal_geometry']['balls_per_row'] = 24
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 75.0
    option['internal_geometry']['parameters']['outside'] = 105.0
    option['internal_geometry']['parameters']['width'] = 16.0
    option['internal_geometry']['parameters']['edge'] = 0.8999999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 45.0
    option['internal_geometry']['parameters']['ball_radius'] = 4.2
    option['internal_geometry']['parameters']['groove_radius'] = 4.305000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 42.396
    option['internal_geometry']['parameters']['outer_shoulder'] = 47.604
    option['internal_geometry']['parameters']['cage_half_width'] = 2.3100000000000005
    option['internal_geometry']['parameters']['cage_low'] = 3.9899999999999998
    option['internal_geometry']['parameters']['cage_high'] = 4.83
    option['internal_geometry']['parameters']['window_radius'] = 2.016
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '165'
    options.append(copy.deepcopy(option))

    # 6916: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6900_series_6916_size_80_mm_id_110_mm_od_16_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6900_series_6916_size_80_mm_id_110_mm_od_16_mm_depth'
    option['size'] = '6916'
    option['series'] = '6900'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 80.0
    option['dimensions']['outside'] = 110.0
    option['dimensions']['width'] = 16.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 26
    option['internal_geometry']['balls_per_row'] = 26
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 80.0
    option['internal_geometry']['parameters']['outside'] = 110.0
    option['internal_geometry']['parameters']['width'] = 16.0
    option['internal_geometry']['parameters']['edge'] = 0.8999999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 47.5
    option['internal_geometry']['parameters']['ball_radius'] = 4.2
    option['internal_geometry']['parameters']['groove_radius'] = 4.305000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 44.896
    option['internal_geometry']['parameters']['outer_shoulder'] = 50.104
    option['internal_geometry']['parameters']['cage_half_width'] = 2.3100000000000005
    option['internal_geometry']['parameters']['cage_low'] = 3.9899999999999998
    option['internal_geometry']['parameters']['cage_high'] = 4.83
    option['internal_geometry']['parameters']['window_radius'] = 2.016
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '173'
    options.append(copy.deepcopy(option))

    # 6917: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6900_series_6917_size_85_mm_id_120_mm_od_18_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6900_series_6917_size_85_mm_id_120_mm_od_18_mm_depth'
    option['size'] = '6917'
    option['series'] = '6900'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 85.0
    option['dimensions']['outside'] = 120.0
    option['dimensions']['width'] = 18.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 24
    option['internal_geometry']['balls_per_row'] = 24
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 85.0
    option['internal_geometry']['parameters']['outside'] = 120.0
    option['internal_geometry']['parameters']['width'] = 18.0
    option['internal_geometry']['parameters']['edge'] = 1.05
    option['internal_geometry']['parameters']['pitch_radius'] = 51.25
    option['internal_geometry']['parameters']['ball_radius'] = 4.9
    option['internal_geometry']['parameters']['groove_radius'] = 5.0225
    option['internal_geometry']['parameters']['inner_shoulder'] = 48.212
    option['internal_geometry']['parameters']['outer_shoulder'] = 54.288
    option['internal_geometry']['parameters']['cage_half_width'] = 2.6950000000000003
    option['internal_geometry']['parameters']['cage_low'] = 4.655
    option['internal_geometry']['parameters']['cage_high'] = 5.635
    option['internal_geometry']['parameters']['window_radius'] = 2.352
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '243'
    options.append(copy.deepcopy(option))

    # 6918: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6900_series_6918_size_90_mm_id_125_mm_od_18_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6900_series_6918_size_90_mm_id_125_mm_od_18_mm_depth'
    option['size'] = '6918'
    option['series'] = '6900'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 90.0
    option['dimensions']['outside'] = 125.0
    option['dimensions']['width'] = 18.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 25
    option['internal_geometry']['balls_per_row'] = 25
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 90.0
    option['internal_geometry']['parameters']['outside'] = 125.0
    option['internal_geometry']['parameters']['width'] = 18.0
    option['internal_geometry']['parameters']['edge'] = 1.05
    option['internal_geometry']['parameters']['pitch_radius'] = 53.75
    option['internal_geometry']['parameters']['ball_radius'] = 4.9
    option['internal_geometry']['parameters']['groove_radius'] = 5.0225
    option['internal_geometry']['parameters']['inner_shoulder'] = 50.712
    option['internal_geometry']['parameters']['outer_shoulder'] = 56.788
    option['internal_geometry']['parameters']['cage_half_width'] = 2.6950000000000003
    option['internal_geometry']['parameters']['cage_low'] = 4.655
    option['internal_geometry']['parameters']['cage_high'] = 5.635
    option['internal_geometry']['parameters']['window_radius'] = 2.352
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '257'
    options.append(copy.deepcopy(option))

    # 6919: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6900_series_6919_size_95_mm_id_130_mm_od_18_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6900_series_6919_size_95_mm_id_130_mm_od_18_mm_depth'
    option['size'] = '6919'
    option['series'] = '6900'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 95.0
    option['dimensions']['outside'] = 130.0
    option['dimensions']['width'] = 18.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 26
    option['internal_geometry']['balls_per_row'] = 26
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 95.0
    option['internal_geometry']['parameters']['outside'] = 130.0
    option['internal_geometry']['parameters']['width'] = 18.0
    option['internal_geometry']['parameters']['edge'] = 1.05
    option['internal_geometry']['parameters']['pitch_radius'] = 56.25
    option['internal_geometry']['parameters']['ball_radius'] = 4.9
    option['internal_geometry']['parameters']['groove_radius'] = 5.0225
    option['internal_geometry']['parameters']['inner_shoulder'] = 53.212
    option['internal_geometry']['parameters']['outer_shoulder'] = 59.288
    option['internal_geometry']['parameters']['cage_half_width'] = 2.6950000000000003
    option['internal_geometry']['parameters']['cage_low'] = 4.655
    option['internal_geometry']['parameters']['cage_high'] = 5.635
    option['internal_geometry']['parameters']['window_radius'] = 2.352
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '320'
    options.append(copy.deepcopy(option))

    # 6920: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6900_series_6920_size_100_mm_id_140_mm_od_20_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6900_series_6920_size_100_mm_id_140_mm_od_20_mm_depth'
    option['size'] = '6920'
    option['series'] = '6900'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 100.0
    option['dimensions']['outside'] = 140.0
    option['dimensions']['width'] = 20.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 24
    option['internal_geometry']['balls_per_row'] = 24
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 100.0
    option['internal_geometry']['parameters']['outside'] = 140.0
    option['internal_geometry']['parameters']['width'] = 20.0
    option['internal_geometry']['parameters']['edge'] = 1.2
    option['internal_geometry']['parameters']['pitch_radius'] = 60.0
    option['internal_geometry']['parameters']['ball_radius'] = 5.6000000000000005
    option['internal_geometry']['parameters']['groove_radius'] = 5.74
    option['internal_geometry']['parameters']['inner_shoulder'] = 56.528
    option['internal_geometry']['parameters']['outer_shoulder'] = 63.472
    option['internal_geometry']['parameters']['cage_half_width'] = 3.0800000000000005
    option['internal_geometry']['parameters']['cage_low'] = 5.32
    option['internal_geometry']['parameters']['cage_high'] = 6.44
    option['internal_geometry']['parameters']['window_radius'] = 2.688
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '436'
    options.append(copy.deepcopy(option))

    # 6921: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6900_series_6921_size_105_mm_id_145_mm_od_20_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6900_series_6921_size_105_mm_id_145_mm_od_20_mm_depth'
    option['size'] = '6921'
    option['series'] = '6900'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 105.0
    option['dimensions']['outside'] = 145.0
    option['dimensions']['width'] = 20.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 25
    option['internal_geometry']['balls_per_row'] = 25
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 105.0
    option['internal_geometry']['parameters']['outside'] = 145.0
    option['internal_geometry']['parameters']['width'] = 20.0
    option['internal_geometry']['parameters']['edge'] = 1.2
    option['internal_geometry']['parameters']['pitch_radius'] = 62.5
    option['internal_geometry']['parameters']['ball_radius'] = 5.6000000000000005
    option['internal_geometry']['parameters']['groove_radius'] = 5.74
    option['internal_geometry']['parameters']['inner_shoulder'] = 59.028
    option['internal_geometry']['parameters']['outer_shoulder'] = 65.972
    option['internal_geometry']['parameters']['cage_half_width'] = 3.0800000000000005
    option['internal_geometry']['parameters']['cage_low'] = 5.32
    option['internal_geometry']['parameters']['cage_high'] = 6.44
    option['internal_geometry']['parameters']['window_radius'] = 2.688
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '454'
    options.append(copy.deepcopy(option))

    # 6922: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6900_series_6922_size_110_mm_id_150_mm_od_20_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6900_series_6922_size_110_mm_id_150_mm_od_20_mm_depth'
    option['size'] = '6922'
    option['series'] = '6900'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 110.0
    option['dimensions']['outside'] = 150.0
    option['dimensions']['width'] = 20.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 26
    option['internal_geometry']['balls_per_row'] = 26
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 110.0
    option['internal_geometry']['parameters']['outside'] = 150.0
    option['internal_geometry']['parameters']['width'] = 20.0
    option['internal_geometry']['parameters']['edge'] = 1.2
    option['internal_geometry']['parameters']['pitch_radius'] = 65.0
    option['internal_geometry']['parameters']['ball_radius'] = 5.6000000000000005
    option['internal_geometry']['parameters']['groove_radius'] = 5.74
    option['internal_geometry']['parameters']['inner_shoulder'] = 61.528
    option['internal_geometry']['parameters']['outer_shoulder'] = 68.472
    option['internal_geometry']['parameters']['cage_half_width'] = 3.0800000000000005
    option['internal_geometry']['parameters']['cage_low'] = 5.32
    option['internal_geometry']['parameters']['cage_high'] = 6.44
    option['internal_geometry']['parameters']['window_radius'] = 2.688
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '472'
    options.append(copy.deepcopy(option))

    # 6924: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6900_series_6924_size_120_mm_id_165_mm_od_22_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6900_series_6924_size_120_mm_id_165_mm_od_22_mm_depth'
    option['size'] = '6924'
    option['series'] = '6900'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 120.0
    option['dimensions']['outside'] = 165.0
    option['dimensions']['width'] = 22.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 26
    option['internal_geometry']['balls_per_row'] = 26
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 120.0
    option['internal_geometry']['parameters']['outside'] = 165.0
    option['internal_geometry']['parameters']['width'] = 22.0
    option['internal_geometry']['parameters']['edge'] = 1.3199999999999998
    option['internal_geometry']['parameters']['pitch_radius'] = 71.25
    option['internal_geometry']['parameters']['ball_radius'] = 6.16
    option['internal_geometry']['parameters']['groove_radius'] = 6.314
    option['internal_geometry']['parameters']['inner_shoulder'] = 67.4308
    option['internal_geometry']['parameters']['outer_shoulder'] = 75.0692
    option['internal_geometry']['parameters']['cage_half_width'] = 3.3880000000000003
    option['internal_geometry']['parameters']['cage_low'] = 5.851999999999999
    option['internal_geometry']['parameters']['cage_high'] = 7.084
    option['internal_geometry']['parameters']['window_radius'] = 2.9568
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '640'
    options.append(copy.deepcopy(option))

    # 6926: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6900_series_6926_size_130_mm_id_180_mm_od_24_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6900_series_6926_size_130_mm_id_180_mm_od_24_mm_depth'
    option['size'] = '6926'
    option['series'] = '6900'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 130.0
    option['dimensions']['outside'] = 180.0
    option['dimensions']['width'] = 24.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 26
    option['internal_geometry']['balls_per_row'] = 26
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 130.0
    option['internal_geometry']['parameters']['outside'] = 180.0
    option['internal_geometry']['parameters']['width'] = 24.0
    option['internal_geometry']['parameters']['edge'] = 1.44
    option['internal_geometry']['parameters']['pitch_radius'] = 77.5
    option['internal_geometry']['parameters']['ball_radius'] = 6.720000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 6.888000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 73.3336
    option['internal_geometry']['parameters']['outer_shoulder'] = 81.6664
    option['internal_geometry']['parameters']['cage_half_width'] = 3.6960000000000006
    option['internal_geometry']['parameters']['cage_low'] = 6.384
    option['internal_geometry']['parameters']['cage_high'] = 7.728
    option['internal_geometry']['parameters']['window_radius'] = 3.2256
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '844'
    options.append(copy.deepcopy(option))

    # 6928: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6900_series_6928_size_140_mm_id_190_mm_od_24_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6900_series_6928_size_140_mm_id_190_mm_od_24_mm_depth'
    option['size'] = '6928'
    option['series'] = '6900'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 140.0
    option['dimensions']['outside'] = 190.0
    option['dimensions']['width'] = 24.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 28
    option['internal_geometry']['balls_per_row'] = 28
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 140.0
    option['internal_geometry']['parameters']['outside'] = 190.0
    option['internal_geometry']['parameters']['width'] = 24.0
    option['internal_geometry']['parameters']['edge'] = 1.44
    option['internal_geometry']['parameters']['pitch_radius'] = 82.5
    option['internal_geometry']['parameters']['ball_radius'] = 6.720000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 6.888000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 78.3336
    option['internal_geometry']['parameters']['outer_shoulder'] = 86.6664
    option['internal_geometry']['parameters']['cage_half_width'] = 3.6960000000000006
    option['internal_geometry']['parameters']['cage_low'] = 6.384
    option['internal_geometry']['parameters']['cage_high'] = 7.728
    option['internal_geometry']['parameters']['window_radius'] = 3.2256
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '899'
    options.append(copy.deepcopy(option))

    # 6930: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_6900_series_6930_size_150_mm_id_210_mm_od_28_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_6900_series_6930_size_150_mm_id_210_mm_od_28_mm_depth'
    option['size'] = '6930'
    option['series'] = '6900'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 150.0
    option['dimensions']['outside'] = 210.0
    option['dimensions']['width'] = 28.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 26
    option['internal_geometry']['balls_per_row'] = 26
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 150.0
    option['internal_geometry']['parameters']['outside'] = 210.0
    option['internal_geometry']['parameters']['width'] = 28.0
    option['internal_geometry']['parameters']['edge'] = 1.68
    option['internal_geometry']['parameters']['pitch_radius'] = 90.0
    option['internal_geometry']['parameters']['ball_radius'] = 7.840000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 8.036000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 85.1392
    option['internal_geometry']['parameters']['outer_shoulder'] = 94.8608
    option['internal_geometry']['parameters']['cage_half_width'] = 4.312000000000001
    option['internal_geometry']['parameters']['cage_low'] = 7.448
    option['internal_geometry']['parameters']['cage_high'] = 9.016
    option['internal_geometry']['parameters']['window_radius'] = 3.7632000000000003
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1,385'
    options.append(copy.deepcopy(option))

    # F603: flanged deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_f600_series_f603_size_3_mm_id_9_mm_od_3_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_f600_series_f603_size_3_mm_id_9_mm_od_3_mm_depth'
    option['size'] = 'F603'
    option['series'] = 'F600'
    option['family'] = 'flanged_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 3.0
    option['dimensions']['outside'] = 9.0
    option['dimensions']['width'] = 3.0
    option['dimensions']['flange_diameter'] = 10.5
    option['dimensions']['flange_thickness'] = 0.7
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F603']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'flanged_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 3.0
    option['internal_geometry']['parameters']['outside'] = 9.0
    option['internal_geometry']['parameters']['width'] = 3.0
    option['internal_geometry']['parameters']['edge'] = 0.18
    option['internal_geometry']['parameters']['pitch_radius'] = 3.0
    option['internal_geometry']['parameters']['ball_radius'] = 0.8400000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 0.8610000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 2.4792
    option['internal_geometry']['parameters']['outer_shoulder'] = 3.5208
    option['internal_geometry']['parameters']['cage_half_width'] = 0.4620000000000001
    option['internal_geometry']['parameters']['cage_low'] = 0.798
    option['internal_geometry']['parameters']['cage_high'] = 0.966
    option['internal_geometry']['parameters']['window_radius'] = 0.4032
    option['internal_geometry']['parameters']['flange_diameter'] = 10.5
    option['internal_geometry']['parameters']['flange_thickness'] = 0.7
    option['internal_geometry']['parameters']['flange_edge'] = 0.105
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_f600_series_f603_size_3_mm_id_9_mm_od_5_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F603']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # F604: flanged deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_f600_series_f604_size_4_mm_id_12_mm_od_4_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_F600_series_F604_size_4_mm_id_12_mm_od_4_mm_depth'
    option['size'] = 'F604'
    option['series'] = 'F600'
    option['family'] = 'flanged_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 4.0
    option['dimensions']['outside'] = 12.0
    option['dimensions']['width'] = 4.0
    option['dimensions']['flange_diameter'] = 13.5
    option['dimensions']['flange_thickness'] = 1.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F604']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'flanged_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 4.0
    option['internal_geometry']['parameters']['outside'] = 12.0
    option['internal_geometry']['parameters']['width'] = 4.0
    option['internal_geometry']['parameters']['edge'] = 0.24
    option['internal_geometry']['parameters']['pitch_radius'] = 4.0
    option['internal_geometry']['parameters']['ball_radius'] = 1.12
    option['internal_geometry']['parameters']['groove_radius'] = 1.1480000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 3.3056
    option['internal_geometry']['parameters']['outer_shoulder'] = 4.6944
    option['internal_geometry']['parameters']['cage_half_width'] = 0.6160000000000001
    option['internal_geometry']['parameters']['cage_low'] = 1.064
    option['internal_geometry']['parameters']['cage_high'] = 1.288
    option['internal_geometry']['parameters']['window_radius'] = 0.5376000000000001
    option['internal_geometry']['parameters']['flange_diameter'] = 13.5
    option['internal_geometry']['parameters']['flange_thickness'] = 1.0
    option['internal_geometry']['parameters']['flange_edge'] = 0.15
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '2'
    options.append(copy.deepcopy(option))

    # F605: flanged deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_f600_series_f605_size_5_mm_id_14_mm_od_5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_F600_series_F605_size_5_mm_id_14_mm_od_5_mm_depth'
    option['size'] = 'F605'
    option['series'] = 'F600'
    option['family'] = 'flanged_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 5.0
    option['dimensions']['outside'] = 14.0
    option['dimensions']['width'] = 5.0
    option['dimensions']['flange_diameter'] = 16.0
    option['dimensions']['flange_thickness'] = 1.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F605']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'flanged_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 5.0
    option['internal_geometry']['parameters']['outside'] = 14.0
    option['internal_geometry']['parameters']['width'] = 5.0
    option['internal_geometry']['parameters']['edge'] = 0.27
    option['internal_geometry']['parameters']['pitch_radius'] = 4.75
    option['internal_geometry']['parameters']['ball_radius'] = 1.2600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.2915000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 3.9688
    option['internal_geometry']['parameters']['outer_shoulder'] = 5.5312
    option['internal_geometry']['parameters']['cage_half_width'] = 0.6930000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.197
    option['internal_geometry']['parameters']['cage_high'] = 1.449
    option['internal_geometry']['parameters']['window_radius'] = 0.6048000000000001
    option['internal_geometry']['parameters']['flange_diameter'] = 16.0
    option['internal_geometry']['parameters']['flange_thickness'] = 1.0
    option['internal_geometry']['parameters']['flange_edge'] = 0.15
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '4'
    options.append(copy.deepcopy(option))

    # F606: flanged deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_f600_series_f606_size_6_mm_id_17_mm_od_6_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_F600_series_F606_size_6_mm_id_17_mm_od_6_mm_depth'
    option['size'] = 'F606'
    option['series'] = 'F600'
    option['family'] = 'flanged_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 6.0
    option['dimensions']['outside'] = 17.0
    option['dimensions']['width'] = 6.0
    option['dimensions']['flange_diameter'] = 19.0
    option['dimensions']['flange_thickness'] = 1.2
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F606']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'flanged_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 6.0
    option['internal_geometry']['parameters']['outside'] = 17.0
    option['internal_geometry']['parameters']['width'] = 6.0
    option['internal_geometry']['parameters']['edge'] = 0.32999999999999996
    option['internal_geometry']['parameters']['pitch_radius'] = 5.75
    option['internal_geometry']['parameters']['ball_radius'] = 1.54
    option['internal_geometry']['parameters']['groove_radius'] = 1.5785
    option['internal_geometry']['parameters']['inner_shoulder'] = 4.7952
    option['internal_geometry']['parameters']['outer_shoulder'] = 6.7048
    option['internal_geometry']['parameters']['cage_half_width'] = 0.8470000000000001
    option['internal_geometry']['parameters']['cage_low'] = 1.4629999999999999
    option['internal_geometry']['parameters']['cage_high'] = 1.771
    option['internal_geometry']['parameters']['window_radius'] = 0.7392
    option['internal_geometry']['parameters']['flange_diameter'] = 19.0
    option['internal_geometry']['parameters']['flange_thickness'] = 1.2
    option['internal_geometry']['parameters']['flange_edge'] = 0.18
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '6'
    options.append(copy.deepcopy(option))

    # F607: flanged deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_f600_series_f607_size_7_mm_id_19_mm_od_6_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_F600_series_F607_size_7_mm_id_19_mm_od_6_mm_depth'
    option['size'] = 'F607'
    option['series'] = 'F600'
    option['family'] = 'flanged_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 7.0
    option['dimensions']['outside'] = 19.0
    option['dimensions']['width'] = 6.0
    option['dimensions']['flange_diameter'] = 22.0
    option['dimensions']['flange_thickness'] = 1.5
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F607']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'flanged_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 7.0
    option['internal_geometry']['parameters']['outside'] = 19.0
    option['internal_geometry']['parameters']['width'] = 6.0
    option['internal_geometry']['parameters']['edge'] = 0.36
    option['internal_geometry']['parameters']['pitch_radius'] = 6.5
    option['internal_geometry']['parameters']['ball_radius'] = 1.6800000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.7220000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 5.4584
    option['internal_geometry']['parameters']['outer_shoulder'] = 7.5416
    option['internal_geometry']['parameters']['cage_half_width'] = 0.9240000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.596
    option['internal_geometry']['parameters']['cage_high'] = 1.932
    option['internal_geometry']['parameters']['window_radius'] = 0.8064
    option['internal_geometry']['parameters']['flange_diameter'] = 22.0
    option['internal_geometry']['parameters']['flange_thickness'] = 1.5
    option['internal_geometry']['parameters']['flange_edge'] = 0.22499999999999998
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '9'
    options.append(copy.deepcopy(option))

    # F608: flanged deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_f600_series_f608_size_8_mm_id_22_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_F600_series_F608_size_8_mm_id_22_mm_od_7_mm_depth'
    option['size'] = 'F608'
    option['series'] = 'F600'
    option['family'] = 'flanged_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 8.0
    option['dimensions']['outside'] = 22.0
    option['dimensions']['width'] = 7.0
    option['dimensions']['flange_diameter'] = 25.0
    option['dimensions']['flange_thickness'] = 1.5
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F608']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'flanged_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 8.0
    option['internal_geometry']['parameters']['outside'] = 22.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.42
    option['internal_geometry']['parameters']['pitch_radius'] = 7.5
    option['internal_geometry']['parameters']['ball_radius'] = 1.9600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 2.0090000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 6.2848
    option['internal_geometry']['parameters']['outer_shoulder'] = 8.7152
    option['internal_geometry']['parameters']['cage_half_width'] = 1.0780000000000003
    option['internal_geometry']['parameters']['cage_low'] = 1.862
    option['internal_geometry']['parameters']['cage_high'] = 2.254
    option['internal_geometry']['parameters']['window_radius'] = 0.9408000000000001
    option['internal_geometry']['parameters']['flange_diameter'] = 25.0
    option['internal_geometry']['parameters']['flange_thickness'] = 1.5
    option['internal_geometry']['parameters']['flange_edge'] = 0.22499999999999998
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '13'
    options.append(copy.deepcopy(option))

    # F623: flanged deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_f600_series_f623_size_3_mm_id_10_mm_od_4_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_F600_series_F623_size_3_mm_id_10_mm_od_4_mm_depth'
    option['size'] = 'F623'
    option['series'] = 'F600'
    option['family'] = 'flanged_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 3.0
    option['dimensions']['outside'] = 10.0
    option['dimensions']['width'] = 4.0
    option['dimensions']['flange_diameter'] = 11.5
    option['dimensions']['flange_thickness'] = 1.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F623']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'flanged_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 7
    option['internal_geometry']['balls_per_row'] = 7
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 3.0
    option['internal_geometry']['parameters']['outside'] = 10.0
    option['internal_geometry']['parameters']['width'] = 4.0
    option['internal_geometry']['parameters']['edge'] = 0.21
    option['internal_geometry']['parameters']['pitch_radius'] = 3.25
    option['internal_geometry']['parameters']['ball_radius'] = 0.9800000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 1.0045000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 2.6424
    option['internal_geometry']['parameters']['outer_shoulder'] = 3.8576
    option['internal_geometry']['parameters']['cage_half_width'] = 0.5390000000000001
    option['internal_geometry']['parameters']['cage_low'] = 0.931
    option['internal_geometry']['parameters']['cage_high'] = 1.127
    option['internal_geometry']['parameters']['window_radius'] = 0.47040000000000004
    option['internal_geometry']['parameters']['flange_diameter'] = 11.5
    option['internal_geometry']['parameters']['flange_thickness'] = 1.0
    option['internal_geometry']['parameters']['flange_edge'] = 0.15
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '2'
    options.append(copy.deepcopy(option))

    # F624: flanged deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_f600_series_f624_size_4_mm_id_13_mm_od_5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_F600_series_F624_size_4_mm_id_13_mm_od_5_mm_depth'
    option['size'] = 'F624'
    option['series'] = 'F600'
    option['family'] = 'flanged_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 4.0
    option['dimensions']['outside'] = 13.0
    option['dimensions']['width'] = 5.0
    option['dimensions']['flange_diameter'] = 15.0
    option['dimensions']['flange_thickness'] = 1.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F624']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'flanged_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 7
    option['internal_geometry']['balls_per_row'] = 7
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 4.0
    option['internal_geometry']['parameters']['outside'] = 13.0
    option['internal_geometry']['parameters']['width'] = 5.0
    option['internal_geometry']['parameters']['edge'] = 0.27
    option['internal_geometry']['parameters']['pitch_radius'] = 4.25
    option['internal_geometry']['parameters']['ball_radius'] = 1.2600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.2915000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 3.4688
    option['internal_geometry']['parameters']['outer_shoulder'] = 5.0312
    option['internal_geometry']['parameters']['cage_half_width'] = 0.6930000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.197
    option['internal_geometry']['parameters']['cage_high'] = 1.449
    option['internal_geometry']['parameters']['window_radius'] = 0.6048000000000001
    option['internal_geometry']['parameters']['flange_diameter'] = 15.0
    option['internal_geometry']['parameters']['flange_thickness'] = 1.0
    option['internal_geometry']['parameters']['flange_edge'] = 0.15
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '3'
    options.append(copy.deepcopy(option))

    # F625: flanged deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_f600_series_f625_size_5_mm_id_16_mm_od_5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_F600_series_F625_size_5_mm_id_16_mm_od_5_mm_depth'
    option['size'] = 'F625'
    option['series'] = 'F600'
    option['family'] = 'flanged_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 5.0
    option['dimensions']['outside'] = 16.0
    option['dimensions']['width'] = 5.0
    option['dimensions']['flange_diameter'] = 18.0
    option['dimensions']['flange_thickness'] = 1.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F625']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'flanged_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 5.0
    option['internal_geometry']['parameters']['outside'] = 16.0
    option['internal_geometry']['parameters']['width'] = 5.0
    option['internal_geometry']['parameters']['edge'] = 0.3
    option['internal_geometry']['parameters']['pitch_radius'] = 5.25
    option['internal_geometry']['parameters']['ball_radius'] = 1.4000000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 1.435
    option['internal_geometry']['parameters']['inner_shoulder'] = 4.382
    option['internal_geometry']['parameters']['outer_shoulder'] = 6.118
    option['internal_geometry']['parameters']['cage_half_width'] = 0.7700000000000001
    option['internal_geometry']['parameters']['cage_low'] = 1.33
    option['internal_geometry']['parameters']['cage_high'] = 1.61
    option['internal_geometry']['parameters']['window_radius'] = 0.672
    option['internal_geometry']['parameters']['flange_diameter'] = 18.0
    option['internal_geometry']['parameters']['flange_thickness'] = 1.0
    option['internal_geometry']['parameters']['flange_edge'] = 0.15
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '5'
    options.append(copy.deepcopy(option))

    # F626: flanged deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_f600_series_f626_size_6_mm_id_19_mm_od_6_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_F600_series_F626_size_6_mm_id_19_mm_od_6_mm_depth'
    option['size'] = 'F626'
    option['series'] = 'F600'
    option['family'] = 'flanged_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 6.0
    option['dimensions']['outside'] = 19.0
    option['dimensions']['width'] = 6.0
    option['dimensions']['flange_diameter'] = 22.0
    option['dimensions']['flange_thickness'] = 1.5
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F626']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'flanged_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 6.0
    option['internal_geometry']['parameters']['outside'] = 19.0
    option['internal_geometry']['parameters']['width'] = 6.0
    option['internal_geometry']['parameters']['edge'] = 0.36
    option['internal_geometry']['parameters']['pitch_radius'] = 6.25
    option['internal_geometry']['parameters']['ball_radius'] = 1.6800000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.7220000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 5.2084
    option['internal_geometry']['parameters']['outer_shoulder'] = 7.2916
    option['internal_geometry']['parameters']['cage_half_width'] = 0.9240000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.596
    option['internal_geometry']['parameters']['cage_high'] = 1.932
    option['internal_geometry']['parameters']['window_radius'] = 0.8064
    option['internal_geometry']['parameters']['flange_diameter'] = 22.0
    option['internal_geometry']['parameters']['flange_thickness'] = 1.5
    option['internal_geometry']['parameters']['flange_edge'] = 0.22499999999999998
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '9'
    options.append(copy.deepcopy(option))

    # F627: flanged deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_f600_series_f627_size_7_mm_id_22_mm_od_7_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_F600_series_F627_size_7_mm_id_22_mm_od_7_mm_depth'
    option['size'] = 'F627'
    option['series'] = 'F600'
    option['family'] = 'flanged_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 7.0
    option['dimensions']['outside'] = 22.0
    option['dimensions']['width'] = 7.0
    option['dimensions']['flange_diameter'] = 25.0
    option['dimensions']['flange_thickness'] = 1.5
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F627']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'flanged_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 7.0
    option['internal_geometry']['parameters']['outside'] = 22.0
    option['internal_geometry']['parameters']['width'] = 7.0
    option['internal_geometry']['parameters']['edge'] = 0.42
    option['internal_geometry']['parameters']['pitch_radius'] = 7.25
    option['internal_geometry']['parameters']['ball_radius'] = 1.9600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 2.0090000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 6.0348
    option['internal_geometry']['parameters']['outer_shoulder'] = 8.4652
    option['internal_geometry']['parameters']['cage_half_width'] = 1.0780000000000003
    option['internal_geometry']['parameters']['cage_low'] = 1.862
    option['internal_geometry']['parameters']['cage_high'] = 2.254
    option['internal_geometry']['parameters']['window_radius'] = 0.9408000000000001
    option['internal_geometry']['parameters']['flange_diameter'] = 25.0
    option['internal_geometry']['parameters']['flange_thickness'] = 1.5
    option['internal_geometry']['parameters']['flange_edge'] = 0.22499999999999998
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '14'
    options.append(copy.deepcopy(option))

    # F634: flanged deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_f600_series_f634_size_4_mm_id_16_mm_od_5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_F600_series_F634_size_4_mm_id_16_mm_od_5_mm_depth'
    option['size'] = 'F634'
    option['series'] = 'F600'
    option['family'] = 'flanged_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 4.0
    option['dimensions']['outside'] = 16.0
    option['dimensions']['width'] = 5.0
    option['dimensions']['flange_diameter'] = 18.0
    option['dimensions']['flange_thickness'] = 1.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F634']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'flanged_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 4.0
    option['internal_geometry']['parameters']['outside'] = 16.0
    option['internal_geometry']['parameters']['width'] = 5.0
    option['internal_geometry']['parameters']['edge'] = 0.3
    option['internal_geometry']['parameters']['pitch_radius'] = 5.0
    option['internal_geometry']['parameters']['ball_radius'] = 1.4000000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 1.435
    option['internal_geometry']['parameters']['inner_shoulder'] = 4.132
    option['internal_geometry']['parameters']['outer_shoulder'] = 5.868
    option['internal_geometry']['parameters']['cage_half_width'] = 0.7700000000000001
    option['internal_geometry']['parameters']['cage_low'] = 1.33
    option['internal_geometry']['parameters']['cage_high'] = 1.61
    option['internal_geometry']['parameters']['window_radius'] = 0.672
    option['internal_geometry']['parameters']['flange_diameter'] = 18.0
    option['internal_geometry']['parameters']['flange_thickness'] = 1.0
    option['internal_geometry']['parameters']['flange_edge'] = 0.15
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '6'
    options.append(copy.deepcopy(option))

    # F635: flanged deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_f600_series_f635_size_5_mm_id_19_mm_od_6_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_F600_series_F635_size_5_mm_id_19_mm_od_6_mm_depth'
    option['size'] = 'F635'
    option['series'] = 'F600'
    option['family'] = 'flanged_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 5.0
    option['dimensions']['outside'] = 19.0
    option['dimensions']['width'] = 6.0
    option['dimensions']['flange_diameter'] = 22.0
    option['dimensions']['flange_thickness'] = 1.5
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F635']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'flanged_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 5.0
    option['internal_geometry']['parameters']['outside'] = 19.0
    option['internal_geometry']['parameters']['width'] = 6.0
    option['internal_geometry']['parameters']['edge'] = 0.36
    option['internal_geometry']['parameters']['pitch_radius'] = 6.0
    option['internal_geometry']['parameters']['ball_radius'] = 1.6800000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.7220000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 4.9584
    option['internal_geometry']['parameters']['outer_shoulder'] = 7.0416
    option['internal_geometry']['parameters']['cage_half_width'] = 0.9240000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.596
    option['internal_geometry']['parameters']['cage_high'] = 1.932
    option['internal_geometry']['parameters']['window_radius'] = 0.8064
    option['internal_geometry']['parameters']['flange_diameter'] = 22.0
    option['internal_geometry']['parameters']['flange_thickness'] = 1.5
    option['internal_geometry']['parameters']['flange_edge'] = 0.22499999999999998
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '9'
    options.append(copy.deepcopy(option))

    # F683: flanged deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_f600_series_f683_size_3_mm_id_7_mm_od_2_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_f600_series_f683_size_3_mm_id_7_mm_od_2_mm_depth'
    option['size'] = 'F683'
    option['series'] = 'F600'
    option['family'] = 'flanged_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 3.0
    option['dimensions']['outside'] = 7.0
    option['dimensions']['width'] = 2.0
    option['dimensions']['flange_diameter'] = 8.1
    option['dimensions']['flange_thickness'] = 0.5
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F683']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'flanged_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 10
    option['internal_geometry']['balls_per_row'] = 10
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 3.0
    option['internal_geometry']['parameters']['outside'] = 7.0
    option['internal_geometry']['parameters']['width'] = 2.0
    option['internal_geometry']['parameters']['edge'] = 0.12
    option['internal_geometry']['parameters']['pitch_radius'] = 2.5
    option['internal_geometry']['parameters']['ball_radius'] = 0.56
    option['internal_geometry']['parameters']['groove_radius'] = 0.5740000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 2.1528
    option['internal_geometry']['parameters']['outer_shoulder'] = 2.8472
    option['internal_geometry']['parameters']['cage_half_width'] = 0.30800000000000005
    option['internal_geometry']['parameters']['cage_low'] = 0.532
    option['internal_geometry']['parameters']['cage_high'] = 0.644
    option['internal_geometry']['parameters']['window_radius'] = 0.26880000000000004
    option['internal_geometry']['parameters']['flange_diameter'] = 8.1
    option['internal_geometry']['parameters']['flange_thickness'] = 0.5
    option['internal_geometry']['parameters']['flange_edge'] = 0.075
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '0'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_f600_series_f683_size_3_mm_id_7_mm_od_3_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F683']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # F684: flanged deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_f600_series_f684_size_4_mm_id_9_mm_od_2.5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_f600_series_f684_size_4_mm_id_9_mm_od_2_5_mm_depth'
    option['size'] = 'F684'
    option['series'] = 'F600'
    option['family'] = 'flanged_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 4.0
    option['dimensions']['outside'] = 9.0
    option['dimensions']['width'] = 2.5
    option['dimensions']['flange_diameter'] = 10.3
    option['dimensions']['flange_thickness'] = 0.6
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F684']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'flanged_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 10
    option['internal_geometry']['balls_per_row'] = 10
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 4.0
    option['internal_geometry']['parameters']['outside'] = 9.0
    option['internal_geometry']['parameters']['width'] = 2.5
    option['internal_geometry']['parameters']['edge'] = 0.15
    option['internal_geometry']['parameters']['pitch_radius'] = 3.25
    option['internal_geometry']['parameters']['ball_radius'] = 0.7000000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 0.7175
    option['internal_geometry']['parameters']['inner_shoulder'] = 2.816
    option['internal_geometry']['parameters']['outer_shoulder'] = 3.684
    option['internal_geometry']['parameters']['cage_half_width'] = 0.38500000000000006
    option['internal_geometry']['parameters']['cage_low'] = 0.665
    option['internal_geometry']['parameters']['cage_high'] = 0.805
    option['internal_geometry']['parameters']['window_radius'] = 0.336
    option['internal_geometry']['parameters']['flange_diameter'] = 10.3
    option['internal_geometry']['parameters']['flange_thickness'] = 0.6
    option['internal_geometry']['parameters']['flange_edge'] = 0.09
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_f600_series_f684_size_4_mm_id_9_mm_od_4_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F684']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # F685: flanged deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_f600_series_f685_size_5_mm_id_11_mm_od_3_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_f600_series_f685_size_5_mm_id_11_mm_od_3_mm_depth'
    option['size'] = 'F685'
    option['series'] = 'F600'
    option['family'] = 'flanged_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 5.0
    option['dimensions']['outside'] = 11.0
    option['dimensions']['width'] = 3.0
    option['dimensions']['flange_diameter'] = 12.5
    option['dimensions']['flange_thickness'] = 0.8
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F685']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'flanged_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 10
    option['internal_geometry']['balls_per_row'] = 10
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 5.0
    option['internal_geometry']['parameters']['outside'] = 11.0
    option['internal_geometry']['parameters']['width'] = 3.0
    option['internal_geometry']['parameters']['edge'] = 0.18
    option['internal_geometry']['parameters']['pitch_radius'] = 4.0
    option['internal_geometry']['parameters']['ball_radius'] = 0.8400000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 0.8610000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 3.4792
    option['internal_geometry']['parameters']['outer_shoulder'] = 4.5208
    option['internal_geometry']['parameters']['cage_half_width'] = 0.4620000000000001
    option['internal_geometry']['parameters']['cage_low'] = 0.798
    option['internal_geometry']['parameters']['cage_high'] = 0.966
    option['internal_geometry']['parameters']['window_radius'] = 0.4032
    option['internal_geometry']['parameters']['flange_diameter'] = 12.5
    option['internal_geometry']['parameters']['flange_thickness'] = 0.8
    option['internal_geometry']['parameters']['flange_edge'] = 0.12
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_f600_series_f685_size_5_mm_id_11_mm_od_5_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F685']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # F686: flanged deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_f600_series_f686_size_6_mm_id_13_mm_od_3.5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_f600_series_f686_size_6_mm_id_13_mm_od_3_5_mm_depth'
    option['size'] = 'F686'
    option['series'] = 'F600'
    option['family'] = 'flanged_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 6.0
    option['dimensions']['outside'] = 13.0
    option['dimensions']['width'] = 3.5
    option['dimensions']['flange_diameter'] = 15.0
    option['dimensions']['flange_thickness'] = 1.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F686']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'flanged_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 11
    option['internal_geometry']['balls_per_row'] = 11
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 6.0
    option['internal_geometry']['parameters']['outside'] = 13.0
    option['internal_geometry']['parameters']['width'] = 3.5
    option['internal_geometry']['parameters']['edge'] = 0.21
    option['internal_geometry']['parameters']['pitch_radius'] = 4.75
    option['internal_geometry']['parameters']['ball_radius'] = 0.9800000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 1.0045000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 4.1424
    option['internal_geometry']['parameters']['outer_shoulder'] = 5.3576
    option['internal_geometry']['parameters']['cage_half_width'] = 0.5390000000000001
    option['internal_geometry']['parameters']['cage_low'] = 0.931
    option['internal_geometry']['parameters']['cage_high'] = 1.127
    option['internal_geometry']['parameters']['window_radius'] = 0.47040000000000004
    option['internal_geometry']['parameters']['flange_diameter'] = 15.0
    option['internal_geometry']['parameters']['flange_thickness'] = 1.0
    option['internal_geometry']['parameters']['flange_edge'] = 0.15
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '2'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_f600_series_f686_size_6_mm_id_13_mm_od_5_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F686']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # F687: flanged deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_f600_series_f687_size_7_mm_id_14_mm_od_3.5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_f600_series_f687_size_7_mm_id_14_mm_od_3_5_mm_depth'
    option['size'] = 'F687'
    option['series'] = 'F600'
    option['family'] = 'flanged_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 7.0
    option['dimensions']['outside'] = 14.0
    option['dimensions']['width'] = 3.5
    option['dimensions']['flange_diameter'] = 16.0
    option['dimensions']['flange_thickness'] = 1.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F687']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'flanged_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 12
    option['internal_geometry']['balls_per_row'] = 12
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 7.0
    option['internal_geometry']['parameters']['outside'] = 14.0
    option['internal_geometry']['parameters']['width'] = 3.5
    option['internal_geometry']['parameters']['edge'] = 0.21
    option['internal_geometry']['parameters']['pitch_radius'] = 5.25
    option['internal_geometry']['parameters']['ball_radius'] = 0.9800000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 1.0045000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 4.6424
    option['internal_geometry']['parameters']['outer_shoulder'] = 5.8576
    option['internal_geometry']['parameters']['cage_half_width'] = 0.5390000000000001
    option['internal_geometry']['parameters']['cage_low'] = 0.931
    option['internal_geometry']['parameters']['cage_high'] = 1.127
    option['internal_geometry']['parameters']['window_radius'] = 0.47040000000000004
    option['internal_geometry']['parameters']['flange_diameter'] = 16.0
    option['internal_geometry']['parameters']['flange_thickness'] = 1.0
    option['internal_geometry']['parameters']['flange_edge'] = 0.15
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '2'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_f600_series_f687_size_7_mm_id_14_mm_od_5_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F687']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # F688: flanged deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_f600_series_f688_size_8_mm_id_16_mm_od_4_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_f600_series_f688_size_8_mm_id_16_mm_od_4_mm_depth'
    option['size'] = 'F688'
    option['series'] = 'F600'
    option['family'] = 'flanged_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 8.0
    option['dimensions']['outside'] = 16.0
    option['dimensions']['width'] = 4.0
    option['dimensions']['flange_diameter'] = 18.0
    option['dimensions']['flange_thickness'] = 1.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F688']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'flanged_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 12
    option['internal_geometry']['balls_per_row'] = 12
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 8.0
    option['internal_geometry']['parameters']['outside'] = 16.0
    option['internal_geometry']['parameters']['width'] = 4.0
    option['internal_geometry']['parameters']['edge'] = 0.24
    option['internal_geometry']['parameters']['pitch_radius'] = 6.0
    option['internal_geometry']['parameters']['ball_radius'] = 1.12
    option['internal_geometry']['parameters']['groove_radius'] = 1.1480000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 5.3056
    option['internal_geometry']['parameters']['outer_shoulder'] = 6.6944
    option['internal_geometry']['parameters']['cage_half_width'] = 0.6160000000000001
    option['internal_geometry']['parameters']['cage_low'] = 1.064
    option['internal_geometry']['parameters']['cage_high'] = 1.288
    option['internal_geometry']['parameters']['window_radius'] = 0.5376000000000001
    option['internal_geometry']['parameters']['flange_diameter'] = 18.0
    option['internal_geometry']['parameters']['flange_thickness'] = 1.0
    option['internal_geometry']['parameters']['flange_edge'] = 0.15
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '4'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_f600_series_f688_size_8_mm_id_16_mm_od_5_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F688']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # F689: flanged deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_f600_series_f689_size_9_mm_id_17_mm_od_4_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_f600_series_f689_size_9_mm_id_17_mm_od_4_mm_depth'
    option['size'] = 'F689'
    option['series'] = 'F600'
    option['family'] = 'flanged_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 9.0
    option['dimensions']['outside'] = 17.0
    option['dimensions']['width'] = 4.0
    option['dimensions']['flange_diameter'] = 19.0
    option['dimensions']['flange_thickness'] = 1.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F689']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'flanged_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 13
    option['internal_geometry']['balls_per_row'] = 13
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 9.0
    option['internal_geometry']['parameters']['outside'] = 17.0
    option['internal_geometry']['parameters']['width'] = 4.0
    option['internal_geometry']['parameters']['edge'] = 0.24
    option['internal_geometry']['parameters']['pitch_radius'] = 6.5
    option['internal_geometry']['parameters']['ball_radius'] = 1.12
    option['internal_geometry']['parameters']['groove_radius'] = 1.1480000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 5.8056
    option['internal_geometry']['parameters']['outer_shoulder'] = 7.1944
    option['internal_geometry']['parameters']['cage_half_width'] = 0.6160000000000001
    option['internal_geometry']['parameters']['cage_low'] = 1.064
    option['internal_geometry']['parameters']['cage_high'] = 1.288
    option['internal_geometry']['parameters']['window_radius'] = 0.5376000000000001
    option['internal_geometry']['parameters']['flange_diameter'] = 19.0
    option['internal_geometry']['parameters']['flange_thickness'] = 1.0
    option['internal_geometry']['parameters']['flange_edge'] = 0.15
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '4'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_f600_series_f689_size_9_mm_id_17_mm_od_5_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F689']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # F693: flanged deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_f600_series_f693_size_3_mm_id_8_mm_od_3_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_f600_series_f693_size_3_mm_id_8_mm_od_3_mm_depth'
    option['size'] = 'F693'
    option['series'] = 'F600'
    option['family'] = 'flanged_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 3.0
    option['dimensions']['outside'] = 8.0
    option['dimensions']['width'] = 3.0
    option['dimensions']['flange_diameter'] = 9.5
    option['dimensions']['flange_thickness'] = 0.7
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F693']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'flanged_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 3.0
    option['internal_geometry']['parameters']['outside'] = 8.0
    option['internal_geometry']['parameters']['width'] = 3.0
    option['internal_geometry']['parameters']['edge'] = 0.15
    option['internal_geometry']['parameters']['pitch_radius'] = 2.75
    option['internal_geometry']['parameters']['ball_radius'] = 0.7000000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 0.7175
    option['internal_geometry']['parameters']['inner_shoulder'] = 2.316
    option['internal_geometry']['parameters']['outer_shoulder'] = 3.184
    option['internal_geometry']['parameters']['cage_half_width'] = 0.38500000000000006
    option['internal_geometry']['parameters']['cage_low'] = 0.665
    option['internal_geometry']['parameters']['cage_high'] = 0.805
    option['internal_geometry']['parameters']['window_radius'] = 0.336
    option['internal_geometry']['parameters']['flange_diameter'] = 9.5
    option['internal_geometry']['parameters']['flange_thickness'] = 0.7
    option['internal_geometry']['parameters']['flange_edge'] = 0.105
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1'
    option['catalogue_metadata']['dimension_selection'] = {}
    option['catalogue_metadata']['dimension_selection']['policy'] = 'standard_metric_open_catalogue'
    option['catalogue_metadata']['dimension_selection']['previous_id'] = 'hardware_bearing_f600_series_f693_size_3_mm_id_8_mm_od_4_mm_depth'
    option['catalogue_metadata']['dimension_selection']['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F693']
    option['catalogue_metadata']['dimension_selection']['note'] = 'User selected standard catalogue variants on 2026-10-27; no sales ranking asserted.'
    options.append(copy.deepcopy(option))

    # F694: flanged deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_f600_series_f694_size_4_mm_id_11_mm_od_4_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_F600_series_F694_size_4_mm_id_11_mm_od_4_mm_depth'
    option['size'] = 'F694'
    option['series'] = 'F600'
    option['family'] = 'flanged_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 4.0
    option['dimensions']['outside'] = 11.0
    option['dimensions']['width'] = 4.0
    option['dimensions']['flange_diameter'] = 12.5
    option['dimensions']['flange_thickness'] = 1.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F694']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'flanged_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 4.0
    option['internal_geometry']['parameters']['outside'] = 11.0
    option['internal_geometry']['parameters']['width'] = 4.0
    option['internal_geometry']['parameters']['edge'] = 0.21
    option['internal_geometry']['parameters']['pitch_radius'] = 3.75
    option['internal_geometry']['parameters']['ball_radius'] = 0.9800000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 1.0045000000000002
    option['internal_geometry']['parameters']['inner_shoulder'] = 3.1424
    option['internal_geometry']['parameters']['outer_shoulder'] = 4.3576
    option['internal_geometry']['parameters']['cage_half_width'] = 0.5390000000000001
    option['internal_geometry']['parameters']['cage_low'] = 0.931
    option['internal_geometry']['parameters']['cage_high'] = 1.127
    option['internal_geometry']['parameters']['window_radius'] = 0.47040000000000004
    option['internal_geometry']['parameters']['flange_diameter'] = 12.5
    option['internal_geometry']['parameters']['flange_thickness'] = 1.0
    option['internal_geometry']['parameters']['flange_edge'] = 0.15
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '2'
    options.append(copy.deepcopy(option))

    # F695: flanged deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_f600_series_f695_size_5_mm_id_13_mm_od_4_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_F600_series_F695_size_5_mm_id_13_mm_od_4_mm_depth'
    option['size'] = 'F695'
    option['series'] = 'F600'
    option['family'] = 'flanged_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 5.0
    option['dimensions']['outside'] = 13.0
    option['dimensions']['width'] = 4.0
    option['dimensions']['flange_diameter'] = 15.0
    option['dimensions']['flange_thickness'] = 1.0
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F695']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'flanged_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 9
    option['internal_geometry']['balls_per_row'] = 9
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 5.0
    option['internal_geometry']['parameters']['outside'] = 13.0
    option['internal_geometry']['parameters']['width'] = 4.0
    option['internal_geometry']['parameters']['edge'] = 0.24
    option['internal_geometry']['parameters']['pitch_radius'] = 4.5
    option['internal_geometry']['parameters']['ball_radius'] = 1.12
    option['internal_geometry']['parameters']['groove_radius'] = 1.1480000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 3.8056
    option['internal_geometry']['parameters']['outer_shoulder'] = 5.1944
    option['internal_geometry']['parameters']['cage_half_width'] = 0.6160000000000001
    option['internal_geometry']['parameters']['cage_low'] = 1.064
    option['internal_geometry']['parameters']['cage_high'] = 1.288
    option['internal_geometry']['parameters']['window_radius'] = 0.5376000000000001
    option['internal_geometry']['parameters']['flange_diameter'] = 15.0
    option['internal_geometry']['parameters']['flange_thickness'] = 1.0
    option['internal_geometry']['parameters']['flange_edge'] = 0.15
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '3'
    options.append(copy.deepcopy(option))

    # F696: flanged deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_f600_series_f696_size_6_mm_id_15_mm_od_5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_F600_series_F696_size_6_mm_id_15_mm_od_5_mm_depth'
    option['size'] = 'F696'
    option['series'] = 'F600'
    option['family'] = 'flanged_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 6.0
    option['dimensions']['outside'] = 15.0
    option['dimensions']['width'] = 5.0
    option['dimensions']['flange_diameter'] = 17.0
    option['dimensions']['flange_thickness'] = 1.2
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F696']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'flanged_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 9
    option['internal_geometry']['balls_per_row'] = 9
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 6.0
    option['internal_geometry']['parameters']['outside'] = 15.0
    option['internal_geometry']['parameters']['width'] = 5.0
    option['internal_geometry']['parameters']['edge'] = 0.27
    option['internal_geometry']['parameters']['pitch_radius'] = 5.25
    option['internal_geometry']['parameters']['ball_radius'] = 1.2600000000000002
    option['internal_geometry']['parameters']['groove_radius'] = 1.2915000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 4.4688
    option['internal_geometry']['parameters']['outer_shoulder'] = 6.0312
    option['internal_geometry']['parameters']['cage_half_width'] = 0.6930000000000002
    option['internal_geometry']['parameters']['cage_low'] = 1.197
    option['internal_geometry']['parameters']['cage_high'] = 1.449
    option['internal_geometry']['parameters']['window_radius'] = 0.6048000000000001
    option['internal_geometry']['parameters']['flange_diameter'] = 17.0
    option['internal_geometry']['parameters']['flange_thickness'] = 1.2
    option['internal_geometry']['parameters']['flange_edge'] = 0.18
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '4'
    options.append(copy.deepcopy(option))

    # F697: flanged deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_f600_series_f697_size_7_mm_id_17_mm_od_5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_F600_series_F697_size_7_mm_id_17_mm_od_5_mm_depth'
    option['size'] = 'F697'
    option['series'] = 'F600'
    option['family'] = 'flanged_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 7.0
    option['dimensions']['outside'] = 17.0
    option['dimensions']['width'] = 5.0
    option['dimensions']['flange_diameter'] = 19.0
    option['dimensions']['flange_thickness'] = 1.2
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F697']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'flanged_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 9
    option['internal_geometry']['balls_per_row'] = 9
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 7.0
    option['internal_geometry']['parameters']['outside'] = 17.0
    option['internal_geometry']['parameters']['width'] = 5.0
    option['internal_geometry']['parameters']['edge'] = 0.3
    option['internal_geometry']['parameters']['pitch_radius'] = 6.0
    option['internal_geometry']['parameters']['ball_radius'] = 1.4000000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 1.435
    option['internal_geometry']['parameters']['inner_shoulder'] = 5.132
    option['internal_geometry']['parameters']['outer_shoulder'] = 6.868
    option['internal_geometry']['parameters']['cage_half_width'] = 0.7700000000000001
    option['internal_geometry']['parameters']['cage_low'] = 1.33
    option['internal_geometry']['parameters']['cage_high'] = 1.61
    option['internal_geometry']['parameters']['window_radius'] = 0.672
    option['internal_geometry']['parameters']['flange_diameter'] = 19.0
    option['internal_geometry']['parameters']['flange_thickness'] = 1.2
    option['internal_geometry']['parameters']['flange_edge'] = 0.18
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '6'
    options.append(copy.deepcopy(option))

    # F698: flanged deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_f600_series_f698_size_8_mm_id_19_mm_od_6_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_F600_series_F698_size_8_mm_id_19_mm_od_6_mm_depth'
    option['size'] = 'F698'
    option['series'] = 'F600'
    option['family'] = 'flanged_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 8.0
    option['dimensions']['outside'] = 19.0
    option['dimensions']['width'] = 6.0
    option['dimensions']['flange_diameter'] = 22.0
    option['dimensions']['flange_thickness'] = 1.5
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F698']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'flanged_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 10
    option['internal_geometry']['balls_per_row'] = 10
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 8.0
    option['internal_geometry']['parameters']['outside'] = 19.0
    option['internal_geometry']['parameters']['width'] = 6.0
    option['internal_geometry']['parameters']['edge'] = 0.32999999999999996
    option['internal_geometry']['parameters']['pitch_radius'] = 6.75
    option['internal_geometry']['parameters']['ball_radius'] = 1.54
    option['internal_geometry']['parameters']['groove_radius'] = 1.5785
    option['internal_geometry']['parameters']['inner_shoulder'] = 5.7952
    option['internal_geometry']['parameters']['outer_shoulder'] = 7.7048
    option['internal_geometry']['parameters']['cage_half_width'] = 0.8470000000000001
    option['internal_geometry']['parameters']['cage_low'] = 1.4629999999999999
    option['internal_geometry']['parameters']['cage_high'] = 1.771
    option['internal_geometry']['parameters']['window_radius'] = 0.7392
    option['internal_geometry']['parameters']['flange_diameter'] = 22.0
    option['internal_geometry']['parameters']['flange_thickness'] = 1.5
    option['internal_geometry']['parameters']['flange_edge'] = 0.22499999999999998
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '8'
    options.append(copy.deepcopy(option))

    # F699: flanged deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_f600_series_f699_size_9_mm_id_20_mm_od_6_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_F600_series_F699_size_9_mm_id_20_mm_od_6_mm_depth'
    option['size'] = 'F699'
    option['series'] = 'F600'
    option['family'] = 'flanged_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 9.0
    option['dimensions']['outside'] = 20.0
    option['dimensions']['width'] = 6.0
    option['dimensions']['flange_diameter'] = 23.0
    option['dimensions']['flange_thickness'] = 1.5
    option['dimension_authority'] = 'manufacturer_checked'
    option['sources'] = ['https://koyo.jtekt.co.jp/en/products/detail/print.php?pno=F699']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'flanged_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 10
    option['internal_geometry']['balls_per_row'] = 10
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 9.0
    option['internal_geometry']['parameters']['outside'] = 20.0
    option['internal_geometry']['parameters']['width'] = 6.0
    option['internal_geometry']['parameters']['edge'] = 0.32999999999999996
    option['internal_geometry']['parameters']['pitch_radius'] = 7.25
    option['internal_geometry']['parameters']['ball_radius'] = 1.54
    option['internal_geometry']['parameters']['groove_radius'] = 1.5785
    option['internal_geometry']['parameters']['inner_shoulder'] = 6.2952
    option['internal_geometry']['parameters']['outer_shoulder'] = 8.2048
    option['internal_geometry']['parameters']['cage_half_width'] = 0.8470000000000001
    option['internal_geometry']['parameters']['cage_low'] = 1.4629999999999999
    option['internal_geometry']['parameters']['cage_high'] = 1.771
    option['internal_geometry']['parameters']['window_radius'] = 0.7392
    option['internal_geometry']['parameters']['flange_diameter'] = 23.0
    option['internal_geometry']['parameters']['flange_thickness'] = 1.5
    option['internal_geometry']['parameters']['flange_edge'] = 0.22499999999999998
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '9'
    options.append(copy.deepcopy(option))

    # MR104: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_mr_series_mr104_size_4_mm_id_10_mm_od_4_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_MR_series_MR104_size_4_mm_id_10_mm_od_4_mm_depth'
    option['size'] = 'MR104'
    option['series'] = 'MR'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 4.0
    option['dimensions']['outside'] = 10.0
    option['dimensions']['width'] = 4.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 9
    option['internal_geometry']['balls_per_row'] = 9
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 4.0
    option['internal_geometry']['parameters']['outside'] = 10.0
    option['internal_geometry']['parameters']['width'] = 4.0
    option['internal_geometry']['parameters']['edge'] = 0.18
    option['internal_geometry']['parameters']['pitch_radius'] = 3.5
    option['internal_geometry']['parameters']['ball_radius'] = 0.8400000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 0.8610000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 2.9792
    option['internal_geometry']['parameters']['outer_shoulder'] = 4.0208
    option['internal_geometry']['parameters']['cage_half_width'] = 0.4620000000000001
    option['internal_geometry']['parameters']['cage_low'] = 0.798
    option['internal_geometry']['parameters']['cage_high'] = 0.966
    option['internal_geometry']['parameters']['window_radius'] = 0.4032
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1'
    options.append(copy.deepcopy(option))

    # MR105: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_mr_series_mr105_size_5_mm_id_10_mm_od_4_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_MR_series_MR105_size_5_mm_id_10_mm_od_4_mm_depth'
    option['size'] = 'MR105'
    option['series'] = 'MR'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 5.0
    option['dimensions']['outside'] = 10.0
    option['dimensions']['width'] = 4.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 12
    option['internal_geometry']['balls_per_row'] = 12
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 5.0
    option['internal_geometry']['parameters']['outside'] = 10.0
    option['internal_geometry']['parameters']['width'] = 4.0
    option['internal_geometry']['parameters']['edge'] = 0.15
    option['internal_geometry']['parameters']['pitch_radius'] = 3.75
    option['internal_geometry']['parameters']['ball_radius'] = 0.7000000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 0.7175
    option['internal_geometry']['parameters']['inner_shoulder'] = 3.316
    option['internal_geometry']['parameters']['outer_shoulder'] = 4.184
    option['internal_geometry']['parameters']['cage_half_width'] = 0.38500000000000006
    option['internal_geometry']['parameters']['cage_low'] = 0.665
    option['internal_geometry']['parameters']['cage_high'] = 0.805
    option['internal_geometry']['parameters']['window_radius'] = 0.336
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1'
    options.append(copy.deepcopy(option))

    # MR106: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_mr_series_mr106_size_6_mm_id_10_mm_od_3_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_MR_series_MR106_size_6_mm_id_10_mm_od_3_mm_depth'
    option['size'] = 'MR106'
    option['series'] = 'MR'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 6.0
    option['dimensions']['outside'] = 10.0
    option['dimensions']['width'] = 3.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 16
    option['internal_geometry']['balls_per_row'] = 16
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 6.0
    option['internal_geometry']['parameters']['outside'] = 10.0
    option['internal_geometry']['parameters']['width'] = 3.0
    option['internal_geometry']['parameters']['edge'] = 0.12
    option['internal_geometry']['parameters']['pitch_radius'] = 4.0
    option['internal_geometry']['parameters']['ball_radius'] = 0.56
    option['internal_geometry']['parameters']['groove_radius'] = 0.5740000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 3.6528
    option['internal_geometry']['parameters']['outer_shoulder'] = 4.3472
    option['internal_geometry']['parameters']['cage_half_width'] = 0.30800000000000005
    option['internal_geometry']['parameters']['cage_low'] = 0.532
    option['internal_geometry']['parameters']['cage_high'] = 0.644
    option['internal_geometry']['parameters']['window_radius'] = 0.26880000000000004
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1'
    options.append(copy.deepcopy(option))

    # MR117: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_mr_series_mr117_size_7_mm_id_11_mm_od_3_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_MR_series_MR117_size_7_mm_id_11_mm_od_3_mm_depth'
    option['size'] = 'MR117'
    option['series'] = 'MR'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 7.0
    option['dimensions']['outside'] = 11.0
    option['dimensions']['width'] = 3.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 18
    option['internal_geometry']['balls_per_row'] = 18
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 7.0
    option['internal_geometry']['parameters']['outside'] = 11.0
    option['internal_geometry']['parameters']['width'] = 3.0
    option['internal_geometry']['parameters']['edge'] = 0.12
    option['internal_geometry']['parameters']['pitch_radius'] = 4.5
    option['internal_geometry']['parameters']['ball_radius'] = 0.56
    option['internal_geometry']['parameters']['groove_radius'] = 0.5740000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 4.1528
    option['internal_geometry']['parameters']['outer_shoulder'] = 4.8472
    option['internal_geometry']['parameters']['cage_half_width'] = 0.30800000000000005
    option['internal_geometry']['parameters']['cage_low'] = 0.532
    option['internal_geometry']['parameters']['cage_high'] = 0.644
    option['internal_geometry']['parameters']['window_radius'] = 0.26880000000000004
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1'
    options.append(copy.deepcopy(option))

    # MR126: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_mr_series_mr126_size_6_mm_id_12_mm_od_4_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_MR_series_MR126_size_6_mm_id_12_mm_od_4_mm_depth'
    option['size'] = 'MR126'
    option['series'] = 'MR'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 6.0
    option['dimensions']['outside'] = 12.0
    option['dimensions']['width'] = 4.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 12
    option['internal_geometry']['balls_per_row'] = 12
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 6.0
    option['internal_geometry']['parameters']['outside'] = 12.0
    option['internal_geometry']['parameters']['width'] = 4.0
    option['internal_geometry']['parameters']['edge'] = 0.18
    option['internal_geometry']['parameters']['pitch_radius'] = 4.5
    option['internal_geometry']['parameters']['ball_radius'] = 0.8400000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 0.8610000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 3.9792
    option['internal_geometry']['parameters']['outer_shoulder'] = 5.0208
    option['internal_geometry']['parameters']['cage_half_width'] = 0.4620000000000001
    option['internal_geometry']['parameters']['cage_low'] = 0.798
    option['internal_geometry']['parameters']['cage_high'] = 0.966
    option['internal_geometry']['parameters']['window_radius'] = 0.4032
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1'
    options.append(copy.deepcopy(option))

    # MR128: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_mr_series_mr128_size_8_mm_id_12_mm_od_3.5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_MR_series_MR128_size_8_mm_id_12_mm_od_3_5_mm_depth'
    option['size'] = 'MR128'
    option['series'] = 'MR'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 8.0
    option['dimensions']['outside'] = 12.0
    option['dimensions']['width'] = 3.5
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 20
    option['internal_geometry']['balls_per_row'] = 20
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 8.0
    option['internal_geometry']['parameters']['outside'] = 12.0
    option['internal_geometry']['parameters']['width'] = 3.5
    option['internal_geometry']['parameters']['edge'] = 0.12
    option['internal_geometry']['parameters']['pitch_radius'] = 5.0
    option['internal_geometry']['parameters']['ball_radius'] = 0.56
    option['internal_geometry']['parameters']['groove_radius'] = 0.5740000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 4.6528
    option['internal_geometry']['parameters']['outer_shoulder'] = 5.3472
    option['internal_geometry']['parameters']['cage_half_width'] = 0.30800000000000005
    option['internal_geometry']['parameters']['cage_low'] = 0.532
    option['internal_geometry']['parameters']['cage_high'] = 0.644
    option['internal_geometry']['parameters']['window_radius'] = 0.26880000000000004
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1'
    options.append(copy.deepcopy(option))

    # MR137: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_mr_series_mr137_size_7_mm_id_13_mm_od_4_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_MR_series_MR137_size_7_mm_id_13_mm_od_4_mm_depth'
    option['size'] = 'MR137'
    option['series'] = 'MR'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 7.0
    option['dimensions']['outside'] = 13.0
    option['dimensions']['width'] = 4.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 13
    option['internal_geometry']['balls_per_row'] = 13
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 7.0
    option['internal_geometry']['parameters']['outside'] = 13.0
    option['internal_geometry']['parameters']['width'] = 4.0
    option['internal_geometry']['parameters']['edge'] = 0.18
    option['internal_geometry']['parameters']['pitch_radius'] = 5.0
    option['internal_geometry']['parameters']['ball_radius'] = 0.8400000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 0.8610000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 4.4792
    option['internal_geometry']['parameters']['outer_shoulder'] = 5.5208
    option['internal_geometry']['parameters']['cage_half_width'] = 0.4620000000000001
    option['internal_geometry']['parameters']['cage_low'] = 0.798
    option['internal_geometry']['parameters']['cage_high'] = 0.966
    option['internal_geometry']['parameters']['window_radius'] = 0.4032
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '2'
    options.append(copy.deepcopy(option))

    # MR148: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_mr_series_mr148_size_8_mm_id_14_mm_od_4_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_MR_series_MR148_size_8_mm_id_14_mm_od_4_mm_depth'
    option['size'] = 'MR148'
    option['series'] = 'MR'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 8.0
    option['dimensions']['outside'] = 14.0
    option['dimensions']['width'] = 4.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 15
    option['internal_geometry']['balls_per_row'] = 15
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 8.0
    option['internal_geometry']['parameters']['outside'] = 14.0
    option['internal_geometry']['parameters']['width'] = 4.0
    option['internal_geometry']['parameters']['edge'] = 0.18
    option['internal_geometry']['parameters']['pitch_radius'] = 5.5
    option['internal_geometry']['parameters']['ball_radius'] = 0.8400000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 0.8610000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 4.9792
    option['internal_geometry']['parameters']['outer_shoulder'] = 6.0208
    option['internal_geometry']['parameters']['cage_half_width'] = 0.4620000000000001
    option['internal_geometry']['parameters']['cage_low'] = 0.798
    option['internal_geometry']['parameters']['cage_high'] = 0.966
    option['internal_geometry']['parameters']['window_radius'] = 0.4032
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '2'
    options.append(copy.deepcopy(option))

    # MR31: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_mr_series_mr31_size_1_mm_id_3_mm_od_1.5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_MR_series_MR31_size_1_mm_id_3_mm_od_1_5_mm_depth'
    option['size'] = 'MR31'
    option['series'] = 'MR'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 1.0
    option['dimensions']['outside'] = 3.0
    option['dimensions']['width'] = 1.5
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 1.0
    option['internal_geometry']['parameters']['outside'] = 3.0
    option['internal_geometry']['parameters']['width'] = 1.5
    option['internal_geometry']['parameters']['edge'] = 0.06
    option['internal_geometry']['parameters']['pitch_radius'] = 1.0
    option['internal_geometry']['parameters']['ball_radius'] = 0.28
    option['internal_geometry']['parameters']['groove_radius'] = 0.28700000000000003
    option['internal_geometry']['parameters']['inner_shoulder'] = 0.8264
    option['internal_geometry']['parameters']['outer_shoulder'] = 1.1736
    option['internal_geometry']['parameters']['cage_half_width'] = 0.15400000000000003
    option['internal_geometry']['parameters']['cage_low'] = 0.266
    option['internal_geometry']['parameters']['cage_high'] = 0.322
    option['internal_geometry']['parameters']['window_radius'] = 0.13440000000000002
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '0'
    options.append(copy.deepcopy(option))

    # MR41: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_mr_series_mr41_size_1.2_mm_id_4_mm_od_2.5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_MR_series_MR41_size_1_2_mm_id_4_mm_od_2_5_mm_depth'
    option['size'] = 'MR41'
    option['series'] = 'MR'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 1.2
    option['dimensions']['outside'] = 4.0
    option['dimensions']['width'] = 2.5
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 7
    option['internal_geometry']['balls_per_row'] = 7
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 1.2
    option['internal_geometry']['parameters']['outside'] = 4.0
    option['internal_geometry']['parameters']['width'] = 2.5
    option['internal_geometry']['parameters']['edge'] = 0.08399999999999999
    option['internal_geometry']['parameters']['pitch_radius'] = 1.3
    option['internal_geometry']['parameters']['ball_radius'] = 0.392
    option['internal_geometry']['parameters']['groove_radius'] = 0.4018
    option['internal_geometry']['parameters']['inner_shoulder'] = 1.0569600000000001
    option['internal_geometry']['parameters']['outer_shoulder'] = 1.54304
    option['internal_geometry']['parameters']['cage_half_width'] = 0.2156
    option['internal_geometry']['parameters']['cage_low'] = 0.3724
    option['internal_geometry']['parameters']['cage_high'] = 0.4508
    option['internal_geometry']['parameters']['window_radius'] = 0.18816
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '0'
    options.append(copy.deepcopy(option))

    # MR52: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_mr_series_mr52_size_2_mm_id_5_mm_od_2.5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_MR_series_MR52_size_2_mm_id_5_mm_od_2_5_mm_depth'
    option['size'] = 'MR52'
    option['series'] = 'MR'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 2.0
    option['dimensions']['outside'] = 5.0
    option['dimensions']['width'] = 2.5
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 9
    option['internal_geometry']['balls_per_row'] = 9
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 2.0
    option['internal_geometry']['parameters']['outside'] = 5.0
    option['internal_geometry']['parameters']['width'] = 2.5
    option['internal_geometry']['parameters']['edge'] = 0.09
    option['internal_geometry']['parameters']['pitch_radius'] = 1.75
    option['internal_geometry']['parameters']['ball_radius'] = 0.42000000000000004
    option['internal_geometry']['parameters']['groove_radius'] = 0.43050000000000005
    option['internal_geometry']['parameters']['inner_shoulder'] = 1.4896
    option['internal_geometry']['parameters']['outer_shoulder'] = 2.0104
    option['internal_geometry']['parameters']['cage_half_width'] = 0.23100000000000004
    option['internal_geometry']['parameters']['cage_low'] = 0.399
    option['internal_geometry']['parameters']['cage_high'] = 0.483
    option['internal_geometry']['parameters']['window_radius'] = 0.2016
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '0'
    options.append(copy.deepcopy(option))

    # MR62: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_mr_series_mr62_size_2_mm_id_6_mm_od_2.5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_MR_series_MR62_size_2_mm_id_6_mm_od_2_5_mm_depth'
    option['size'] = 'MR62'
    option['series'] = 'MR'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 2.0
    option['dimensions']['outside'] = 6.0
    option['dimensions']['width'] = 2.5
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 2.0
    option['internal_geometry']['parameters']['outside'] = 6.0
    option['internal_geometry']['parameters']['width'] = 2.5
    option['internal_geometry']['parameters']['edge'] = 0.12
    option['internal_geometry']['parameters']['pitch_radius'] = 2.0
    option['internal_geometry']['parameters']['ball_radius'] = 0.56
    option['internal_geometry']['parameters']['groove_radius'] = 0.5740000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 1.6528
    option['internal_geometry']['parameters']['outer_shoulder'] = 2.3472
    option['internal_geometry']['parameters']['cage_half_width'] = 0.30800000000000005
    option['internal_geometry']['parameters']['cage_low'] = 0.532
    option['internal_geometry']['parameters']['cage_high'] = 0.644
    option['internal_geometry']['parameters']['window_radius'] = 0.26880000000000004
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '0'
    options.append(copy.deepcopy(option))

    # MR63: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_mr_series_mr63_size_3_mm_id_6_mm_od_2.5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_MR_series_MR63_size_3_mm_id_6_mm_od_2_5_mm_depth'
    option['size'] = 'MR63'
    option['series'] = 'MR'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 3.0
    option['dimensions']['outside'] = 6.0
    option['dimensions']['width'] = 2.5
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 12
    option['internal_geometry']['balls_per_row'] = 12
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 3.0
    option['internal_geometry']['parameters']['outside'] = 6.0
    option['internal_geometry']['parameters']['width'] = 2.5
    option['internal_geometry']['parameters']['edge'] = 0.09
    option['internal_geometry']['parameters']['pitch_radius'] = 2.25
    option['internal_geometry']['parameters']['ball_radius'] = 0.42000000000000004
    option['internal_geometry']['parameters']['groove_radius'] = 0.43050000000000005
    option['internal_geometry']['parameters']['inner_shoulder'] = 1.9896
    option['internal_geometry']['parameters']['outer_shoulder'] = 2.5104
    option['internal_geometry']['parameters']['cage_half_width'] = 0.23100000000000004
    option['internal_geometry']['parameters']['cage_low'] = 0.399
    option['internal_geometry']['parameters']['cage_high'] = 0.483
    option['internal_geometry']['parameters']['window_radius'] = 0.2016
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '0'
    options.append(copy.deepcopy(option))

    # MR72: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_mr_series_mr72_size_2_mm_id_7_mm_od_3_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_MR_series_MR72_size_2_mm_id_7_mm_od_3_mm_depth'
    option['size'] = 'MR72'
    option['series'] = 'MR'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 2.0
    option['dimensions']['outside'] = 7.0
    option['dimensions']['width'] = 3.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 7
    option['internal_geometry']['balls_per_row'] = 7
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 2.0
    option['internal_geometry']['parameters']['outside'] = 7.0
    option['internal_geometry']['parameters']['width'] = 3.0
    option['internal_geometry']['parameters']['edge'] = 0.15
    option['internal_geometry']['parameters']['pitch_radius'] = 2.25
    option['internal_geometry']['parameters']['ball_radius'] = 0.7000000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 0.7175
    option['internal_geometry']['parameters']['inner_shoulder'] = 1.8159999999999998
    option['internal_geometry']['parameters']['outer_shoulder'] = 2.684
    option['internal_geometry']['parameters']['cage_half_width'] = 0.38500000000000006
    option['internal_geometry']['parameters']['cage_low'] = 0.665
    option['internal_geometry']['parameters']['cage_high'] = 0.805
    option['internal_geometry']['parameters']['window_radius'] = 0.336
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '0'
    options.append(copy.deepcopy(option))

    # MR74: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_mr_series_mr74_size_4_mm_id_7_mm_od_2.5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_MR_series_MR74_size_4_mm_id_7_mm_od_2_5_mm_depth'
    option['size'] = 'MR74'
    option['series'] = 'MR'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 4.0
    option['dimensions']['outside'] = 7.0
    option['dimensions']['width'] = 2.5
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 15
    option['internal_geometry']['balls_per_row'] = 15
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 4.0
    option['internal_geometry']['parameters']['outside'] = 7.0
    option['internal_geometry']['parameters']['width'] = 2.5
    option['internal_geometry']['parameters']['edge'] = 0.09
    option['internal_geometry']['parameters']['pitch_radius'] = 2.75
    option['internal_geometry']['parameters']['ball_radius'] = 0.42000000000000004
    option['internal_geometry']['parameters']['groove_radius'] = 0.43050000000000005
    option['internal_geometry']['parameters']['inner_shoulder'] = 2.4896
    option['internal_geometry']['parameters']['outer_shoulder'] = 3.0104
    option['internal_geometry']['parameters']['cage_half_width'] = 0.23100000000000004
    option['internal_geometry']['parameters']['cage_low'] = 0.399
    option['internal_geometry']['parameters']['cage_high'] = 0.483
    option['internal_geometry']['parameters']['window_radius'] = 0.2016
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '0'
    options.append(copy.deepcopy(option))

    # MR82: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_mr_series_mr82_size_2.5_mm_id_8_mm_od_3_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_MR_series_MR82_size_2_5_mm_id_8_mm_od_3_mm_depth'
    option['size'] = 'MR82'
    option['series'] = 'MR'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 2.5
    option['dimensions']['outside'] = 8.0
    option['dimensions']['width'] = 3.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 7
    option['internal_geometry']['balls_per_row'] = 7
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 2.5
    option['internal_geometry']['parameters']['outside'] = 8.0
    option['internal_geometry']['parameters']['width'] = 3.0
    option['internal_geometry']['parameters']['edge'] = 0.16499999999999998
    option['internal_geometry']['parameters']['pitch_radius'] = 2.625
    option['internal_geometry']['parameters']['ball_radius'] = 0.77
    option['internal_geometry']['parameters']['groove_radius'] = 0.78925
    option['internal_geometry']['parameters']['inner_shoulder'] = 2.1476
    option['internal_geometry']['parameters']['outer_shoulder'] = 3.1024
    option['internal_geometry']['parameters']['cage_half_width'] = 0.42350000000000004
    option['internal_geometry']['parameters']['cage_low'] = 0.7314999999999999
    option['internal_geometry']['parameters']['cage_high'] = 0.8855
    option['internal_geometry']['parameters']['window_radius'] = 0.3696
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1'
    options.append(copy.deepcopy(option))

    # MR83: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_mr_series_mr83_size_3_mm_id_8_mm_od_3_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_MR_series_MR83_size_3_mm_id_8_mm_od_3_mm_depth'
    option['size'] = 'MR83'
    option['series'] = 'MR'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 3.0
    option['dimensions']['outside'] = 8.0
    option['dimensions']['width'] = 3.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 3.0
    option['internal_geometry']['parameters']['outside'] = 8.0
    option['internal_geometry']['parameters']['width'] = 3.0
    option['internal_geometry']['parameters']['edge'] = 0.15
    option['internal_geometry']['parameters']['pitch_radius'] = 2.75
    option['internal_geometry']['parameters']['ball_radius'] = 0.7000000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 0.7175
    option['internal_geometry']['parameters']['inner_shoulder'] = 2.316
    option['internal_geometry']['parameters']['outer_shoulder'] = 3.184
    option['internal_geometry']['parameters']['cage_half_width'] = 0.38500000000000006
    option['internal_geometry']['parameters']['cage_low'] = 0.665
    option['internal_geometry']['parameters']['cage_high'] = 0.805
    option['internal_geometry']['parameters']['window_radius'] = 0.336
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1'
    options.append(copy.deepcopy(option))

    # MR84: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_mr_series_mr84_size_4_mm_id_8_mm_od_3_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_MR_series_MR84_size_4_mm_id_8_mm_od_3_mm_depth'
    option['size'] = 'MR84'
    option['series'] = 'MR'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 4.0
    option['dimensions']['outside'] = 8.0
    option['dimensions']['width'] = 3.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 12
    option['internal_geometry']['balls_per_row'] = 12
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 4.0
    option['internal_geometry']['parameters']['outside'] = 8.0
    option['internal_geometry']['parameters']['width'] = 3.0
    option['internal_geometry']['parameters']['edge'] = 0.12
    option['internal_geometry']['parameters']['pitch_radius'] = 3.0
    option['internal_geometry']['parameters']['ball_radius'] = 0.56
    option['internal_geometry']['parameters']['groove_radius'] = 0.5740000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 2.6528
    option['internal_geometry']['parameters']['outer_shoulder'] = 3.3472
    option['internal_geometry']['parameters']['cage_half_width'] = 0.30800000000000005
    option['internal_geometry']['parameters']['cage_low'] = 0.532
    option['internal_geometry']['parameters']['cage_high'] = 0.644
    option['internal_geometry']['parameters']['window_radius'] = 0.26880000000000004
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '0'
    options.append(copy.deepcopy(option))

    # MR85: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_mr_series_mr85_size_5_mm_id_8_mm_od_2.5_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_MR_series_MR85_size_5_mm_id_8_mm_od_2_5_mm_depth'
    option['size'] = 'MR85'
    option['series'] = 'MR'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 5.0
    option['dimensions']['outside'] = 8.0
    option['dimensions']['width'] = 2.5
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 17
    option['internal_geometry']['balls_per_row'] = 17
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 5.0
    option['internal_geometry']['parameters']['outside'] = 8.0
    option['internal_geometry']['parameters']['width'] = 2.5
    option['internal_geometry']['parameters']['edge'] = 0.09
    option['internal_geometry']['parameters']['pitch_radius'] = 3.25
    option['internal_geometry']['parameters']['ball_radius'] = 0.42000000000000004
    option['internal_geometry']['parameters']['groove_radius'] = 0.43050000000000005
    option['internal_geometry']['parameters']['inner_shoulder'] = 2.9896
    option['internal_geometry']['parameters']['outer_shoulder'] = 3.5104
    option['internal_geometry']['parameters']['cage_half_width'] = 0.23100000000000004
    option['internal_geometry']['parameters']['cage_low'] = 0.399
    option['internal_geometry']['parameters']['cage_high'] = 0.483
    option['internal_geometry']['parameters']['window_radius'] = 0.2016
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '0'
    options.append(copy.deepcopy(option))

    # MR93: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_mr_series_mr93_size_3_mm_id_9_mm_od_4_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_MR_series_MR93_size_3_mm_id_9_mm_od_4_mm_depth'
    option['size'] = 'MR93'
    option['series'] = 'MR'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 3.0
    option['dimensions']['outside'] = 9.0
    option['dimensions']['width'] = 4.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 8
    option['internal_geometry']['balls_per_row'] = 8
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 3.0
    option['internal_geometry']['parameters']['outside'] = 9.0
    option['internal_geometry']['parameters']['width'] = 4.0
    option['internal_geometry']['parameters']['edge'] = 0.18
    option['internal_geometry']['parameters']['pitch_radius'] = 3.0
    option['internal_geometry']['parameters']['ball_radius'] = 0.8400000000000001
    option['internal_geometry']['parameters']['groove_radius'] = 0.8610000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 2.4792
    option['internal_geometry']['parameters']['outer_shoulder'] = 3.5208
    option['internal_geometry']['parameters']['cage_half_width'] = 0.4620000000000001
    option['internal_geometry']['parameters']['cage_low'] = 0.798
    option['internal_geometry']['parameters']['cage_high'] = 0.966
    option['internal_geometry']['parameters']['window_radius'] = 0.4032
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '1'
    options.append(copy.deepcopy(option))

    # MR95: single row deep groove
    option = {}
    option['oomp_id'] = 'hardware_bearing_mr_series_mr95_size_5_mm_id_9_mm_od_3_mm_depth'
    option['legacy_source_id'] = 'hardware_bearing_MR_series_MR95_size_5_mm_id_9_mm_od_3_mm_depth'
    option['size'] = 'MR95'
    option['series'] = 'MR'
    option['family'] = 'single_row_deep_groove'
    option['dimensions'] = {}
    option['dimensions']['bore'] = 5.0
    option['dimensions']['outside'] = 9.0
    option['dimensions']['width'] = 3.0
    option['dimension_authority'] = 'local_catalogue_only'
    option['sources'] = ['source_file/dimension/oomp_bearing_sizes.csv']
    option['source_checked'] = '2026-10-27'
    option['internal_geometry'] = {}
    option['internal_geometry']['family'] = 'single_row_deep_groove'
    option['internal_geometry']['closure'] = 'open'
    option['internal_geometry']['ball_count'] = 14
    option['internal_geometry']['balls_per_row'] = 14
    option['internal_geometry']['row_count'] = 1
    option['internal_geometry']['parameters'] = {}
    option['internal_geometry']['parameters']['bore'] = 5.0
    option['internal_geometry']['parameters']['outside'] = 9.0
    option['internal_geometry']['parameters']['width'] = 3.0
    option['internal_geometry']['parameters']['edge'] = 0.12
    option['internal_geometry']['parameters']['pitch_radius'] = 3.5
    option['internal_geometry']['parameters']['ball_radius'] = 0.56
    option['internal_geometry']['parameters']['groove_radius'] = 0.5740000000000001
    option['internal_geometry']['parameters']['inner_shoulder'] = 3.1528
    option['internal_geometry']['parameters']['outer_shoulder'] = 3.8472
    option['internal_geometry']['parameters']['cage_half_width'] = 0.30800000000000005
    option['internal_geometry']['parameters']['cage_low'] = 0.532
    option['internal_geometry']['parameters']['cage_high'] = 0.644
    option['internal_geometry']['parameters']['window_radius'] = 0.26880000000000004
    option['internal_geometry']['contact_angle_authority'] = 'not_applicable'
    option['internal_geometry']['ball_specification'] = 'illustrative'
    option['model_note'] = ('Nominal presentation model. Raceways, pitch circle, chamfers and retainer geometry '
     'are illustrative; ball count/diameter are illustrative unless individually sourced. '
     'Not a manufacturer reconstruction, load-rating model or manufacturing/tolerance '
     'certification. Unspecified closure is presented open. The mesh shows open races and '
     'balls; retainers, seals and exact contact surfaces are omitted.')
    option['catalogue_metadata'] = {}
    option['catalogue_metadata']['weight'] = '0'
    options.append(copy.deepcopy(option))

    return options
