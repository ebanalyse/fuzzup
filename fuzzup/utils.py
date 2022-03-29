# flatten list
def flatten(x):
    flat_list = []
    for sublist in x:
        for item in sublist:
            flat_list.append(item)
    return flat_list

complist = [
  {
    "name": "ALDI Danmark ApS",
    "municipality": "Albertslund"
  },
  {
    "name": "FAKTA A/S",
    "municipality": "Albertslund"
  },
  {
    "name": "G4S SECURITY SERVICES A/S",
    "municipality": "Albertslund"
  },
  {
    "name": "COOP DANMARK A/S",
    "municipality": "Albertslund"
  },
  {
    "name": "KEOLIS DANMARK A/S",
    "municipality": "Albertslund"
  },
  {
    "name": "KEMP & LAURITZEN A/S",
    "municipality": "Albertslund"
  },
  {
    "name": "HB-CARE A/S",
    "municipality": "Albertslund"
  },
  {
    "name": "HOFFMANN A/S",
    "municipality": "Albertslund"
  },
  {
    "name": "NOBINA A/S",
    "municipality": "Albertslund"
  },
  {
    "name": "U.P.S. DANMARK A/S",
    "municipality": "Albertslund"
  },
  {
    "name": "CG JENSEN A/S",
    "municipality": "Albertslund"
  },
  {
    "name": "BRØDRENE A. & O. JOHANSEN A/S",
    "municipality": "Albertslund"
  },
  {
    "name": "WELLTEC A/S",
    "municipality": "Allerød"
  },
  {
    "name": "SUNDVIKAR ApS",
    "municipality": "Allerød"
  },
  {
    "name": "BURMEISTER & WAIN SCANDINAVIAN CONTRACTOR A/S",
    "municipality": "Allerød"
  },
  {
    "name": "Røde Kors Asylafdeling",
    "municipality": "Allerød"
  },
  {
    "name": "NIRAS A/S",
    "municipality": "Allerød"
  },
  {
    "name": "MATAS OPERATIONS A/S",
    "municipality": "Allerød"
  },
  {
    "name": "WIDEX A/S",
    "municipality": "Allerød"
  },
  {
    "name": "DPA MICROPHONES A/S",
    "municipality": "Allerød"
  },
  {
    "name": "Essity Denmark A/S",
    "municipality": "Allerød"
  },
  {
    "name": "LILLERØD BRUGSFORENING",
    "municipality": "Allerød"
  },
  {
    "name": "HEWLETT-PACKARD ApS",
    "municipality": "Allerød"
  },
  {
    "name": "WEIBEL SCIENTIFIC A/S",
    "municipality": "Allerød"
  },
  {
    "name": "City Container Danmark A/S",
    "municipality": "Allerød"
  },
  {
    "name": "FRITZ HANSEN A/S",
    "municipality": "Allerød"
  },
  {
    "name": "MATAS A/S",
    "municipality": "Allerød"
  },
  {
    "name": "BROEN A/S",
    "municipality": "Assens"
  },
  {
    "name": "CREMO INGREDIENTS A/S",
    "municipality": "Assens"
  },
  {
    "name": "MONTANA FURNITURE A/S",
    "municipality": "Assens"
  },
  {
    "name": "KiiltoClean A/S",
    "municipality": "Assens"
  },
  {
    "name": "AKTIESELSKABET BRYGGERIET VESTFYEN",
    "municipality": "Assens"
  },
  {
    "name": "Summerbird  A/S",
    "municipality": "Assens"
  },
  {
    "name": "GoSkov ApS",
    "municipality": "Assens"
  },
  {
    "name": "CABINPLANT A/S",
    "municipality": "Assens"
  },
  {
    "name": "DAN-FOAM ApS",
    "municipality": "Assens"
  },
  {
    "name": "SCANDINAVIAN TOBACCO GROUP ASSENS A/S",
    "municipality": "Assens"
  },
  {
    "name": "HARTMANNS A/S",
    "municipality": "Ballerup"
  },
  {
    "name": "Sportmaster Danmark ApS",
    "municipality": "Ballerup"
  },
  {
    "name": "KMD A/S",
    "municipality": "Ballerup"
  },
  {
    "name": "LEO PHARMA A/S",
    "municipality": "Ballerup"
  },
  {
    "name": "NETS Denmark A/S",
    "municipality": "Ballerup"
  },
  {
    "name": "TRYG FORSIKRING A/S",
    "municipality": "Ballerup"
  },
  {
    "name": "TOPDANMARK FORSIKRING A/S",
    "municipality": "Ballerup"
  },
  {
    "name": "ATEA A/S",
    "municipality": "Ballerup"
  },
  {
    "name": "SDC A/S",
    "municipality": "Ballerup"
  },
  {
    "name": "Velliv, Pension & Livsforsikring A/S",
    "municipality": "Ballerup"
  },
  {
    "name": "SIEMENS AKTIESELSKAB",
    "municipality": "Ballerup"
  },
  {
    "name": "EG A/S",
    "municipality": "Ballerup"
  },
  {
    "name": "TOMS GRUPPEN A/S",
    "municipality": "Ballerup"
  },
  {
    "name": "SCHNEIDER ELECTRIC DANMARK A/S",
    "municipality": "Ballerup"
  },
  {
    "name": "GN HEARING A/S",
    "municipality": "Ballerup"
  },
  {
    "name": "GN STORE NORD A/S",
    "municipality": "Ballerup"
  },
  {
    "name": "LALANDIA BILLUND A/S",
    "municipality": "Billund"
  },
  {
    "name": "BALL GROUP DENMARK ApS",
    "municipality": "Billund"
  },
  {
    "name": "LEGOLAND ApS",
    "municipality": "Billund"
  },
  {
    "name": "SAGRO I/S",
    "municipality": "Billund"
  },
  {
    "name": "LEGO SYSTEM A/S",
    "municipality": "Billund"
  },
  {
    "name": "BILLUND LUFTHAVN A/S",
    "municipality": "Billund"
  },
  {
    "name": "DANFOREL A/S",
    "municipality": "Billund"
  },
  {
    "name": "SUN-AIR OF SCANDINAVIA A/S",
    "municipality": "Billund"
  },
  {
    "name": "OMME LIFT A/S",
    "municipality": "Billund"
  },
  {
    "name": "BILLUND AQUACULTURE A/S",
    "municipality": "Billund"
  },
  {
    "name": "KOLDINGVEJ 2, BILLUND A/S",
    "municipality": "Billund"
  },
  {
    "name": "H.T. TRANSPORT & SPEDITION A/S",
    "municipality": "Billund"
  },
  {
    "name": "KIRKBI A/S",
    "municipality": "Billund"
  },
  {
    "name": "K.G. HANSEN & SØNNER A/S",
    "municipality": "Billund"
  },
  {
    "name": "LEGO A/S",
    "municipality": "Billund"
  },
  {
    "name": "EL OG VVS CENTER BORNHOLM ApS",
    "municipality": "Bornholm"
  },
  {
    "name": "Restauration Texas Bornholm ApS",
    "municipality": "Bornholm"
  },
  {
    "name": "OLE ALMEBORG A/S",
    "municipality": "Bornholm"
  },
  {
    "name": "ENTREPRENØRFIRMAET JENS MØLLER, GUDHJEM A/S",
    "municipality": "Bornholm"
  },
  {
    "name": "Bornholms Andelsmejeri a.m.b.a.",
    "municipality": "Bornholm"
  },
  {
    "name": "JENSEN DENMARK A/S",
    "municipality": "Bornholm"
  },
  {
    "name": "Bornholm Hotels ApS",
    "municipality": "Bornholm"
  },
  {
    "name": "FUGATO A/S",
    "municipality": "Bornholm"
  },
  {
    "name": "FAMILIEPLEJEN PÅ BORNHOLM",
    "municipality": "Bornholm"
  },
  {
    "name": "Bornholms Energi og Forsyning A/S",
    "municipality": "Bornholm"
  },
  {
    "name": "A. ESPERSEN A/S",
    "municipality": "Bornholm"
  },
  {
    "name": "PL BETON A/S",
    "municipality": "Bornholm"
  },
  {
    "name": "PL ENTREPRISE A/S",
    "municipality": "Bornholm"
  },
  {
    "name": "AKTIESELSKABET BORNHOLMS TIDENDE",
    "municipality": "Bornholm"
  },
  {
    "name": "BHS Logistics A/S",
    "municipality": "Bornholm"
  },
  {
    "name": "ALLIANCEPLUS A/S",
    "municipality": "Brøndby"
  },
  {
    "name": "IBM DANMARK ApS",
    "municipality": "Brøndby"
  },
  {
    "name": "SEMLER RETAIL A/S",
    "municipality": "Brøndby"
  },
  {
    "name": "SAINT-GOBAIN DISTRIBUTION DENMARK A/S",
    "municipality": "Brøndby"
  },
  {
    "name": "BRAVIDA DANMARK A/S",
    "municipality": "Brøndby"
  },
  {
    "name": "FORCE Technology",
    "municipality": "Brøndby"
  },
  {
    "name": "REMONDIS A/S",
    "municipality": "Brøndby"
  },
  {
    "name": "M.J. ERIKSSON AKTIESELSKAB",
    "municipality": "Brøndby"
  },
  {
    "name": "NKT Invest A/S",
    "municipality": "Brøndby"
  },
  {
    "name": "INTERVARE A/S",
    "municipality": "Brøndby"
  },
  {
    "name": "NATIONAL OILWELL VARCO DENMARK I/S",
    "municipality": "Brøndby"
  },
  {
    "name": "NILFISK A/S",
    "municipality": "Brøndby"
  },
  {
    "name": "CUBIC- MODULSYSTEM A/S",
    "municipality": "Brønderslev"
  },
  {
    "name": "LandboNord",
    "municipality": "Brønderslev"
  },
  {
    "name": "BPA SERVICE ApS",
    "municipality": "Brønderslev"
  },
  {
    "name": "KLOKKERHOLM KAROSSERIDELE A/S",
    "municipality": "Brønderslev"
  },
  {
    "name": "BG Brønderslev Invest A/S",
    "municipality": "Brønderslev"
  },
  {
    "name": "NORDEX FOOD A/S",
    "municipality": "Brønderslev"
  },
  {
    "name": "PEDERSHAAB CONCRETE TECHNOLOGIES A/S",
    "municipality": "Brønderslev"
  },
  {
    "name": "INVENTNORD OG PAKKECENTERNORD APS",
    "municipality": "Brønderslev"
  },
  {
    "name": "INTECH INTERNATIONAL A/S",
    "municipality": "Brønderslev"
  },
  {
    "name": "NØRAGER MEJERI A/S",
    "municipality": "Brønderslev"
  },
  {
    "name": "KR. ØSTERGAARD SØRENSENS BILER HJALLERUP ApS",
    "municipality": "Brønderslev"
  },
  {
    "name": "NK-Care ApS",
    "municipality": "Brønderslev"
  },
  {
    "name": "DRONNINGLUND HOTEL ApS",
    "municipality": "Brønderslev"
  },
  {
    "name": "HI-CON A/S",
    "municipality": "Brønderslev"
  },
  {
    "name": "A/S PEDER NIELSEN BESLAGFABRIK",
    "municipality": "Brønderslev"
  },
  {
    "name": "RESERVEDELSFABRIKKEN A/S",
    "municipality": "Brønderslev"
  },
  {
    "name": "DRONNINGLUND BRUGSFORENING",
    "municipality": "Brønderslev"
  },
  {
    "name": "PM ENERGI A/S",
    "municipality": "Brønderslev"
  },
  {
    "name": "NOVABIL A/S",
    "municipality": "Brønderslev"
  },
  {
    "name": "HOSTA INDUSTRIES A/S",
    "municipality": "Brønderslev"
  },
  {
    "name": "JKE DESIGN A/S",
    "municipality": "Brønderslev"
  },
  {
    "name": "Storm Textil v/Niels Storm",
    "municipality": "Brønderslev"
  },
  {
    "name": "Sparekassen Vendsyssels Fond, Dronninglund",
    "municipality": "Brønderslev"
  },
  {
    "name": "KANGAMIUT HOLDING A/S",
    "municipality": "Brønderslev"
  },
  {
    "name": "RenEksperterne ApS",
    "municipality": "Dragør"
  },
  {
    "name": "THOKA FINMEKANIK DRAGØR ApS",
    "municipality": "Dragør"
  },
  {
    "name": "RE 2A ApS",
    "municipality": "Dragør"
  },
  {
    "name": "BVS BEKLÆDNING ApS",
    "municipality": "Dragør"
  },
  {
    "name": "CAFE ESPERSEN ApS",
    "municipality": "Dragør"
  },
  {
    "name": "Lauren Erhvervsrengøring A/S",
    "municipality": "Dragør"
  },
  {
    "name": "Johs. Clausen Retail ApS",
    "municipality": "Dragør"
  },
  {
    "name": "DRAGØR KIRKE",
    "municipality": "Dragør"
  },
  {
    "name": "STORE MAGLEBY MENIGHEDSRAAD",
    "municipality": "Dragør"
  },
  {
    "name": "TRÆNINGSSKOLENS ARB UDD",
    "municipality": "Dragør"
  },
  {
    "name": "PAW SKO ApS",
    "municipality": "Dragør"
  },
  {
    "name": "CELSA STEEL SERVICE A/S",
    "municipality": "Egedal"
  },
  {
    "name": "Oticon Denmark A/S",
    "municipality": "Egedal"
  },
  {
    "name": "JB METALINDUSTRI A/S",
    "municipality": "Egedal"
  },
  {
    "name": "Audika ApS",
    "municipality": "Egedal"
  },
  {
    "name": "KILTIN A/S",
    "municipality": "Egedal"
  },
  {
    "name": "SANIVA FACILITY A/S",
    "municipality": "Egedal"
  },
  {
    "name": "BENNY JOHANSEN & SØNNER A/S",
    "municipality": "Egedal"
  },
  {
    "name": "Ganløse Kro af 2017 ApS",
    "municipality": "Egedal"
  },
  {
    "name": "Egedal Hjemmeservice / Egedal Gruppen",
    "municipality": "Egedal"
  },
  {
    "name": "OTICON A/S",
    "municipality": "Egedal"
  },
  {
    "name": "DE FORENEDE DAMPVASKERIER A/S",
    "municipality": "Egedal"
  },
  {
    "name": "Demant A/S",
    "municipality": "Egedal"
  },
  {
    "name": "VIKING LIFE-SAVING EQUIPMENT A/S",
    "municipality": "Esbjerg"
  },
  {
    "name": "POLYTECH A/S",
    "municipality": "Esbjerg"
  },
  {
    "name": "BABCOCK & WILCOX VØLUND A/S",
    "municipality": "Esbjerg"
  },
  {
    "name": "CLAUS SØRENSEN A/S",
    "municipality": "Esbjerg"
  },
  {
    "name": "NorSea Denmark A/S",
    "municipality": "Esbjerg"
  },
  {
    "name": "SEMCO INSTITUTE A/S",
    "municipality": "Esbjerg"
  },
  {
    "name": "JOBTEAM A/S",
    "municipality": "Esbjerg"
  },
  {
    "name": "BLUE WATER STEVEDORING A/S",
    "municipality": "Esbjerg"
  },
  {
    "name": "DIN FORSYNING A/S",
    "municipality": "Esbjerg"
  },
  {
    "name": "HOLGER CHRISTIANSEN A/S",
    "municipality": "Esbjerg"
  },
  {
    "name": "Norlys Infrastruktur A/S",
    "municipality": "Esbjerg"
  },
  {
    "name": "A/S VESTFROST",
    "municipality": "Esbjerg"
  },
  {
    "name": "C&D FOODS (DENMARK) A/S",
    "municipality": "Esbjerg"
  },
  {
    "name": "Det Faglige Hus - A-kasse",
    "municipality": "Esbjerg"
  },
  {
    "name": "AOF Center Sydjylland",
    "municipality": "Esbjerg"
  },
  {
    "name": "BLUE WATER SHIPPING A/S",
    "municipality": "Esbjerg"
  },
  {
    "name": "ESVAGT A/S",
    "municipality": "Esbjerg"
  },
  {
    "name": "SEMCO MARITIME A/S",
    "municipality": "Esbjerg"
  },
  {
    "name": "FANØ BRUGSFORENING",
    "municipality": "Fanø"
  },
  {
    "name": "Boidan Ejendomme I/S",
    "municipality": "Fanø"
  },
  {
    "name": "AB CATERING AARHUS A/S",
    "municipality": "Favrskov"
  },
  {
    "name": "SKATEPRO ApS",
    "municipality": "Favrskov"
  },
  {
    "name": "A/S KNUD JEPSEN",
    "municipality": "Favrskov"
  },
  {
    "name": "EC POWER A/S",
    "municipality": "Favrskov"
  },
  {
    "name": "HPH TOTALBYG A/S",
    "municipality": "Favrskov"
  },
  {
    "name": "EDGEMO A/S",
    "municipality": "Favrskov"
  },
  {
    "name": "HAMMEL FURNITURE A/S",
    "municipality": "Favrskov"
  },
  {
    "name": "R&D Test Systems A/S",
    "municipality": "Favrskov"
  },
  {
    "name": "ENKON A/S",
    "municipality": "Favrskov"
  },
  {
    "name": "POMPDELUX ApS",
    "municipality": "Favrskov"
  },
  {
    "name": "Junget A/S",
    "municipality": "Favrskov"
  },
  {
    "name": "REMA 1000, 974 Hadsten ApS",
    "municipality": "Favrskov"
  },
  {
    "name": "SVEND HOYER A/S",
    "municipality": "Favrskov"
  },
  {
    "name": "ØSTJYSK VINFORSYNING A/S",
    "municipality": "Favrskov"
  },
  {
    "name": "DANSK COMPUTER CENTER A/S",
    "municipality": "Favrskov"
  },
  {
    "name": "SCAN CHOCO A/S",
    "municipality": "Favrskov"
  },
  {
    "name": "OPTIMATE A/S",
    "municipality": "Favrskov"
  },
  {
    "name": "MC EMBALLAGE A/S",
    "municipality": "Favrskov"
  },
  {
    "name": "Leca Danmark A/S",
    "municipality": "Favrskov"
  },
  {
    "name": "JYDSK TAGTEKNIK A/S, AFDELING VEST",
    "municipality": "Favrskov"
  },
  {
    "name": "Duka A/S",
    "municipality": "Favrskov"
  },
  {
    "name": "AKTIESELSKABET ROLD SKOV SAVVÆRK",
    "municipality": "Favrskov"
  },
  {
    "name": "IN-STORE A/S",
    "municipality": "Favrskov"
  },
  {
    "name": "R&D Engineering A/S",
    "municipality": "Favrskov"
  },
  {
    "name": "MIKO GULVE A/S",
    "municipality": "Favrskov"
  },
  {
    "name": "HINNERUP OG OMEGNS GYMNASTIKFORENING",
    "municipality": "Favrskov"
  },
  {
    "name": "Kanonen",
    "municipality": "Favrskov"
  },
  {
    "name": "DE GRØNNE BUSSER I/S",
    "municipality": "Favrskov"
  },
  {
    "name": "FRODE LAURSEN A/S",
    "municipality": "Favrskov"
  },
  {
    "name": "EXPEDIT A/S",
    "municipality": "Favrskov"
  },
  {
    "name": "NORDISK WAVIN A/S",
    "municipality": "Favrskov"
  },
  {
    "name": "velas I/S",
    "municipality": "Favrskov"
  },
  {
    "name": "ROYAL UNIBREW A/S",
    "municipality": "Faxe"
  },
  {
    "name": "DANISH AGRO A.M.B.A.",
    "municipality": "Faxe"
  },
  {
    "name": "HARIBO PRODUKTION A/S",
    "municipality": "Faxe"
  },
  {
    "name": "A/S MORTALIN",
    "municipality": "Faxe"
  },
  {
    "name": "FINN L. & DAVIDSEN A/S",
    "municipality": "Faxe"
  },
  {
    "name": "FAXE KALK A/S",
    "municipality": "Faxe"
  },
  {
    "name": "Lev-Vel Hjemmepleje ApS",
    "municipality": "Faxe"
  },
  {
    "name": "Nestlé Professional Food A/S",
    "municipality": "Faxe"
  },
  {
    "name": "MENY HASLEV ApS",
    "municipality": "Faxe"
  },
  {
    "name": "H.E. JØRGENSEN A/S",
    "municipality": "Faxe"
  },
  {
    "name": "DA SHOPPEN A/S",
    "municipality": "Faxe"
  },
  {
    "name": "HELDAGSSKOLEN BRÅBY ApS",
    "municipality": "Faxe"
  },
  {
    "name": "UNO UNIQA GROUP A/S",
    "municipality": "Faxe"
  },
  {
    "name": "MAD SYNERGI ApS",
    "municipality": "Faxe"
  },
  {
    "name": "HabitusHuset Sølyst ApS",
    "municipality": "Faxe"
  },
  {
    "name": "Serviceerhverv ApS",
    "municipality": "Fredensborg"
  },
  {
    "name": "TitiBo-gruppen Aps",
    "municipality": "Fredensborg"
  },
  {
    "name": "NIKE RETAIL DENMARK, FILIAL AF NIKE RETAIL BV, HOLLAND",
    "municipality": "Fredensborg"
  },
  {
    "name": "FREDERIK OBELITZ, 936 KOKKEDAL ApS",
    "municipality": "Fredensborg"
  },
  {
    "name": "FREDENSBORG FORSYNING A/S",
    "municipality": "Fredensborg"
  },
  {
    "name": "SCANOMAT A/S",
    "municipality": "Fredensborg"
  },
  {
    "name": "DIVERSEY DANMARK ApS",
    "municipality": "Fredensborg"
  },
  {
    "name": "ALS DENMARK A/S",
    "municipality": "Fredensborg"
  },
  {
    "name": "LEIF ANDERSEN",
    "municipality": "Fredensborg"
  },
  {
    "name": "De selvejende institution Else Mariehjemmet",
    "municipality": "Fredensborg"
  },
  {
    "name": "Den selvejende institution Dyssegården",
    "municipality": "Fredensborg"
  },
  {
    "name": "COLOPLAST A/S",
    "municipality": "Fredensborg"
  },
  {
    "name": "COMM2IG A/S",
    "municipality": "Fredensborg"
  },
  {
    "name": "FREDENSBORG OG OMEGNS BRUGSFORENING",
    "municipality": "Fredensborg"
  },
  {
    "name": "Taastruphøj Properties",
    "municipality": "Fredensborg"
  },
  {
    "name": "Nordsjællands Brandvæsen",
    "municipality": "Fredensborg"
  },
  {
    "name": "LOUISIANA - FONDEN",
    "municipality": "Fredensborg"
  },
  {
    "name": "DANSAC A/S",
    "municipality": "Fredensborg"
  },
  {
    "name": "Ørsted A/S",
    "municipality": "Fredericia"
  },
  {
    "name": "GLOBAL WIND SERVICE A/S",
    "municipality": "Fredericia"
  },
  {
    "name": "Energinet Forretningsservice A/S",
    "municipality": "Fredericia"
  },
  {
    "name": "EGIL RASMUSSEN A/S",
    "municipality": "Fredericia"
  },
  {
    "name": "EM EL HOLDING A/S",
    "municipality": "Fredericia"
  },
  {
    "name": "A/S DANSK SHELL",
    "municipality": "Fredericia"
  },
  {
    "name": "Ørsted Wind Power A/S",
    "municipality": "Fredericia"
  },
  {
    "name": "DANSK LANDBRUGS GROVVARESELSKAB A.M.B.A.",
    "municipality": "Fredericia"
  },
  {
    "name": "Ørsted Services A/S",
    "municipality": "Fredericia"
  },
  {
    "name": "Energinet Eltransmission A/S",
    "municipality": "Fredericia"
  },
  {
    "name": "AUTOHUSET VESTERGAARD A/S PERSONVOGNE",
    "municipality": "Fredericia"
  },
  {
    "name": "CAVERION DANMARK A/S",
    "municipality": "Fredericia"
  },
  {
    "name": "Ørsted Bioenergy & Thermal Power A/S",
    "municipality": "Fredericia"
  },
  {
    "name": "EY Godkendt Revisionspartnerselskab",
    "municipality": "Frederiksberg"
  },
  {
    "name": "ADECCO A/S",
    "municipality": "Frederiksberg"
  },
  {
    "name": "CODAN FORSIKRING A/S",
    "municipality": "Frederiksberg"
  },
  {
    "name": "DEAS A/S",
    "municipality": "Frederiksberg"
  },
  {
    "name": "SOS INTERNATIONAL A/S",
    "municipality": "Frederiksberg"
  },
  {
    "name": "EY Danmark A/S",
    "municipality": "Frederiksberg"
  },
  {
    "name": "UNITED PRODUCTION ApS",
    "municipality": "Frederiksberg"
  },
  {
    "name": "PVB ADMINISTRATION ApS",
    "municipality": "Frederiksberg"
  },
  {
    "name": "KUBEN EJENDOMSADMINISTRATION A/S",
    "municipality": "Frederiksberg"
  },
  {
    "name": "BY MALENE BIRGER A/S",
    "municipality": "Frederiksberg"
  },
  {
    "name": "Capture One A/S",
    "municipality": "Frederiksberg"
  },
  {
    "name": "FREDERIKSBERG FORSYNING A/S",
    "municipality": "Frederiksberg"
  },
  {
    "name": "Fonden NOVAVI",
    "municipality": "Frederiksberg"
  },
  {
    "name": "BODENHOFFS BAGERI ApS",
    "municipality": "Frederiksberg"
  },
  {
    "name": "REINH. VAN HAUEN. GL. KONGEVEJ 177. FREDERIKSBERG ApS",
    "municipality": "Frederiksberg"
  },
  {
    "name": "PHILIPS DANMARK A/S",
    "municipality": "Frederiksberg"
  },
  {
    "name": "CABINN A/S",
    "municipality": "Frederiksberg"
  },
  {
    "name": "Michael West ApS",
    "municipality": "Frederiksberg"
  },
  {
    "name": "EDLUND A/S",
    "municipality": "Frederiksberg"
  },
  {
    "name": "MENY BORUPS ALLÉ I/S",
    "municipality": "Frederiksberg"
  },
  {
    "name": "Fonden Den danske Diakonissestiftelse",
    "municipality": "Frederiksberg"
  },
  {
    "name": "Copenhagen Phil",
    "municipality": "Frederiksberg"
  },
  {
    "name": "PROACTIVE A/S",
    "municipality": "Frederiksberg"
  },
  {
    "name": "DM",
    "municipality": "Frederiksberg"
  },
  {
    "name": "GEORG JENSEN A/S",
    "municipality": "Frederiksberg"
  },
  {
    "name": "MAGISTRENES ARBEJDSLØSHEDSKASSE",
    "municipality": "Frederiksberg"
  },
  {
    "name": "DAB",
    "municipality": "Frederiksberg"
  },
  {
    "name": "Gigtskolen",
    "municipality": "Frederiksberg"
  },
  {
    "name": "Hovedstadens Svømmeklub",
    "municipality": "Frederiksberg"
  },
  {
    "name": "DEN SELVEJ INST SØNDERVANG",
    "municipality": "Frederiksberg"
  },
  {
    "name": "ZOOLOGISK HAVE I KØBENHAVN",
    "municipality": "Frederiksberg"
  },
  {
    "name": "Im. Stiholt A/S",
    "municipality": "Frederikshavn"
  },
  {
    "name": "STENA LINE DENMARK A/S",
    "municipality": "Frederikshavn"
  },
  {
    "name": "Scandic Pelagic A/S",
    "municipality": "Frederikshavn"
  },
  {
    "name": "KARSTENSENS SKIBSVÆRFT A/S",
    "municipality": "Frederikshavn"
  },
  {
    "name": "AKTIESELSKABET SÆBY FISKE-INDUSTRI",
    "municipality": "Frederikshavn"
  },
  {
    "name": "SKIOLD A/S",
    "municipality": "Frederikshavn"
  },
  {
    "name": "FF SKAGEN A/S",
    "municipality": "Frederikshavn"
  },
  {
    "name": "AKTIV HVERDAG HJEMMESERVICE ApS",
    "municipality": "Frederikshavn"
  },
  {
    "name": "VMS Group A/S",
    "municipality": "Frederikshavn"
  },
  {
    "name": "SKAGEN SANDBLÆSERI & SKIBS-SERVICE ApS",
    "municipality": "Frederikshavn"
  },
  {
    "name": "PRIME OCEAN A/S",
    "municipality": "Frederikshavn"
  },
  {
    "name": "SVEND AAGE CHRISTIANSEN, HELLUM A/S",
    "municipality": "Frederikshavn"
  },
  {
    "name": "ME PRODUCTION A/S",
    "municipality": "Frederikshavn"
  },
  {
    "name": "FREDERIKSHAVN FORSYNING A/S",
    "municipality": "Frederikshavn"
  },
  {
    "name": "TERN SKAGEN MANAGEMENT A/S",
    "municipality": "Frederikshavn"
  },
  {
    "name": "ORSKOV YARD A/S",
    "municipality": "Frederikshavn"
  },
  {
    "name": "UGGERHØJ A/S",
    "municipality": "Frederikshavn"
  },
  {
    "name": "SCANEL INTERNATIONAL A/S",
    "municipality": "Frederikshavn"
  },
  {
    "name": "Robco Engineering A/S",
    "municipality": "Frederikshavn"
  },
  {
    "name": "Frederikshavn Boligforening",
    "municipality": "Frederikshavn"
  },
  {
    "name": "HORNSHERRED BRUGSFORENING",
    "municipality": "Frederikssund"
  },
  {
    "name": "Mountain Top (Denmark) ApS",
    "municipality": "Frederikssund"
  },
  {
    "name": "LOMAX A/S",
    "municipality": "Frederikssund"
  },
  {
    "name": "SØNDERGAARD A/S",
    "municipality": "Frederikssund"
  },
  {
    "name": "Topsil GlobalWafers A/S",
    "municipality": "Frederikssund"
  },
  {
    "name": "TELEDYNE RESON A/S",
    "municipality": "Frederikssund"
  },
  {
    "name": "PROCOM A/S",
    "municipality": "Frederikssund"
  },
  {
    "name": "SLANGERUP BRUGSFORENING AMBA",
    "municipality": "Frederikssund"
  },
  {
    "name": "Frederiksborg Brand og Redning",
    "municipality": "Frederikssund"
  },
  {
    "name": "A.P. Grønt v/Annette & Per Hardenberg",
    "municipality": "Frederikssund"
  },
  {
    "name": "CO-RO A/S",
    "municipality": "Frederikssund"
  },
  {
    "name": "ATTENDO A/S",
    "municipality": "Frederikssund"
  },
  {
    "name": "TOYOTA MATERIAL HANDLING DANMARK A/S",
    "municipality": "Frederikssund"
  },
  {
    "name": "E. SÆTHER A/S",
    "municipality": "Furesø"
  },
  {
    "name": "RITTER OG JENSEN MARKETING ApS",
    "municipality": "Furesø"
  },
  {
    "name": "ADSERBALLE & KNUDSEN A/S",
    "municipality": "Furesø"
  },
  {
    "name": "NTI A/S",
    "municipality": "Furesø"
  },
  {
    "name": "GERRESHEIMER VAERLOESE A/S",
    "municipality": "Furesø"
  },
  {
    "name": "HARESKOV ELEKTRIC A/S",
    "municipality": "Furesø"
  },
  {
    "name": "DEN SELVEJENDE INSTITUTION RYETBO",
    "municipality": "Furesø"
  },
  {
    "name": "Solgaven",
    "municipality": "Furesø"
  },
  {
    "name": "JONSTRUPVANG BEBYGGELSEN",
    "municipality": "Furesø"
  },
  {
    "name": "FARUMHUS A/S",
    "municipality": "Furesø"
  },
  {
    "name": "FC NORDSJÆLLAND A/S",
    "municipality": "Furesø"
  },
  {
    "name": "AASTED ApS",
    "municipality": "Furesø"
  },
  {
    "name": "SPEJDER SPORT A/S,",
    "municipality": "Furesø"
  },
  {
    "name": "CHANGE OF SCANDINAVIA RETAIL A/S",
    "municipality": "Furesø"
  },
  {
    "name": "PENSAM A/S",
    "municipality": "Furesø"
  },
  {
    "name": "REBRA ApS",
    "municipality": "Faaborg-Midtfyn"
  },
  {
    "name": "FJ INDUSTRIES A/S",
    "municipality": "Faaborg-Midtfyn"
  },
  {
    "name": "Aabo-Ideal A/S",
    "municipality": "Faaborg-Midtfyn"
  },
  {
    "name": "NASSAU DOOR A/S",
    "municipality": "Faaborg-Midtfyn"
  },
  {
    "name": "LACTOSAN A/S",
    "municipality": "Faaborg-Midtfyn"
  },
  {
    "name": "BRUGSENS SUPERMARKED RINGE",
    "municipality": "Faaborg-Midtfyn"
  },
  {
    "name": "RINGE KOST & REALSKOLE",
    "municipality": "Faaborg-Midtfyn"
  },
  {
    "name": "MARIUS PEDERSEN A/S",
    "municipality": "Faaborg-Midtfyn"
  },
  {
    "name": "KEN HYGIENE SYSTEMS A/S",
    "municipality": "Faaborg-Midtfyn"
  },
  {
    "name": "RYNKEBY FOODS A/S",
    "municipality": "Faaborg-Midtfyn"
  },
  {
    "name": "DANSK TRÆEMBALLAGE A/S",
    "municipality": "Faaborg-Midtfyn"
  },
  {
    "name": "LØGISMOSE A/S",
    "municipality": "Faaborg-Midtfyn"
  },
  {
    "name": "BRØDRENE HARTMANN A/S",
    "municipality": "Gentofte"
  },
  {
    "name": "PRICEWATERHOUSECOOPERS STATSAUTORISERET REVISIONSPARTNERSELSKAB",
    "municipality": "Gentofte"
  },
  {
    "name": "SAXO BANK A/S",
    "municipality": "Gentofte"
  },
  {
    "name": "DAMPSKIBSSELSKABET NORDEN A/S",
    "municipality": "Gentofte"
  },
  {
    "name": "ARP-HANSEN HOTEL GROUP A/S",
    "municipality": "Gentofte"
  },
  {
    "name": "SCANDINAVIAN TOBACCO GROUP A/S",
    "municipality": "Gentofte"
  },
  {
    "name": "BAVARIAN NORDIC A/S",
    "municipality": "Gentofte"
  },
  {
    "name": "FONDEN DIAKONISSEHUSET SANKT LUKAS STIFTELSEN",
    "municipality": "Gentofte"
  },
  {
    "name": "CHEVAL BLANC KANTINER A/S",
    "municipality": "Gentofte"
  },
  {
    "name": "HORTEN ADVOKATPARTNERSELSKAB",
    "municipality": "Gentofte"
  },
  {
    "name": "TORM A/S",
    "municipality": "Gentofte"
  },
  {
    "name": "IMPLEMENT CONSULTING GROUP P/S",
    "municipality": "Gentofte"
  },
  {
    "name": "ORACLE DANMARK ApS",
    "municipality": "Gentofte"
  },
  {
    "name": "BEMANDINGSKOMPAGNIET A/S",
    "municipality": "Gentofte"
  },
  {
    "name": "A/S KJØBENHAVNS EJENDOMSSELSKAB",
    "municipality": "Gentofte"
  },
  {
    "name": "FORCA A/S",
    "municipality": "Gentofte"
  },
  {
    "name": "LAURITZEN BULKERS A/S",
    "municipality": "Gentofte"
  },
  {
    "name": "Capio CFR A/S",
    "municipality": "Gentofte"
  },
  {
    "name": "SAMPENSION ADMINISTRATIONSSELSKAB A/S",
    "municipality": "Gentofte"
  },
  {
    "name": "Gigtforeningen",
    "municipality": "Gentofte"
  },
  {
    "name": "ISS A/S",
    "municipality": "Gladsaxe"
  },
  {
    "name": "PERSONALEGRUPPEN A/S",
    "municipality": "Gladsaxe"
  },
  {
    "name": "ISS FACILITY SERVICES A/S",
    "municipality": "Gladsaxe"
  },
  {
    "name": "NOVOZYMES A/S",
    "municipality": "Gladsaxe"
  },
  {
    "name": "MT Højgaard Danmark A/S",
    "municipality": "Gladsaxe"
  },
  {
    "name": "NCC DANMARK A/S",
    "municipality": "Gladsaxe"
  },
  {
    "name": "NNIT A/S",
    "municipality": "Gladsaxe"
  },
  {
    "name": "Elis Danmark A/S",
    "municipality": "Gladsaxe"
  },
  {
    "name": "NOVO NORDISK A/S",
    "municipality": "Gladsaxe"
  },
  {
    "name": "BYGMA A/S",
    "municipality": "Gladsaxe"
  },
  {
    "name": "FORENEDE SERVICE A/S",
    "municipality": "Gladsaxe"
  },
  {
    "name": "ALERIS HAMLET HOSPITALER A/S",
    "municipality": "Gladsaxe"
  },
  {
    "name": "MOE A/S",
    "municipality": "Gladsaxe"
  },
  {
    "name": "ALFA LAVAL COPENHAGEN A/S",
    "municipality": "Gladsaxe"
  },
  {
    "name": "GEA PROCESS ENGINEERING A/S",
    "municipality": "Gladsaxe"
  },
  {
    "name": "CFD",
    "municipality": "Gladsaxe"
  },
  {
    "name": "UNO-X DANMARK A/S",
    "municipality": "Gladsaxe"
  },
  {
    "name": "YX Danmark A/S",
    "municipality": "Gladsaxe"
  },
  {
    "name": "SECURITAS A/S",
    "municipality": "Glostrup"
  },
  {
    "name": "AGILENT TECHNOLOGIES DENMARK ApS",
    "municipality": "Glostrup"
  },
  {
    "name": "POWER A/S",
    "municipality": "Glostrup"
  },
  {
    "name": "Verisure A/S",
    "municipality": "Glostrup"
  },
  {
    "name": "AjourCare ApS",
    "municipality": "Glostrup"
  },
  {
    "name": "DANSK PELSDYRAVLERFORENING a.m.b.a.",
    "municipality": "Glostrup"
  },
  {
    "name": "HCS A/S TRANSPORT & SPEDITION",
    "municipality": "Glostrup"
  },
  {
    "name": "PROFIL MATCH ApS",
    "municipality": "Glostrup"
  },
  {
    "name": "HUMAC A/S",
    "municipality": "Glostrup"
  },
  {
    "name": "EINAR KORNERUP A/S",
    "municipality": "Glostrup"
  },
  {
    "name": "CHRISTIANSEN & ESSENBÆK A/S",
    "municipality": "Glostrup"
  },
  {
    "name": "I/S VESTFORBRÆNDING",
    "municipality": "Glostrup"
  },
  {
    "name": "ALDI KARLSLUNDE K/S",
    "municipality": "Greve"
  },
  {
    "name": "NEYE A/S",
    "municipality": "Greve"
  },
  {
    "name": "HOVEDSTADENS BYGNINGSENTREPRISE A/S",
    "municipality": "Greve"
  },
  {
    "name": "MAN TRUCK & BUS DANMARK A/S",
    "municipality": "Greve"
  },
  {
    "name": "LEMAN A/S",
    "municipality": "Greve"
  },
  {
    "name": "SNEDKERMESTER ARNE PEDERSEN A/S",
    "municipality": "Greve"
  },
  {
    "name": "ANDERSEN & MARTINI A/S",
    "municipality": "Greve"
  },
  {
    "name": "Bring E-commerce & Logistics A/S",
    "municipality": "Greve"
  },
  {
    "name": "GREVE STRAND DISTRIBUTION ApS",
    "municipality": "Greve"
  },
  {
    "name": "BWT Danmark A/S",
    "municipality": "Greve"
  },
  {
    "name": "DUEMOSE A/S",
    "municipality": "Gribskov"
  },
  {
    "name": "Anticimex Innovation Center A/S",
    "municipality": "Gribskov"
  },
  {
    "name": "A/S SKADEMOSEGÅRD",
    "municipality": "Gribskov"
  },
  {
    "name": "JMV Partner IVS",
    "municipality": "Gribskov"
  },
  {
    "name": "HabitusHuset Kæderupvej ApS",
    "municipality": "Gribskov"
  },
  {
    "name": "SAN ELECTRO HEAT A/S",
    "municipality": "Gribskov"
  },
  {
    "name": "PERSANO GROUP A/S",
    "municipality": "Gribskov"
  },
  {
    "name": "METRO THERM A/S",
    "municipality": "Gribskov"
  },
  {
    "name": "Egernsund Wienerberger A/S",
    "municipality": "Gribskov"
  },
  {
    "name": "GILLELEJE BRUGSFORENING",
    "municipality": "Gribskov"
  },
  {
    "name": "SCT TRANSPORT A/S",
    "municipality": "Gribskov"
  },
  {
    "name": "HELSINGE BRUGSFORENING AMBA",
    "municipality": "Gribskov"
  },
  {
    "name": "ENTREPRENØRFIRMAET NORDKYSTEN A/S",
    "municipality": "Gribskov"
  },
  {
    "name": "SAX-TRANS A/S",
    "municipality": "Guldborgsund"
  },
  {
    "name": "IDEBYG ApS",
    "municipality": "Guldborgsund"
  },
  {
    "name": "Mano Foods ApS",
    "municipality": "Guldborgsund"
  },
  {
    "name": "KARL MERTZ A/S",
    "municipality": "Guldborgsund"
  },
  {
    "name": "Kim Andersen, 978 Nordensvej ApS",
    "municipality": "Guldborgsund"
  },
  {
    "name": "NYMAND A/S",
    "municipality": "Guldborgsund"
  },
  {
    "name": "FRIMANN BILER A/S",
    "municipality": "Guldborgsund"
  },
  {
    "name": "GuldBoSund ApS",
    "municipality": "Guldborgsund"
  },
  {
    "name": "GRANBY PACK A/S",
    "municipality": "Guldborgsund"
  },
  {
    "name": "HOTEL FALSTER ApS",
    "municipality": "Guldborgsund"
  },
  {
    "name": "GULDBORGSUND FORSYNING A/S",
    "municipality": "Guldborgsund"
  },
  {
    "name": "TROELS JØRGENSEN A/S",
    "municipality": "Guldborgsund"
  },
  {
    "name": "BO-HUS A/S",
    "municipality": "Guldborgsund"
  },
  {
    "name": "RAACO A/S",
    "municipality": "Guldborgsund"
  },
  {
    "name": "MSE ENTREPRISE A/S",
    "municipality": "Guldborgsund"
  },
  {
    "name": "Nykøbing F. Sogns menighedsråd og Klosterkirken",
    "municipality": "Guldborgsund"
  },
  {
    "name": "Fora Fritid",
    "municipality": "Guldborgsund"
  },
  {
    "name": "Delta Rengøring",
    "municipality": "Guldborgsund"
  },
  {
    "name": "Fælleskøkkenet I/S",
    "municipality": "Guldborgsund"
  },
  {
    "name": "LOLLAND-FALSTERS FOLKETIDENDE A/S",
    "municipality": "Guldborgsund"
  },
  {
    "name": "JOB2SEA CREWING ApS",
    "municipality": "Guldborgsund"
  },
  {
    "name": "KJV A/S",
    "municipality": "Guldborgsund"
  },
  {
    "name": "SAKSKØBING BRUGSFORENING",
    "municipality": "Guldborgsund"
  },
  {
    "name": "I/S REFA",
    "municipality": "Guldborgsund"
  },
  {
    "name": "LOLLAND-FALSTERS STIFT",
    "municipality": "Guldborgsund"
  },
  {
    "name": "HARDI INTERNATIONAL A/S",
    "municipality": "Guldborgsund"
  },
  {
    "name": "ROBERT DAMKJÆR A/S",
    "municipality": "Haderslev"
  },
  {
    "name": "GRAM OG NYBØL GODSER A/S",
    "municipality": "Haderslev"
  },
  {
    "name": "X-YACHTS A/S",
    "municipality": "Haderslev"
  },
  {
    "name": "F. ENGEL K/S",
    "municipality": "Haderslev"
  },
  {
    "name": "DANSANI A/S",
    "municipality": "Haderslev"
  },
  {
    "name": "VVS SØBERG A/S",
    "municipality": "Haderslev"
  },
  {
    "name": "VOJENS TAXI OG SERVICETRAFIK ApS",
    "municipality": "Haderslev"
  },
  {
    "name": "PHARMA NORD ApS",
    "municipality": "Haderslev"
  },
  {
    "name": "Sønderjysk Landboforening",
    "municipality": "Haderslev"
  },
  {
    "name": "GRAM COMMERCIAL A/S",
    "municipality": "Haderslev"
  },
  {
    "name": "ARKIL A/S",
    "municipality": "Haderslev"
  },
  {
    "name": "BACK UP VIKAR A/S",
    "municipality": "Haderslev"
  },
  {
    "name": "DAVIDSENS TØMMERHANDEL A/S",
    "municipality": "Haderslev"
  },
  {
    "name": "LINDAB A/S",
    "municipality": "Haderslev"
  },
  {
    "name": "HADERSLEV STIFT",
    "municipality": "Haderslev"
  },
  {
    "name": "Mille Food A/S",
    "municipality": "Halsnæs"
  },
  {
    "name": "AQUAPRI A/S",
    "municipality": "Halsnæs"
  },
  {
    "name": "DUFERCO DANISH STEEL A/S",
    "municipality": "Halsnæs"
  },
  {
    "name": "CITY BAKERY ApS",
    "municipality": "Halsnæs"
  },
  {
    "name": "Deerland Probiotics & Enzymes A/S",
    "municipality": "Halsnæs"
  },
  {
    "name": "HALSNÆS FORSYNING A/S",
    "municipality": "Halsnæs"
  },
  {
    "name": "HALSNÆS BRYGHUS A/S",
    "municipality": "Halsnæs"
  },
  {
    "name": "KNUDSEN PLAST A/S",
    "municipality": "Halsnæs"
  },
  {
    "name": "Spar Karsemose ApS",
    "municipality": "Halsnæs"
  },
  {
    "name": "BALTIC SHIPPING COMPANY A/S",
    "municipality": "Halsnæs"
  },
  {
    "name": "APPLIED MANAGEMENT GROUP ApS",
    "municipality": "Halsnæs"
  },
  {
    "name": "A/S O.V. JØRGENSEN. HUNDESTED FISKEEXPORT",
    "municipality": "Halsnæs"
  },
  {
    "name": "LISELEJE BAGEREN ApS",
    "municipality": "Halsnæs"
  },
  {
    "name": "KNUDSEN KILEN A/S",
    "municipality": "Halsnæs"
  },
  {
    "name": "Norplan Entreprise A/S",
    "municipality": "Halsnæs"
  },
  {
    "name": "NORDISK STAAL A/S",
    "municipality": "Halsnæs"
  },
  {
    "name": "HALSNÆS SMEDEN A/S",
    "municipality": "Halsnæs"
  },
  {
    "name": "Jakob Tidemand, 877 Frederiksværk Aps",
    "municipality": "Halsnæs"
  },
  {
    "name": "NÆRREVISION A/S",
    "municipality": "Halsnæs"
  },
  {
    "name": "CHRISTIAN HANSEN ApS",
    "municipality": "Halsnæs"
  },
  {
    "name": "ESTRIDS PLEJE & HJEMMESERVICE A/S",
    "municipality": "Halsnæs"
  },
  {
    "name": "Lars Lippert-Scherwin, 900 Hundested ApS",
    "municipality": "Halsnæs"
  },
  {
    "name": "KTS-ENTREPRISE A/S",
    "municipality": "Halsnæs"
  },
  {
    "name": "ESTATE INVEST A/S",
    "municipality": "Halsnæs"
  },
  {
    "name": "TØMRERMESTER EGON BECH A/S",
    "municipality": "Halsnæs"
  },
  {
    "name": "A/S AUTOCO",
    "municipality": "Halsnæs"
  },
  {
    "name": "MS Maler & Byg ApS",
    "municipality": "Halsnæs"
  },
  {
    "name": "MENY Hundested I/S",
    "municipality": "Halsnæs"
  },
  {
    "name": "QUALITY PELLETS A/S",
    "municipality": "Halsnæs"
  },
  {
    "name": "A. HENRIKSEN SHIPPING A/S",
    "municipality": "Halsnæs"
  },
  {
    "name": "HUNDESTED PROPELLER A/S",
    "municipality": "Halsnæs"
  },
  {
    "name": "TØMRERENTREPRISEN A/S",
    "municipality": "Halsnæs"
  },
  {
    "name": "EURO SPAR FREDERIKSVÆRK ApS",
    "municipality": "Halsnæs"
  },
  {
    "name": "J.F. STÅL ApS",
    "municipality": "Halsnæs"
  },
  {
    "name": "TORUP SOGNS KIRKEKASSE",
    "municipality": "Halsnæs"
  },
  {
    "name": "Webport Ltd. T/A RTS-Scandinavia",
    "municipality": "Halsnæs"
  },
  {
    "name": "Skipperstuen",
    "municipality": "Halsnæs"
  },
  {
    "name": "Arresødal Hospice",
    "municipality": "Halsnæs"
  },
  {
    "name": "NLMK DANSTEEL A/S",
    "municipality": "Halsnæs"
  },
  {
    "name": "Envases Europe A/S",
    "municipality": "Hedensted"
  },
  {
    "name": "KLOSTER A/S",
    "municipality": "Hedensted"
  },
  {
    "name": "KJÆRGAARD A/S",
    "municipality": "Hedensted"
  },
  {
    "name": "ELM. KRAGELUND A/S",
    "municipality": "Hedensted"
  },
  {
    "name": "HOTEL VEJLEFJORD A/S",
    "municipality": "Hedensted"
  },
  {
    "name": "NILAN A/S",
    "municipality": "Hedensted"
  },
  {
    "name": "Polyprint A/S",
    "municipality": "Hedensted"
  },
  {
    "name": "JUAL A/S",
    "municipality": "Hedensted"
  },
  {
    "name": "VVS-EKSPERTEN A/S",
    "municipality": "Hedensted"
  },
  {
    "name": "BRDR. PLAGBORG A/S",
    "municipality": "Hedensted"
  },
  {
    "name": "GM PLAST A/S",
    "municipality": "Hedensted"
  },
  {
    "name": "VEJLEFJORD REHABILITERINGSCENTER A/S",
    "municipality": "Hedensted"
  },
  {
    "name": "Elogic A/S",
    "municipality": "Hedensted"
  },
  {
    "name": "HORNSYLD KØBMANDSGAARD A/S",
    "municipality": "Hedensted"
  },
  {
    "name": "TRIAX A/S",
    "municipality": "Hedensted"
  },
  {
    "name": "STENHØJ A/S",
    "municipality": "Hedensted"
  },
  {
    "name": "DAKA DENMARK A/S",
    "municipality": "Hedensted"
  },
  {
    "name": "AARSTIDERNE A/S",
    "municipality": "Hedensted"
  },
  {
    "name": "ELTRONIC A/S",
    "municipality": "Hedensted"
  },
  {
    "name": "A/S BOLIGBETON",
    "municipality": "Hedensted"
  },
  {
    "name": "PALSGAARD A/S",
    "municipality": "Hedensted"
  },
  {
    "name": "SP MOULDING A/S",
    "municipality": "Hedensted"
  },
  {
    "name": "SERVICEFIRMAET RENELL A/S",
    "municipality": "Helsingør"
  },
  {
    "name": "FORSEA Helsingør ApS",
    "municipality": "Helsingør"
  },
  {
    "name": "STRAND- & BADEHOTEL MARIENLYST A/S",
    "municipality": "Helsingør"
  },
  {
    "name": "TRELLEBORG SEALING SOLUTIONS HELSINGOR A/S",
    "municipality": "Helsingør"
  },
  {
    "name": "BARSLUND A/S",
    "municipality": "Helsingør"
  },
  {
    "name": "Helsingør Stiftsadministration",
    "municipality": "Helsingør"
  },
  {
    "name": "FORSYNING HELSINGØR SERVICE A/S",
    "municipality": "Helsingør"
  },
  {
    "name": "A/S LØGSTRUP STEEL",
    "municipality": "Helsingør"
  },
  {
    "name": "IJH A/S",
    "municipality": "Helsingør"
  },
  {
    "name": "NOA NOA A/S",
    "municipality": "Helsingør"
  },
  {
    "name": "COMWELL BORUPGAARD A/S",
    "municipality": "Helsingør"
  },
  {
    "name": "MENY Espergærde I/S",
    "municipality": "Helsingør"
  },
  {
    "name": "MEGGITT A/S",
    "municipality": "Helsingør"
  },
  {
    "name": "PETER BEIER CHOKOLADE A/S",
    "municipality": "Helsingør"
  },
  {
    "name": "Nordsjællands Park og Vej I/S",
    "municipality": "Helsingør"
  },
  {
    "name": "Den Selvejende Institution Birkebo",
    "municipality": "Helsingør"
  },
  {
    "name": "Boliggården",
    "municipality": "Helsingør"
  },
  {
    "name": "LOF ØRESUND",
    "municipality": "Helsingør"
  },
  {
    "name": "OTIS A/S",
    "municipality": "Herlev"
  },
  {
    "name": "Azets Insight A/S",
    "municipality": "Herlev"
  },
  {
    "name": "KONE A/S",
    "municipality": "Herlev"
  },
  {
    "name": "BRUNATA A/S",
    "municipality": "Herlev"
  },
  {
    "name": "CARL RAS A/S",
    "municipality": "Herlev"
  },
  {
    "name": "SSG A/S",
    "municipality": "Herlev"
  },
  {
    "name": "Omsorgscentret Hjortespring",
    "municipality": "Herlev"
  },
  {
    "name": "LEMVIGH-MüLLER A/S",
    "municipality": "Herlev"
  },
  {
    "name": "OLIVIA DANMARK A/S",
    "municipality": "Herlev"
  },
  {
    "name": "COOR SERVICE MANAGEMENT A/S",
    "municipality": "Herlev"
  },
  {
    "name": "IMERCO A/S",
    "municipality": "Herlev"
  },
  {
    "name": "ELTEL NETWORKS A/S",
    "municipality": "Herlev"
  },
  {
    "name": "NCC Industry A/S",
    "municipality": "Herlev"
  },
  {
    "name": "SYNOPTIK A/S",
    "municipality": "Herlev"
  },
  {
    "name": "KVIK A/S",
    "municipality": "Herning"
  },
  {
    "name": "FASTERHOLT HOLDING A/S",
    "municipality": "Herning"
  },
  {
    "name": "IT RELATION A/S",
    "municipality": "Herning"
  },
  {
    "name": "ÅF Buildings Denmark P/S",
    "municipality": "Herning"
  },
  {
    "name": "STOFF & STIL A/S",
    "municipality": "Herning"
  },
  {
    "name": "DOT A/S",
    "municipality": "Herning"
  },
  {
    "name": "SAMDISTRIBUTIONSSELSKABET MIDT-VEST A/S",
    "municipality": "Herning"
  },
  {
    "name": "MEDIEHUSENE MIDTJYLLAND A/S",
    "municipality": "Herning"
  },
  {
    "name": "MCH A/S",
    "municipality": "Herning"
  },
  {
    "name": "BONE'S RESTAURANTER A/S",
    "municipality": "Herning"
  },
  {
    "name": "A/S JYDSK ALUMINIUM INDUSTRI",
    "municipality": "Herning"
  },
  {
    "name": "FC MIDTJYLLAND A/S",
    "municipality": "Herning"
  },
  {
    "name": "KYOCERA UNIMERCO TOOLING A/S",
    "municipality": "Herning"
  },
  {
    "name": "BLÜCHER METAL A/S",
    "municipality": "Herning"
  },
  {
    "name": "Ege Carpets A/S",
    "municipality": "Herning"
  },
  {
    "name": "FUJIFILM Diosynth Biotechnologies Denmark ApS",
    "municipality": "Hillerød"
  },
  {
    "name": "FOSS ANALYTICAL A/S",
    "municipality": "Hillerød"
  },
  {
    "name": "PHARMAKON A/S",
    "municipality": "Hillerød"
  },
  {
    "name": "SSI Diagnostica A/S",
    "municipality": "Hillerød"
  },
  {
    "name": "ELOS MEDTECH PINOL A/S",
    "municipality": "Hillerød"
  },
  {
    "name": "NEDRIVNINGSAKTIESELSKABET J. JENSEN",
    "municipality": "Hillerød"
  },
  {
    "name": "ERA A/S",
    "municipality": "Hillerød"
  },
  {
    "name": "TØMRER- OG SNEDKERMESTER BØRGE NIELSEN A/S",
    "municipality": "Hillerød"
  },
  {
    "name": "HILLERØD SERVICE A/S",
    "municipality": "Hillerød"
  },
  {
    "name": "ULLERØD BRUGSFORENING",
    "municipality": "Hillerød"
  },
  {
    "name": "TESLA MOTORS DENMARK ApS",
    "municipality": "Hillerød"
  },
  {
    "name": "DEKRA Nordsjælland ApS",
    "municipality": "Hillerød"
  },
  {
    "name": "HHM A/S",
    "municipality": "Hillerød"
  },
  {
    "name": "ERA BILER A/S",
    "municipality": "Hillerød"
  },
  {
    "name": "FJORD LINE DANMARK A/S",
    "municipality": "Hjørring"
  },
  {
    "name": "SPAREKASSEN VENDSYSSEL",
    "municipality": "Hjørring"
  },
  {
    "name": "McDonald's Hjørring",
    "municipality": "Hjørring"
  },
  {
    "name": "GLASEKSPERTEN A/S",
    "municipality": "Hjørring"
  },
  {
    "name": "EKKOFONDEN",
    "municipality": "Hjørring"
  },
  {
    "name": "MESSAGE A/S",
    "municipality": "Hjørring"
  },
  {
    "name": "Vennelyst Ingeniør- og entreprenørforretning v/Jan Iver Christiansen",
    "municipality": "Hjørring"
  },
  {
    "name": "Blæksprutten ApS",
    "municipality": "Hjørring"
  },
  {
    "name": "KRONE VINDUER A/S",
    "municipality": "Hjørring"
  },
  {
    "name": "COLOR LINE. DANMARK A/S",
    "municipality": "Hjørring"
  },
  {
    "name": "SKALLERUP SEASIDE RESORT A/S",
    "municipality": "Hjørring"
  },
  {
    "name": "VRÅ DAMPVASKERI A/S",
    "municipality": "Hjørring"
  },
  {
    "name": "SEJLSTRUP ENTREPRENØRFORRETNING A/S",
    "municipality": "Hjørring"
  },
  {
    "name": "ARNE ANDERSEN, VRÅ A/S",
    "municipality": "Hjørring"
  },
  {
    "name": "NORDJYSKE JERNBANER A/S",
    "municipality": "Hjørring"
  },
  {
    "name": "DANHATCH Denmark A/S",
    "municipality": "Hjørring"
  },
  {
    "name": "AFFALDSSELSKABET VENDSYSSEL VEST I/S",
    "municipality": "Hjørring"
  },
  {
    "name": "Bakkafrost Danmark ApS",
    "municipality": "Hjørring"
  },
  {
    "name": "GRANHØJEN A/S",
    "municipality": "Holbæk"
  },
  {
    "name": "PS Contact / Øvejens Ridecenter v/Pia Saaby Sørensen",
    "municipality": "Holbæk"
  },
  {
    "name": "FIBIA P/S",
    "municipality": "Holbæk"
  },
  {
    "name": "DITOBUS LINJETRAFIK A/S",
    "municipality": "Holbæk"
  },
  {
    "name": "SEAS-NVE Service A/S",
    "municipality": "Holbæk"
  },
  {
    "name": "Sparekassen Sjælland-Fyn A/S",
    "municipality": "Holbæk"
  },
  {
    "name": "Andel Holding A/S",
    "municipality": "Holbæk"
  },
  {
    "name": "BEWI Denmark A/S",
    "municipality": "Holbæk"
  },
  {
    "name": "SØBÆKSKOLEN ApS",
    "municipality": "Holbæk"
  },
  {
    "name": "KILDEHAVEN A/S",
    "municipality": "Holbæk"
  },
  {
    "name": "FORS A/S",
    "municipality": "Holbæk"
  },
  {
    "name": "DBR RENGØRING A/S",
    "municipality": "Holbæk"
  },
  {
    "name": "PHARMACOSMOS A/S",
    "municipality": "Holbæk"
  },
  {
    "name": "FJORDSTJERNEN BOLIGER OG SUNDHEDSCENTER A/S",
    "municipality": "Holbæk"
  },
  {
    "name": "KAJ BECH A/S",
    "municipality": "Holstebro"
  },
  {
    "name": "MUSIKTEATRET-HOLSTEBRO FOND",
    "municipality": "Holstebro"
  },
  {
    "name": "CREATIV COMPANY A/S",
    "municipality": "Holstebro"
  },
  {
    "name": "KASTRUP A/S",
    "municipality": "Holstebro"
  },
  {
    "name": "EILER THOMSEN ALUFACADER A/S",
    "municipality": "Holstebro"
  },
  {
    "name": "PRIESS A/S",
    "municipality": "Holstebro"
  },
  {
    "name": "VESTFORSYNING ERHVERV A/S",
    "municipality": "Holstebro"
  },
  {
    "name": "FLEMMING KROGH A/S",
    "municipality": "Holstebro"
  },
  {
    "name": "V. T. I. VINDERUP TRÆINDUSTRI A/S",
    "municipality": "Holstebro"
  },
  {
    "name": "STS BILER A/S",
    "municipality": "Holstebro"
  },
  {
    "name": "CATER FOOD A/S",
    "municipality": "Holstebro"
  },
  {
    "name": "SKIOLD JYDEN A/S",
    "municipality": "Holstebro"
  },
  {
    "name": "ACTONA COMPANY A/S",
    "municipality": "Holstebro"
  },
  {
    "name": "TMK A/S",
    "municipality": "Holstebro"
  },
  {
    "name": "SINNERUP ApS",
    "municipality": "Holstebro"
  },
  {
    "name": "AktivPersonale A/S",
    "municipality": "Holstebro"
  },
  {
    "name": "McBride Denmark A/S",
    "municipality": "Holstebro"
  },
  {
    "name": "Faerch A/S",
    "municipality": "Holstebro"
  },
  {
    "name": "VINDERUP POULTRY ApS",
    "municipality": "Holstebro"
  },
  {
    "name": "HKSCAN DENMARK A/S",
    "municipality": "Holstebro"
  },
  {
    "name": "VALD. BIRN A/S",
    "municipality": "Holstebro"
  },
  {
    "name": "MEDARBEJDERNE ApS",
    "municipality": "Horsens"
  },
  {
    "name": "LANTMÄNNEN UNIBAKE DENMARK A/S",
    "municipality": "Horsens"
  },
  {
    "name": "A/S ØSTBIRK BYGNINGSINDUSTRI",
    "municipality": "Horsens"
  },
  {
    "name": "Steel Products Aage Østergaard A/S",
    "municipality": "Horsens"
  },
  {
    "name": "JYSK VIKARSERVICE A/S",
    "municipality": "Horsens"
  },
  {
    "name": "WEST PHARMACEUTICAL SERVICES DANMARK A/S",
    "municipality": "Horsens"
  },
  {
    "name": "VOLA A/S",
    "municipality": "Horsens"
  },
  {
    "name": "Nissens Cooling Solutions A/S",
    "municipality": "Horsens"
  },
  {
    "name": "OLUF JØRGENSEN A/S",
    "municipality": "Horsens"
  },
  {
    "name": "ITELLIGENCE A/S",
    "municipality": "Horsens"
  },
  {
    "name": "HATTING A/S",
    "municipality": "Horsens"
  },
  {
    "name": "DOVISTA A/S",
    "municipality": "Horsens"
  },
  {
    "name": "AMCOR FLEXIBLES DENMARK ApS",
    "municipality": "Horsens"
  },
  {
    "name": "JYDSK MILJØ RENGØRING A/S",
    "municipality": "Horsens"
  },
  {
    "name": "Umove Vest A/S",
    "municipality": "Horsens"
  },
  {
    "name": "REITAN DISTRIBUTION A/S",
    "municipality": "Horsens"
  },
  {
    "name": "LØVBJERG SUPERMARKED A/S",
    "municipality": "Horsens"
  },
  {
    "name": "REMA 1000 DANMARK A/S",
    "municipality": "Horsens"
  },
  {
    "name": "HusCompagniet A/S",
    "municipality": "Horsens"
  },
  {
    "name": "DE 5 STJERNER A/S",
    "municipality": "Hvidovre"
  },
  {
    "name": "LANTMÄNNEN SCHULSTAD A/S",
    "municipality": "Hvidovre"
  },
  {
    "name": "KN Rengøring I/S",
    "municipality": "Hvidovre"
  },
  {
    "name": "NTG Nordic Transport Group A/S",
    "municipality": "Hvidovre"
  },
  {
    "name": "LAKRIDS BY JOHAN BÜLOW A/S",
    "municipality": "Hvidovre"
  },
  {
    "name": "RECOVER NORDIC ApS",
    "municipality": "Hvidovre"
  },
  {
    "name": "DACHSER DENMARK A/S",
    "municipality": "Hvidovre"
  },
  {
    "name": "TNT DANMARK ApS",
    "municipality": "Hvidovre"
  },
  {
    "name": "SCHENKER A/S",
    "municipality": "Hvidovre"
  },
  {
    "name": "ANCHERSEN A/S",
    "municipality": "Hvidovre"
  },
  {
    "name": "AIR Group A/S",
    "municipality": "Hvidovre"
  },
  {
    "name": "SANTANDER CONSUMER BANK, FILIAL AF SANTANDER CONSUMER BANK AS, NORGE",
    "municipality": "Hvidovre"
  },
  {
    "name": "IF SKADEFORSIKRING, FILIAL AF IF SKADEFÖRSÄKRING AB (PUBL), SVERIGE",
    "municipality": "Hvidovre"
  },
  {
    "name": "Polygon DB A/S",
    "municipality": "Hvidovre"
  },
  {
    "name": "DSB VEDLIGEHOLD A/S",
    "municipality": "Høje-Taastrup"
  },
  {
    "name": "DSV ROAD A/S",
    "municipality": "Høje-Taastrup"
  },
  {
    "name": "IKEA A/S",
    "municipality": "Høje-Taastrup"
  },
  {
    "name": "FORBRUGER-KONTAKT A/S",
    "municipality": "Høje-Taastrup"
  },
  {
    "name": "LOBPA",
    "municipality": "Høje-Taastrup"
  },
  {
    "name": "TEAMVIKAREN.DK, KØBENHAVN ApS",
    "municipality": "Høje-Taastrup"
  },
  {
    "name": "TDC TELCO ApS",
    "municipality": "Høje-Taastrup"
  },
  {
    "name": "ROCKWOOL A/S",
    "municipality": "Høje-Taastrup"
  },
  {
    "name": "WICOTEC KIRKEBJERG A/S",
    "municipality": "Høje-Taastrup"
  },
  {
    "name": "DSB Service & Retail A/S",
    "municipality": "Høje-Taastrup"
  },
  {
    "name": "Synsam Group Denmark A/S",
    "municipality": "Høje-Taastrup"
  },
  {
    "name": "ANDERS ANDERSEN'S RENGØRING",
    "municipality": "Høje-Taastrup"
  },
  {
    "name": "DSV Panalpina A/S",
    "municipality": "Høje-Taastrup"
  },
  {
    "name": "DSB",
    "municipality": "Høje-Taastrup"
  },
  {
    "name": "ALSO A/S",
    "municipality": "Høje-Taastrup"
  },
  {
    "name": "TJELLESEN MAX JENNE A/S",
    "municipality": "Høje-Taastrup"
  },
  {
    "name": "CECA FOODS HILLERØD ApS",
    "municipality": "Hørsholm"
  },
  {
    "name": "ICM A/S",
    "municipality": "Hørsholm"
  },
  {
    "name": "GUBRA ApS",
    "municipality": "Hørsholm"
  },
  {
    "name": "K.L.A. Food ApS",
    "municipality": "Hørsholm"
  },
  {
    "name": "ROSENDAHL DESIGN GROUP A/S",
    "municipality": "Hørsholm"
  },
  {
    "name": "SKOU GRUPPEN A/S",
    "municipality": "Hørsholm"
  },
  {
    "name": "FORSIKRINGSAKADEMIET A/S",
    "municipality": "Hørsholm"
  },
  {
    "name": "S/I Breelteparken",
    "municipality": "Hørsholm"
  },
  {
    "name": "VELUX A/S",
    "municipality": "Hørsholm"
  },
  {
    "name": "CBJ-HOLDING A/S",
    "municipality": "Hørsholm"
  },
  {
    "name": "ERKO HOLDING ApS",
    "municipality": "Hørsholm"
  },
  {
    "name": "MERCEDES-BENZ CPH A/S",
    "municipality": "Hørsholm"
  },
  {
    "name": "EJNER HESSEL A/S",
    "municipality": "Ikast-Brande"
  },
  {
    "name": "Siemens Gamesa Renewable Energy A/S",
    "municipality": "Ikast-Brande"
  },
  {
    "name": "BESTSELLER A/S",
    "municipality": "Ikast-Brande"
  },
  {
    "name": "A/S IKAST BETONVAREFABRIK",
    "municipality": "Ikast-Brande"
  },
  {
    "name": "ONLY STORES DENMARK A/S",
    "municipality": "Ikast-Brande"
  },
  {
    "name": "BESTSELLER Stores Denmark A/S",
    "municipality": "Ikast-Brande"
  },
  {
    "name": "BESTSELLER Stores A/S",
    "municipality": "Ikast-Brande"
  },
  {
    "name": "DK COMPANY A/S",
    "municipality": "Ikast-Brande"
  },
  {
    "name": "BRANDE BUSLINIER ApS",
    "municipality": "Ikast-Brande"
  },
  {
    "name": "KELSEN GROUP A/S",
    "municipality": "Ikast-Brande"
  },
  {
    "name": "MASCOT INTERNATIONAL A/S",
    "municipality": "Ikast-Brande"
  },
  {
    "name": "Give Steel A/S",
    "municipality": "Ikast-Brande"
  },
  {
    "name": "DAGROFA FOODSERVICE A/S",
    "municipality": "Ishøj"
  },
  {
    "name": "SCANIA DANMARK A/S",
    "municipality": "Ishøj"
  },
  {
    "name": "ANTICIMEX A/S",
    "municipality": "Ishøj"
  },
  {
    "name": "ZACHO-LIND A/S",
    "municipality": "Ishøj"
  },
  {
    "name": "Orkla Care A/S",
    "municipality": "Ishøj"
  },
  {
    "name": "Hovedstadsregionens og Midt-Nords Naturgasselskab I/S",
    "municipality": "Ishøj"
  },
  {
    "name": "ISHØJ HEGN A/S",
    "municipality": "Ishøj"
  },
  {
    "name": "PLATFORM.AS A/S",
    "municipality": "Ishøj"
  },
  {
    "name": "H.W.LARSEN A/S",
    "municipality": "Ishøj"
  },
  {
    "name": "TRIPLAN INTERNATIONAL A/S",
    "municipality": "Ishøj"
  },
  {
    "name": "HEKA DENTAL A/S",
    "municipality": "Ishøj"
  },
  {
    "name": "DANX A/S",
    "municipality": "Ishøj"
  },
  {
    "name": "KNUD ANDERSEN",
    "municipality": "Ishøj"
  },
  {
    "name": "Ølandhus ApS",
    "municipality": "Jammerbugt"
  },
  {
    "name": "SILVASTI TRANSPORT A/S",
    "municipality": "Jammerbugt"
  },
  {
    "name": "FERIECENTER SLETTESTRAND A/S",
    "municipality": "Jammerbugt"
  },
  {
    "name": "TEEJET TECHNOLOGIES DENMARK ApS",
    "municipality": "Jammerbugt"
  },
  {
    "name": "SCANIRO A/S",
    "municipality": "Jammerbugt"
  },
  {
    "name": "EVENT CREW ApS",
    "municipality": "Jammerbugt"
  },
  {
    "name": "FÅRUP SOMMERLAND A/S",
    "municipality": "Jammerbugt"
  },
  {
    "name": "EURO INDUSTRIES A/S",
    "municipality": "Jammerbugt"
  },
  {
    "name": "EVAPCO Air Solutions a/s",
    "municipality": "Jammerbugt"
  },
  {
    "name": "Meny Saltum A/S",
    "municipality": "Jammerbugt"
  },
  {
    "name": "Resolut.",
    "municipality": "Jammerbugt"
  },
  {
    "name": "SOL OG STRAND FERIEHUSUDLEJNING A/S",
    "municipality": "Jammerbugt"
  },
  {
    "name": "Kn Rengøring Henrik Krogstrup Nielsen",
    "municipality": "Jammerbugt"
  },
  {
    "name": "SVEJSEMASKINEFABRIKKEN MIGATRONIC A/S",
    "municipality": "Jammerbugt"
  },
  {
    "name": "BEJSTRUP MASKINSTATION A/S",
    "municipality": "Jammerbugt"
  },
  {
    "name": "TELCO ELECTRONICS A/S",
    "municipality": "Jammerbugt"
  },
  {
    "name": "Altiden Solskovgaard ApS",
    "municipality": "Jammerbugt"
  },
  {
    "name": "FJERRITSLEV & OMEGNS BRUGSFORENING",
    "municipality": "Jammerbugt"
  },
  {
    "name": "HOTEL SØPARKEN AF 7/6 1994 ApS",
    "municipality": "Jammerbugt"
  },
  {
    "name": "NØRHALNE VVS A/S",
    "municipality": "Jammerbugt"
  },
  {
    "name": "VSV Personalerekruttering IVS",
    "municipality": "Jammerbugt"
  },
  {
    "name": "MENY Kalundborg ApS",
    "municipality": "Kalundborg"
  },
  {
    "name": "JOHS. RASMUSSEN. SVEBØLLE A/S",
    "municipality": "Kalundborg"
  },
  {
    "name": "MUSHOLM A/S",
    "municipality": "Kalundborg"
  },
  {
    "name": "GAMMELRAND BETON A/S",
    "municipality": "Kalundborg"
  },
  {
    "name": "KALUNDBORG FORSYNING A/S",
    "municipality": "Kalundborg"
  },
  {
    "name": "MEREDIN A/S",
    "municipality": "Kalundborg"
  },
  {
    "name": "BILCENTRET PEER GLAD A/S",
    "municipality": "Kalundborg"
  },
  {
    "name": "Crispy Food A/S",
    "municipality": "Kalundborg"
  },
  {
    "name": "JERSLEV STILLADSSERVICE A/S",
    "municipality": "Kalundborg"
  },
  {
    "name": "AVISTA Green ApS",
    "municipality": "Kalundborg"
  },
  {
    "name": "Hvidebæk Slagteri og Pølsefabrik ApS",
    "municipality": "Kalundborg"
  },
  {
    "name": "MULTI-TECH A/S",
    "municipality": "Kalundborg"
  },
  {
    "name": "Hrs A/S",
    "municipality": "Kalundborg"
  },
  {
    "name": "Kragerup Gods",
    "municipality": "Kalundborg"
  },
  {
    "name": "LOF Nordvestsjælland",
    "municipality": "Kalundborg"
  },
  {
    "name": "Equinor Refining Denmark A/S",
    "municipality": "Kalundborg"
  },
  {
    "name": "KALUNDBORG BRUGSFORENING",
    "municipality": "Kalundborg"
  },
  {
    "name": "Vestsjællands Brandvæsen I/S",
    "municipality": "Kalundborg"
  },
  {
    "name": "IB ANDRESEN INDUSTRI A/S",
    "municipality": "Kerteminde"
  },
  {
    "name": "JØRGEN KRUUSE A/S",
    "municipality": "Kerteminde"
  },
  {
    "name": "EXHAUSTO A/S",
    "municipality": "Kerteminde"
  },
  {
    "name": "FAYARD A/S",
    "municipality": "Kerteminde"
  },
  {
    "name": "KERTEMINDE BRUGSFORENING",
    "municipality": "Kerteminde"
  },
  {
    "name": "ROSA DANICA A/S",
    "municipality": "Kerteminde"
  },
  {
    "name": "PERSOLIT ENTREPRENØRFIRMA A/S",
    "municipality": "Kerteminde"
  },
  {
    "name": "KVERNELAND GROUP KERTEMINDE A/S",
    "municipality": "Kerteminde"
  },
  {
    "name": "MDHB 1717 ApS",
    "municipality": "Kerteminde"
  },
  {
    "name": "EURO-DK SERVICE A/S",
    "municipality": "Kerteminde"
  },
  {
    "name": "JM MANPOWER ApS",
    "municipality": "Kerteminde"
  },
  {
    "name": "MEDICOPACK A/S",
    "municipality": "Kerteminde"
  },
  {
    "name": "HYDAC A/S",
    "municipality": "Kerteminde"
  },
  {
    "name": "LANGESKOV BRUGSFORENING",
    "municipality": "Kerteminde"
  },
  {
    "name": "KERTEMINDE FORSYNING A/S",
    "municipality": "Kerteminde"
  },
  {
    "name": "STOK EMBALLAGE K/S",
    "municipality": "Kerteminde"
  },
  {
    "name": "MOGENS KNUDSEN LANGESKOV A/S",
    "municipality": "Kerteminde"
  },
  {
    "name": "NEDSCHROEF LANGESKOV ApS",
    "municipality": "Kerteminde"
  },
  {
    "name": "GREAT NORTHERN A/S",
    "municipality": "Kerteminde"
  },
  {
    "name": "PERSOLIT STILLADSFIRMA A/S",
    "municipality": "Kerteminde"
  },
  {
    "name": "SAKATA ORNAMENTALS EUROPE A/S",
    "municipality": "Kerteminde"
  },
  {
    "name": "Orana Denmark A/S",
    "municipality": "Kerteminde"
  },
  {
    "name": "Østfyns Museer",
    "municipality": "Kerteminde"
  },
  {
    "name": "DANSK AUTO LOGIK A/S",
    "municipality": "Kolding"
  },
  {
    "name": "PIERRE.DK AUTOLAKERING A/S",
    "municipality": "Kolding"
  },
  {
    "name": "DSV Prime Cargo A/S",
    "municipality": "Kolding"
  },
  {
    "name": "GRAM EQUIPMENT A/S",
    "municipality": "Kolding"
  },
  {
    "name": "LM WIND POWER A/S",
    "municipality": "Kolding"
  },
  {
    "name": "TRESU A/S",
    "municipality": "Kolding"
  },
  {
    "name": "TOLKEKONTORET A/S",
    "municipality": "Kolding"
  },
  {
    "name": "DAT A/S",
    "municipality": "Kolding"
  },
  {
    "name": "VATTENFALL VINDKRAFT A/S",
    "municipality": "Kolding"
  },
  {
    "name": "NY-FORM, KOLDING A/S",
    "municipality": "Kolding"
  },
  {
    "name": "RESPONCE A/S",
    "municipality": "Kolding"
  },
  {
    "name": "GKN WHEELS NAGBØL A/S",
    "municipality": "Kolding"
  },
  {
    "name": "Lidl Danmark K/S",
    "municipality": "Kolding"
  },
  {
    "name": "WÜRTH DANMARK A/S",
    "municipality": "Kolding"
  },
  {
    "name": "GENERAL LOGISTICS SYSTEMS DENMARK A/S",
    "municipality": "Kolding"
  },
  {
    "name": "ALDI KOLDING K/S",
    "municipality": "Kolding"
  },
  {
    "name": "DANSKE KONCEPT RESTAURANTER A/S",
    "municipality": "Kolding"
  },
  {
    "name": "SMURFIT KAPPA DANMARK A/S",
    "municipality": "Kolding"
  },
  {
    "name": "J.A.A.K. ApS",
    "municipality": "Kolding"
  },
  {
    "name": "ALFA LAVAL KOLDING A/S",
    "municipality": "Kolding"
  },
  {
    "name": "HOFOR A/S",
    "municipality": "København"
  },
  {
    "name": "CIRCLE K DANMARK A/S",
    "municipality": "København"
  },
  {
    "name": "Netcompany A/S",
    "municipality": "København"
  },
  {
    "name": "REDERIET A. P. MØLLER A/S",
    "municipality": "København"
  },
  {
    "name": "Total E&P Danmark A/S",
    "municipality": "København"
  },
  {
    "name": "TDC A/S",
    "municipality": "København"
  },
  {
    "name": "NYKREDIT REALKREDIT A/S",
    "municipality": "København"
  },
  {
    "name": "DFDS A/S",
    "municipality": "København"
  },
  {
    "name": "Sweco Danmark A/S",
    "municipality": "København"
  },
  {
    "name": "BC Hospitality Group A/S",
    "municipality": "København"
  },
  {
    "name": "LAGKAGEHUSET A/S",
    "municipality": "København"
  },
  {
    "name": "RAMBØLL DANMARK A/S",
    "municipality": "København"
  },
  {
    "name": "AKTIESELSKABET ARBEJDERNES LANDSBANK",
    "municipality": "København"
  },
  {
    "name": "ELGIGANTEN A/S",
    "municipality": "København"
  },
  {
    "name": "TELENOR A/S",
    "municipality": "København"
  },
  {
    "name": "POST DANMARK A/S",
    "municipality": "København"
  },
  {
    "name": "RADIOMETER MEDICAL ApS",
    "municipality": "København"
  },
  {
    "name": "ALM. BRAND FORSIKRING A/S",
    "municipality": "København"
  },
  {
    "name": "TIVOLI A/S",
    "municipality": "København"
  },
  {
    "name": "AKTIESELSKABET TH. WESSEL & VETT. MAGASIN DU NORD",
    "municipality": "København"
  },
  {
    "name": "CARLSBERG SUPPLY COMPANY DANMARK A/S",
    "municipality": "København"
  },
  {
    "name": "DUOS A/S",
    "municipality": "København"
  },
  {
    "name": "COMPASS GROUP DANMARK A/S",
    "municipality": "København"
  },
  {
    "name": "MOMENT A/S",
    "municipality": "København"
  },
  {
    "name": "Q8 DANMARK A/S",
    "municipality": "København"
  },
  {
    "name": "H & M HENNES & MAURITZ A/S",
    "municipality": "København"
  },
  {
    "name": "MAN Energy Solutions, filial af MAN Energy Solutions SE, TYSKLAND",
    "municipality": "København"
  },
  {
    "name": "DUPONT NUTRITION BIOSCIENCES ApS",
    "municipality": "København"
  },
  {
    "name": "DELOITTE STATSAUTORISERET REVISIONSPARTNERSELSKAB",
    "municipality": "København"
  },
  {
    "name": "H. LUNDBECK A/S",
    "municipality": "København"
  },
  {
    "name": "PFA PENSION, FORSIKRINGSAKTIESELSKAB.",
    "municipality": "København"
  },
  {
    "name": "Nordea Danmark, Filial af Nordea Bank Abp, Finland",
    "municipality": "København"
  },
  {
    "name": "FALCK DANMARK A/S",
    "municipality": "København"
  },
  {
    "name": "SCANDIC HOTEL A/S",
    "municipality": "København"
  },
  {
    "name": "DANSKE BANK A/S",
    "municipality": "København"
  },
  {
    "name": "ZEBRA A/S",
    "municipality": "København"
  },
  {
    "name": "DANSK FLYGTNINGEHJÆLP",
    "municipality": "København"
  },
  {
    "name": "DR",
    "municipality": "København"
  },
  {
    "name": "F A D L S VAGTBUREAU",
    "municipality": "København"
  },
  {
    "name": "NORDISK FILM BIOGRAFER A/S",
    "municipality": "København"
  },
  {
    "name": "NYKREDIT BANK A/S",
    "municipality": "København"
  },
  {
    "name": "Old Irish Pub Denmark A/S",
    "municipality": "København"
  },
  {
    "name": "Altiden Omsorg A/S",
    "municipality": "København"
  },
  {
    "name": "NESTLE DANMARK A/S",
    "municipality": "København"
  },
  {
    "name": "DANICA PENSION, LIVSFORSIKRINGSAKTIESELSKAB",
    "municipality": "København"
  },
  {
    "name": "MAERSK SUPPLY SERVICE A/S",
    "municipality": "København"
  },
  {
    "name": "DAT-SCHAUB A/S",
    "municipality": "København"
  },
  {
    "name": "MAERSK A/S",
    "municipality": "København"
  },
  {
    "name": "TEMP TEAM A/S",
    "municipality": "København"
  },
  {
    "name": "ACCENTURE A/S",
    "municipality": "København"
  },
  {
    "name": "Nuuday A/S",
    "municipality": "København"
  },
  {
    "name": "NOMECO A/S",
    "municipality": "København"
  },
  {
    "name": "SHIPCO TRANSPORT HOLDING A/S",
    "municipality": "København"
  },
  {
    "name": "SIMCORP A/S",
    "municipality": "København"
  },
  {
    "name": "GJENSIDIGE FORSIKRING, DANSK FILIAL AF GJENSIDIGE FORSIKRING ASA, NORGE",
    "municipality": "København"
  },
  {
    "name": "A.P. MØLLER - MÆRSK A/S",
    "municipality": "København"
  },
  {
    "name": "ALLER MEDIA A/S",
    "municipality": "København"
  },
  {
    "name": "OK-FONDEN",
    "municipality": "København"
  },
  {
    "name": "LB FORSIKRING A/S",
    "municipality": "København"
  },
  {
    "name": "NORDIC SERVICE PARTNERS A/S",
    "municipality": "København"
  },
  {
    "name": "FLSMIDTH A/S",
    "municipality": "København"
  },
  {
    "name": "MAERSK TANKERS A/S",
    "municipality": "København"
  },
  {
    "name": "DXC Technology Danmark A/S",
    "municipality": "København"
  },
  {
    "name": "TELIA DANMARK, FILIAL AF TELIA NÄTTJÄNSTER NORDEN AB, SVERIGE",
    "municipality": "København"
  },
  {
    "name": "KPMG P/S",
    "municipality": "København"
  },
  {
    "name": "XELLIA PHARMACEUTICALS ApS",
    "municipality": "København"
  },
  {
    "name": "SAMSØE & SAMSØE WHOLE SALE ApS",
    "municipality": "København"
  },
  {
    "name": "FERRING PHARMACEUTICALS A/S",
    "municipality": "København"
  },
  {
    "name": "FALCK HEALTHCARE A/S",
    "municipality": "København"
  },
  {
    "name": "AJ Vaccines A/S",
    "municipality": "København"
  },
  {
    "name": "Meyers Contract Catering A/S",
    "municipality": "København"
  },
  {
    "name": "HI3G DENMARK ApS",
    "municipality": "København"
  },
  {
    "name": "STICKS 'N' SUSHI A/S",
    "municipality": "København"
  },
  {
    "name": "Espresso House Denmark A/S",
    "municipality": "København"
  },
  {
    "name": "L'ORÉAL DANMARK A/S",
    "municipality": "København"
  },
  {
    "name": "Randstad A/S",
    "municipality": "København"
  },
  {
    "name": "HANDELSBANKEN, FILIAL AF SVENSKA HANDELSBANKEN AB (PUBL),SVERIGE",
    "municipality": "København"
  },
  {
    "name": "KRÆFTENS BEKÆMPELSE",
    "municipality": "København"
  },
  {
    "name": "FOF København",
    "municipality": "København"
  },
  {
    "name": "KL",
    "municipality": "København"
  },
  {
    "name": "Poul Schmith/Kammeradvokaten I/S",
    "municipality": "København"
  },
  {
    "name": "NEXT Uddannelse København",
    "municipality": "København"
  },
  {
    "name": "Hovedstadens Beredskab I/S",
    "municipality": "København"
  },
  {
    "name": "Røde Kors",
    "municipality": "København"
  },
  {
    "name": "DI",
    "municipality": "København"
  },
  {
    "name": "Fagligt Fælles Forbund",
    "municipality": "København"
  },
  {
    "name": "Pandora A/S",
    "municipality": "København"
  },
  {
    "name": "STORY HOUSE EGMONT A/S",
    "municipality": "København"
  },
  {
    "name": "NORDISK FILM A/S",
    "municipality": "København"
  },
  {
    "name": "HOUSE OF PRINCE A/S",
    "municipality": "København"
  },
  {
    "name": "GENMAB A/S",
    "municipality": "København"
  },
  {
    "name": "Maersk Product Tankers A/S",
    "municipality": "København"
  },
  {
    "name": "DSV Miljø Group A/S",
    "municipality": "København"
  },
  {
    "name": "SCANDFERRIES ApS",
    "municipality": "København"
  },
  {
    "name": "SUND OG BÆLT HOLDING A/S",
    "municipality": "København"
  },
  {
    "name": "WILLIAM COOK EUROPE ApS",
    "municipality": "Køge"
  },
  {
    "name": "F. JUNCKERS INDUSTRIER A/S",
    "municipality": "Køge"
  },
  {
    "name": "CP KELCO ApS",
    "municipality": "Køge"
  },
  {
    "name": "LOKALBUS A/S",
    "municipality": "Køge"
  },
  {
    "name": "CF PETERSEN & SØN A/S",
    "municipality": "Køge"
  },
  {
    "name": "Scantox A/S",
    "municipality": "Køge"
  },
  {
    "name": "FONDEN DBK",
    "municipality": "Køge"
  },
  {
    "name": "POSTNORD LOGISTICS A/S",
    "municipality": "Køge"
  },
  {
    "name": "DANA LIM A/S",
    "municipality": "Køge"
  },
  {
    "name": "DI-TEKNIK A/S",
    "municipality": "Køge"
  },
  {
    "name": "Strukton Rail A/S",
    "municipality": "Køge"
  },
  {
    "name": "SDK Shipping A/S",
    "municipality": "Køge"
  },
  {
    "name": "Novo Nordisk Pharmatech A/S",
    "municipality": "Køge"
  },
  {
    "name": "FOMACO A/S",
    "municipality": "Køge"
  },
  {
    "name": "The Whole Company Food A/S",
    "municipality": "Køge"
  },
  {
    "name": "Folkeligt Oplysningsforbund Køge/Vallø",
    "municipality": "Køge"
  },
  {
    "name": "OLE MOGENSEN A/S",
    "municipality": "Langeland"
  },
  {
    "name": "Danish Pilot Service ApS",
    "municipality": "Langeland"
  },
  {
    "name": "TJØRNTVED A/S",
    "municipality": "Langeland"
  },
  {
    "name": "TTS ApS",
    "municipality": "Langeland"
  },
  {
    "name": "RUBENLUND AGRO A/S",
    "municipality": "Langeland"
  },
  {
    "name": "GVCO ApS",
    "municipality": "Langeland"
  },
  {
    "name": "RISBJERG EL & KØLETEKNIK A/S",
    "municipality": "Langeland"
  },
  {
    "name": "TULLEBØLLE BRUGSFORENING",
    "municipality": "Langeland"
  },
  {
    "name": "HORSECREEK A/S",
    "municipality": "Langeland"
  },
  {
    "name": "FONDEN LANGELANDS ELFORSYNING",
    "municipality": "Langeland"
  },
  {
    "name": "HOU BRUGSFORENING",
    "municipality": "Langeland"
  },
  {
    "name": "PH-SERVICE A/S",
    "municipality": "Langeland"
  },
  {
    "name": "ALF JENSEN A/S. SPODSBJERG",
    "municipality": "Langeland"
  },
  {
    "name": "KÆDEBY MASKINFORRETNING A/S",
    "municipality": "Langeland"
  },
  {
    "name": "Rudkøbing Apotek",
    "municipality": "Langeland"
  },
  {
    "name": "STM VINDUER A/S",
    "municipality": "Langeland"
  },
  {
    "name": "DENWIND ApS",
    "municipality": "Langeland"
  },
  {
    "name": "Geveko Markings Denmark A/S",
    "municipality": "Langeland"
  },
  {
    "name": "DENCAM COMPOSITE A/S",
    "municipality": "Langeland"
  },
  {
    "name": "LANGELAND FORSYNING A/S",
    "municipality": "Langeland"
  },
  {
    "name": "RUDKØBING BRUGSFORENING",
    "municipality": "Langeland"
  },
  {
    "name": "HANDICAPFORMIDLINGEN ApS",
    "municipality": "Lejre"
  },
  {
    "name": "SPECIALSKOLEN BRAMSNÆSVIG'S DØGN OG AFLASTNINGSTILBUD ApS",
    "municipality": "Lejre"
  },
  {
    "name": "C5 VVS-TEKNIK A/S",
    "municipality": "Lejre"
  },
  {
    "name": "VVS-INSTALLATØR POUL CHRISTENSEN A/S",
    "municipality": "Lejre"
  },
  {
    "name": "OSTED AGRO ApS",
    "municipality": "Lejre"
  },
  {
    "name": "MENY Kirke Hyllinge ApS",
    "municipality": "Lejre"
  },
  {
    "name": "MM VISION A/S",
    "municipality": "Lejre"
  },
  {
    "name": "K.S. Multiservice ApS",
    "municipality": "Lejre"
  },
  {
    "name": "Opholdsstedet Hjortemarksgaard ApS",
    "municipality": "Lejre"
  },
  {
    "name": "HVALSØ SAVVÆRK A/S",
    "municipality": "Lejre"
  },
  {
    "name": "HANS JØRGEN POULSEN, 793 FLØNG ApS",
    "municipality": "Lejre"
  },
  {
    "name": "HERTHADALEN ApS",
    "municipality": "Lejre"
  },
  {
    "name": "PN Skoemagerkroen ApS",
    "municipality": "Lejre"
  },
  {
    "name": "Flemming Braasch, 431 Kirke Hyllinge ApS",
    "municipality": "Lejre"
  },
  {
    "name": "Spar Borrevejle ApS",
    "municipality": "Lejre"
  },
  {
    "name": "EUROPEAN FREEZE DRY ApS",
    "municipality": "Lejre"
  },
  {
    "name": "DKT A/S",
    "municipality": "Lejre"
  },
  {
    "name": "CONSTRUCTOR DANMARK A/S",
    "municipality": "Lejre"
  },
  {
    "name": "FONDEN SAGNLANDET LEJRE, HISTORISK-ARKÆOLOGISK FORSKNINGS- OG FORMIDLINGSCENTER",
    "municipality": "Lejre"
  },
  {
    "name": "FJ TRADING A/S BOLIG- OG INSTITUTIONSINVENTAR",
    "municipality": "Lejre"
  },
  {
    "name": "SCANTAGO A/S",
    "municipality": "Lejre"
  },
  {
    "name": "GRANLY DIESEL A/S",
    "municipality": "Lejre"
  },
  {
    "name": "HERSLEV BRYGHUS ApS",
    "municipality": "Lejre"
  },
  {
    "name": "Kirke Hvalsø-Særløse Kirkekasse",
    "municipality": "Lejre"
  },
  {
    "name": "Fjordskolen v/Ingvald Kamarinum",
    "municipality": "Lejre"
  },
  {
    "name": "Udlejningsejendom og udlejning til Ride-fysioterapi v/Frederik Kolmorgen Søndergaard",
    "municipality": "Lejre"
  },
  {
    "name": "Sonnerupgaard Gods v/Anders Puge Knudsen",
    "municipality": "Lejre"
  },
  {
    "name": "Midtsjællands Efterskole",
    "municipality": "Lejre"
  },
  {
    "name": "Shell Servicecenter v/Jesper Ravnholdt Frisenholm",
    "municipality": "Lejre"
  },
  {
    "name": "VESTERGAARD COMPANY A/S",
    "municipality": "Lejre"
  },
  {
    "name": "UNOMEDICAL A/S",
    "municipality": "Lejre"
  },
  {
    "name": "HVALSØ BRUGSFORENING",
    "municipality": "Lejre"
  },
  {
    "name": "OSTED FRI OG EFTERSKOLE",
    "municipality": "Lejre"
  },
  {
    "name": "TripleNine Thyborøn A/S",
    "municipality": "Lemvig"
  },
  {
    "name": "PELSDYRCENTER VESTJYLLAND A.M.B.A",
    "municipality": "Lemvig"
  },
  {
    "name": "CHEMINOVA A/S",
    "municipality": "Lemvig"
  },
  {
    "name": "VESTJYSK BANK A/S",
    "municipality": "Lemvig"
  },
  {
    "name": "Dan-Lat-Farms v/Jørgen Lind",
    "municipality": "Lemvig"
  },
  {
    "name": "THYBORØN SKIBSSMEDIE A/S",
    "municipality": "Lemvig"
  },
  {
    "name": "HETA A/S",
    "municipality": "Lemvig"
  },
  {
    "name": "STEEN JØRGENSEN. UDLEJNINGSBUREAU ApS",
    "municipality": "Lemvig"
  },
  {
    "name": "DANTRAFO A/S",
    "municipality": "Lemvig"
  },
  {
    "name": "IB G. JENSEN A/S",
    "municipality": "Lemvig"
  },
  {
    "name": "TMS Invest A/S",
    "municipality": "Lemvig"
  },
  {
    "name": "DANSKE FISKEAUKTIONER A/S",
    "municipality": "Lemvig"
  },
  {
    "name": "JEKA FISH A/S",
    "municipality": "Lemvig"
  },
  {
    "name": "KYNDE OG TOFT",
    "municipality": "Lemvig"
  },
  {
    "name": "AKTIV-EL A/S",
    "municipality": "Lolland"
  },
  {
    "name": "RASK EL-SERVICE ApS",
    "municipality": "Lolland"
  },
  {
    "name": "SB PETERS A/S",
    "municipality": "Lolland"
  },
  {
    "name": "JOHANNES MERTZ A/S",
    "municipality": "Lolland"
  },
  {
    "name": "VIKIMA SEED A/S",
    "municipality": "Lolland"
  },
  {
    "name": "RUSTFRI DK DESIGN ApS",
    "municipality": "Lolland"
  },
  {
    "name": "LOLLAND FORSYNING A/S",
    "municipality": "Lolland"
  },
  {
    "name": "EURO-WORKERS A/S",
    "municipality": "Lolland"
  },
  {
    "name": "SOFTLINE A/S",
    "municipality": "Lolland"
  },
  {
    "name": "AUTO CENTRO A/S",
    "municipality": "Lolland"
  },
  {
    "name": "LOLLANDS BANK A/S",
    "municipality": "Lolland"
  },
  {
    "name": "K.F. Entreprise ApS",
    "municipality": "Lolland"
  },
  {
    "name": "AKTIESELSKABET P. HATTEN & CO",
    "municipality": "Lolland"
  },
  {
    "name": "Claus Sørensen, 758 Nakskov ApS",
    "municipality": "Lolland"
  },
  {
    "name": "CODAN MEDICAL ApS",
    "municipality": "Lolland"
  },
  {
    "name": "ORTOFON A/S",
    "municipality": "Lolland"
  },
  {
    "name": "NORDIC AIR FILTRATION A/S",
    "municipality": "Lolland"
  },
  {
    "name": "MariboHilleshög ApS",
    "municipality": "Lolland"
  },
  {
    "name": "ALFA LAVAL NAKSKOV A/S",
    "municipality": "Lolland"
  },
  {
    "name": "VIKAR SPECIALISTEN ApS",
    "municipality": "Lolland"
  },
  {
    "name": "LALANDIA A/S",
    "municipality": "Lolland"
  },
  {
    "name": "NOVASOL A/S",
    "municipality": "Lyngby-Taarbæk"
  },
  {
    "name": "HALDOR TOPSØE A/S",
    "municipality": "Lyngby-Taarbæk"
  },
  {
    "name": "SATS Danmark A/S",
    "municipality": "Lyngby-Taarbæk"
  },
  {
    "name": "COWI A/S",
    "municipality": "Lyngby-Taarbæk"
  },
  {
    "name": "MAERSK DRILLING A/S",
    "municipality": "Lyngby-Taarbæk"
  },
  {
    "name": "THRANE & THRANE A/S",
    "municipality": "Lyngby-Taarbæk"
  },
  {
    "name": "JOHANNES FOG A/S",
    "municipality": "Lyngby-Taarbæk"
  },
  {
    "name": "NNE A/S",
    "municipality": "Lyngby-Taarbæk"
  },
  {
    "name": "The Drilling Company of 1972 A/S",
    "municipality": "Lyngby-Taarbæk"
  },
  {
    "name": "JAN NYGAARD A/S",
    "municipality": "Lyngby-Taarbæk"
  },
  {
    "name": "HEMPEL A/S",
    "municipality": "Lyngby-Taarbæk"
  },
  {
    "name": "KX A/S",
    "municipality": "Lyngby-Taarbæk"
  },
  {
    "name": "MICROSOFT DEVELOPMENT CENTER COPENHAGEN ApS",
    "municipality": "Lyngby-Taarbæk"
  },
  {
    "name": "MICROSOFT DANMARK ApS",
    "municipality": "Lyngby-Taarbæk"
  },
  {
    "name": "Newsec Property Asset Management Denmark A/S",
    "municipality": "Lyngby-Taarbæk"
  },
  {
    "name": "BPA Support ApS",
    "municipality": "Lyngby-Taarbæk"
  },
  {
    "name": "A/S LÆSØ FISKEINDUSTRI",
    "municipality": "Læsø"
  },
  {
    "name": "Færgeselskabet Læsø K/S",
    "municipality": "Læsø"
  },
  {
    "name": "SUPERBRUGSEN BYRUM",
    "municipality": "Læsø"
  },
  {
    "name": "KNAUF A/S",
    "municipality": "Mariagerfjord"
  },
  {
    "name": "JKF INDUSTRI A/S",
    "municipality": "Mariagerfjord"
  },
  {
    "name": "AGRI-NORCOLD A/S",
    "municipality": "Mariagerfjord"
  },
  {
    "name": "DS STÅLKONSTRUKTION A/S",
    "municipality": "Mariagerfjord"
  },
  {
    "name": "Dansk Salt A/S",
    "municipality": "Mariagerfjord"
  },
  {
    "name": "SSI SCHÄFER A/S",
    "municipality": "Mariagerfjord"
  },
  {
    "name": "Körber Supply Chain DK A/S",
    "municipality": "Mariagerfjord"
  },
  {
    "name": "NOPA NORDIC A/S",
    "municipality": "Mariagerfjord"
  },
  {
    "name": "DAVA Foods Denmark A/S",
    "municipality": "Mariagerfjord"
  },
  {
    "name": "SKIVE KØLETRANSPORT A/S",
    "municipality": "Mariagerfjord"
  },
  {
    "name": "ASSA ABLOY ENTRANCE SYSTEMS DENMARK A/S",
    "municipality": "Mariagerfjord"
  },
  {
    "name": "Midsona Danmark A/S",
    "municipality": "Mariagerfjord"
  },
  {
    "name": "DS ELCOBYG A/S",
    "municipality": "Mariagerfjord"
  },
  {
    "name": "SINTEX A/S",
    "municipality": "Mariagerfjord"
  },
  {
    "name": "A/S UNITED SHIPPING & TRADING COMPANY",
    "municipality": "Middelfart"
  },
  {
    "name": "T. HANSEN GRUPPEN A/S",
    "municipality": "Middelfart"
  },
  {
    "name": "FOCUS PEOPLE A/S",
    "municipality": "Middelfart"
  },
  {
    "name": "MIDDELFART SPAREKASSE",
    "municipality": "Middelfart"
  },
  {
    "name": "ITW CONSTRUCTION PRODUCTS ApS",
    "municipality": "Middelfart"
  },
  {
    "name": "BRUGSFORENINGEN FOR MIDDELFART OG OMEGN",
    "municipality": "Middelfart"
  },
  {
    "name": "FIBERLINE COMPOSITES A/S",
    "municipality": "Middelfart"
  },
  {
    "name": "MUEHLHAN A/S",
    "municipality": "Middelfart"
  },
  {
    "name": "JACOBS DOUWE EGBERTS DK ApS",
    "municipality": "Middelfart"
  },
  {
    "name": "CARL HANSEN & SØN MØBELFABRIK A/S",
    "municipality": "Middelfart"
  },
  {
    "name": "OUTRUP VINDUER & DØRE A/S",
    "municipality": "Morsø"
  },
  {
    "name": "HE-VA ApS",
    "municipality": "Morsø"
  },
  {
    "name": "Imers Industries ApS",
    "municipality": "Morsø"
  },
  {
    "name": "THY-MORS ENERGI HOLDING A/S",
    "municipality": "Morsø"
  },
  {
    "name": "MALTE HAANING PLASTIC A/S",
    "municipality": "Morsø"
  },
  {
    "name": "DENCKER A/S",
    "municipality": "Morsø"
  },
  {
    "name": "MOLLERUP MØLLE A/S",
    "municipality": "Morsø"
  },
  {
    "name": "MTH Biler A/S",
    "municipality": "Morsø"
  },
  {
    "name": "Worm ApS",
    "municipality": "Morsø"
  },
  {
    "name": "ENTREPRENØR ERLING JENSEN A/S",
    "municipality": "Morsø"
  },
  {
    "name": "MORSØ JERNSTØBERI A/S",
    "municipality": "Morsø"
  },
  {
    "name": "ORNESTATION MORS ApS",
    "municipality": "Morsø"
  },
  {
    "name": "KUNSTSTOF-KEMI. SKANDINAVIA A/S",
    "municipality": "Morsø"
  },
  {
    "name": "VILS ENTREPRENØRFORRETNING A/S",
    "municipality": "Morsø"
  },
  {
    "name": "VILSUND BLUE A/S",
    "municipality": "Morsø"
  },
  {
    "name": "JESPERHUS RESORT ApS",
    "municipality": "Morsø"
  },
  {
    "name": "KPK DØRE OG VINDUER A/S",
    "municipality": "Morsø"
  },
  {
    "name": "BILA A/S",
    "municipality": "Morsø"
  },
  {
    "name": "DFI-GEISLER A/S",
    "municipality": "Morsø"
  },
  {
    "name": "TØMMERGAARDEN A/S",
    "municipality": "Morsø"
  },
  {
    "name": "VAM A/S",
    "municipality": "Norddjurs"
  },
  {
    "name": "HSM INDUSTRI A/S",
    "municipality": "Norddjurs"
  },
  {
    "name": "L-TEK A/S",
    "municipality": "Norddjurs"
  },
  {
    "name": "DAVAI ApS",
    "municipality": "Norddjurs"
  },
  {
    "name": "DE DANSKE GÆRFABRIKKER A/S",
    "municipality": "Norddjurs"
  },
  {
    "name": "DANCARROT ApS",
    "municipality": "Norddjurs"
  },
  {
    "name": "DS SMITH PACKAGING DENMARK A/S",
    "municipality": "Norddjurs"
  },
  {
    "name": "DJURSLANDS BANK A/S",
    "municipality": "Norddjurs"
  },
  {
    "name": "TERMA AEROSTRUCTURES A/S",
    "municipality": "Norddjurs"
  },
  {
    "name": "MURERFIRMAET BENT KLAUSEN ApS",
    "municipality": "Norddjurs"
  },
  {
    "name": "KYSTVEJENS KONFERENCECENTER A/S",
    "municipality": "Norddjurs"
  },
  {
    "name": "DERKETEK ApS",
    "municipality": "Norddjurs"
  },
  {
    "name": "GLESBORG BRUGSFORENING",
    "municipality": "Norddjurs"
  },
  {
    "name": "JOHNSEN GRAPHIC SOLUTIONS A/S",
    "municipality": "Norddjurs"
  },
  {
    "name": "HUJ A/S",
    "municipality": "Norddjurs"
  },
  {
    "name": "Activ Rengøring Grenaa ApS",
    "municipality": "Norddjurs"
  },
  {
    "name": "BRUGSEN AUNING",
    "municipality": "Norddjurs"
  },
  {
    "name": "NØRGAARD TEKNIK A/S",
    "municipality": "Norddjurs"
  },
  {
    "name": "VOGNMANDSFIRMAET GERT SVITH A/S",
    "municipality": "Norddjurs"
  },
  {
    "name": "RASMUS JAKOBSEN A/S",
    "municipality": "Norddjurs"
  },
  {
    "name": "RYGAARD TRANSPORT & LOGISTIC A/S",
    "municipality": "Norddjurs"
  },
  {
    "name": "BORDING LINK A/S",
    "municipality": "Norddjurs"
  },
  {
    "name": "ÅLSRODE SMEDE- OG MASKINFABRIK A/S",
    "municipality": "Norddjurs"
  },
  {
    "name": "GL. ESTRUP GARTNERI A/S",
    "municipality": "Norddjurs"
  },
  {
    "name": "FOF-Djursland",
    "municipality": "Norddjurs"
  },
  {
    "name": "RENO DJURS I/S",
    "municipality": "Norddjurs"
  },
  {
    "name": "KATTEGATCENTRETS DRIFTSFOND",
    "municipality": "Norddjurs"
  },
  {
    "name": "SØNDERSØ BRUGSFORENING",
    "municipality": "Nordfyns"
  },
  {
    "name": "SENMATIC A/S",
    "municipality": "Nordfyns"
  },
  {
    "name": "BOGENSE PLAST A/S",
    "municipality": "Nordfyns"
  },
  {
    "name": "LP BOGENSE ApS",
    "municipality": "Nordfyns"
  },
  {
    "name": "HAARSLEV GROUP A/S",
    "municipality": "Nordfyns"
  },
  {
    "name": "REA AUTOMATDREJNING ApS",
    "municipality": "Nordfyns"
  },
  {
    "name": "TINBY A/S",
    "municipality": "Nordfyns"
  },
  {
    "name": "Strandvejen Otterup ApS",
    "municipality": "Nordfyns"
  },
  {
    "name": "HAARSLEV INDUSTRIES A/S",
    "municipality": "Nordfyns"
  },
  {
    "name": "ORKLA CONFECTIONERY & SNACKS DANMARK A/S",
    "municipality": "Nordfyns"
  },
  {
    "name": "MUNCK FORSYNINGSLEDNINGER A/S",
    "municipality": "Nyborg"
  },
  {
    "name": "TENAX SILD A/S",
    "municipality": "Nyborg"
  },
  {
    "name": "MR Restaurants ApS",
    "municipality": "Nyborg"
  },
  {
    "name": "Fortum Waste Solutions A/S",
    "municipality": "Nyborg"
  },
  {
    "name": "DALOON A/S",
    "municipality": "Nyborg"
  },
  {
    "name": "YOUR PARTNER ApS",
    "municipality": "Nyborg"
  },
  {
    "name": "Trioworld Nyborg A/S",
    "municipality": "Nyborg"
  },
  {
    "name": "HOTEL NYBORG STRAND A/S",
    "municipality": "Nyborg"
  },
  {
    "name": "MUNCK ASFALT A/S",
    "municipality": "Nyborg"
  },
  {
    "name": "Scan Facility Service ApS",
    "municipality": "Nyborg"
  },
  {
    "name": "ARDO A/S",
    "municipality": "Nyborg"
  },
  {
    "name": "ELLINGE SMEDIE A/S",
    "municipality": "Nyborg"
  },
  {
    "name": "WITZEL VIKAR ApS",
    "municipality": "Nyborg"
  },
  {
    "name": "NYBORG FORSYNING OG SERVICE A/S",
    "municipality": "Nyborg"
  },
  {
    "name": "MUNCK HAVNE & ANLÆG A/S",
    "municipality": "Nyborg"
  },
  {
    "name": "KOPPERS DENMARK ApS",
    "municipality": "Nyborg"
  },
  {
    "name": "Dansk Firmaidrætsforbund",
    "municipality": "Nyborg"
  },
  {
    "name": "HOS TINE P. BLOMSTERVÆRKSTED V/JONNA DUELUND PETERSEN",
    "municipality": "Nyborg"
  },
  {
    "name": "HOLBØLL A/S",
    "municipality": "Næstved"
  },
  {
    "name": "NAESBORG A/S",
    "municipality": "Næstved"
  },
  {
    "name": "NOVENCO BUILDING & INDUSTRY A/S",
    "municipality": "Næstved"
  },
  {
    "name": "SAINT-GOBAIN ECOPHON A/S",
    "municipality": "Næstved"
  },
  {
    "name": "EVIDENSIA DYREHOSPITAL A/S",
    "municipality": "Næstved"
  },
  {
    "name": "HOWDEN AXIAL FANS ApS",
    "municipality": "Næstved"
  },
  {
    "name": "H. NIELSEN & SØN A/S",
    "municipality": "Næstved"
  },
  {
    "name": "FREDE ANDERSEN & SØN A/S",
    "municipality": "Næstved"
  },
  {
    "name": "LOKAL FORSIKRING G/S",
    "municipality": "Næstved"
  },
  {
    "name": "FENSMARK BRUGSFORENING A.M.B.A.",
    "municipality": "Næstved"
  },
  {
    "name": "DAMCOS A/S",
    "municipality": "Næstved"
  },
  {
    "name": "Midt- og Sydsjællands Brand & Redning I/S",
    "municipality": "Næstved"
  },
  {
    "name": "Tvedemose Champignon v/Jens Chr. Hansen",
    "municipality": "Næstved"
  },
  {
    "name": "Solgaven Specialplejeboliger for synshandicappede",
    "municipality": "Næstved"
  },
  {
    "name": "SOS VIKAR A/S",
    "municipality": "Næstved"
  },
  {
    "name": "BONBON-LAND A/S",
    "municipality": "Næstved"
  },
  {
    "name": "ARDAGH GLASS HOLMEGAARD A/S",
    "municipality": "Næstved"
  },
  {
    "name": "I/S AffaldPlus",
    "municipality": "Næstved"
  },
  {
    "name": "Driftsfonden Marjatta",
    "municipality": "Næstved"
  },
  {
    "name": "Dinel A/S",
    "municipality": "Odder"
  },
  {
    "name": "SIMPSON STRONG-TIE A/S",
    "municipality": "Odder"
  },
  {
    "name": "IDE RENGØRING ApS",
    "municipality": "Odder"
  },
  {
    "name": "OLE NONBYE A/S",
    "municipality": "Odder"
  },
  {
    "name": "PROTRUCK A/S",
    "municipality": "Odder"
  },
  {
    "name": "VB Gruppen ApS",
    "municipality": "Odder"
  },
  {
    "name": "HESSELLUND EL A/S",
    "municipality": "Odder"
  },
  {
    "name": "ODDER PARKHOTEL ApS",
    "municipality": "Odder"
  },
  {
    "name": "STAERMOSE INDUSTRY A/S",
    "municipality": "Odder"
  },
  {
    "name": "DEN ALMENNYTTIGE FOND HADRUPLUND",
    "municipality": "Odder"
  },
  {
    "name": "Tornsbjerggårdfonden",
    "municipality": "Odder"
  },
  {
    "name": "SYSTEM TM A/S",
    "municipality": "Odder"
  },
  {
    "name": "KVICKLY ODDER",
    "municipality": "Odder"
  },
  {
    "name": "HARALD NYBORG A/S",
    "municipality": "Odense"
  },
  {
    "name": "Compass Group FS Denmark A/S",
    "municipality": "Odense"
  },
  {
    "name": "FTZ AUTODELE & VÆRKTØJ A/S",
    "municipality": "Odense"
  },
  {
    "name": "TV2/DANMARK A/S",
    "municipality": "Odense"
  },
  {
    "name": "TIDE BUS DANMARK A/S",
    "municipality": "Odense"
  },
  {
    "name": "JENSEN'S BØFHUS A/S",
    "municipality": "Odense"
  },
  {
    "name": "DANREN BOGDOL A/S",
    "municipality": "Odense"
  },
  {
    "name": "BlueCollar A/S",
    "municipality": "Odense"
  },
  {
    "name": "OBI SPORT A/S",
    "municipality": "Odense"
  },
  {
    "name": "GASA GROUP DENMARK A/S",
    "municipality": "Odense"
  },
  {
    "name": "NIELSEN'S A/S",
    "municipality": "Odense"
  },
  {
    "name": "Geopartner Landinspektører A/S",
    "municipality": "Odense"
  },
  {
    "name": "GF FORSIKRING A/S",
    "municipality": "Odense"
  },
  {
    "name": "P. CHRISTENSEN A/S",
    "municipality": "Odense"
  },
  {
    "name": "UNIVERSAL ROBOTS A/S",
    "municipality": "Odense"
  },
  {
    "name": "Værsgo A/S",
    "municipality": "Odense"
  },
  {
    "name": "Euro Site Services ApS",
    "municipality": "Odense"
  },
  {
    "name": "ODENSE SPORT & EVENT A/S",
    "municipality": "Odense"
  },
  {
    "name": "Fjernvarme Fyn Service A/S",
    "municipality": "Odense"
  },
  {
    "name": "JJ INVEST FYN A/S",
    "municipality": "Odense"
  },
  {
    "name": "ALEX ANDERSEN. ØLUND A/S",
    "municipality": "Odense"
  },
  {
    "name": "3C RETAIL A/S",
    "municipality": "Odense"
  },
  {
    "name": "ALUMECO A/S",
    "municipality": "Odense"
  },
  {
    "name": "Nagel Liller A/S",
    "municipality": "Odense"
  },
  {
    "name": "VKAREN.DK ApS",
    "municipality": "Odense"
  },
  {
    "name": "CATERING DANMARK ApS",
    "municipality": "Odense"
  },
  {
    "name": "GASA ODENSE - BLOMSTER A.M.B.A.",
    "municipality": "Odense"
  },
  {
    "name": "HANSSON & KNUDSEN A/S",
    "municipality": "Odense"
  },
  {
    "name": "C.A. LARSEN AUTOMOBILER A/S",
    "municipality": "Odense"
  },
  {
    "name": "COMWELL H.C. ANDERSEN ODENSE A/S",
    "municipality": "Odense"
  },
  {
    "name": "Fyens Stift",
    "municipality": "Odense"
  },
  {
    "name": "Civica",
    "municipality": "Odense"
  },
  {
    "name": "THORNICO A/S",
    "municipality": "Odense"
  },
  {
    "name": "ORIFARM A/S",
    "municipality": "Odense"
  },
  {
    "name": "R & S MADSEN ApS",
    "municipality": "Odsherred"
  },
  {
    "name": "ASNÆS OG OMEGNS BRUGSFORENING",
    "municipality": "Odsherred"
  },
  {
    "name": "NKT (Denmark) A/S",
    "municipality": "Odsherred"
  },
  {
    "name": "Storøhage Kartofler ApS",
    "municipality": "Odsherred"
  },
  {
    "name": "HØJBY SJÆLLAND BRUGSFORENING",
    "municipality": "Odsherred"
  },
  {
    "name": "KAJ LARSEN A/S",
    "municipality": "Odsherred"
  },
  {
    "name": "POUL JOHANSEN MASKINER A/S",
    "municipality": "Odsherred"
  },
  {
    "name": "YRSAS RENGØRING A/S",
    "municipality": "Odsherred"
  },
  {
    "name": "DRAGSHOLM SLOT P/S",
    "municipality": "Odsherred"
  },
  {
    "name": "Flux A/S",
    "municipality": "Odsherred"
  },
  {
    "name": "VIG BRUGSFORENING",
    "municipality": "Odsherred"
  },
  {
    "name": "NYKØBING SJÆLLAND OG OMEGNS BRUGSFORENING",
    "municipality": "Odsherred"
  },
  {
    "name": "VORUP TØMMERHANDEL OG BYGGECENTER A/S",
    "municipality": "Randers"
  },
  {
    "name": "PEDERSEN & NIELSEN AUTOMOBILFORRETNING A/S",
    "municipality": "Randers"
  },
  {
    "name": "MEDFLEX A/S",
    "municipality": "Randers"
  },
  {
    "name": "KOSAN CRISPLANT A/S",
    "municipality": "Randers"
  },
  {
    "name": "CARELINK A/S",
    "municipality": "Randers"
  },
  {
    "name": "DANISH STEVEDORE A/S",
    "municipality": "Randers"
  },
  {
    "name": "Danish Crown Foods A/S",
    "municipality": "Randers"
  },
  {
    "name": "HR-INDUSTRIES A/S",
    "municipality": "Randers"
  },
  {
    "name": "PRODAN A/S",
    "municipality": "Randers"
  },
  {
    "name": "RANDERS FC A/S",
    "municipality": "Randers"
  },
  {
    "name": "ID-SPARINVEST, FILIAL AF SPARINVEST S.A., LUXEMBOURG",
    "municipality": "Randers"
  },
  {
    "name": "DANISH CROWN A/S",
    "municipality": "Randers"
  },
  {
    "name": "Kvist & Jensen Statsautoriseret Revisionspartnerselskab",
    "municipality": "Randers"
  },
  {
    "name": "VERDO TEKNIK A/S",
    "municipality": "Randers"
  },
  {
    "name": "Sekura Cabins A/S",
    "municipality": "Randers"
  },
  {
    "name": "HOUNØ A/S",
    "municipality": "Randers"
  },
  {
    "name": "SPAREKASSEN KRONJYLLAND",
    "municipality": "Randers"
  },
  {
    "name": "CONFAC A/S",
    "municipality": "Randers"
  },
  {
    "name": "DERMA PHARM A/S",
    "municipality": "Randers"
  },
  {
    "name": "PM Salon Group A/S",
    "municipality": "Randers"
  },
  {
    "name": "VPK PACKAGING A/S",
    "municipality": "Randers"
  },
  {
    "name": "VINK PLAST ApS",
    "municipality": "Randers"
  },
  {
    "name": "THORTRANS A/S",
    "municipality": "Randers"
  },
  {
    "name": "BACH & PEDERSEN FRAGT A/S",
    "municipality": "Randers"
  },
  {
    "name": "EJENDOMSMÆGLERFIRMAET JOHN FRANDSEN A/S",
    "municipality": "Randers"
  },
  {
    "name": "LIMO LABELS A/S",
    "municipality": "Randers"
  },
  {
    "name": "CCL LABEL A/S",
    "municipality": "Randers"
  },
  {
    "name": "Beredskab og Sikkerhed - Randers Favrskov Djursland I/S",
    "municipality": "Randers"
  },
  {
    "name": "FONDEN FOR RANDERS REGNSKOV",
    "municipality": "Randers"
  },
  {
    "name": "AMKA I/S",
    "municipality": "Randers"
  },
  {
    "name": "BQ Administration v/Carina Dahl",
    "municipality": "Randers"
  },
  {
    "name": "Jysk Dyretransport A/S",
    "municipality": "Rebild"
  },
  {
    "name": "HAGENS FJEDRE A/S",
    "municipality": "Rebild"
  },
  {
    "name": "MANFORCE NORDIC ApS",
    "municipality": "Rebild"
  },
  {
    "name": "COMWELL REBILD BAKKER A/S",
    "municipality": "Rebild"
  },
  {
    "name": "LIFTUP A/S",
    "municipality": "Rebild"
  },
  {
    "name": "Seritronic A/S",
    "municipality": "Rebild"
  },
  {
    "name": "DTEK A/S",
    "municipality": "Rebild"
  },
  {
    "name": "A.E. STÅLMONTAGE A/S",
    "municipality": "Rebild"
  },
  {
    "name": "AS Solvarmeservice A/S",
    "municipality": "Rebild"
  },
  {
    "name": "A/S HYDREMA DANMARK",
    "municipality": "Rebild"
  },
  {
    "name": "DALI A/S",
    "municipality": "Rebild"
  },
  {
    "name": "Rold Storkro I/S v/Jørgen Pedersen/Lars Kæp Jensen",
    "municipality": "Rebild"
  },
  {
    "name": "Sønderup Landkøkken v/Dorthe Nørhave Johansen",
    "municipality": "Rebild"
  },
  {
    "name": "AudioNord International A/S",
    "municipality": "Rebild"
  },
  {
    "name": "A/S HYDREMA PRODUKTION",
    "municipality": "Rebild"
  },
  {
    "name": "TERNDRUP TAXA OG TURISTBUSSER A/S",
    "municipality": "Rebild"
  },
  {
    "name": "ALDI HAVERSLEV K/S",
    "municipality": "Rebild"
  },
  {
    "name": "AMBERCON A/S",
    "municipality": "Rebild"
  },
  {
    "name": "SAWO A/S",
    "municipality": "Rebild"
  },
  {
    "name": "MEKOPRINT A/S",
    "municipality": "Rebild"
  },
  {
    "name": "MAREL SALMON A/S",
    "municipality": "Rebild"
  },
  {
    "name": "VEN-TO ApS",
    "municipality": "Ringkøbing-Skjern"
  },
  {
    "name": "Baettr Lem A/S",
    "municipality": "Ringkøbing-Skjern"
  },
  {
    "name": "JSB GROUP A/S",
    "municipality": "Ringkøbing-Skjern"
  },
  {
    "name": "EAGLEBURGMANN KE A/S",
    "municipality": "Ringkøbing-Skjern"
  },
  {
    "name": "SKJERN BANK A/S",
    "municipality": "Ringkøbing-Skjern"
  },
  {
    "name": "LIND JENSENS MASKINFABRIK A/S",
    "municipality": "Ringkøbing-Skjern"
  },
  {
    "name": "A/S HVIDE SANDE SKIBS- OG BAADEBYGGERI",
    "municipality": "Ringkøbing-Skjern"
  },
  {
    "name": "A/S HENRY KJELDSEN",
    "municipality": "Ringkøbing-Skjern"
  },
  {
    "name": "RINGKJØBING LANDBOBANK. AKTIESELSKAB",
    "municipality": "Ringkøbing-Skjern"
  },
  {
    "name": "HENRY KJELDSEN. RINGKØBING TØMMERHANDEL A/S",
    "municipality": "Ringkøbing-Skjern"
  },
  {
    "name": "JKS A/S",
    "municipality": "Ringkøbing-Skjern"
  },
  {
    "name": "HSHANSEN A/S",
    "municipality": "Ringkøbing-Skjern"
  },
  {
    "name": "VESTJYLLANDS ANDEL A.M.B.A.",
    "municipality": "Ringkøbing-Skjern"
  },
  {
    "name": "BOUMATIC A/S",
    "municipality": "Ringkøbing-Skjern"
  },
  {
    "name": "GÅSDAL BYGNINGSINDUSTRI A/S",
    "municipality": "Ringkøbing-Skjern"
  },
  {
    "name": "KP Components A/S",
    "municipality": "Ringkøbing-Skjern"
  },
  {
    "name": "Industri Beton A/S",
    "municipality": "Ringkøbing-Skjern"
  },
  {
    "name": "VM TARM A/S",
    "municipality": "Ringkøbing-Skjern"
  },
  {
    "name": "HydraSpecma A/S",
    "municipality": "Ringkøbing-Skjern"
  },
  {
    "name": "ESMARK FERIEHUSUDLEJNING A/S",
    "municipality": "Ringkøbing-Skjern"
  },
  {
    "name": "KRAMP DANMARK A/S",
    "municipality": "Ringkøbing-Skjern"
  },
  {
    "name": "Lokaltog A/S",
    "municipality": "Ringsted"
  },
  {
    "name": "TITAN LASTVOGNE A/S",
    "municipality": "Ringsted"
  },
  {
    "name": "TØMRERMESTER BO FILTENBORG BORUP ApS",
    "municipality": "Ringsted"
  },
  {
    "name": "Sørup Herregaard A/S",
    "municipality": "Ringsted"
  },
  {
    "name": "VELTEC INDUSTRIAL SERVICES A/S",
    "municipality": "Ringsted"
  },
  {
    "name": "Aleris Hamlet Ringsted A/S",
    "municipality": "Ringsted"
  },
  {
    "name": "SJÆLLANDSKE MEDIER A/S",
    "municipality": "Ringsted"
  },
  {
    "name": "Dagrofa ApS",
    "municipality": "Ringsted"
  },
  {
    "name": "ENEMÆRKE & PETERSEN A/S",
    "municipality": "Ringsted"
  },
  {
    "name": "EHB-Montøren A/S",
    "municipality": "Ringsted"
  },
  {
    "name": "GS SEACON ApS",
    "municipality": "Ringsted"
  },
  {
    "name": "CS-Online A/S",
    "municipality": "Ringsted"
  },
  {
    "name": "PLASTMO A/S",
    "municipality": "Ringsted"
  },
  {
    "name": "HEIDELBERGCEMENT NORTHERN EUROPE PUMPS AND TRUCKS A/S",
    "municipality": "Ringsted"
  },
  {
    "name": "EUROWRAP A/S",
    "municipality": "Ringsted"
  },
  {
    "name": "Glunz & Jensen A/S",
    "municipality": "Ringsted"
  },
  {
    "name": "WATSON-MARLOW FLEXICON A/S",
    "municipality": "Ringsted"
  },
  {
    "name": "A/S BEVOLA",
    "municipality": "Ringsted"
  },
  {
    "name": "AB-ELCO A/S",
    "municipality": "Ringsted"
  },
  {
    "name": "ENGSKOV MASKINFABRIK A/S",
    "municipality": "Ringsted"
  },
  {
    "name": "DK BETON A/S",
    "municipality": "Ringsted"
  },
  {
    "name": "HBN - TEKNIK A/S",
    "municipality": "Ringsted"
  },
  {
    "name": "MOCON Europe A/S",
    "municipality": "Ringsted"
  },
  {
    "name": "PP JENSEN A/S",
    "municipality": "Ringsted"
  },
  {
    "name": "Sofaco Design ApS",
    "municipality": "Ringsted"
  },
  {
    "name": "ØSTAGERGÅRD",
    "municipality": "Ringsted"
  },
  {
    "name": "FORENINGEN SØGAARDEN",
    "municipality": "Ringsted"
  },
  {
    "name": "I.M. FRELLSEN K/S",
    "municipality": "Roskilde"
  },
  {
    "name": "PLEJEVIKAR ApS",
    "municipality": "Roskilde"
  },
  {
    "name": "LYRECO DANMARK A/S",
    "municipality": "Roskilde"
  },
  {
    "name": "VIKARCOMPAGNIET ApS",
    "municipality": "Roskilde"
  },
  {
    "name": "STRYHNS A/S",
    "municipality": "Roskilde"
  },
  {
    "name": "DLF Seeds A/S",
    "municipality": "Roskilde"
  },
  {
    "name": "NUNC A/S",
    "municipality": "Roskilde"
  },
  {
    "name": "Boligselskabet Sjælland",
    "municipality": "Roskilde"
  },
  {
    "name": "ROSKILDE STIFTØVRIGHED",
    "municipality": "Roskilde"
  },
  {
    "name": "CRH CONCRETE A/S",
    "municipality": "Roskilde"
  },
  {
    "name": "BANKERNES EDB CENTRAL A.M.B.A.",
    "municipality": "Roskilde"
  },
  {
    "name": "Urbaser A/S",
    "municipality": "Roskilde"
  },
  {
    "name": "MENY Nærumvænge Torv I/S",
    "municipality": "Rudersdal"
  },
  {
    "name": "SiccaDania A/S",
    "municipality": "Rudersdal"
  },
  {
    "name": "MANSOFT A/S",
    "municipality": "Rudersdal"
  },
  {
    "name": "DCC ENERGI CENTER A/S",
    "municipality": "Rudersdal"
  },
  {
    "name": "CHR. HANSEN NATURAL COLORS A/S",
    "municipality": "Rudersdal"
  },
  {
    "name": "INEOS E&P A/S",
    "municipality": "Rudersdal"
  },
  {
    "name": "TRIUMPH INTERNATIONAL TEXTIL A/S",
    "municipality": "Rudersdal"
  },
  {
    "name": "NOVAFOS A/S",
    "municipality": "Rudersdal"
  },
  {
    "name": "NKT PHOTONICS A/S",
    "municipality": "Rudersdal"
  },
  {
    "name": "Hottinger Brüel & Kjær A/S",
    "municipality": "Rudersdal"
  },
  {
    "name": "TRACKMAN A/S",
    "municipality": "Rudersdal"
  },
  {
    "name": "DE BLAA OMNIBUSSER A/S",
    "municipality": "Rudersdal"
  },
  {
    "name": "G.R.A.S. SOUND & VIBRATION ApS",
    "municipality": "Rudersdal"
  },
  {
    "name": "Dinesen - Sjælsø Holding ApS",
    "municipality": "Rudersdal"
  },
  {
    "name": "Umicore Denmark ApS",
    "municipality": "Rudersdal"
  },
  {
    "name": "Willis Towers Watson I/S",
    "municipality": "Rudersdal"
  },
  {
    "name": "KURHOTEL SKODSBORG A/S",
    "municipality": "Rudersdal"
  },
  {
    "name": "EET GROUP A/S",
    "municipality": "Rudersdal"
  },
  {
    "name": "PANKAS A/S",
    "municipality": "Rudersdal"
  },
  {
    "name": "DEN SELVEJENDE INSTITUTION LIONS PARK BIRKERØD",
    "municipality": "Rudersdal"
  },
  {
    "name": "FONDEN LIONS PARK SØLLERØD",
    "municipality": "Rudersdal"
  },
  {
    "name": "ACTIVCARE A/S",
    "municipality": "Rudersdal"
  },
  {
    "name": "CHR. HANSEN A/S",
    "municipality": "Rudersdal"
  },
  {
    "name": "ALK-ABELLÓ A/S",
    "municipality": "Rudersdal"
  },
  {
    "name": "FITNESS WORLD A/S",
    "municipality": "Rødovre"
  },
  {
    "name": "TOLKDANMARK ApS",
    "municipality": "Rødovre"
  },
  {
    "name": "PETRI & HAUGSTED A/S",
    "municipality": "Rødovre"
  },
  {
    "name": "Flügger group A/S",
    "municipality": "Rødovre"
  },
  {
    "name": "BABYSAM A/S",
    "municipality": "Rødovre"
  },
  {
    "name": "A/S BLADKOMPAGNIET",
    "municipality": "Rødovre"
  },
  {
    "name": "CHRISTOFFERSEN & KNUDSEN A/S",
    "municipality": "Rødovre"
  },
  {
    "name": "C. MØLLMANN & CO. A/S",
    "municipality": "Rødovre"
  },
  {
    "name": "S.E. Dagligvarer A/S",
    "municipality": "Rødovre"
  },
  {
    "name": "Business Danmark",
    "municipality": "Rødovre"
  },
  {
    "name": "PTU (UlykkesPatientForeningen, PolioForeningen, Specialhospital for Polio- og Ulykkespatienter)",
    "municipality": "Rødovre"
  },
  {
    "name": "Dorthe Mariehjemmet",
    "municipality": "Rødovre"
  },
  {
    "name": "Brdr. Kjeldahl I/S",
    "municipality": "Samsø"
  },
  {
    "name": "SAMSØ SYLTEFABRIK A/S",
    "municipality": "Samsø"
  },
  {
    "name": "EXAM VISION ApS",
    "municipality": "Samsø"
  },
  {
    "name": "SAMSØ REDNINGSKORPS ApS",
    "municipality": "Samsø"
  },
  {
    "name": "Samsø Kirkekasse/Pastorat",
    "municipality": "Samsø"
  },
  {
    "name": "BRATTINGSBORG GODS",
    "municipality": "Samsø"
  },
  {
    "name": "Peab Asfalt A/S",
    "municipality": "Silkeborg"
  },
  {
    "name": "SPX FLOW TECHNOLOGY DANMARK A/S",
    "municipality": "Silkeborg"
  },
  {
    "name": "Eniig Holding A/S",
    "municipality": "Silkeborg"
  },
  {
    "name": "Bucher Municipal A/S",
    "municipality": "Silkeborg"
  },
  {
    "name": "HYDRATECH INDUSTRIES A/S",
    "municipality": "Silkeborg"
  },
  {
    "name": "BJARNE NIELSEN HERNING A/S",
    "municipality": "Silkeborg"
  },
  {
    "name": "Stofa Fiber A/S",
    "municipality": "Silkeborg"
  },
  {
    "name": "Midtjysk Brand & Redning I/S",
    "municipality": "Silkeborg"
  },
  {
    "name": "JYSKE BANK A/S",
    "municipality": "Silkeborg"
  },
  {
    "name": "Tvilum A/S 2018",
    "municipality": "Silkeborg"
  },
  {
    "name": "JN DATA A/S",
    "municipality": "Silkeborg"
  },
  {
    "name": "SPORT24 A/S",
    "municipality": "Silkeborg"
  },
  {
    "name": "EUROMASTER DANMARK A/S",
    "municipality": "Skanderborg"
  },
  {
    "name": "PRESSALIT A/S",
    "municipality": "Skanderborg"
  },
  {
    "name": "AVK INTERNATIONAL A/S",
    "municipality": "Skanderborg"
  },
  {
    "name": "DYNAUDIO A/S",
    "municipality": "Skanderborg"
  },
  {
    "name": "SKOVBY MØBELFABRIK A/S",
    "municipality": "Skanderborg"
  },
  {
    "name": "AURA A/S",
    "municipality": "Skanderborg"
  },
  {
    "name": "RELATIONMEDIA A/S",
    "municipality": "Skanderborg"
  },
  {
    "name": "DANSK INGENIØRSERVICE A/S",
    "municipality": "Skanderborg"
  },
  {
    "name": "KAMSTRUP A/S",
    "municipality": "Skanderborg"
  },
  {
    "name": "NORMAL A/S",
    "municipality": "Skanderborg"
  },
  {
    "name": "DANTHERM A/S",
    "municipality": "Skive"
  },
  {
    "name": "FREJA TRANSPORT & LOGISTICS A/S",
    "municipality": "Skive"
  },
  {
    "name": "THISE MEJERI A.M.B.A.",
    "municipality": "Skive"
  },
  {
    "name": "DEIF A/S",
    "municipality": "Skive"
  },
  {
    "name": "N.C. Nielsen A/S",
    "municipality": "Skive"
  },
  {
    "name": "SKIVE FOLKEBLAD G/S",
    "municipality": "Skive"
  },
  {
    "name": "BGB A/S",
    "municipality": "Skive"
  },
  {
    "name": "ROSLEV TRÆLASTHANDEL A/S",
    "municipality": "Skive"
  },
  {
    "name": "Imerys Industrial Minerals Denmark A/S",
    "municipality": "Skive"
  },
  {
    "name": "DAN-ELEMENT A/S",
    "municipality": "Skive"
  },
  {
    "name": "SCANTRUCK A/S",
    "municipality": "Skive"
  },
  {
    "name": "VIKAN A/S",
    "municipality": "Skive"
  },
  {
    "name": "IDE-PRO SKIVE A/S",
    "municipality": "Skive"
  },
  {
    "name": "Frontmatec Skive A/S",
    "municipality": "Skive"
  },
  {
    "name": "DEN ERHVERVSDRIVENDE FOND KULTURCENTER-LIMFJORD",
    "municipality": "Skive"
  },
  {
    "name": "SKOV A/S. GLYNGØRE",
    "municipality": "Skive"
  },
  {
    "name": "SK SERVICE A/S",
    "municipality": "Slagelse"
  },
  {
    "name": "GRØNVOLD & SCHOU A/S",
    "municipality": "Slagelse"
  },
  {
    "name": "VIMINCO A/S",
    "municipality": "Slagelse"
  },
  {
    "name": "EBK HUSE A/S",
    "municipality": "Slagelse"
  },
  {
    "name": "DANAPAK FLEXIBLES A/S",
    "municipality": "Slagelse"
  },
  {
    "name": "COMWELL STOREBÆLT A/S",
    "municipality": "Slagelse"
  },
  {
    "name": "BELFOR Danmark A/S",
    "municipality": "Slagelse"
  },
  {
    "name": "WESTRUP A/S",
    "municipality": "Slagelse"
  },
  {
    "name": "FOF Syd- og Vestsjælland",
    "municipality": "Slagelse"
  },
  {
    "name": "VIVALDI GRUPPEN A/S",
    "municipality": "Slagelse"
  },
  {
    "name": "C.A. NIELSEN & PETERSENS MASKINFABRIKER A/S",
    "municipality": "Slagelse"
  },
  {
    "name": "EGONS A/S",
    "municipality": "Slagelse"
  },
  {
    "name": "KINGS AND QUEENS ApS",
    "municipality": "Slagelse"
  },
  {
    "name": "PLEJE HOLDING ApS",
    "municipality": "Slagelse"
  },
  {
    "name": "BAHNE SØRENSEN A/S",
    "municipality": "Slagelse"
  },
  {
    "name": "BILTEMA DANMARK A/S",
    "municipality": "Slagelse"
  },
  {
    "name": "HARBOES BRYGGERI A/S",
    "municipality": "Slagelse"
  },
  {
    "name": "EGON OLSEN & SØN A/S",
    "municipality": "Solrød"
  },
  {
    "name": "HAVDRUP BRUGSFORENING",
    "municipality": "Solrød"
  },
  {
    "name": "KØBMAND LARS NIELSEN ApS",
    "municipality": "Solrød"
  },
  {
    "name": "OJD TRADING ApS",
    "municipality": "Solrød"
  },
  {
    "name": "TJW Fragt A/S",
    "municipality": "Solrød"
  },
  {
    "name": "FINN OLSEN A/S VVS",
    "municipality": "Solrød"
  },
  {
    "name": "SCANBUR A/S",
    "municipality": "Solrød"
  },
  {
    "name": "STRUNGE JENSEN A/S. RÅDGIVENDE INGENIØRFIRMA. FRI",
    "municipality": "Solrød"
  },
  {
    "name": "KVISGAARDS MASKINFABRIK A/S",
    "municipality": "Solrød"
  },
  {
    "name": "FINI ApS",
    "municipality": "Solrød"
  },
  {
    "name": "A/S NINOLAB",
    "municipality": "Solrød"
  },
  {
    "name": "THAIAWAY ApS",
    "municipality": "Solrød"
  },
  {
    "name": "EJENDOMSSELSKABET AF 1/1 2012 A/S",
    "municipality": "Solrød"
  },
  {
    "name": "A/S BOTICA ENTREPRISE",
    "municipality": "Solrød"
  },
  {
    "name": "KROGHS FLASKEGENBRUG A/S",
    "municipality": "Solrød"
  },
  {
    "name": "ABILDHAUGES FYSIOTERAPI & TRÆNING ApS",
    "municipality": "Solrød"
  },
  {
    "name": "STORE-HEDEBYG ENTREPRISE A/S",
    "municipality": "Solrød"
  },
  {
    "name": "SOLKYSTENS RENGØRING OG PLEJE ApS",
    "municipality": "Solrød"
  },
  {
    "name": "KLIMA GRUPPEN ApS",
    "municipality": "Solrød"
  },
  {
    "name": "A/S HAVDRUP MASKINFORRETNING",
    "municipality": "Solrød"
  },
  {
    "name": "Nybolig v/Mariann Trolledahl",
    "municipality": "Solrød"
  },
  {
    "name": "Taxavognmand Per Saabye",
    "municipality": "Solrød"
  },
  {
    "name": "SceneKunst I/S",
    "municipality": "Solrød"
  },
  {
    "name": "Dansk Kennel Klub",
    "municipality": "Solrød"
  },
  {
    "name": "TM Transport v/Thomas Milkowski",
    "municipality": "Solrød"
  },
  {
    "name": "SOLRØD PASTORAT",
    "municipality": "Solrød"
  },
  {
    "name": "Solrød Svømmeklub",
    "municipality": "Solrød"
  },
  {
    "name": "PROFILSERVICE A/S",
    "municipality": "Solrød"
  },
  {
    "name": "DBI PLASTICS A/S",
    "municipality": "Sorø"
  },
  {
    "name": "RØLUND A/S",
    "municipality": "Sorø"
  },
  {
    "name": "Simatek A/S",
    "municipality": "Sorø"
  },
  {
    "name": "KOPP SORØ A/S",
    "municipality": "Sorø"
  },
  {
    "name": "CHRIS JENSEN. STENLILLE A/S",
    "municipality": "Sorø"
  },
  {
    "name": "GLOBAL TUNNELLING EXPERTS (DANMARK) ApS",
    "municipality": "Sorø"
  },
  {
    "name": "EHLERS SUPERMARKED SORØ A/S",
    "municipality": "Sorø"
  },
  {
    "name": "ASGER G. JØRGENSEN A/S",
    "municipality": "Sorø"
  },
  {
    "name": "MURERMESTER CLAUS QUISTGAARD A/S",
    "municipality": "Sorø"
  },
  {
    "name": "P H AUTOMOBILER. SORØ ApS",
    "municipality": "Sorø"
  },
  {
    "name": "A/S POUL LARSEN AUTORISERET EL- OG VVS-INSTALLATØR",
    "municipality": "Sorø"
  },
  {
    "name": "SORØ DETAIL A/S",
    "municipality": "Sorø"
  },
  {
    "name": "LYSEN BILER A/S",
    "municipality": "Sorø"
  },
  {
    "name": "COMWELL SORØ A/S",
    "municipality": "Sorø"
  },
  {
    "name": "Egfond",
    "municipality": "Sorø"
  },
  {
    "name": "HØRKRAM FOODSERVICE A/S",
    "municipality": "Sorø"
  },
  {
    "name": "ALTAN.DK A/S",
    "municipality": "Sorø"
  },
  {
    "name": "HØJVANG LABORATORIER A/S",
    "municipality": "Sorø"
  },
  {
    "name": "MULTILINE A/S",
    "municipality": "Sorø"
  },
  {
    "name": "ASA-LIFT A/S",
    "municipality": "Sorø"
  },
  {
    "name": "Kongskilde Industries A/S",
    "municipality": "Sorø"
  },
  {
    "name": "VKST I/S",
    "municipality": "Sorø"
  },
  {
    "name": "FLEMMING SCHRØDER A/S",
    "municipality": "Stevns"
  },
  {
    "name": "VINZENT A/S",
    "municipality": "Stevns"
  },
  {
    "name": "STRØBY BRUGSFORENING",
    "municipality": "Stevns"
  },
  {
    "name": "HÅRLEV BRUGSFORENING",
    "municipality": "Stevns"
  },
  {
    "name": "OMYA A/S",
    "municipality": "Stevns"
  },
  {
    "name": "THOMAS KJÆRULFF, 764 STRØBY EGEDE ApS",
    "municipality": "Stevns"
  },
  {
    "name": "LL-transport ApS",
    "municipality": "Stevns"
  },
  {
    "name": "KNUD FREITAG. FRØSLEV ApS",
    "municipality": "Stevns"
  },
  {
    "name": "PARITAS KOLDING A/S",
    "municipality": "Stevns"
  },
  {
    "name": "JAN NIELSEN A/S",
    "municipality": "Stevns"
  },
  {
    "name": "Ingleby Farms & Forests ApS",
    "municipality": "Stevns"
  },
  {
    "name": "VALLØ STIFT",
    "municipality": "Stevns"
  },
  {
    "name": "HØJAGER BELYSNING A/S",
    "municipality": "Stevns"
  },
  {
    "name": "STORE HEDDINGE DETAIL A/S",
    "municipality": "Stevns"
  },
  {
    "name": "KOK MED KUL PÅ ApS",
    "municipality": "Stevns"
  },
  {
    "name": "Rødvig Kro & Badehotel A/S",
    "municipality": "Stevns"
  },
  {
    "name": "VOGNMAND JOHN JØRGENSEN ApS",
    "municipality": "Stevns"
  },
  {
    "name": "LOF Stevns",
    "municipality": "Stevns"
  },
  {
    "name": "AT Rengøring",
    "municipality": "Stevns"
  },
  {
    "name": "Traktørstedet Højeruplund v/Karl Peter Andersen",
    "municipality": "Stevns"
  },
  {
    "name": "Gjorslev Gods",
    "municipality": "Stevns"
  },
  {
    "name": "HK-KØBENHAVNS KURSUSEJENDOM KLINTEN",
    "municipality": "Stevns"
  },
  {
    "name": "SHS-Stevns",
    "municipality": "Stevns"
  },
  {
    "name": "Phillips-Medisize A/S",
    "municipality": "Struer"
  },
  {
    "name": "ALPHA OFFSHORE SERVICE A/S",
    "municipality": "Struer"
  },
  {
    "name": "HVIDBJERG VINDUET A/S",
    "municipality": "Struer"
  },
  {
    "name": "HVIDBJERG BANK A/S",
    "municipality": "Struer"
  },
  {
    "name": "HVIDBERG A/S",
    "municipality": "Struer"
  },
  {
    "name": "IVAN JAKOBSEN ENTREPRENØRFIRMA A/S",
    "municipality": "Struer"
  },
  {
    "name": "THYHOLM MURER A/S",
    "municipality": "Struer"
  },
  {
    "name": "MARTIN MUNKEBO A/S",
    "municipality": "Struer"
  },
  {
    "name": "CHOKOLAND A/S",
    "municipality": "Struer"
  },
  {
    "name": "K.N. TAGDÆKNING A/S",
    "municipality": "Struer"
  },
  {
    "name": "ENGBAKKENS SKOVENTREPRISE ApS",
    "municipality": "Struer"
  },
  {
    "name": "CHOKODAN STRUER ApS",
    "municipality": "Struer"
  },
  {
    "name": "Struer Transportcenter ApS",
    "municipality": "Struer"
  },
  {
    "name": "B&O PLAY A/S",
    "municipality": "Struer"
  },
  {
    "name": "Nordvestjyllands Brandvæsen I/S",
    "municipality": "Struer"
  },
  {
    "name": "Privathjælpen v/Anne Kjærgaard",
    "municipality": "Struer"
  },
  {
    "name": "BANG & OLUFSEN A/S",
    "municipality": "Struer"
  },
  {
    "name": "BANG & OLUFSEN OPERATIONS A/S",
    "municipality": "Struer"
  },
  {
    "name": "TRYKSAGSOMDELINGEN FYN A/S",
    "municipality": "Svendborg"
  },
  {
    "name": "MAERSK TRAINING A/S",
    "municipality": "Svendborg"
  },
  {
    "name": "VESTER SKERNINGE BILERNE AF 1974 ApS",
    "municipality": "Svendborg"
  },
  {
    "name": "FYNSKE BANK A/S",
    "municipality": "Svendborg"
  },
  {
    "name": "SCAN-HIDE A.M.B.A",
    "municipality": "Svendborg"
  },
  {
    "name": "JENS SCHULTZ A/S",
    "municipality": "Svendborg"
  },
  {
    "name": "Taasinge Elementer A/S",
    "municipality": "Svendborg"
  },
  {
    "name": "MAC BAREN TOBACCO COMPANY A/S",
    "municipality": "Svendborg"
  },
  {
    "name": "REDERIET M.H.SIMONSEN ApS",
    "municipality": "Svendborg"
  },
  {
    "name": "EGN Group A/S",
    "municipality": "Svendborg"
  },
  {
    "name": "AOF Center Fyn",
    "municipality": "Svendborg"
  },
  {
    "name": "C.C. JENSEN A/S",
    "municipality": "Svendborg"
  },
  {
    "name": "SH GROUP A/S",
    "municipality": "Svendborg"
  },
  {
    "name": "VARO SPECIALMASKINER A/S",
    "municipality": "Syddjurs"
  },
  {
    "name": "DANSK VILOMIX A/S",
    "municipality": "Syddjurs"
  },
  {
    "name": "PINDSTRUP MOSEBRUG A/S",
    "municipality": "Syddjurs"
  },
  {
    "name": "CONNECTED WIND SERVICES DANMARK A/S",
    "municipality": "Syddjurs"
  },
  {
    "name": "BRUGSFORENINGEN HORNSLET",
    "municipality": "Syddjurs"
  },
  {
    "name": "DJURS SOMMERLAND A/S",
    "municipality": "Syddjurs"
  },
  {
    "name": "HOTEL FUGLSØCENTRET A/S",
    "municipality": "Syddjurs"
  },
  {
    "name": "REFURB A/S",
    "municipality": "Syddjurs"
  },
  {
    "name": "GERSTRØM ENTREPRENØR ApS",
    "municipality": "Syddjurs"
  },
  {
    "name": "Meny Rønde v/René Sønderby Povlsen",
    "municipality": "Syddjurs"
  },
  {
    "name": "DANMARKS JÆGERFORBUND",
    "municipality": "Syddjurs"
  },
  {
    "name": "DJURSLAND LANDBOFORENING",
    "municipality": "Syddjurs"
  },
  {
    "name": "i.h.kft",
    "municipality": "Syddjurs"
  },
  {
    "name": "Vognsen & Co A/S",
    "municipality": "Syddjurs"
  },
  {
    "name": "PR ELECTRONICS A/S",
    "municipality": "Syddjurs"
  },
  {
    "name": "SCANPAN A/S",
    "municipality": "Syddjurs"
  },
  {
    "name": "AARHUS AIRPORT A/S",
    "municipality": "Syddjurs"
  },
  {
    "name": "EBELTOFT DETAIL A/S",
    "municipality": "Syddjurs"
  },
  {
    "name": "KVADRAT A/S",
    "municipality": "Syddjurs"
  },
  {
    "name": "Kronospan ApS",
    "municipality": "Syddjurs"
  },
  {
    "name": "PETERSEN TEGL A/S",
    "municipality": "Sønderborg"
  },
  {
    "name": "OJ ELECTRONICS A/S",
    "municipality": "Sønderborg"
  },
  {
    "name": "BITZER Electronics A/S",
    "municipality": "Sønderborg"
  },
  {
    "name": "SØNDERBORG FORSYNINGSSERVICE A/S",
    "municipality": "Sønderborg"
  },
  {
    "name": "AKTIESELSKABET SAM. ANDERSEN",
    "municipality": "Sønderborg"
  },
  {
    "name": "AGRAMKOW FLUID SYSTEMS A/S",
    "municipality": "Sønderborg"
  },
  {
    "name": "HELSAM A/S",
    "municipality": "Sønderborg"
  },
  {
    "name": "SØNDERBORG INGENIØR- OG BYGGEFORRETNING A/S",
    "municipality": "Sønderborg"
  },
  {
    "name": "AIR ALSIE A/S",
    "municipality": "Sønderborg"
  },
  {
    "name": "MÜLLER GAS EQUIPMENT A/S",
    "municipality": "Sønderborg"
  },
  {
    "name": "BRØDR. EWERS A/S",
    "municipality": "Sønderborg"
  },
  {
    "name": "Frontmatec Tandslet A/S",
    "municipality": "Sønderborg"
  },
  {
    "name": "DANFOSS POWER ELECTRONICS A/S",
    "municipality": "Sønderborg"
  },
  {
    "name": "DANFOSS POWER SOLUTIONS ApS",
    "municipality": "Sønderborg"
  },
  {
    "name": "DANFOSS POWER SOLUTIONS HOLDING ApS",
    "municipality": "Sønderborg"
  },
  {
    "name": "DANFOSS A/S",
    "municipality": "Sønderborg"
  },
  {
    "name": "LINAK A/S",
    "municipality": "Sønderborg"
  },
  {
    "name": "BRUGSFORENINGEN FOR ALS OG SUNDEVED",
    "municipality": "Sønderborg"
  },
  {
    "name": "BHJ A/S",
    "municipality": "Sønderborg"
  },
  {
    "name": "IDEALCOMBI A/S",
    "municipality": "Thisted"
  },
  {
    "name": "TICAN FRESH MEAT A/S",
    "municipality": "Thisted"
  },
  {
    "name": "SJØRRING MASKINFABRIK A/S",
    "municipality": "Thisted"
  },
  {
    "name": "THISTED-FJERRITSLEV CEMENTVAREFABRIK A/S",
    "municipality": "Thisted"
  },
  {
    "name": "CIMBRIA MANUFACTURING A/S",
    "municipality": "Thisted"
  },
  {
    "name": "SPAREKASSEN THY",
    "municipality": "Thisted"
  },
  {
    "name": "JAMMERBUGTENS FERIEHUSUDLEJNING A/S",
    "municipality": "Thisted"
  },
  {
    "name": "Thisted Forsikring A/S",
    "municipality": "Thisted"
  },
  {
    "name": "NETIP A/S",
    "municipality": "Thisted"
  },
  {
    "name": "CSK STÅLINDUSTRI A/S",
    "municipality": "Thisted"
  },
  {
    "name": "MEJERIGAARDEN A/S",
    "municipality": "Thisted"
  },
  {
    "name": "DRAGSBÆK A/S",
    "municipality": "Thisted"
  },
  {
    "name": "LETH BETON A/S",
    "municipality": "Thisted"
  },
  {
    "name": "CIMBRIA UNIGRAIN A/S",
    "municipality": "Thisted"
  },
  {
    "name": "BRANDT STATSAUTORISERET REVISIONSPARTNERSELSKAB",
    "municipality": "Thisted"
  },
  {
    "name": "HILDING ANDERS DANMARK A/S",
    "municipality": "Thisted"
  },
  {
    "name": "THYSSEN STÅL A/S",
    "municipality": "Tønder"
  },
  {
    "name": "Vikarservicesyd ApS",
    "municipality": "Tønder"
  },
  {
    "name": "PRO RENGØRING A/S",
    "municipality": "Tønder"
  },
  {
    "name": "SuperBrugsen i Skærbæk og Dagli'Brugsen på Rømø",
    "municipality": "Tønder"
  },
  {
    "name": "TØNDER SERVICE A/S",
    "municipality": "Tønder"
  },
  {
    "name": "PTI EUROPA A/S",
    "municipality": "Tønder"
  },
  {
    "name": "EJNAR CHRISTIANSEN SØLSTED A/S",
    "municipality": "Tønder"
  },
  {
    "name": "ECKHOLDTS BAGERI ApS",
    "municipality": "Tønder"
  },
  {
    "name": "VOGNMAND OG ENTREPRENØR MADS VEJRUP A/S",
    "municipality": "Tønder"
  },
  {
    "name": "TOFTLUND BRUGSFORENING",
    "municipality": "Tønder"
  },
  {
    "name": "Studenterkurset & Kostskolen i Sønderjylland",
    "municipality": "Tønder"
  },
  {
    "name": "AGERSKOV KRO V/PETER OTTE",
    "municipality": "Tønder"
  },
  {
    "name": "Det Gamle Apotek A/S",
    "municipality": "Tønder"
  },
  {
    "name": "SKÆRBÆK BYGNINGSINDUSTRI A/S",
    "municipality": "Tønder"
  },
  {
    "name": "BENTELER Automotive Tønder A/S",
    "municipality": "Tønder"
  },
  {
    "name": "TØNDER OG OMEGNS BRUGSFORENING",
    "municipality": "Tønder"
  },
  {
    "name": "Landbrugsrådgivning Syd I/S",
    "municipality": "Tønder"
  },
  {
    "name": "ECCO SKO A/S",
    "municipality": "Tønder"
  },
  {
    "name": "Hydro Extrusion Denmark A/S",
    "municipality": "Tønder"
  },
  {
    "name": "HYDRO PRECISION TUBING TØNDER A/S",
    "municipality": "Tønder"
  },
  {
    "name": "KJELKVIST A/S",
    "municipality": "Tønder"
  },
  {
    "name": "FONDEN SKÆRBÆKcentret",
    "municipality": "Tønder"
  },
  {
    "name": "M. SCHACK ENGEL A/S",
    "municipality": "Tønder"
  },
  {
    "name": "SAS GROUND HANDLING DENMARK A/S",
    "municipality": "Tårnby"
  },
  {
    "name": "SAS DANMARK A/S",
    "municipality": "Tårnby"
  },
  {
    "name": "ARRIVA DANMARK A/S",
    "municipality": "Tårnby"
  },
  {
    "name": "KØBENHAVNS LUFTHAVNE A/S",
    "municipality": "Tårnby"
  },
  {
    "name": "Scandinavian Airlines System Denmark-Norway-Sweden",
    "municipality": "Tårnby"
  },
  {
    "name": "SELECT SERVICE PARTNER DENMARK A/S",
    "municipality": "Tårnby"
  },
  {
    "name": "GATE GOURMET DENMARK ApS",
    "municipality": "Tårnby"
  },
  {
    "name": "GEBR. HEINEMANN RETAIL ApS",
    "municipality": "Tårnby"
  },
  {
    "name": "HMSHOST DENMARK, FILIAL AF HMSHOSTSWEDEN AB, SVERIGE",
    "municipality": "Tårnby"
  },
  {
    "name": "DHL AVIATION. FILIAL AF DHL AVIATION N.V.. BELGIEN",
    "municipality": "Tårnby"
  },
  {
    "name": "STAR AIR A/S",
    "municipality": "Tårnby"
  },
  {
    "name": "SCAN GLOBAL LOGISTICS A/S",
    "municipality": "Tårnby"
  },
  {
    "name": "PARTNERSERVICE HVER GANG ApS",
    "municipality": "Tårnby"
  },
  {
    "name": "MENZIES AVIATION (DENMARK) A/S",
    "municipality": "Tårnby"
  },
  {
    "name": "SATAIR A/S",
    "municipality": "Tårnby"
  },
  {
    "name": "ARRIVA TOG A/S",
    "municipality": "Tårnby"
  },
  {
    "name": "DHL EXPRESS (DENMARK) A/S",
    "municipality": "Vallensbæk"
  },
  {
    "name": "ORKLA FOODS DANMARK A/S",
    "municipality": "Vallensbæk"
  },
  {
    "name": "TAKEDA PHARMA A/S",
    "municipality": "Vallensbæk"
  },
  {
    "name": "ESTEE LAUDER COSMETICS A/S",
    "municipality": "Vallensbæk"
  },
  {
    "name": "CAPGEMINI DANMARK A/S",
    "municipality": "Vallensbæk"
  },
  {
    "name": "HONEYWELL A/S",
    "municipality": "Vallensbæk"
  },
  {
    "name": "TIKKURILA DANMARK A/S",
    "municipality": "Vallensbæk"
  },
  {
    "name": "Haribo Lakrids A/S",
    "municipality": "Vallensbæk"
  },
  {
    "name": "RICOH DANMARK A/S",
    "municipality": "Vallensbæk"
  },
  {
    "name": "PLANDENT A/S",
    "municipality": "Vallensbæk"
  },
  {
    "name": "RESURS BANK, FILIAL AF RESURS BANK AKTIEBOLAG, SVERIGE",
    "municipality": "Vallensbæk"
  },
  {
    "name": "NOBIA DENMARK A/S",
    "municipality": "Varde"
  },
  {
    "name": "SYDVESTJYSK PELSCENTER A.M.B.A.",
    "municipality": "Varde"
  },
  {
    "name": "Brugsforeningen for Nørre Nebel og Omegn amba",
    "municipality": "Varde"
  },
  {
    "name": "KVIST INDUSTRIES A/S",
    "municipality": "Varde"
  },
  {
    "name": "SKY-LIGHT A/S",
    "municipality": "Varde"
  },
  {
    "name": "ADMIRAL STRAND FERIEHUSE ApS",
    "municipality": "Varde"
  },
  {
    "name": "NORDISK SVEJSE KONTROL A/S",
    "municipality": "Varde"
  },
  {
    "name": "FLENSTED SNITGRØNT A/S",
    "municipality": "Varde"
  },
  {
    "name": "FLENSTED Food Group A/S",
    "municipality": "Varde"
  },
  {
    "name": "PRIMO DANMARK A/S",
    "municipality": "Varde"
  },
  {
    "name": "L&P SPRINGS DENMARK ApS",
    "municipality": "Varde"
  },
  {
    "name": "ROUST TRÆ A/S",
    "municipality": "Varde"
  },
  {
    "name": "NOBIA DENMARK RETAIL A/S",
    "municipality": "Varde"
  },
  {
    "name": "FiberVisions A/S",
    "municipality": "Varde"
  },
  {
    "name": "BOCONCEPT A/S",
    "municipality": "Varde"
  },
  {
    "name": "NORLAX A/S",
    "municipality": "Varde"
  },
  {
    "name": "KVICKLY VARDE",
    "municipality": "Varde"
  },
  {
    "name": "K. HANSEN TRANSPORT A/S",
    "municipality": "Vejen"
  },
  {
    "name": "HANS FRISESDAHL A/S",
    "municipality": "Vejen"
  },
  {
    "name": "PRO-AUTOMATIC A/S",
    "municipality": "Vejen"
  },
  {
    "name": "DINESEN FLOORS A/S",
    "municipality": "Vejen"
  },
  {
    "name": "EPOKE A/S",
    "municipality": "Vejen"
  },
  {
    "name": "FRØS SPAREKASSE",
    "municipality": "Vejen"
  },
  {
    "name": "ENTREPRENØR HENNING HAVE A/S",
    "municipality": "Vejen"
  },
  {
    "name": "VEJEN IDRÆTSCENTER",
    "municipality": "Vejen"
  },
  {
    "name": "SKARE MEAT PACKERS K/S",
    "municipality": "Vejen"
  },
  {
    "name": "NDI Group A/S",
    "municipality": "Vejen"
  },
  {
    "name": "SPF-DANMARK A/S",
    "municipality": "Vejen"
  },
  {
    "name": "SOLAR A/S",
    "municipality": "Vejen"
  },
  {
    "name": "SUPER DÆK SERVICE DANMARK A/S",
    "municipality": "Vejen"
  },
  {
    "name": "JYSK FYNSKE MEDIER P/S",
    "municipality": "Vejle"
  },
  {
    "name": "JEM & FIX A/S",
    "municipality": "Vejle"
  },
  {
    "name": "FERTIN PHARMA A/S",
    "municipality": "Vejle"
  },
  {
    "name": "DANSK AVIS OMDELING A/S",
    "municipality": "Vejle"
  },
  {
    "name": "DANPO A/S",
    "municipality": "Vejle"
  },
  {
    "name": "DK COMPANY VEJLE A/S",
    "municipality": "Vejle"
  },
  {
    "name": "GPV INTERNATIONAL A/S",
    "municipality": "Vejle"
  },
  {
    "name": "SCANDIC FOOD A/S",
    "municipality": "Vejle"
  },
  {
    "name": "TEKNICLEAN A/S",
    "municipality": "Vejle"
  },
  {
    "name": "APCOA PARKING DANMARK A/S",
    "municipality": "Vejle"
  },
  {
    "name": "FORSTAS A/S",
    "municipality": "Vejle"
  },
  {
    "name": "JACO SUPERMARKEDER A/S",
    "municipality": "Vejle"
  },
  {
    "name": "Dagrofa Logistik a/s",
    "municipality": "Vejle"
  },
  {
    "name": "WELCON A/S",
    "municipality": "Vejle"
  },
  {
    "name": "Munkebjerg Hotel",
    "municipality": "Vejle"
  },
  {
    "name": "DGI",
    "municipality": "Vejle"
  },
  {
    "name": "Trekantområdets Brandvæsen I/S",
    "municipality": "Vejle"
  },
  {
    "name": "JELD-WEN DANMARK A/S",
    "municipality": "Vesthimmerlands"
  },
  {
    "name": "LOGSTOR A/S",
    "municipality": "Vesthimmerlands"
  },
  {
    "name": "MAT DANIA ApS",
    "municipality": "Vesthimmerlands"
  },
  {
    "name": "OUTLINE VINDUER A/S",
    "municipality": "Vesthimmerlands"
  },
  {
    "name": "JUTLANDER BANK A/S",
    "municipality": "Vesthimmerlands"
  },
  {
    "name": "SCANDI BYG A/S",
    "municipality": "Vesthimmerlands"
  },
  {
    "name": "Versalift Denmark A/S",
    "municipality": "Vesthimmerlands"
  },
  {
    "name": "TRECO A/S",
    "municipality": "Vesthimmerlands"
  },
  {
    "name": "HGSR A/S",
    "municipality": "Vesthimmerlands"
  },
  {
    "name": "HMC Byg & Anlæg driftsmateriel HMN A/S",
    "municipality": "Vesthimmerlands"
  },
  {
    "name": "NORDKABEL A/S",
    "municipality": "Vesthimmerlands"
  },
  {
    "name": "GUNNAR NIELSEN. AARS A/S",
    "municipality": "Vesthimmerlands"
  },
  {
    "name": "HIMMERLANDSKØD A/S",
    "municipality": "Vesthimmerlands"
  },
  {
    "name": "Servido A/S",
    "municipality": "Vesthimmerlands"
  },
  {
    "name": "HMC Byg & Anlæg driftsmateriel H&M A/S",
    "municipality": "Vesthimmerlands"
  },
  {
    "name": "LYNGSOE SYSTEMS A/S",
    "municipality": "Vesthimmerlands"
  },
  {
    "name": "F & H A/S",
    "municipality": "Viborg"
  },
  {
    "name": "Mammen Mejerierne A/S",
    "municipality": "Viborg"
  },
  {
    "name": "DANSKE ANDELSKASSERS BANK A/S",
    "municipality": "Viborg"
  },
  {
    "name": "BRØNDUM A/S",
    "municipality": "Viborg"
  },
  {
    "name": "SAMSON AGRO A/S",
    "municipality": "Viborg"
  },
  {
    "name": "Viborg Stiftsadministration",
    "municipality": "Viborg"
  },
  {
    "name": "GRUNDFOS A/S",
    "municipality": "Viborg"
  },
  {
    "name": "GRUNDFOS HOLDING A/S",
    "municipality": "Viborg"
  },
  {
    "name": "HOLMRIS B8 A/S",
    "municipality": "Viborg"
  },
  {
    "name": "HEDEDANMARK A/S",
    "municipality": "Viborg"
  },
  {
    "name": "BACH GRUPPEN KØBENHAVN A/S",
    "municipality": "Viborg"
  },
  {
    "name": "Bach Gruppen Holding A/S",
    "municipality": "Viborg"
  },
  {
    "name": "BACH GRUPPEN A/S",
    "municipality": "Viborg"
  },
  {
    "name": "LURENA ApS",
    "municipality": "Vordingborg"
  },
  {
    "name": "VORDINGBORG KØKKENET A/S",
    "municipality": "Vordingborg"
  },
  {
    "name": "MALERMESTER BJÖRN FORSBERG A/S",
    "municipality": "Vordingborg"
  },
  {
    "name": "BISCA A/S",
    "municipality": "Vordingborg"
  },
  {
    "name": "NORDISK POLERING ApS",
    "municipality": "Vordingborg"
  },
  {
    "name": "JENS H. HANSEN ApS",
    "municipality": "Vordingborg"
  },
  {
    "name": "PPC, FILIAL AF PPC BROADBAND, INC., USA",
    "municipality": "Vordingborg"
  },
  {
    "name": "INSATECH A/S",
    "municipality": "Vordingborg"
  },
  {
    "name": "MENY Præstø I/S",
    "municipality": "Vordingborg"
  },
  {
    "name": "LENDEMARK BRUGSFORENING",
    "municipality": "Vordingborg"
  },
  {
    "name": "MØNS BANK A/S",
    "municipality": "Vordingborg"
  },
  {
    "name": "Ørslev Servicetrafik A/S",
    "municipality": "Vordingborg"
  },
  {
    "name": "CORNING OPTICAL COMMUNICATIONS ApS",
    "municipality": "Vordingborg"
  },
  {
    "name": "Museum Sydøstdanmark",
    "municipality": "Vordingborg"
  },
  {
    "name": "Skovbyholm Grønt v/Hans-Erik Nielsen",
    "municipality": "Vordingborg"
  },
  {
    "name": "MARSTAL BRUGSFORENING",
    "municipality": "Ærø"
  },
  {
    "name": "SØBY VÆRFT A/S",
    "municipality": "Ærø"
  },
  {
    "name": "ÆRØ HOTEL ApS",
    "municipality": "Ærø"
  },
  {
    "name": "RISE FLEMLØSE SPAREKASSE",
    "municipality": "Ærø"
  },
  {
    "name": "NAUTIC WOOD ApS",
    "municipality": "Ærø"
  },
  {
    "name": "ÆRØ MØBLER A/S",
    "municipality": "Ærø"
  },
  {
    "name": "ÆRØ REDNINGSKORPS OG VOGNMANDSFORRETNING DUNKÆR ApS",
    "municipality": "Ærø"
  },
  {
    "name": "Ærø Menighedsråd",
    "municipality": "Ærø"
  },
  {
    "name": "Syd ABB A/S",
    "municipality": "Aabenraa"
  },
  {
    "name": "CONTIGA A/S",
    "municipality": "Aabenraa"
  },
  {
    "name": "VALMONT SM A/S",
    "municipality": "Aabenraa"
  },
  {
    "name": "ABENA A/S",
    "municipality": "Aabenraa"
  },
  {
    "name": "DANFOSS DISTRIBUTION SERVICES A/S",
    "municipality": "Aabenraa"
  },
  {
    "name": "EURODAN-HUSE A/S",
    "municipality": "Aabenraa"
  },
  {
    "name": "ABENA PRODUKTION A/S",
    "municipality": "Aabenraa"
  },
  {
    "name": "MELDGAARD MILJØ A/S",
    "municipality": "Aabenraa"
  },
  {
    "name": "SYDBANK A/S",
    "municipality": "Aabenraa"
  },
  {
    "name": "KING FOOD DANMARK A/S",
    "municipality": "Aabenraa"
  },
  {
    "name": "KOHBERG BAKERY GROUP A/S",
    "municipality": "Aabenraa"
  },
  {
    "name": "FLEGGAARD HOLDING A/S",
    "municipality": "Aabenraa"
  },
  {
    "name": "SPAR NORD BANK A/S",
    "municipality": "Aalborg"
  },
  {
    "name": "BEIERHOLM, STATSAUTORISERET REVISIONSPARTNERSELSKAB",
    "municipality": "Aalborg"
  },
  {
    "name": "SANISTÅL A/S",
    "municipality": "Aalborg"
  },
  {
    "name": "NORDJYSKE MEDIER A/S",
    "municipality": "Aalborg"
  },
  {
    "name": "PWT GROUP A/S",
    "municipality": "Aalborg"
  },
  {
    "name": "INTEGO A/S",
    "municipality": "Aalborg"
  },
  {
    "name": "AALBORG BOLDSPILKLUB A/S",
    "municipality": "Aalborg"
  },
  {
    "name": "A. ENGGAARD A/S",
    "municipality": "Aalborg"
  },
  {
    "name": "RESTAURANT PAPEGØJEHAVEN A/S",
    "municipality": "Aalborg"
  },
  {
    "name": "MATCHMIND A/S",
    "municipality": "Aalborg"
  },
  {
    "name": "ROYAL GREENLAND SEAFOOD A/S",
    "municipality": "Aalborg"
  },
  {
    "name": "EVENTFORCE RETAIL A/S",
    "municipality": "Aalborg"
  },
  {
    "name": "HP-BYG A/S",
    "municipality": "Aalborg"
  },
  {
    "name": "Centrica Energy Trading A/S",
    "municipality": "Aalborg"
  },
  {
    "name": "TL BYG A/S",
    "municipality": "Aalborg"
  },
  {
    "name": "Aalborg Portland A/S",
    "municipality": "Aalborg"
  },
  {
    "name": "BMS A/S",
    "municipality": "Aalborg"
  },
  {
    "name": "MARIENDAL EL-TEKNIK A/S",
    "municipality": "Aalborg"
  },
  {
    "name": "CARSOE A/S",
    "municipality": "Aalborg"
  },
  {
    "name": "BLADT INDUSTRIES A/S",
    "municipality": "Aalborg"
  },
  {
    "name": "ALFA LAVAL AALBORG A/S",
    "municipality": "Aalborg"
  },
  {
    "name": "UGGERLY INSTALLATION A/S",
    "municipality": "Aalborg"
  },
  {
    "name": "GOMSPACE A/S",
    "municipality": "Aalborg"
  },
  {
    "name": "RANDERS TEGL A/S",
    "municipality": "Aalborg"
  },
  {
    "name": "JYSK TELEMARKETING A/S",
    "municipality": "Aalborg"
  },
  {
    "name": "Aalborg Lufthavn A.M.B.A.",
    "municipality": "Aalborg"
  },
  {
    "name": "Aalborg Stiftsøvrighed",
    "municipality": "Aalborg"
  },
  {
    "name": "EURO CATER GROUP A/S",
    "municipality": "Aalborg"
  },
  {
    "name": "Nordjyllands Beredskab I/S",
    "municipality": "Aalborg"
  },
  {
    "name": "WRIST SHIP SUPPLY A/S",
    "municipality": "Aalborg"
  },
  {
    "name": "BDO STATSAUTORISERET REVISIONSAKTIESELSKAB",
    "municipality": "Aarhus"
  },
  {
    "name": "ARLA FOODS AMBA",
    "municipality": "Aarhus"
  },
  {
    "name": "VESTAS OFFSHORE WIND A/S",
    "municipality": "Aarhus"
  },
  {
    "name": "Silvan A/S",
    "municipality": "Aarhus"
  },
  {
    "name": "VESTAS WIND SYSTEMS A/S",
    "municipality": "Aarhus"
  },
  {
    "name": "BEUMER Group A/S",
    "municipality": "Aarhus"
  },
  {
    "name": "TERMA A/S",
    "municipality": "Aarhus"
  },
  {
    "name": "DANSKE FRAGTMÆND A/S",
    "municipality": "Aarhus"
  },
  {
    "name": "Molslinjen A/S",
    "municipality": "Aarhus"
  },
  {
    "name": "TeamVikaren.dk, Kolding ApS",
    "municipality": "Aarhus"
  },
  {
    "name": "ILVA A/S",
    "municipality": "Aarhus"
  },
  {
    "name": "AARSLEFF RAIL A/S",
    "municipality": "Aarhus"
  },
  {
    "name": "Kongsvang Cleaning & Facility A/S",
    "municipality": "Aarhus"
  },
  {
    "name": "HMF GROUP A/S",
    "municipality": "Aarhus"
  },
  {
    "name": "POWERCARE A/S",
    "municipality": "Aarhus"
  },
  {
    "name": "UA/FK DISTRIBUTION A/S",
    "municipality": "Aarhus"
  },
  {
    "name": "PV AF 2007 ApS",
    "municipality": "Aarhus"
  },
  {
    "name": "STOFA A/S",
    "municipality": "Aarhus"
  },
  {
    "name": "SYSTEMATIC A/S",
    "municipality": "Aarhus"
  },
  {
    "name": "EL:CON A/S",
    "municipality": "Aarhus"
  },
  {
    "name": "OK A.M.B.A.",
    "municipality": "Aarhus"
  },
  {
    "name": "VIKTECH P/S",
    "municipality": "Aarhus"
  },
  {
    "name": "JOHNSON CONTROLS DENMARK ApS",
    "municipality": "Aarhus"
  },
  {
    "name": "AARHUS TECH",
    "municipality": "Aarhus"
  },
  {
    "name": "KRISTELIG FAGFORENING",
    "municipality": "Aarhus"
  },
  {
    "name": "Midttrafik",
    "municipality": "Aarhus"
  },
  {
    "name": "ARLA FOODS INGREDIENTS GROUP P/S",
    "municipality": "Aarhus"
  },
  {
    "name": "DANSKE COMMODITIES A/S",
    "municipality": "Aarhus"
  },
  {
    "name": "ENERGI DANMARK A/S",
    "municipality": "Aarhus"
  },
  {
    "name": "AKTIESELSKABET SCHOUW & CO.",
    "municipality": "Aarhus"
  },
  {
    "name": "TEAMVIKAREN.DK, AARHUS ApS",
    "municipality": "Aarhus"
  },
  {
    "name": "BAUHAUS DANMARK A/S",
    "municipality": "Aarhus"
  },
  {
    "name": "Stark Danmark A/S",
    "municipality": "Aarhus"
  },
  {
    "name": "JP/POLITIKENS HUS A/S",
    "municipality": "Aarhus"
  },
  {
    "name": "F. SALLING HOLDING A/S",
    "municipality": "Aarhus"
  },
  {
    "name": "JYSK A/S",
    "municipality": "Aarhus"
  },
  {
    "name": "Salling Group A/S",
    "municipality": "Aarhus"
  },
  {
    "name": "UNIFEEDER A/S",
    "municipality": "Aarhus"
  },
  {
    "name": "VESTAS MANUFACTURING A/S",
    "municipality": "Aarhus"
  },
  {
    "name": "Per Aarsleff A/S",
    "municipality": "Aarhus"
  }
]