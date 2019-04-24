from flask import Blueprint, render_template

page = Blueprint('page', __name__, template_folder='templates')


@page.route('/home')
def home():
    return render_template('page/home.html')

@page.route('/terms')
def terms():
    return render_template('page/terms.html')

@page.route('/privacy')
def privacy():
    return render_template('page/privacy.html')

@page.route('/general')
def general():
    return render_template('page/faq/general.html')

@page.route('/brand')
def brand():
    return render_template('page/faq/brand.html')

@page.route('/costing')
def costing():
    return render_template('page/faq/costing.html')

@page.route('/durability')
def durability():
    return render_template('page/faq/durability.html')

@page.route('/health')
def health():
    return render_template('page/faq/health.html')

@page.route('/installation')
def installation():
    return render_template('page/faq/installation.html')

@page.route('/maintenance')
def maintenance():
    return render_template('page/faq/maintenance.html')

@page.route('/others')
def others():
    return render_template('page/faq/others.html')

@page.route('/technical')
def technical():
    return render_template('page/faq/technical.html')

@page.route('/warranty')
def warranty():
    return render_template('page/faq/warranty.html')

@page.route('/brands')
def brands():
    return render_template('page/brands.html')

@page.route('/tile')
def tile():
    return render_template('tc/tilecollection/spruceomorika.html')

@page.route('/g1')
def g1():
    return render_template('page/gallery/g1.html')

@page.route('/g2')
def g2():
    return render_template('page/gallery/g2.html')

@page.route('/g3')
def g3():
    return render_template('page/gallery/g3.html')

@page.route('/g4')
def g4():
    return render_template('page/gallery/g4.html')

@page.route('/g5')
def g5():
    return render_template('page/gallery/g5.html')

@page.route('/g6')
def g6():
    return render_template('page/gallery/g6.html')

@page.route('/g7')
def g7():
    return render_template('page/gallery/g7.html')

@page.route('/g8')
def g8():
    return render_template('page/gallery/g8.html')

@page.route('/g9')
def g9():
    return render_template('page/gallery/g9.html')

@page.route('/g10')
def g10():
    return render_template('page/gallery/g10.html')

@page.route('/g11')
def g11():
    return render_template('page/gallery/g11.html')