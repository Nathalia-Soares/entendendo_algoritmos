def finding_key(box):
    for item in box:
        if item.is_a_box():
            finding_key(item)
        elif item.is_a_key():
            print("Found the key!")