
import copy

from oomp_populate_helper import build_oomp_id, write_extras


def main(**kwargs):
    
    options = []
    #define single parts (take the default options add one with the extra details)
    option = {}
    

    if True:
        #source file source_file/oomp_bearing_sizes.csv
        #load from csv
        import csv
        with open("source_file/dimension/oomp_bearing_sizes.csv", 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                #sampple 
                #size,id,od,depth,weight,series
                #6000,10,26,8,19,6000
                option = {}
                option["size"] = row.get("size", "")
                option["id"] = row.get("id", "")    
                option["od"] = row.get("od", "")
                option["depth"] = row.get("width", "")
                option["width"] = row.get("width", "")
                option["weight"] = row.get("weight", "")
                option["series"] = row.get("series", "")
                options.append(option)



        
    
    #load from working_manual.yaml
    if False:
        with open("working_manual.yaml", 'r', encoding='utf-8') as file:
            import yaml
            data = yaml.safe_load(file)
            options_yaml = data.get("options", [])
            for option_yaml in options_yaml:
                options.append(option_yaml)

    
    ###### populate taxonomy details and oobb details
    if True:
        for option in options:            
            #format hardware_bearing_600_series_637_size_7_mm_id_26_mm_od_9_mm_depth
            option["taxonomy_1"] = f"hardware"
            option["taxonomy_2"] = f"bearing"
            series = option.get("series", "")
            option["taxonomy_3"] = f"{series}_series"
            size = option.get("size", "")
            option["taxonomy_4"] = f"{size}_size"
            id = option.get("id", "")
            option["taxonomy_5"] = f"{id}_mm_id"
            od = option.get("od", "")
            option["taxonomy_6"] = f"{od}_mm_od"
            depth = option.get("depth", "")
            option["taxonomy_7"] = f"{depth}_mm_depth"

    # Add mechanical drawing svg_details for each bearing
    for option in options:
        try:
            id_mm    = float(option.get("id",    0))
            od_mm    = float(option.get("od",    0))
            width_mm = float(option.get("width", 0))
        except (ValueError, TypeError):
            continue
        series_code = option.get("series", "")
        size_code   = option.get("size",   "")
        mech = {
            "svg_name":      "oomp_mech_drawing_hardware",
            "filename":      "working_mechanical_drawing",
            "hardware_type": "bearing",
            "part_title":    size_code,
            "part_series":   f"{series_code} SERIES BALL BEARING",
            "part_category": "HARDWARE / BEARING",
            "id_mm":         id_mm,
            "od_mm":         od_mm,
            "width_mm":      width_mm,
            "part_code":     "ISO 15 / DIN 625",
            "part_name":     build_oomp_id(option),
        }
        option["svg_details"] = mech

    #load the options into full list
    extras = []
    for option in options:
        extra = {}
        extra.update(option)
        extras.append(extra)

    
    ######### add notes from an id string
    import working_oomp_populate_extra_detail
    working_oomp_populate_extra_detail.main(extras=extras)


    write_extras(extras)



# Call main automatically
if __name__ == "__main__":
    main()
