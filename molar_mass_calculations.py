molar_mass_list = []
easy_list = []
total_mass = 0
atomic_masses = [
    1.01, 4.00, 6.94, 9.01, 10.81, 12.01, 14.01, 16.00, 19.00, 20.18,
    22.99, 24.31, 26.98, 28.09, 30.97, 32.07, 35.45, 39.95, 39.10, 40.08,
    44.96, 47.87, 50.94, 51.99, 54.94, 55.85, 58.93, 58.69, 63.55, 65.38,
    69.72, 72.63, 74.92, 78.96, 79.90, 83.80, 85.47, 87.62, 88.91, 91.22,
    92.91, 95.95, 98.00, 101.07, 102.91, 106.42, 107.87, 112.41, 114.82, 118.71,
    121.76, 127.60, 126.90, 131.29, 132.91, 137.33, 138.91, 140.12, 140.91, 144.24,
    145.00, 150.36, 151.96, 157.25, 158.93, 162.50, 164.93, 167.26, 168.93, 173.04,
    174.97, 178.49, 180.95, 183.84, 186.21, 190.23, 192.22, 195.08, 196.97, 200.59,
    204.38, 207.20, 208.98, 209.00, 210.00, 222.00, 223.00, 226.00, 227.00, 232.04,
    231.04, 238.03, 237.00, 244.00, 243.00, 247.00, 247.00, 251.00, 252.00, 257.00,
    258.00, 259.00, 262.00, 267.00, 270.00, 271.00, 270.00, 277.00, 276.00, 281.00,
    282.00, 285.00, 286.00, 289.00, 290.00, 293.00, 294.00, 294.00
]
already_convert_mass = False
already_convert_moles = False

element_names = [
    "HYDROGEN", "HELIUM", "LITHIUM", "BERYLLIUM", "BORON", "CARBON", "NITROGEN", "OXYGEN", "FLUORINE", "NEON",
    "SODIUM", "MAGNESIUM", "ALUMINUM", "SILICON", "PHOSPHORUS", "SULFUR", "CHLORINE", "ARGON", "POTASSIUM", "CALCIUM",
    "SCANDIUM", "TITANIUM", "VANADIUM", "CHROMIUM", "MANGANESE", "IRON", "COBALT", "NICKEL", "COPPER", "ZINC",
    "GALLIUM", "GERMANIUM", "ARSENIC", "SELENIUM", "BROMINE", "KRYPTON", "RUBIDIUM", "STRONTIUM", "YTTRIUM", "ZIRCONIUM",
    "NIOBIUM", "MOLYBDENUM", "TECHNETIUM", "RUTHENIUM", "RHODIUM", "PALLADIUM", "SILVER", "CADMIUM", "INDIUM", "TIN",
    "ANTIMONY", "TELLURIUM", "IODINE", "XENON", "CESIUM", "BARIUM", "LANTHANUM", "CERIUM", "PRASEODYMIUM", "NEODYMIUM",
    "PROMETHIUM", "SAMARIUM", "EUROPIUM", "GADOLINIUM", "TERBIUM", "DYSPROSIUM", "HOLMIUM", "ERBIUM", "THULIUM", "YTTERBIUM",
    "LUTETIUM", "HAFNIUM", "TANTALUM", "TUNGSTEN", "RHENIUM", "OSMIUM", "IRIDIUM", "PLATINUM", "GOLD", "MERCURY",
    "THALLIUM", "LEAD", "BISMUTH", "POLONIUM", "ASTATINE", "RADON", "FRANCIUM", "RADIUM", "ACTINIUM", "THORIUM",
    "PROTACTINIUM", "URANIUM", "NEPTUNIUM", "PLUTONIUM", "AMERICIUM", "CURIUM", "BERKELIUM", "CALIFORNIUM", "EINSTEINIUM", "FERMIUM",
    "MENDELEVIUM", "NOBELIUM", "LAWRENCIUM", "RUTHERFORDIUM", "DUBNIUM", "SEABORGIUM", "BOHRIUM", "HASSIUM", "MEITNERIUM", "DARMSTADTIUM",
    "ROENTGENIUM", "COPERNICIUM", "NIHONIUM", "FLEROVIUM", "MOSCOVIUM", "LIVERMORIUM", "TENNESSINE", "OGANESSON"
]
def molar_mass_calc():
    global total_mass
    global molar_mass
    iter = int(input("How many elements are there: "))
    for i in range(0, iter):
        list_nums = list(map(int, str(i)))
        if list_nums[len(list_nums) - 1] + 1 == 1:
            name = input("What is the name of the " + str(i + 1) + "st element: ")
        elif list_nums[len(list_nums) - 1] + 1 == 2:
            name = input("What is the name of the " + str(i + 1) + "nd element: ")
        elif list_nums[len(list_nums) - 1] + 1 == 3:
            name = input("What is the name of the " + str(i + 1) + "rd element: ")
        else:
            name = input("What is the name of the " + str(i + 1) + "th element: ")
        element_nums = int(input("How many of this element is in the compound/molecule: "))
        element_index = element_names.index(name.upper())
        molar_mass_list.append(element_nums * atomic_masses[element_index])
        easy_list.append(
            name.capitalize() + ": " + str(element_nums) + "*" + str(atomic_masses[element_index]) + " -> " + str(
                (element_nums * atomic_masses[element_index])))
    for j in range(0, len(molar_mass_list)):
        total_mass += molar_mass_list[j]

    for k in range(0, len(easy_list)):
        print(easy_list[k])

    molar_mass = round(total_mass, 5)
    print(molar_mass)

def convert_moles_grams():
    global nums_total_moles
    global already_convert_moles
    global molar_mass
    global new_moles
    molar_mass_calc()
    print("\n")
    if already_convert_moles == False:
        moles_nums = float(input("How many moles of the compound/element/molecule is there: "))
    else:
        moles_nums = nums_total_moles
    new_moles = round((moles_nums * molar_mass), 5)

def convert_grams_moles():
    global molar_mass
    global new_grams
    molar_mass_calc()
    print("\n")
    grams_compound = float(input("How many grams of the compound/element/molecule is there: "))
    new_grams = round((grams_compound/molar_mass), 5)

def convert_moles_particles():
    global already_convert_mass
    global nums_total_particles
    if already_convert_mass == False:
        nums_moles = float(input("How many moles of the substance is there: "))
    else:
        nums_moles = new_grams
    nums_total_particles = nums_moles*(6.02e23)

def convert_particles_moles():
    global nums_total_moles
    nums_particles = float(input("How many particles/atoms/molecules/formula units of the substance is there: "))
    nums_total_moles = nums_particles/(6.02e23)

def run_program():
    global convert_choice
    global convert_second_choice
    global convert_third_choice
    global already_convert_mass
    global already_convert_moles

    choice = input("What are you doing today (c for converting mass-moles, m for molar mass calculations, p for converting particles-mass, and r for converting moles-particles): ")

    if choice == "c":
        convert_choice = input("Are you converting moles to grams or grams to moles (m for moles->grams, g for grams->moles): ")
        if convert_choice == "m":
            convert_moles_grams()
            print(new_moles)
        elif convert_choice == "g":
            convert_grams_moles()
            print(new_grams)
        else:
            run_program()
    elif choice == "m":
        molar_mass_calc()
        print(molar_mass)
    elif choice == "p":
        convert_second_choice = input("Are you converting mass to particles or particles to mass (a for mass-> particles, b for particles-> mass): ")
        if convert_second_choice == "a":
            convert_grams_moles()
            already_convert_mass = True
            convert_moles_particles()
            print(nums_total_particles)
            already_convert_mass = False
        elif convert_second_choice == "b":
             convert_particles_moles()
             already_convert_moles = True
             convert_moles_grams()
             print(new_moles)
             already_convert_moles = False
        else:
            run_program()

    elif choice == "r":
        convert_third_choice = input("Are you converting particles to moles or moles to particles (pm for particles-> moles and mp for moles-> particles): ")
        if convert_third_choice == "pm":
            convert_particles_moles()
            print(nums_total_moles)
        elif convert_third_choice == "mp":
            convert_moles_particles()
            print(nums_total_particles)
        else:
            run_program()
    else:
        run_program()

run_program()