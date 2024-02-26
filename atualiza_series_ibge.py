class dataImesc:
    def __init__(self):     
        self.dicio={1:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2688]",
                    2:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2689]",
                    3:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2691]",
                    4:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2692]",
                    5:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2694]",
                    6:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2696]",
                    7:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2701]",
                    8:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2702]",
                    9:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2708]",
                    10:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2709]",
                    11:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2710]",
                    12:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2711]",
                    13:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2713]",
                    14:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2714]",
                    15:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2715]",
                    16:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[0]",
                    17:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2688]",
                    18:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2689]",
                    19:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2691]",
                    20:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2692]",
                    21:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2694]",
                    22:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2696]",
                    23:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2701]",
                    24:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2702]",
                    25:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2708]",
                    26:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2709]",
                    27:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2710]",
                    28:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2711]",
                    29:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2713]",
                    30:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2714]",
                    31:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2715]",
                    32:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2688]",
                    33:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2689]",
                    34:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2691]",
                    35:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2692]",
                    36:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2694]",
                    37:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2696]",
                    38:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2701]",
                    39:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2702]",
                    40:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2708]",
                    41:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2709]",
                    42:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2710]",
                    43:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2711]",
                    44:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2713]",
                    45:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2714]",
                    46:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2715]",
                    47:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[0]",
                    48:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2688]",
                    49:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2689]",
                    50:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2691]",
                    51:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2692]",
                    52:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2694]",
                    53:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2696]",
                    54:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2701]",
                    55:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2702]",
                    56:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2708]",
                    57:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2709]",
                    58:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2710]",
                    59:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2711]",
                    60:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2713]",
                    61:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2714]",
                    62:"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2715]",
                    63:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2720]",
                    64:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2721]",
                    65:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2725]",
                    66:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2727]",
                    67:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2733]",
                    68:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2734]",
                    69:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2736]",
                    70:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2737]",
                    71:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2738]",
                    72:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2743]",
                    73:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2745]",
                    74:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2747]",
                    75:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[0]",
                    76:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2720]",
                    77:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2721]",
                    78:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2725]",
                    79:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2727]",
                    80:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2733]",
                    81:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2734]",
                    82:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2736]",
                    83:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2737]",
                    84:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2738]",
                    85:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2743]",
                    86:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2745]",
                    87:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2747]",
                    88:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2720]",
                    89:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2721]",
                    90:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2725]",
                    91:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2727]",
                    92:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2733]",
                    93:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2734]",
                    94:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2736]",
                    95:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2737]",
                    96:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2738]",
                    97:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2743]",
                    98:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2745]",
                    99:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2747]",
                    100:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[0]",
                    101:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2720]",
                    102:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2721]",
                    103:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2725]",
                    104:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2727]",
                    105:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2733]",
                    106:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2734]",
                    107:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2736]",
                    108:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2737]",
                    109:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2738]",
                    110:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2743]",
                    111:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2745]",
                    112:"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2747]",
                    113:"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/-22/variaveis/142?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[33247]",
                    114:"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/-22/variaveis/142?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[33248]",
                    115:"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/-22/variaveis/142?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[33249]",
                    116:"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/-22/variaveis/142?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[33250]",
                    117:"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/-22/variaveis/142?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[33251]",
                    118:"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/-22/variaveis/142?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[33252]",
                    119:"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/-22/variaveis/142?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[3458]",
                    120:"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/-22/variaveis/142?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[3459]",
                    121:"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/-22/variaveis/143?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[33247]",
                    122:"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/-22/variaveis/143?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[33248]",
                    123:"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/-22/variaveis/143?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[33249]",
                    124:"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/-22/variaveis/143?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[33250]",
                    125:"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/-22/variaveis/143?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[33251]",
                    126:"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/-22/variaveis/143?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[33252]",
                    127:"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/-22/variaveis/143?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[3458]",
                    128:"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/-22/variaveis/143?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[3459]",
                    129:"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/-22/variaveis/143?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[0]",
                    130:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3403]",
                    131:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3404]",
                    132:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3407]",
                    133:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[39409]",
                    134:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[11296]",
                    135:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3403]",
                    136:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3404]",
                    137:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3407]",
                    138:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[39409]",
                    139:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[11296]",
                    140:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[0]",
                    141:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3413]",
                    142:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3415]",
                    143:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3421]",
                    144:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3422]",
                    145:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3424]",
                    146:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3425]",
                    147:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3426]",
                    148:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3427]",
                    149:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3433]",
                    150:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]]&classificacao=193[3434]",
                    151:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]]&classificacao=193[3435]",
                    152:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]]&classificacao=193[3439]",
                    153:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]}]&classificacao=193[3444]",
                    154:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]]&classificacao=193[3445]",
                    155:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3446]",
                    156:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3413]|193[3413]",
                    157:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3415]|193[3415]",
                    158:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3421]|193[3421]",
                    159:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3422]|193[3422]",
                    160:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3424]|193[3424]",
                    161:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3425]|193[3425]",
                    162:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3426]|193[3426]",
                    163:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3427]|193[3427]",
                    164:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3433]|193[3433]",
                    165:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3434]|193[3434]",
                    166:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3435]|193[3435]",
                    167:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3439]|193[3439]",
                    168:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3444]|193[3444]",
                    169:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3445]|193[3445]",
                    170:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3446]|193[3446]",
                    171:"https://servicodados.ibge.gov.br/api/v3/agregados/74/periodos/-22/variaveis/106?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=80[2682]",
                    172:"https://servicodados.ibge.gov.br/api/v3/agregados/74/periodos/-22/variaveis/106?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=80[2685]",
                    173:"https://servicodados.ibge.gov.br/api/v3/agregados/74/periodos/-22/variaveis/106?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=80[2686]",
                    174:"https://servicodados.ibge.gov.br/api/v3/agregados/74/periodos/-22/variaveis/106?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=80[2687]",
                    175:"https://servicodados.ibge.gov.br/api/v3/agregados/74/periodos/-22/variaveis/106?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=80[2683]",
                    176:"https://servicodados.ibge.gov.br/api/v3/agregados/74/periodos/-22/variaveis/106?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=80[2684]",
                    177:"https://servicodados.ibge.gov.br/api/v3/agregados/74/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=80[2682]",
                    178:"https://servicodados.ibge.gov.br/api/v3/agregados/74/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=80[2685]",
                    179:"https://servicodados.ibge.gov.br/api/v3/agregados/74/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=80[2686]",
                    180:"https://servicodados.ibge.gov.br/api/v3/agregados/74/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=80[2687]",
                    181:"https://servicodados.ibge.gov.br/api/v3/agregados/74/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=80[2683]",
                    182:"https://servicodados.ibge.gov.br/api/v3/agregados/74/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=80[2684]",
                    183:"https://servicodados.ibge.gov.br/api/v3/agregados/74/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=80[0]",
                    184:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32861]",
                    185:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32865]",
                    186:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32867]",
                    187:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32869]",
                    188:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32870]",
                    189:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32871]",
                    190:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32872]",
                    191:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32873]",
                    192:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32874]",
                    193:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32875]",
                    194:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32876]",
                    195:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32877]",
                    196:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32878]",
                    197:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32880]",
                    198:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32881]",
                    199:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32886]",
                    200:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32887]",
                    201:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32889]",
                    202:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32861]",
                    203:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32865]",
                    204:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32867]",
                    205:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32869]",
                    206:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32870]",
                    207:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32871]",
                    208:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32872]",
                    209:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32873]",
                    210:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32874]",
                    211:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32875]",
                    212:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32876]",
                    213:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32877]",
                    214:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32878]",
                    215:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32880]",
                    216:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32881]",
                    217:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32886]",
                    218:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32887]",
                    219:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32889]",
                    220:"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/-22/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[0]",
                    221:"https://servicodados.ibge.gov.br/api/v3/agregados/3939/periodos/-22/variaveis/105?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=79[2670]",
                    222:"https://servicodados.ibge.gov.br/api/v3/agregados/3939/periodos/-22/variaveis/105?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=79[2675]",
                    223:"https://servicodados.ibge.gov.br/api/v3/agregados/3939/periodos/-22/variaveis/105?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=79[2672]",
                    224:"https://servicodados.ibge.gov.br/api/v3/agregados/3939/periodos/-22/variaveis/105?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=79[32794]",
                    225:"https://servicodados.ibge.gov.br/api/v3/agregados/3939/periodos/-22/variaveis/105?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=79[32795]",
                    226:"https://servicodados.ibge.gov.br/api/v3/agregados/3939/periodos/-22/variaveis/105?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=79[2681]",
                    227:"https://servicodados.ibge.gov.br/api/v3/agregados/3939/periodos/-22/variaveis/105?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=79[2677]",
                    228:"https://servicodados.ibge.gov.br/api/v3/agregados/3939/periodos/-22/variaveis/105?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=79[32796]",
                    229:"https://servicodados.ibge.gov.br/api/v3/agregados/3939/periodos/-22/variaveis/105?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=79[32793]",
                    230:"https://servicodados.ibge.gov.br/api/v3/agregados/3939/periodos/-22/variaveis/105?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=79[2680]",
                    231:"https://servicodados.ibge.gov.br/api/v3/agregados/5938/periodos/-22/variaveis/37?localidades=N1[all]|N3[all]",
                    232:"",
                    233:"https://servicodados.ibge.gov.br/api/v3/agregados/5938/periodos/-22/variaveis/498?localidades=N1[all]|N3[all]",
                    234:"https://servicodados.ibge.gov.br/api/v3/agregados/5938/periodos/-22/variaveis/513?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]",
                    235:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3440]",
                    240:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3440]",
                    251:"https://servicodados.ibge.gov.br/api/v3/agregados/5938/periodos/-22/variaveis/37?localidades=N1[all]|N6[N3[21]]|N2[all]|N3[all]",
                    252:"https://servicodados.ibge.gov.br/api/v3/agregados/5938/periodos/-22/variaveis/543?localidades=N1[all]|N6[N3[21]]|N2[all]|N3[all]",
                    253:"https://servicodados.ibge.gov.br/api/v3/agregados/5938/periodos/-22/variaveis/498?localidades=N1[all]|N6[N3[21]]|N2[all]|N3[all]",
                    254:"https://servicodados.ibge.gov.br/api/v3/agregados/5938/periodos/-22/variaveis/513?localidades=N1[all]|N6[N3[21]]|N2[all]|N3[all]",
                    255:"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/-22/variaveis/142?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[3455]",
                    256:"https://servicodados.ibge.gov.br/api/v3/agregados/5938/periodos/-22/variaveis/517?localidades=N1[all]|N6[N3[21]]|N2[all]|N3[all]",
                    257:"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/-22/variaveis/142?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[3456]",
                    258:"https://servicodados.ibge.gov.br/api/v3/agregados/5938/periodos/-22/variaveis/6575?localidades=N1[all]|N6[N3[21]]|N2[all]|N3[all]",
                    259:"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/-22/variaveis/142?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[3457]",
                    260:"https://servicodados.ibge.gov.br/api/v3/agregados/5938/periodos/-22/variaveis/525?localidades=N1[all]|N6[N3[21]]|N2[all]|N3[all]",
                    261:"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/-22/variaveis/143?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[3455]",
                    268:"https://servicodados.ibge.gov.br/api/v3/agregados/7431/periodos/-22/variaveis/10765?localidades=N1[all]|N2[all]|N3[all]&classificacao=86[2776]",
                    269:"https://servicodados.ibge.gov.br/api/v3/agregados/7431/periodos/-22/variaveis/10765?localidades=N1[all]|N2[all]|N3[all]&classificacao=86[2779]",
                    278:"https://servicodados.ibge.gov.br/api/v3/agregados/7431/periodos/-22/variaveis/10765?localidades=N1[all]|N2[all]|N3[all]&classificacao=86[95251]",
                    279:"https://servicodados.ibge.gov.br/api/v3/agregados/7434/periodos/-22/variaveis/10765?localidades=N1[all]|N2[all]|N3[all]&classificacao=2[4]",
                    280:"https://servicodados.ibge.gov.br/api/v3/agregados/7434/periodos/-22/variaveis/10765?localidades=N1[all]|N2[all]|N3[all]&classificacao=2[5]",
                    281:"https://servicodados.ibge.gov.br/api/v3/agregados/7433/periodos/-22/variaveis/10765?localidades=N1[all]|N2[all]|N3[all]&classificacao=1568[18837]",
                    282:"https://servicodados.ibge.gov.br/api/v3/agregados/7433/periodos/-22/variaveis/10765?localidades=N1[all]|N2[all]|N3[all]&classificacao=1568[11779]",
                    283:"https://servicodados.ibge.gov.br/api/v3/agregados/7433/periodos/-22/variaveis/10765?localidades=N1[all]|N2[all]|N3[all]&classificacao=1568[11628]",
                    284:"https://servicodados.ibge.gov.br/api/v3/agregados/7433/periodos/-22/variaveis/10765?localidades=N1[all]|N2[all]|N3[all]&classificacao=1568[11629]",
                    285:"https://servicodados.ibge.gov.br/api/v3/agregados/7433/periodos/-22/variaveis/10765?localidades=N1[all]|N2[all]|N3[all]&classificacao=1568[11630]",
                    286:"https://servicodados.ibge.gov.br/api/v3/agregados/7433/periodos/-22/variaveis/10765?localidades=N1[all]|N2[all]|N3[all]&classificacao=1568[11631]",
                    287:"https://servicodados.ibge.gov.br/api/v3/agregados/7433/periodos/-22/variaveis/10765?localidades=N1[all]|N2[all]|N3[all]&classificacao=1568[99713]",
                    288:"https://servicodados.ibge.gov.br/api/v3/agregados/7444/periodos/-22/variaveis/10774?localidades=N1[all]|N2[all]|N3[all]&classificacao=2[6794]",
                    289:"https://servicodados.ibge.gov.br/api/v3/agregados/7444/periodos/-22/variaveis/10774?localidades=N1[all]|N2[all]|N3[all]&classificacao=2[4]",
                    290:"https://servicodados.ibge.gov.br/api/v3/agregados/7444/periodos/-22/variaveis/10774?localidades=N1[all]|N2[all]|N3[all]&classificacao=2[5]",
                    291:"https://servicodados.ibge.gov.br/api/v3/agregados/7441/periodos/-22/variaveis/10774?localidades=N1[all]|N2[all]|N3[all]&classificacao=86[2776]",
                    292:"https://servicodados.ibge.gov.br/api/v3/agregados/7441/periodos/-22/variaveis/10774?localidades=N1[all]|N2[all]|N3[all]&classificacao=86[2779]",
                    293:"https://servicodados.ibge.gov.br/api/v3/agregados/7441/periodos/-22/variaveis/10774?localidades=N1[all]|N2[all]|N3[all]&classificacao=86[2777]",
                    294:"https://servicodados.ibge.gov.br/api/v3/agregados/7443/periodos/-22/variaveis/10774?localidades=N1[all]|N2[all]|N3[all]&classificacao=1568[18837]",
                    295:"https://servicodados.ibge.gov.br/api/v3/agregados/7443/periodos/-22/variaveis/10774?localidades=N1[all]|N2[all]|N3[all]&classificacao=1568[11779]",
                    296:"https://servicodados.ibge.gov.br/api/v3/agregados/7443/periodos/-22/variaveis/10774?localidades=N1[all]|N2[all]|N3[all]&classificacao=1568[11628]",
                    297:"https://servicodados.ibge.gov.br/api/v3/agregados/7443/periodos/-22/variaveis/10774?localidades=N1[all]|N2[all]|N3[all]&classificacao=1568[11629]",
                    298:"https://servicodados.ibge.gov.br/api/v3/agregados/7443/periodos/-22/variaveis/10774?localidades=N1[all]|N2[all]|N3[all]&classificacao=1568[11630]",
                    299:"https://servicodados.ibge.gov.br/api/v3/agregados/7443/periodos/-22/variaveis/10774?localidades=N1[all]|N2[all]|N3[all]&classificacao=1568[11631]",
                    300:"https://servicodados.ibge.gov.br/api/v3/agregados/7443/periodos/-22/variaveis/10774?localidades=N1[all]|N2[all]|N3[all]&classificacao=1568[99713]",
                    #393:"https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/-22/variaveis/616?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]",
                    394:"https://servicodados.ibge.gov.br/api/v3/agregados/200/periodos/-22/variaveis/93?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=1[1]",
                    395:"https://servicodados.ibge.gov.br/api/v3/agregados/200/periodos/-22/variaveis/93?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=1[2]",
                    396:"https://servicodados.ibge.gov.br/api/v3/agregados/200/periodos/-3/variaveis/93?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=2[4]",
                    397:"https://servicodados.ibge.gov.br/api/v3/agregados/200/periodos/-22/variaveis/93?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=2[5]",
                    398:"https://servicodados.ibge.gov.br/api/v3/agregados/136/periodos/2000|2010/variaveis/93?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=86[2776]",
                    399:"https://servicodados.ibge.gov.br/api/v3/agregados/136/periodos/2000|2010/variaveis/93?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=86[2777]",
                    400:"https://servicodados.ibge.gov.br/api/v3/agregados/136/periodos/2000|2010/variaveis/93?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=86[2778]",
                    401:"https://servicodados.ibge.gov.br/api/v3/agregados/136/periodos/2000|2010/variaveis/93?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=86[2779]",
                    402:"https://servicodados.ibge.gov.br/api/v3/agregados/136/periodos/2000|2010/variaveis/93?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=86[2780]",
                    403:"https://servicodados.ibge.gov.br/api/v3/agregados/136/periodos/2000|2010/variaveis/93?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=86[2781]",
                    426:"https://servicodados.ibge.gov.br/api/v3/agregados/793/periodos/2007/variaveis/93?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]",
                    427:"https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/-22/variaveis/9324?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]",
                    879:"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/-22/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3434]",
                    882:"https://servicodados.ibge.gov.br/api/v3/agregados/7431/periodos/-22/variaveis/10765?localidades=N1[all]|N2[all]|N3[all]&classificacao=86[2777]"                    
                    }

        self.lista=[]
        self.serie=[]
        
    def procurar_tabela(self, numero_Tabela):
        #Get the request
        import requests as rq
        self.tabela=numero_Tabela
        self.Tabela=self.dicio[numero_Tabela]
        self.Resposta=rq.get(self.Tabela)
        self.Resposta=((self.Resposta).json())
        print(self.Resposta)
        self.organiza_json()
        self.transforma_em_pandas()
        resultado=self.formato_dataimesc()
        return resultado
             
    def organiza_json(self):
        #Unpacking the JSON
        import ast
        self.results=self.Resposta
        self.first=self.results[0]
        self.second=self.first["resultados"]
        self.third=self.second[0]
        self.fouth=self.third["series"]
        for i in self.fouth:
            self.local=i['localidade']
            self.result2=f'"localidade":{self.local["id"]}, "nome":"{self.local["nome"]}"'
            self.serie.append(ast.literal_eval(f"{i['serie']}"))
            self.result3="{"+self.result2+"}"
            self.lista.append(ast.literal_eval(self.result3))
            	     
    def transforma_em_pandas(self):
        import pandas as pd
        data_Cidades=pd.DataFrame(self.lista)
        self.data_Serie=pd.DataFrame(self.serie)
        self.anos=list(self.data_Serie.columns)
        data_frame=pd.concat([data_Cidades,self.data_Serie], axis=1)
        data_frame.loc[(data_frame['localidade']==1 )& (data_frame["nome"]=="Brasil"), ['localidade']] = "BR"
        data_frame.loc[(data_frame['localidade']==1 )& (data_frame["nome"]=="Norte"), ['localidade']] = "N"
        data_frame.loc[(data_frame['localidade']==2 ), ['localidade']] = "NE"
        data_frame.loc[(data_frame['localidade']==3 ), ['localidade']] = "SE"
        data_frame.loc[(data_frame['localidade']==4 ), ['localidade']] = "S"
        data_frame.loc[(data_frame['localidade']==5 ), ['localidade']] = "CO"
        data_frame.loc[(data_frame['localidade']==11 ), ['localidade']] = "RO"
        data_frame.loc[(data_frame['localidade']==12 ), ['localidade']] = "AC"
        data_frame.loc[(data_frame['localidade']==13 ), ['localidade']] = "AM"
        data_frame.loc[(data_frame['localidade']==14 ), ['localidade']] = "RR"
        data_frame.loc[(data_frame['localidade']==15 ), ['localidade']] = "PA"
        data_frame.loc[(data_frame['localidade']==16 ), ['localidade']] = "AP"
        data_frame.loc[(data_frame['localidade']==17 ), ['localidade']] = "TO"
        data_frame.loc[(data_frame['localidade']==21 ), ['localidade']] = "MA"
        data_frame.loc[(data_frame['localidade']==22 ), ['localidade']] = "PI"
        data_frame.loc[(data_frame['localidade']==23 ), ['localidade']] = "CE"
        data_frame.loc[(data_frame['localidade']==24 ), ['localidade']] = "RN"
        data_frame.loc[(data_frame['localidade']==25 ), ['localidade']] = "PB"
        data_frame.loc[(data_frame['localidade']==26 ), ['localidade']] = "PE"
        data_frame.loc[(data_frame['localidade']==27 ), ['localidade']] = "AL"
        data_frame.loc[(data_frame['localidade']==28 ), ['localidade']] = "SE"
        data_frame.loc[(data_frame['localidade']==29 ), ['localidade']] = "BA"
        data_frame.loc[(data_frame['localidade']==31 ), ['localidade']] = "MG"
        data_frame.loc[(data_frame['localidade']==32 ), ['localidade']] = "ES"
        data_frame.loc[(data_frame['localidade']==33 ), ['localidade']] = "RJ"
        data_frame.loc[(data_frame['localidade']==35 ), ['localidade']] = "SP"
        data_frame.loc[(data_frame['localidade']==41 ), ['localidade']] = "PR"
        data_frame.loc[(data_frame['localidade']==42 ), ['localidade']] = "SC"
        data_frame.loc[(data_frame['localidade']==43 ), ['localidade']] = "RS"
        data_frame.loc[(data_frame['localidade']==50 ), ['localidade']] = "MS"
        data_frame.loc[(data_frame['localidade']==51 ), ['localidade']] = "MT"
        data_frame.loc[(data_frame['localidade']==52 ), ['localidade']] = "GO"
        data_frame.loc[(data_frame['localidade']==53 ), ['localidade']] = "DF"
        data_frame.insert(loc=0, column="serie", value=self.tabela)
        data_frame.insert(loc=1, column="abrangencia", value="4")
        data_frame.loc[(data_frame['nome']=="Brasil" ), ['abrangencia']] = "1"
        data_frame.loc[(data_frame['nome']=="Norte" ), ['abrangencia']] = "2"
        data_frame.loc[(data_frame['nome']=="Nordeste" ), ['abrangencia']] = "2"
        data_frame.loc[(data_frame['nome']=="Centro-Oeste" ), ['abrangencia']] = "2"
        data_frame.loc[(data_frame['nome']=="Sul" ), ['abrangencia']] = "2"
        data_frame.loc[(data_frame['nome']=="Sudeste" ), ['abrangencia']] = "2"
        data_frame.loc[(data_frame['nome']=="Rondônia" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Acre" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Amazonas" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Roraima" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Pará" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Amapá" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Tocantins" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Maranhão" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Piauí" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Ceará" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Rio Grande do Norte"), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Paraíba" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Pernambuco" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Alagoas" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Sergipe" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Bahia" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Minas Gerais" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Espírito Santo" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Rio de Janeiro" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="São Paulo" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Paraná" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Santa Catarina" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Rio Grande do Sul" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Mato Grosso do Sul" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Mato Grosso" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Goiás" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Distrito Federal" ), ['abrangencia']] = "3"
        self.data_frame2=data_frame
        #print(data_frame)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', 1)
        resultado6=self.data_frame2[self.data_frame2["abrangencia"]=="4"]
        print(resultado6)
               
    def formato_dataimesc(self):
        import pandas as pd
        dataframe_organizado=pd.melt(self.data_frame2,id_vars=["serie","abrangencia","localidade","nome"],value_vars=self.anos)
        dataframe_organizado2=dataframe_organizado[["serie","abrangencia","localidade","nome","value","variable"]]
        dataframe_final=dataframe_organizado2.set_index("serie")
        return dataframe_final

for i in range(240,241):
    # Iniciando a Classe
    teste = dataImesc()
    # Insira o número da tabela desejada abaixo
    tabela_search = i
    # Pesquisa iniciada
    dataframe_Formatado = teste.procurar_tabela(tabela_search)
    # Exibindo os resultados
    print('\n')
