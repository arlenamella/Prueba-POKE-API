from string import Template



validacion_pokemon = 'Por favor ingrese un nombre válido de algún pokemon: '
validacion_opcion = 'Por favor ingrese una opción válida: '

#esta es la traducción de los tipos, y tipos especiales
tipos_espanol = {'normal': 'Normal',
            'fighting': 'Lucha',
            'flying': 'Volador',
            'poison': 'Venenoso',
            'ground': 'Tierra',
            'rock': 'Roca',
            'bug': 'Bicho',
            'ghost': 'Fantasma',
            'steel': 'Acero',
            'fire': 'Fuego',
            'water': 'Agua',
            'grass': 'Pasto',
            'electric': 'Eléctrico',
            'psychic': 'Psiquico',
            'ice': 'Hielo',
            'dragon': 'Dragón',
            'dark': 'Siniestro',        
            'fairy' : 'Hada',
            'unknown': 'Desconocido',
            'shadow': 'Sombra',            
            }
    
special_es = {'legendary':'Legendario',
               'mythical':'Mitico',
               'baby':'Bebe'
              }

document_template = Template('''<!DOCTYPE html>
                                <html>
                                    <head>
                                    <meta name="viewport" content="width=device-width, initial-scale=1">
                                    <link rel="stylesheet" href="mystyle.css">
                                    </head>
                                <body>

                                $body
                        
                                </body>
                                </html>
                                ''')


single_card = Template('''
                        <div class="column2">
                        <div class="card">
                        <h1>#$id $name</h1>
                            <img src="$url" width="150" height="150">
                        <div class="container">
                            $etapa_previa
                            <h2>Estadísticas</h2>
                            <table>
                                <tr>
                                $table
                                </tr>
                            </table>
                            <h3><b>Tipo</b></h3> 
                                $tipos 
                                
                            <p>$description</p>
                            
                        <h3>Super efectivo contra:</h3>
                            $super_efectivo
                        <h3>Débil contra:</h3>
                            $debil
                        <h3>Resistente contra:</h3>
                            $resistente
                        <h3>Poco Eficaz contra</h3>
                            $poco_ef
                        <h3>Inmune contra:</h3>
                            $inmune
                        <h3>Ineficaz contra:</h3>
                            $inef
                        
                        </div>
                        </div>
                    ''')

tabla_pokemon = Template('''
<td><h5>HP: $hp</h5></td>
<td><h5>Ataque: $attack</h5></td>
<td><h5>Defensa: $defense</h5></td>
<td><h5>Ataque Especial: $esAttck</h5></td>
<td><h5>Defensa Especial: $esDef</h5></td>
<td><h5>Velocidad: $speed</h5></td>''')

span = Template('''<span class="label $class_">$value_</span>''')