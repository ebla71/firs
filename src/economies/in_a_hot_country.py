from economy import Economy
economy = Economy(id = "IN_A_HOT_COUNTRY",
                  numeric_id = 3,
                  # as of May 2015 the following cargos must have fixed positions if used by an economy:
                  # passengers: 0, mail: 2, goods 5, food 11
                  # keep the rest of the cargos alphabetised
                  # bump the min. compatible version if this list changes
                  cargos = ['passengers',
                            'alcohol',
                            'mail',
                            'ammonia',
                            'cassava',
                            'goods',
                            'cement',
                            'chromite_ore',
                            'clay',
                            'coal',
                            'coffee',
                            'food',
                            'copper',
                            'copper_concentrate',
                            'copper_ore',
                            'diamonds',
                            'edible_oil',
                            'engineering_supplies',
                            'explosives',
                            'farm_supplies',
                            'ferrochrome',
                            'fish',
                            'plant_fibres',
                            'formic_acid',
                            'fruits',
                            'limestone',
                            'livestock',
                            'lumber',
                            'maize',
                            'manganese',
                            'nuts',
                            'petrol',
                            'phosphate',
                            'potash',
                            'quicklime',
                            'raw_latex',
                            'soda_ash',
                            'rubber',
                            'sulphur',
                            'textiles',
                            'vehicles',
                            'wood',
                            'wool',
                            'yarn'])
