from flask import Blueprint, render_template

tc = Blueprint('tc', __name__, template_folder='templates')

@tc.route('/tilecollection')
def tilecollection():
    return render_template('tc/tilecollection.html')

# Single tiles

@tc.route('/ambrosiacedar')
def ambrosiacedar():
    return render_template('tile/ambrosiacedar.html')

@tc.route('/balsawood')
def balsawood():
    return render_template('tile/balsawood.html')

@tc.route('/blackacacia')
def blackacacia():
    return render_template('tile/blackacacia.html')

@tc.route('/blackwood')
def blackwood():
    return render_template('tile/blackwood.html')

@tc.route('/boxelderwood')
def boxelderwood():
    return render_template('tile/boxelderwood.html')

@tc.route('/catalpawood')
def catalpawood():
    return render_template('tile/catalpawood.html')

@tc.route('/chadblackwood')
def chadblackwood():
    return render_template('tile/chadblackwood.html')

@tc.route('/cherrywood')
def cherrywood():
    return render_template('tile/cherrywood.html')

@tc.route('/easternhemlock')
def easternhemlock():
    return render_template('tile/easternhemlock.html')

@tc.route('/francemaple')
def francemaple():
    return render_template('tile/francemaple.html')

@tc.route('/hazelplum')
def hazelplum():
    return render_template('tile/hazelplum.html')

@tc.route('/hormigowood')
def hormigowood():
    return render_template('tile/hormigowood.html')

@tc.route('/movinguiwood')
def movinguiwood():
    return render_template('tile/movinguiwood.html')

@tc.route('/oakespana')
def oakespana():
    return render_template('tile/oakespana.html')

@tc.route('/oakfalcata')
def oakfalcata():
    return render_template('tile/oakfalcata.html')

@tc.route('/plumdosato')
def plumdosato():
    return render_template('tile/plumdosato.html')

@tc.route('/pratooak')
def pratooak():
    return render_template('tile/pratooak.html')

@tc.route('/sessileoak')
def sessileoak():
    return render_template('tile/sessileoak.html')

@tc.route('/spruceomorika')
def spruceomorika():
    return render_template('tile/spruceomorika.html')

@tc.route('/thaiteak')
def thaiteak():
    return render_template('tile/thaiteak.html')

@tc.route('/trentooak')
def trentooak():
    return render_template('tile/trentooak.html')

@tc.route('/tulepowood')
def tulepowood():
    return render_template('tile/tulepowood.html')

@tc.route('/canarywood')
def canarywood():
    return render_template('tile/canarywood.html')

@tc.route('/cherryprunus')
def cherryprunus():
    return render_template('tile/cherryprunus.html')

@tc.route('/jabilloglory')
def jabilloglory():
    return render_template('tile/jabilloglory.html')

@tc.route('/oakcorilona')
def oakcorilona():
    return render_template('tile/oakcorilona.html')

@tc.route('/amarellowood')
def amarellowood():
    return render_template('tile/amarellowood.html')

@tc.route('/laureloak')
def laureloak():
    return render_template('tile/laureloak.html')

@tc.route('/mountainash')
def mountainash():
    return render_template('tile/mountainash.html')

@tc.route('/scafitiwalnut')
def scafitiwalnut():
    return render_template('tile/scafitiwalnut.html')

@tc.route('/southernmagnolia')
def southernmagnolia():
    return render_template('tile/southernmagnolia.html')

@tc.route('/afomosiawood')
def afomosiawood():
    return render_template('tile/afomosiawood.html')

@tc.route('/amaziquewood')
def amaziquewood():
    return render_template('tile/amaziquewood.html')

@tc.route('/baliteak')
def baliteak():
    return render_template('tile/baliteak.html')

@tc.route('/macacaubawood')
def macacaubawood():
    return render_template('tile/macacaubawood.html')

@tc.route('/romaniaalder')
def romaniaalder():
    return render_template('tile/romaniaalder.html')

@tc.route('/berliniawood')
def berliniawood():
    return render_template('tile/berliniawood.html')

@tc.route('/burmapaduak')
def burmapaduak():
    return render_template('tile/burmapaduak.html')

@tc.route('/rhodesianteak')
def rhodesianteak():
    return render_template('tile/rhodesianteak.html')

@tc.route('/walnutmimosa')
def walnutmimosa():
    return render_template('tile/walnutmimosa.html')

@tc.route('/albiziawood')
def albiziawood():
    return render_template('tile/albiziawood.html')

@tc.route('/anziochestnut')
def anziochestnut():
    return render_template('tile/anziochestnut.html')

@tc.route('/paleoak')
def paleoak():
    return render_template('tile/paleoak.html')

@tc.route('/oxidizedwood')
def oxidizedwood():
    return render_template('tile/oxidizedwood.html')

@tc.route('/fanooak')
def fanooak():
    return render_template('tile/fanooak.html')

@tc.route('/blackpalm')
def blackpalm():
    return render_template('tile/blackpalm.html')

@tc.route('/chestnutafrica')
def chestnutafrica():
    return render_template('tile/chestnutafrica.html')

@tc.route('/paviacherry')
def paviacherry():
    return render_template('tile/paviacherry.html')
