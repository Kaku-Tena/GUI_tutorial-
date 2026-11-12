import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

#Saving User Info
user_info_frame = tkinter.LabelFrame(frame, text = "User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=20)

first_name_label = tkinter.Label(user_info_frame, text = "First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text = "Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text = "Title")
title_combobox = ttk.Combobox(user_info_frame, values = ["", "Mr", "Ms", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0 )

nationality_label = tkinter.Label(user_info_frame, text = "Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values = [
    "Afghan", "Albanian", "Algerian", "American", "Andorran",
    "Angolan", "Antiguan", "Argentine", "Armenian", "Australian",
    "Austrian", "Azerbaijani", "Bahamian", "Bahraini", "Bangladeshi",
    "Barbadian", "Belarusian", "Belgian", "Belizean", "Beninese",
    "Bhutanese", "Bolivian", "Bosnian", "Botswanan", "Brazilian",
    "British", "Bruneian", "Bulgarian", "Burkinabe", "Burmese",
    "Burundian", "Cambodian", "Cameroonian", "Canadian", "Cape Verdean",
    "Central African", "Chadian", "Chilean", "Chinese", "Colombian",
    "Comoran", "Congolese", "Costa Rican", "Croatian", "Cuban",
    "Cypriot", "Czech", "Danish", "Djiboutian", "Dominican",
    "Dutch", "East Timorese", "Ecuadorean", "Egyptian", "Emirati",
    "Equatorial Guinean", "Eritrean", "Estonian", "Eswatini",
    "Ethiopian", "Fijian", "Filipino", "Finnish", "French",
    "Gabonese", "Gambian", "Georgian", "German", "Ghanaian",
    "Greek", "Grenadian", "Guatemalan", "Guinean", "Guyanese",
    "Haitian", "Honduran", "Hungarian", "Icelandic", "Indian",
    "Indonesian", "Iranian", "Iraqi", "Irish", "Israeli",
    "Italian", "Ivorian", "Jamaican", "Japanese", "Jordanian",
    "Kazakh", "Kenyan", "Kiribati", "Kuwaiti", "Kyrgyz",
    "Lao", "Latvian", "Lebanese", "Lesotho", "Liberian",
    "Libyan", "Liechtensteiner", "Lithuanian", "Luxembourger",
    "Malagasy", "Malawian", "Malaysian", "Maldivian", "Malian",
    "Maltese", "Marshallese", "Mauritanian", "Mauritian", "Mexican",
    "Micronesian", "Moldovan", "Monégasque", "Mongolian", "Montenegrin",
    "Moroccan", "Mozambican", "Namibian", "Nauruan", "Nepalese",
    "New Zealander", "Nicaraguan", "Nigerien", "Nigerian", "North Korean",
    "North Macedonian", "Norwegian", "Omani", "Pakistani", "Palauan",
    "Palestinian", "Panamanian", "Papua New Guinean", "Paraguayan",
    "Peruvian", "Polish", "Portuguese", "Qatari", "Romanian",
    "Russian", "Rwandan", "Saint Lucian", "Salvadoran", "Samoan",
    "San Marinese", "Sao Tomean", "Saudi", "Senegalese", "Serbian",
    "Seychellois", "Sierra Leonean", "Singaporean", "Slovak",
    "Slovenian", "Solomon Islander", "Somali", "South African",
    "South Korean", "South Sudanese", "Spanish", "Sri Lankan",
    "Sudanese", "Surinamese", "Swedish", "Swiss", "Syrian",
    "Taiwanese", "Tajik", "Tanzanian", "Thai", "Togolese",
    "Tongan", "Trinidadian", "Tunisian", "Turkish", "Turkmen",
    "Tuvaluan", "Ugandan", "Ukrainian", "Uruguayan", "Uzbek",
    "Vanuatuan", "Venezuelan", "Vietnamese", "Yemeni", "Zambian",
    "Zimbabwean"
])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)


window.mainloop()