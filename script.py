# Creating an empty string to store xml data
xml_data = ""

# Extracting Anime name and ID for using in xml entries
animenames = []
with open("export.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        if line[0] !=  "#":
            name = line.split("|")[0].strip()
            Id =  line.split("|")[1].strip().split("/")[-1]
            animenames.append([name,Id])

print("✅ Loading Text File")
print("✅ Extracting Data")

# Defining the xml structure
head = '<?xml version="1.0" encoding="UTF-8"?>\n<myanimelist>\n'
subhead = "\t<myinfo>\n\t\t<user_export_type>1</user_export_type>\n\t</myinfo>\n"
tail = "</myanimelist>"
entry_string = "\t<anime>\n\t\t<series_animedb_id>*****</series_animedb_id>\n\t\t<series_title>\n\t\t\t<![CDATA[ ##### ]]>\n\t\t</series_title>\n\t\t<my_watched_episodes>0</my_watched_episodes>\n\t\t<my_status>Plan to Watch</my_status>\n\t\t<update_on_import>1</update_on_import>\n\t</anime>\n"

print("✅ Creating XML structure")

# Creating the xml data
xml_data += head
xml_data += subhead
for  animename in animenames:
    entry_string_copy = entry_string
    entry_string_copy = entry_string_copy.replace("#####",animename[0])
    entry_string_copy = entry_string_copy.replace("*****",animename[1])
    xml_data += entry_string_copy
xml_data += tail

print("✅ Loading Data")

#  Writing the xml data to a file
save_path = "anime_data.xml"
with open(save_path, "w") as file:
    file.write(xml_data)

print(f"✅ Saving file at {save_path}")
print("\nEnjoy! ✌\n")

