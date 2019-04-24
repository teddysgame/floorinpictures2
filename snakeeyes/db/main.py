# main.py

#from app import app
from db_setup import init_db, db_session
from forms import VinylSearchForm, AlbumForm
from flask import flash, render_template, request, redirect
from models import Album, Label
from tables import Results

init_db()


@app.route('/labelresult', methods=['GET', 'POST'])
def index():
    search = MusicSearchForm(request.form)
    
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form=search)


@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']

    if search_string:
        if search.data['select'] == 'Label':
            qry = db_session.query(Album, Label).filter(
                Label.id==Album.label_id).filter(
                    Label.name.contains(search_string))
            results = [item[0] for item in qry.all()]
        elif search.data['select'] == 'Brand':
            qry = db_session.query(Album).filter(
                Album.title.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'Album':
            qry = db_session.query(Album).filter(
                Album.title.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'Code':
            qry = db_session.query(Album).filter(
                Album.Code.contains(search_string))
            results = qry.all()
        else:
            qry = db_session.query(Album)
            results = qry.all()
    else:
        qry = db_session.query(Album)
        results = qry.all()

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = Results(results)
        table.border = False
        return render_template('results.html', table=table)


@app.route('/new_album', methods=['GET', 'POST'])
def new_album():
    """
    Add a new album
    """
    form = AlbumForm(request.form)

    if request.method == 'POST' and form.validate():
        # save the album
        album = Album()
        save_changes(album, form, new=True)
        flash('Data inserted successfully!')
        return redirect('/')

    return render_template('new_album.html', form=form)


def save_changes(album, form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    label = Label()
    label.name = form.label.data

    album.label = label
    album.brand = form.brand.data
    album.title = form.title.data
    album.code = form.code.data
    album.price = form.price.data

    if new:
        # Add the new album to the database
        db_session.add(album)

    # commit the data to the database
    db_session.commit()


@app.route('/item/<int:id>', methods=['GET', 'POST'])
def edit(id):
    """
    Add / edit an item in the database
    """
    qry = db_session.query(Album).filter(
                Album.id==id)
    album = qry.first()

    if album:
        form = AlbumForm(formdata=request.form, obj=album)
        if request.method == 'POST' and form.validate():
            # save edits
            save_changes(album, form)
            flash('Album updated successfully!')
            return redirect('/')
        return render_template('edit_album.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    """
    Delete the item in the database that matches the specified
    id in the URL
    """
    qry = db_session.query(Album).filter(
        Album.id==id)
    album = qry.first()

    if album:
        form = AlbumForm(formdata=request.form, obj=album)
        if request.method == 'POST' and form.validate():
            # delete the item from the database
            db_session.delete(album)
            db_session.commit()

            flash('Album deleted successfully!')
            return redirect('/')
        return render_template('delete_album.html', form=form)
    else:
        return 'Error deleting #{id}'.format(id=id)


# if __name__ == '__main__':
#     import os
#     if 'WINGDB_ACTIVE' in os.environ:
#         app.debug=True
#     app.run(port=5001)